#!/usr/bin/env python3
"""Rank autonomous paid-skill candidates for an AI micro-asset portfolio.

The scoring model deliberately rewards:
- monthly/recurring value
- near-zero marginal runtime cost
- deterministic, testable outputs
- usefulness across many agents/workflows
- low support burden
- easy AI-assisted construction
- low competition/native substitution
- automatic data/rule updates
- platform paid-review fit

This is a decision aid, not an earnings forecast.
"""
from dataclasses import dataclass, asdict
from typing import List
import json


@dataclass
class Candidate:
    name: str
    monthly_value: float
    zero_marginal_cost: float
    deterministic: float
    broad_agent_use: float
    low_support: float
    ai_buildability: float
    novelty: float
    update_automation: float
    moat: float
    review_fit: float
    privacy_safety: float
    native_gap: float
    notes: str = ""

    def score(self) -> float:
        weights = {
            "monthly_value": 1.7,
            "zero_marginal_cost": 1.4,
            "deterministic": 1.4,
            "broad_agent_use": 1.4,
            "low_support": 1.2,
            "ai_buildability": 1.0,
            "novelty": 1.4,
            "update_automation": 1.1,
            "moat": 1.5,
            "review_fit": 1.7,
            "privacy_safety": 1.1,
            "native_gap": 1.8,
        }
        return round(sum(getattr(self, k) * w for k, w in weights.items()), 2)

    def reject(self) -> List[str]:
        reasons = []
        if self.zero_marginal_cost < 8:
            reasons.append("边际运行成本不够低")
        if self.low_support < 7:
            reasons.append("售后负担偏高")
        if self.review_fit < 8:
            reasons.append("付费审核价值支撑不足")
        if self.native_gap < 6:
            reasons.append("平台原生替代过强")
        if self.deterministic < 7:
            reasons.append("难以自动回归测试")
        return reasons


CANDIDATES = [
    Candidate("China DateOps 工作日/调休/截止日引擎", 9,10,10,9,10,9,9,10,8,9,10,10,
              "年度官方假期数据 + 确定性日期算法"),
    Candidate("China RegionOps 行政区划标准化/历史迁移", 9,10,10,8,9,8,9,10,9,10,10,10,
              "版本化区划数据 + 新旧名称/代码映射"),
    Candidate("CRM Import Doctor 导入前数据体检", 10,10,9,9,8,8,9,9,8,10,9,10,
              "字段映射、去重、格式异常、错误报告"),
    Candidate("Knowledge Deduper 知识库近重复清理", 9,10,9,10,8,7,9,9,8,10,10,9,
              "RAG 导入前的重复/版本清理"),
    Candidate("China Data Gate 中文业务数据质量闸门", 10,10,9,9,8,8,9,9,8,10,9,9,
              "写 CRM/数据库之前做验证、规范化、去重"),
    Candidate("PII Redactor 中文隐私信息脱敏", 10,10,9,10,8,7,9,9,9,10,7,9,
              "手机号/身份证/邮箱/地址等一致占位符"),
    Candidate("RAG Sanitizer 内容净化+提示注入风险扫描", 10,10,7,10,7,6,10,8,9,10,9,10,
              "知识库/网页进入 Agent 前做清洗"),
    Candidate("Multi-Agent Handoff 多Agent交接状态包", 9,10,8,10,8,7,10,9,9,10,10,8,
              "压缩上下文、任务状态、已完成/待办/风险"),
    Candidate("JSON Schema Repair", 9,10,10,10,9,9,6,9,6,8,10,3,
              "平台原生结构化/评估能力强，主动降级"),
    Candidate("Agent Tool Parameter Validator", 9,10,10,10,9,9,7,9,6,8,10,2,
              "平台已有强参数校验，主动降级"),
]


def rank(candidates: List[Candidate]):
    rows = []
    for c in candidates:
        rows.append({**asdict(c), "score": c.score(), "rejected_by": c.reject()})
    rows.sort(key=lambda x: x["score"], reverse=True)
    return rows


if __name__ == "__main__":
    print(json.dumps(rank(CANDIDATES), ensure_ascii=False, indent=2))
