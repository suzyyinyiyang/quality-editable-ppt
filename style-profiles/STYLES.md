# Built-In Styles

Built-in style presets for `quality-editable-ppt`.

This package now uses **7 fixed built-in styles + 1 automatic recommendation router**.  
`自动推荐` is not counted as a fixed style; it selects one of the 7 styles based on content and scenario.

These styles are designed to be high-quality, reconstruction-aware, and easy to reproduce in editable PPT.

## Style Index

1. 蓝绿产品发布风
2. 蓝黑科技运营风
3. 紫色科技色块风
4. 紫蓝AI科技风
5. 深蓝深红攻防风
6. 深灰绿色监控风
7. 深灰金色年会风
8. 自动推荐

---

# 1. 蓝绿产品发布风

Use for product launch, version release, capability release, solution overview, and customer-facing product presentations.

## Palette

- Background: light blue / very pale blue gradient.
- Primary blue: `#1135EA`.
- Auxiliary green: `#01B285`.
- Card fill: white or very pale blue.
- Text: deep navy / dark gray.
- Borders: light blue with reduced opacity.

## Visual rules

- Use bold blue and green blocks for page anchors, KPI highlights, capability modules, process numbers, and chart emphasis.
- Use white cards on a light blue background.
- Use `#1135EA` as the primary chart series and `#01B285` as positive/automation/closed-loop accent.
- Use clear product UI language: launch cards, capability tags, large headline, hero product visual.
- Reconstruction difficulty: low to medium.

---

# 2. 蓝黑科技运营风

Use for SOC, AI security operations, command center, threat response, endpoint operations, and dashboards.

## Palette

- Background: deep navy / blue-black.
- Primary accent: cyan-blue / electric blue.
- Auxiliary accent: restrained green for healthy/success states.
- Cards: dark panels with blue/cyan borders.
- Text: white / light blue-gray.

## Visual rules

- Use dark operational dashboard panels.
- Keep glow restrained and structured; avoid excessive neon haze.
- Use grid lines, telemetry, status dots, and dashboard modules.
- Charts should use blue/cyan as main series, with red/orange only for risk.
- Reconstruction difficulty: medium.

---

# 3. 紫色科技色块风

Use for formal technology solution pages, AI product introductions, modern consulting-style tech pages, and high-impact color-block layouts.

## Palette

- Background: light purple / very pale lavender.
- Primary purple: `#5D08D8`.
- Auxiliary blue: `#1135EA`.
- Card fill: white / very pale lavender.
- Text: dark navy / purple-black.
- Borders: light purple or blue with reduced opacity.

## Visual rules

- Replace the old blue-white block style with a stronger purple technology block style.
- Use `#5D08D8` for main title emphasis, section bars, process numbers, KPI highlights, and major chart series.
- Use `#1135EA` as auxiliary color for secondary charts, contrast blocks, and supporting icons.
- Prefer flat blocks, clear cards, bold section anchors, and reconstructable geometry.
- Avoid dark dashboard styling unless requested.
- Reconstruction difficulty: low.

---

# 4. 紫蓝AI科技风

Use for AI platform, AI agent, model capability, data intelligence, knowledge center, and intelligent decision-making themes.

## Palette

- Background: deep blue / purple-blue / AI dark gradient, or pale AI-tech background when the page needs to be light.
- Primary: purple-blue gradient.
- Auxiliary: bright violet, electric blue, cyan highlights.
- Text: white on dark background or deep navy on light background.
- Cards: dark translucent AI panels or clean light cards depending on chosen layout.

## Visual rules

- Use AI core / neural network / data intelligence visual language.
- Purple and blue should form the main atmosphere.
- Glow may be used but must remain reconstructable.
- Keep title, labels, cards, and charts separate from hero illustration.
- Reconstruction difficulty: medium.

---

# 5. 深蓝深红攻防风

Use for attack-defense, threat analysis, ransomware protection, red-blue confrontation, risk warning, and emergency response pages.

## Palette

- Background: `#E3E6ED`.
- Primary deep blue: `#123371`.
- Auxiliary deep red: `#B81615`.
- Card fill: white / very light gray-blue.
- Text: deep navy / dark gray.
- Borders: light blue-gray; red only for risk/attack/high-severity markers.

## Visual rules

- Keep the page light and businesslike; do not turn the whole page into a dark red-blue dashboard unless explicitly requested.
- Use `#123371` as the main structural color for titles, headers, charts, and major lines.
- Use `#B81615` for attack side, high-risk tags, warning highlights, and red-team indicators.
- Use red as an accent, not as large card fill.
- Great for side-by-side attack/defense diagrams.
- Reconstruction difficulty: low to medium.

---

# 6. 深灰绿色监控风

Use for monitoring, compliance status, asset health, terminal state, audit, and operations control pages.

## Palette

- Background: `#E9EDF1`.
- Primary green: `#01B285`.
- Auxiliary dark gray: `#61696A`.
- Card fill: white / very light gray.
- Text: dark gray / charcoal.
- Borders: light gray or green with reduced opacity.

## Visual rules

- Use green for normal/healthy/closed-loop/automation states.
- Use `#61696A` for structural blocks, header strips, neutral labels, and background contrast.
- Avoid excessive decorative glow.
- Prefer monitoring cards, clean tables, status chips, progress bars, and line/bar charts.
- Reconstruction difficulty: low.

---

# 7. 深灰金色年会风

Use for annual summary, strategy release, awards, executive reporting, and ceremonial company presentations.

## Palette

- Background: `#342D2B`.
- Primary gold: `#C9A24D`.
- Auxiliary light gray/beige: `#E8E2D8`.
- Card fill: dark gray-brown panels.
- Text: gold / warm light gray.
- Borders: gold lines with reduced opacity.

## Visual rules

- Use restrained luxury: gold accents, dark panels, elegant dividers, and premium typography.
- Avoid colorful cyber dashboards.
- Charts should use gold as main series and warm gray as comparison series.
- Good for strategy, annual meeting, executive summary, and milestone pages.
- Reconstruction difficulty: medium.

---

# 8. 自动推荐

`自动推荐` is a style router, not a fixed visual style.

## Routing suggestions

- Product launch / version release / capability release → `蓝绿产品发布风`.
- SOC / terminal security operations / command center / dashboard → `蓝黑科技运营风`.
- Formal tech solution / modern color-block page / customer proposal → `紫色科技色块风`.
- AI platform / AI agent / model capability / intelligence center → `紫蓝AI科技风`.
- Attack-defense / red-blue confrontation / threat response / ransomware → `深蓝深红攻防风`.
- Monitoring / compliance / asset health / status overview → `深灰绿色监控风`.
- Annual summary / strategic release / ceremony / executive event → `深灰金色年会风`.

When the user chooses `自动推荐`, briefly state the selected style before producing the visual blueprint.
