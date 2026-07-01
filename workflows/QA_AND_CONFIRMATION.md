# QA and Confirmation

This file consolidates confirmation and QA rules. Mandatory checkpoints remain unchanged: Gate 1 outline, Gate 2 visual blueprint, Gate 3 preview, Gate 4 element/chart/table/detail confirmation, Gate 5 asset confirmation, Gate 6 first 1-3 pages render confirmation.


---

<!-- Source: templates/step-1-4-selfcheck-template.md -->


# Step 1.4 Missing Element Self-Check

For each slide, check and report:

- [ ] All charts are inventoried.
- [ ] All icons are inventoried.
- [ ] All card shadows/glow/borders are recorded.
- [ ] All page numbers and footers are recorded.
- [ ] All bottom bars/conclusion bars are recorded.
- [ ] All connectors/nodes/arrows are recorded.
- [ ] All small card inset illustrations are recorded.
- [ ] Background texture/glow is recorded separately from text.
- [ ] No planned image asset contains editable text.


---

<!-- Source: quality-control/render-compare-checklist.md -->


# Render Compare Checklist

Compare rendered PPTX to locked reference:

- [ ] layout;
- [ ] background;
- [ ] color blocks;
- [ ] card styles;
- [ ] icons;
- [ ] charts;
- [ ] shadows/glow;
- [ ] text placement;
- [ ] page chrome;
- [ ] visual density.

Slides 1-3 must be rendered and confirmed before remaining slides are built.

## Detail-fidelity additions

- [ ] Card colors, shadows, glows, and borders match.
- [ ] Complex hero illustrations are present and visually close.
- [ ] Header beam lines and title separators are present.
- [ ] Icon badges include background, glyph, glow/state dot if present.
- [ ] Background assets do not include card wireframes or editable structures.


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
