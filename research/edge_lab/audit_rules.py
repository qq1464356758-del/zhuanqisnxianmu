from dataclasses import dataclass

@dataclass
class Opportunity:
    name: str
    outbound_customer_acquisition: bool = False
    upfront_capital_needed: bool = False
    advanced_skill_needed: bool = False
    luck_dominant: bool = False
    tos_or_cheating_risk: bool = False
    offline_required: bool = False
    generic_ai_can_replace: bool = False
    platform_has_existing_demand: bool = True
    rmb_cashout_clear: bool = True
    repeatable: bool = True


def audit(x: Opportunity):
    reasons = []
    if x.outbound_customer_acquisition:
        reasons.append("需要主动获客")
    if x.upfront_capital_needed:
        reasons.append("需要前置本金")
    if x.advanced_skill_needed:
        reasons.append("技术/专业门槛过高")
    if x.luck_dominant:
        reasons.append("收益主要靠运气")
    if x.tos_or_cheating_risk:
        reasons.append("依赖作弊、绕规则或高封禁风险")
    if x.offline_required:
        reasons.append("不能纯线上完成")
    if x.generic_ai_can_replace:
        reasons.append("通用AI可直接替代")
    if not x.platform_has_existing_demand:
        reasons.append("平台没有现成需求，需要自己造市场")
    if not x.rmb_cashout_clear:
        reasons.append("人民币兑现链路不清楚")
    if not x.repeatable:
        reasons.append("不可稳定重复")

    return {
        "name": x.name,
        "pass": len(reasons) == 0,
        "reasons": reasons,
    }


if __name__ == "__main__":
    examples = [
        Opportunity("qualification_gated_task_queue"),
        Opportunity("crowdtest_task_radar"),
        Opportunity("creator_bonus_pool", luck_dominant=True),
        Opportunity("freelance_custom_work", outbound_customer_acquisition=True),
        Opportunity("bug_bounty", advanced_skill_needed=True),
        Opportunity("map_photo_tasks", offline_required=True),
    ]
    for item in examples:
        print(audit(item))
