# Public Demo — AI Automation Audit

> **Demo only.** This is a fictional example created to demonstrate the deliverable. It is not a real client case study and contains no claimed performance results.

## Client Profile

**Business:** BrightDesk Cleaning (fictional)  
**Type:** Small office-cleaning company  
**Team:** Owner + 6 cleaners  
**Current tools:** Gmail, Google Calendar, Google Sheets  
**Main problem:** New quote requests arrive by email and web form. The owner manually copies details into a spreadsheet, replies, schedules follow-ups, and sometimes forgets to follow up.

## 1. Executive Summary

BrightDesk does not need a complicated AI agent as its first step. The highest-value opportunity is to standardize incoming lead information and make sure every qualified inquiry receives a fast response and a scheduled follow-up.

**First Build:** Lead Capture + Follow-Up Queue

Why this should come first:

- it is close to revenue;
- the current process has obvious repetitive copy/paste work;
- missed follow-ups are easy to detect and reduce;
- it can start with the company's existing Google tools.

## 2. Current Workflow

```text
Inquiry arrives
  ↓
Owner opens email / form
  ↓
Owner manually copies details to Google Sheets
  ↓
Owner writes a reply
  ↓
Owner adds a reminder to follow up
  ↓
Quote / no response / lost lead
```

### Main Bottlenecks

1. Lead details are stored inconsistently.
2. Reply quality depends on how busy the owner is.
3. Follow-up reminders are manual and can be missed.
4. No simple view shows which leads are waiting for action.

## 3. Opportunity Scorecard

| # | Opportunity | Business Value | Ease | Risk Control | Priority |
|---|---|---:|---:|---:|---|
| 1 | Lead intake + follow-up queue | 5 | 5 | 5 | High |
| 2 | Quote-draft assistant | 4 | 4 | 4 | High |
| 3 | Appointment confirmation workflow | 4 | 5 | 5 | High |
| 4 | Weekly lead-status summary | 3 | 5 | 5 | Medium |
| 5 | FAQ response suggestions | 3 | 4 | 4 | Medium |

## 4. Workflow Blueprint #1 — Lead Intake + Follow-Up Queue

### Desired Outcome

Every new inquiry enters one structured queue and receives a timely response without relying on the owner's memory.

### Flow

```text
New inquiry
  ↓
Validate required fields
  ↓
Create / update lead row
  ↓
Prepare acknowledgement
  ↓
Human review or approved template send
  ↓
Set follow-up date
  ↓
Log status
```

### Detailed Steps

1. **Trigger:** a new form submission or eligible inquiry email.
2. **Input:** name, email, company, address / area, requested service, preferred date, notes.
3. **Validation:** if phone or service area is missing, mark `Needs Info` instead of continuing.
4. **Processing:** standardize the fields and check whether the lead already exists.
5. **Human Check:** owner confirms unusual requests, pricing, or custom promises.
6. **Action:** add lead to the main sheet and prepare / send a standard acknowledgement.
7. **Logging:** timestamp, source, current status, last contact, next follow-up date.
8. **Fallback:** if automation fails, place the inquiry in an `Automation Error` view and send an internal notification.

### Suggested Low-Cost Stack

- Google Forms or current website form;
- Gmail;
- Google Sheets;
- Google Apps Script for lightweight glue logic.

AI is optional in v1. It can later help classify free-text requests or draft personalized responses, but the workflow should still function when AI is unavailable.

## 5. Workflow Blueprint #2 — Quote Draft Assistant

### Desired Outcome

Reduce the time required to turn structured lead information into a consistent quote draft.

### Flow

```text
Qualified lead → Pull structured fields → Apply approved pricing rules → Draft quote → Human approval → Send
```

### Guardrail

The system should not invent prices or discounts. Final pricing stays under owner approval unless the business has explicit, deterministic pricing rules.

## 6. Workflow Blueprint #3 — Appointment Confirmation

### Desired Outcome

Reduce forgotten appointments and repetitive confirmation messages.

### Flow

```text
Job booked → Calendar event created → Confirmation template → Reminder → Completion status logged
```

### Guardrail

Cancellation, rescheduling, or special-access instructions should require confirmation if they conflict with existing bookings.

## 7. Ready-to-Use Asset

### Lead Acknowledgement Template

Hi {{first_name}},

Thanks for contacting BrightDesk Cleaning about {{service}}. We received your request and are reviewing the details now.

If we need any additional information, we'll contact you before preparing the quote. You can reply to this message if there is anything important we should know about the space, access, or timing.

Thanks,
BrightDesk Cleaning

## 8. 7-Day Rollout

| Day | Action | Success Check |
|---|---|---|
| 1 | Define required lead fields | Every lead can fit the same structure |
| 2 | Clean the main lead sheet | No duplicate status columns |
| 3 | Add intake automation | Test leads appear correctly |
| 4 | Add acknowledgement + error handling | Missing fields do not silently fail |
| 5 | Add follow-up dates | Every open lead has a next action |
| 6 | Run with a small batch | Owner reviews real outputs |
| 7 | Measure and revise | Problems are logged and fixed |

## 9. What Not to Automate Yet

- Final custom pricing, until pricing rules are explicit.
- Complaints or sensitive customer disputes.
- Refunds or financial actions.
- Any message that makes a contractual promise without human review.

## 10. Measurements to Establish Before Launch

Because this fictional example has no real baseline, the business should record for one week:

- number of incoming leads;
- average first-response time;
- percentage of leads with a scheduled next action;
- number of missed or late follow-ups;
- owner minutes spent per lead.

Only after establishing those numbers should the business claim that the workflow saved time or improved follow-up performance.

## Internal QA

- Fact reliability: 2/2
- Executability: 2/2
- Cost constraints: 2/2
- Safety & stability: 2/2
- Business value: 2/2

**Total: 10/10**

The score reflects the quality of the fictional demo plan, not a claim that the workflow produced real-world results.
