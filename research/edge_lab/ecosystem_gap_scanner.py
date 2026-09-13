#!/usr/bin/env python3
"""
Ecosystem Gap Scanner

目的：对“官方能力缺口 + 市场供给密度”进行评分，避免凭感觉选插件。

当前版本不主动抓取网站，只接受结构化输入，后续可把 DCloud 官方兼容表和插件市场数据接入。
"""

from dataclasses import dataclass, asdict
from typing import List
import json


@dataclass
class Candidate:
    name: str
    common_need: float          # 0-10 常见需求程度
    platform_gap: float         # 0-10 HarmonyOS/新平台缺口程度
    low_supply: float           # 0-10 竞争越少越高
    auto_delivery: float        # 0-10 可自动交付程度
    no_external_cost: float     # 0-10 不依赖付费API/服务器
    maintainability: float      # 0-10 维护成本越低越高
    support_burden: float       # 0-10 售后负担，越高越差
    manual_per_sale: float      # 0-10 每单人工程度，越高越差

    def score(self) -> float:
        positive = (
            self.common_need * 1.3
            + self.platform_gap * 1.5
            + self.low_supply * 1.5
            + self.auto_delivery * 1.4
            + self.no_external_cost * 1.2
            + self.maintainability * 1.0
        )
        negative = self.support_burden * 1.0 + self.manual_per_sale * 1.6
        return round(positive - negative, 2)

    def reject(self) -> List[str]:
        reasons = []
        if self.auto_delivery < 8:
            reasons.append("不能高度自动交付")
        if self.manual_per_sale > 2:
            reasons.append("每单需要人工")
        if self.no_external_cost < 7:
            reasons.append("运行成本/第三方依赖过高")
        if self.low_supply < 5:
            reasons.append("竞争已经偏高")
        if self.platform_gap < 5:
            reasons.append("生态缺口不明显")
        return reasons


CANDIDATES = [
    Candidate(
        name="三端安全存储 Android Keystore / iOS Keychain / Harmony HUKS",
        common_need=8.5,
        platform_gap=8.0,
        low_supply=8.0,
        auto_delivery=10.0,
        no_external_cost=10.0,
        maintainability=7.5,
        support_burden=4.0,
        manual_per_sale=0.0,
    ),
    Candidate(
        name="全端文件选择器",
        common_need=9.0,
        platform_gap=3.0,
        low_supply=2.0,
        auto_delivery=10.0,
        no_external_cost=10.0,
        maintainability=8.0,
        support_burden=3.0,
        manual_per_sale=0.0,
    ),
    Candidate(
        name="NFC 三端封装",
        common_need=6.0,
        platform_gap=4.0,
        low_supply=2.0,
        auto_delivery=10.0,
        no_external_cost=10.0,
        maintainability=6.0,
        support_burden=6.0,
        manual_per_sale=0.0,
    ),
    Candidate(
        name="微信登录分享支付三端封装",
        common_need=10.0,
        platform_gap=3.0,
        low_supply=1.0,
        auto_delivery=9.5,
        no_external_cost=9.0,
        maintainability=5.0,
        support_burden=7.0,
        manual_per_sale=0.0,
    ),
    Candidate(
        name="防截屏/录屏三端封装",
        common_need=5.5,
        platform_gap=3.0,
        low_supply=2.0,
        auto_delivery=10.0,
        no_external_cost=10.0,
        maintainability=7.0,
        support_burden=4.0,
        manual_per_sale=0.0,
    ),
]


def rank(candidates: List[Candidate]):
    rows = []
    for c in candidates:
        rows.append({
            **asdict(c),
            "score": c.score(),
            "rejected_by": c.reject(),
        })
    rows.sort(key=lambda x: x["score"], reverse=True)
    return rows


if __name__ == "__main__":
    results = rank(CANDIDATES)
    print(json.dumps(results, ensure_ascii=False, indent=2))
