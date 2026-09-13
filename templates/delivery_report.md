# AI Automation Audit — Delivery Template

> Client: [CLIENT NAME]  
> Date: [DATE]  
> Package: [STARTER / GROWTH / BUILD]

## 1. Executive Summary

### 业务目标

[用 2–4 句话说明客户真正想改善的业务结果。]

### 首要建议

**First Build:** [最值得优先实施的工作流]

原因：

- [原因 1]
- [原因 2]
- [原因 3]

### 当前可量化基线

| 指标 | 当前情况 | 目标方向 |
|---|---:|---:|
| 每周人工时间 | [X 小时] | 降低 |
| 平均响应时间 | [X] | 缩短 |
| 漏跟进 / 遗漏 | [X] | 降低 |
| 其他 | [X] | [方向] |

如果客户没有提供基线，请明确写“未提供，实施前建议先记录 7 天”。

## 2. Current Workflow

```text
[触发]
  ↓
[步骤 1]
  ↓
[步骤 2]
  ↓
[步骤 3]
  ↓
[结果]
```

### 当前瓶颈

1. [瓶颈]
2. [瓶颈]
3. [瓶颈]

## 3. Automation Opportunity Scorecard

评分范围 1–5，5 为最高。

| # | 机会 | 业务价值 | 实施容易度 | 风险可控性 | 优先级 |
|---|---|---:|---:|---:|---|
| 1 | [机会] | 5 | 4 | 5 | High |
| 2 | [机会] | 4 | 5 | 4 | High |
| 3 | [机会] | 4 | 3 | 4 | Medium |
| 4 | [机会] | 3 | 4 | 5 | Medium |
| 5 | [机会] | 2 | 2 | 3 | Low |

## 4. Workflow Blueprint #1 — First Build

### Desired Outcome

[一句话说明业务结果。]

### Flow

```text
Trigger → Validate → Process → Human Check → Action → Log
```

### Detailed Steps

1. **Trigger:** [何时开始]
2. **Input:** [需要哪些数据]
3. **Validation:** [缺字段 / 异常怎么办]
4. **Processing:** [规则 / AI 做什么]
5. **Human Check:** [谁确认什么]
6. **Action:** [发送 / 更新 / 创建什么]
7. **Logging:** [记录什么]
8. **Fallback:** [失败时怎么处理]

### Tools

- 首选：[客户已有工具]
- 免费 / 低成本替代：[替代方案]
- 升级方案：[如业务增长后再考虑]

### Risks

- [风险 + 处理方式]

## 5. Workflow Blueprint #2

按 Blueprint #1 相同结构填写。

## 6. Workflow Blueprint #3

按 Blueprint #1 相同结构填写。

## 7. Ready-to-Use Assets

### Prompt / SOP / Message Template A

[可直接复制使用]

### Prompt / SOP / Message Template B

[可直接复制使用]

## 8. 7-Day Implementation Order

| Day | Action | Owner | Done When |
|---|---|---|---|
| 1 | 建立基线 | Client | 已记录当前耗时 / 遗漏 |
| 2 | 整理输入字段 | Client + Builder | 字段完整 |
| 3 | 搭第一版流程 | Builder | 测试数据能跑通 |
| 4 | 异常测试 | Builder | 缺数据 / 重复数据可处理 |
| 5 | 人工确认点测试 | Client | 客户确认可接受 |
| 6 | 小范围上线 | Client | 真实但低风险使用 |
| 7 | 复盘 | Client + Builder | 有结果和问题清单 |

## 9. What We Would NOT Automate Yet

- [环节]：因为 [原因]
- [环节]：因为 [原因]

## 10. Assumptions & Unknowns

明确列出所有未验证内容：

- [假设]
- [未知]

## 11. Next Step

### 建议立即做

[一个最小动作]

### 如果需要代搭建

需要客户提供：

- [必要账号 / 权限]
- [必要样例数据]
- [测试规则]

遵循最小权限原则，不需要密码，不收集无关敏感数据。

---

## Internal QA — Not for Client

- Fact reliability: __/2
- Executability: __/2
- Cost constraints: __/2
- Safety & stability: __/2
- Business value: __/2

**Total: __/10**

低于 8/10 不交付。
