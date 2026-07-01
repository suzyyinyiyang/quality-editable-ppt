# QA Report Templates


---

<!-- Source: templates/chart-data-binding-template.md -->


# Chart Data Binding Template

Use this table in Gate 4 when charts are detected.

| Slide | Chart ID | Type | Data Source | Confidence | Native Chart? | Notes |
|---|---|---|---|---|---|---|
| 02 | slide02_chart01 | column | visual_blueprint | high | yes | Editable data |

If confidence is `estimated` or `low`, ask the user to confirm or correct the values before Phase 2.


---

<!-- Source: templates/table-data-binding-template.md -->


# Table Data Binding Template

Use this table in Gate 4 when real data tables are detected.

| Slide | Table ID | Type | Rows × Columns | Data Source | Confidence | Native Table? | Notes |
|---|---|---|---|---|---|---|---|
| 02 | slide02_table01 | risk_list | 5 × 4 | visible_text | high | yes | Editable cells |

If confidence is `estimated` or `low`, ask the user to confirm or correct the values before Phase 2.


---

<!-- Source: templates/qa-report-template.md -->


# QA Report Template

```markdown
# QA Report

## Gate Summary
- Gate 1 outline confirmed:
- Gate 2 visual blueprint confirmed:
- Gate 3 preview confirmed:
- Gate 4 element inventory confirmed:
- Gate 5 assets confirmed:
- Gate 6 slides 1-3 render confirmed:

## Slide Fidelity
| Slide | Result | Issues | Fixed |
|---|---|---|---|

## Editability
| Slide | Editable text | Editable shapes | Image assets | Notes |
|---|---|---|---|---|

## Failure Checks
- [ ] Visible charts not omitted.
- [ ] Visible icons not omitted.
- [ ] Card shadows/glow not omitted.
- [ ] Text not baked into assets unnecessarily.
- [ ] Background/content separated.
```
