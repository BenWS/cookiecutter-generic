# MM-DD-YYYY

## Data Pipeline Construction

```md
[Write to this file if needed](<data-pipline-!!key!!.md>)

**Topic** - (Topic)

# Tasks
- [ ] Data Modeling
- [ ] Data Pipeline Design
- [ ] Data Pipeline Construction
- [ ] Publish to centralized resources
- [ ] Stakeholder communication

# Folder Structure

(Project Root)
|-- Queries
|  |-- Data Pipeline - (Topic) - Validation.* 
|  |-- Data Pipeline - (Topic).*
|  |-- Miscellaneous.sql
|-- Data Modeling
|  |-- Data Models.md
|  |-- Data Pipeline.drawio
|-- Miscellaneous
|  |-- (Other files as needed)


# Data Models

- `(Model 1)`
    - Grain
    - Scope
- `(Model 2)`
    - Grain
    - Scope

# Data Pipeline Design

- `(Model 1)`
  - Data Pipeline
    - *Dependency tree from 'root' (final) to 'leaf' (sources)*
  - Sub-queries
    - *Define each CTE or sub-query seen in the overall model query - provides further context for the Data Pipeline tree*
```

## Dashboard Construction


```md
__Notes__ - [See here](<dashboard-construction-(topic)/init.txt>)

__Tasks__

__Dashboard Metadata__

- Name - 
- Worksheets -

__Components__
- Component 1
  - __Description__ 
    - (Description) 
- Component 2
  - __Description__
    - (Description) 

__Dashboard Structure__
- Root
  - Header
  - Vertical Space
    - Horizontal Space
      - Component 1
      - Component 2
    - Horizontal Space
      - Component 3


# Files

(Project Root)
|-- Dashboard
|  |-- Dashboard.*
|-- Queries
|  |-- Data Pipeline - (Topic) - Validation.* 
|  |-- Data Pipeline - (Topic).*
|  |-- Miscellaneous.sql
|-- Data Models
|  |-- Data Models.md
|  |-- Data Pipeline.drawio
|-- Miscellaneous
|  |-- (Other files as needed)
```

# Generic Specifications Template

```
# [Feature Name]

<!-- 
  Copy this file to THDSPEC/<jira-id>-<feature-name>.spec.md and fill in each section.
  Use lowercase kebab-case for the filename: e.g. OP-1201-order-ingestion.spec.md
  Keep this template intact — never edit _TEMPLATE.md directly.
-->

**Version:** 1.0
**Date:** YYYY-MM-DD
**Author:** [name or team]

## Status
<!-- Draft | Approved | In Progress | Implemented | Deprecated | Archived -->
`Draft`

---

## Overview
<!-- 2–5 sentences: what does this feature do, why does it exist, and what user or business need does it serve? -->


---

## Requirements

### Functional
- [ ] 

### Non-Functional
<!-- Include measurable thresholds. Use p99 latency, uptime %, data volume, etc. -->
- [ ] **Performance:** 
- [ ] **Scalability:** 
- [ ] **Observability:** Logs MUST capture [events]; metrics MUST include [counters/gauges]; alerts MUST fire on [condition].
- [ ] **Data Retention:** 

---

## Acceptance Criteria
<!-- Specific, testable, binary conditions that define "done". -->
<!-- Format: GIVEN <precondition>, WHEN <action>, THEN <expected outcome> -->
<!-- These drive the pseudocode plan — one plan step per criterion. -->
- [ ] 
- [ ] 

---

## Test Strategy
<!-- How each Acceptance Criterion is proven. Drives the plan's AC × Test matrix. -->
- **Coverage target:** <!-- default ≥80% branch on business logic; state any override + justification -->
- **Required test types:** <!-- unit / integration / e2e -->
- **ACs needing integration or e2e (not just unit):** <!-- list AC IDs, or "none" -->
- **Test data / fixtures:** <!-- notable fixtures, mocks, or seeded data -->

---

## Architecture / Design Notes
<!-- 
  - Language / framework / runtime (drives which *.instructions.md applies).
  - Which classes/components/modules will be created or modified?
  - Which domain folder / package?
  - Key patterns: dependency injection, event-driven, CQRS, etc.
  - Data flow diagram or description if helpful.
-->


---

## Security & Compliance
<!--
  Answer each item. Write "N/A — <reason>" if genuinely not applicable.
  Do NOT leave blank — unanswered items block Approved status.
-->
- **Authentication / Authorization:** 
- **Data Classification:** <!-- Public | Internal | Confidential | PII | PCI -->
- **Compliance Constraints:** <!-- CCPA, PCI-DSS, HIPAA, SOC2, internal policy -->
- **Secret / Credential Management:** <!-- How are secrets stored and rotated? -->
- **Input Validation & Injection Risk:** 
- **Rate Limiting / Abuse Surface:** 
- **Audit Logging:** <!-- What actions must be logged for compliance? -->

---

## Failure Modes & Rollback
<!--
  Describe what happens when this feature fails, degrades, or is rolled back.
  Do NOT leave blank — unanswered items block Approved status.
-->
- **Expected Failure Scenarios:**
  - [ ] 
- **Degraded / Graceful Fallback Behavior:** 
- **Rollback Strategy:** <!-- Feature flag? Blue/green? DB migration reversible? -->
- **Alerting & On-Call Trigger:** <!-- What condition fires an alert? What team owns it? -->
- **Circuit Breaker / Retry Policy:** 

---

## Dependencies
<!-- Other specs, packages, services, or systems this feature relies on. -->
- None

---

## Open Questions
<!-- Unresolved decisions that need human input before this spec can be Approved. -->
- [ ] 

---

## Governance
<!--
  Populated by the Spec Governor agent at each S→P→E→C gate (one block per gate run).
  No spec reaches Approved without a recorded governance verdict. References only — no secrets/PII.
  Controls are scored against .github/agents/_GOVERNANCE_CATALOG.md.
-->
- **Gate:** S→Approved | P→Approved Plan | E/C→pre-merge
- **Run date:** YYYY-MM-DD   |   **Catalog version:** <pin date from _GOVERNANCE_CATALOG.md>
- **AI classification:** AI-using | Not AI  — *Rationale:* <one line>

| Control ID | Verdict (Pass/Fail/N-A) | Evidence or citation |
|---|---|---|
| GOV-LLM-01 | Pass | <spec §/ plan unit / file:line, or N/A rationale> |
| … (every evaluated control) | … | … |

- **Overall verdict:** Governed ✓ | Blocked ✗ | Governed-with-exception ✓ | Re-blocked ✗ (expired)
- **Exceptions:**
  | Control ID | Owner | Justification | Expiry (≤90d) | Status |
  |---|---|---|---|---|
  | <id> | <name> | <why accepted> | YYYY-MM-DD | active / EXPIRED→escalated |
  *(none → "None")*

---

## Changelog
| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| 1.0     | YYYY-MM-DD |        | Initial draft |
```