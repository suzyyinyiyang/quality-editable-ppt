# Checklists

All quality checklists are consolidated here. No checklist requirement has been removed.


---

<!-- Source: quality-control/preview-complexity-budget.md -->


# Preview Complexity Budget

Default limits per slide:

- Complex hero illustration: max 1.
- Complex charts: max 2.
- Cards: max 8.
- Small icons: max 20.
- Main color families: max 3.
- Font hierarchy: max 4.
- Background: solid / native gradient / full-slide texture image.

If exceeded, warn and suggest splitting or simplifying before generating preview images.


---

<!-- Source: quality-control/reconstructable-preview-checklist.md -->


# Reconstructable Preview Checklist

- [ ] Uses bold color blocks.
- [ ] Uses flat icons or faithful PNG/SVG icon assets.
- [ ] Background and content are separated.
- [ ] Text is not embedded inside hero illustration unless the hero is a deliberate complex fused asset whose intrinsic text is preserved for fidelity.
- [ ] Charts are standard and readable.
- [ ] Cards have clear boundaries.
- [ ] No excessive microtext.
- [ ] No poster-like fused background.
- [ ] Visual blueprint exists before preview generation.


---

<!-- Source: quality-control/chart-reconstruction-checklist.md -->


# Chart Reconstruction Checklist

- [ ] Every visible chart has a chart_id.
- [ ] Chart type is identified.
- [ ] Chart bbox is recorded.
- [ ] Chart labels and legends are recorded.
- [ ] Implementation method is selected.
- [ ] Chart is present in final PPT render.
- [ ] If chart is PNG, key title/labels remain editable when practical.


---

<!-- Source: quality-control/native-chart-data-binding-checklist.md -->


# Native Chart Data Binding Checklist

- [ ] Every standard chart has `chart_id`.
- [ ] Every standard chart has data source recorded.
- [ ] Categories, series, values, labels, and colors are recorded.
- [ ] Native PPT chart is used when reliable data exists and the tool supports native charting.
- [ ] If a shape-based chart is used, a CSV/JSON data file is still provided.
- [ ] If data is estimated from image geometry, confidence is marked and user confirmation is requested in Gate 4.
- [ ] Chart title and labels remain editable whenever practical.
- [ ] Visual overlays do not block chart data editability unless explicitly justified.


---

<!-- Source: quality-control/native-table-checklist.md -->


# Native Table Checklist

- [ ] Every visible real table has `table_id`.
- [ ] Header row is recorded.
- [ ] Cell values are recorded.
- [ ] Row/column count is recorded.
- [ ] Column widths and row heights are approximated.
- [ ] Header/body/border styles are recorded.
- [ ] Native PPT table is used when the presentation tool supports it.
- [ ] If shape fallback is used, CSV/JSON table data is still exported.
- [ ] Icons/badges inside cells are overlaid as separate objects when practical.
- [ ] The final PPT render does not replace a real table with disconnected rectangles/lines when native table support is available.


---

<!-- Source: quality-control/icon-reconstruction-checklist.md -->


# Icon Reconstruction Checklist

- [ ] Every visible icon has an icon_id.
- [ ] Icon position and size recorded.
- [ ] Icon style recorded.
- [ ] Implementation selected: SVG/PNG/image_gen (native redraw is not the default for small icons).
- [ ] Small icon body is not replaced by font glyphs, emoji, or rough primitive shapes.
- [ ] Complex icons have clean PNG or SVG assets.
- [ ] Small icons match preview silhouette/style closely.
- [ ] No visible icon is omitted in final PPT render.


---

<!-- Source: quality-control/card-effect-checklist.md -->


# Card Effect Checklist

For every card/panel:

- [ ] fill color recorded;
- [ ] border recorded;
- [ ] radius recorded;
- [ ] opacity recorded;
- [ ] shadow recorded;
- [ ] glow recorded if present;
- [ ] divider recorded if present;
- [ ] highlight line recorded if present;
- [ ] render matches reference card style.


---

<!-- Source: quality-control/hero-asset-checklist.md -->


# Hero Asset Checklist

- [ ] Complex hero illustrations are not redrawn as low-fidelity PPT shapes.
- [ ] Default method is image_gen / image2 regenerated transparent PNG.
- [ ] The generated PNG has transparent background.
- [ ] The asset contains no editable text, labels, numbers, cards, chart axes, page number, or module borders.
- [ ] The asset visually matches the locked preview composition and colors.
- [ ] If generation is not close enough, retry before using crop fallback.
- [ ] Crop fallback is only used when clean and uncontaminated.


---

<!-- Source: quality-control/background-purity-checklist.md -->


# Background Purity Checklist

A background asset may contain only color, gradient, texture, grid, glow, dot pattern, and atmosphere.

It must not contain:

- [ ] card borders;
- [ ] table lines;
- [ ] chart axes;
- [ ] buttons;
- [ ] labels;
- [ ] title text;
- [ ] page numbers;
- [ ] editable structures;
- [ ] module frames.

If any item appears, regenerate or split the background.


---

<!-- Source: quality-control/text-contamination-checklist.md -->


# Text Contamination Checklist

Layer A assets must not contain editable text unless unavoidable.

Check every asset for:

- [ ] title text;
- [ ] body text;
- [ ] KPI number;
- [ ] chart label;
- [ ] legend text;
- [ ] page number;
- [ ] footer text.

If contaminated, recrop, regenerate, or split into asset + editable text.


---

<!-- Source: quality-control/detail-fidelity-checklist.md -->


# Detail Fidelity Checklist

Check before final delivery:

- [ ] Hero illustrations match preview and use clean transparent PNG assets when complex.
- [ ] Card colors/gradients/borders/shadows/glows match the preview.
- [ ] Icon badge backgrounds and gradient icons are reconstructed.
- [ ] Header beams, title separators, and corner lines are present.
- [ ] Background assets are clean and not polluted with card frames or text.
- [ ] Small status dots, legends, labels, and decorative details are not omitted.
- [ ] Detail density is close to the locked reference.


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
- [ ] Complex hero visuals with intrinsic text were kept fused when separation would blur or degrade them.
- [ ] Header beam lines and title separators are present.
- [ ] Icon badges include background, glyph, glow/state dot if present.
- [ ] Background assets do not include card wireframes or editable structures.

---

# Hero Escalation Checklist

- [ ] Complex hero illustration was not started as native-shape reconstruction.
- [ ] image_gen / image2 transparent PNG was attempted first.
- [ ] If regenerated output drifted, a stricter retry was attempted.
- [ ] If regeneration still failed, source-faithful crop fallback was used.
- [ ] Crop fallback was cleaned/masked or marked as source-faithful approved.
- [ ] First 1-3 page render was checked for hero fidelity failure.
- [ ] Bad native hero illustrations were replaced before continuing.

---

# Asset Seamless Integration Checklist

- [ ] Background-integrated visuals are placed in full-slide/local background assets.
- [ ] Independent hero visuals are transparent PNG assets when possible.
- [ ] Source crop fallback is not a raw rectangular screenshot.
- [ ] Crop edges are transparent, feathered, or background matched.
- [ ] No visible color mismatch exists between crop and PPT background.
- [ ] No hard glow cutoff exists.
- [ ] No text/card/chart/table pollution appears inside image assets.

# Card Color Sampling Checklist

- [ ] Card colors are sampled from the locked preview.
- [ ] Page-level color tokens are created.
- [ ] Card fill, gradient, border, shadow, and glow are recorded.
- [ ] Final render card colors are patched if visually different.
- [ ] Style palette tokens follow `style-profiles/STYLES.md`.


# Lightweight Lock Checklist

- [ ] Every confirmed preview/source image has a project-local `local_file`.
- [ ] `local_file` exists and SHA-256 matches the registry.
- [ ] Phase 3 build input summary lists locked reference paths and approved asset paths.
- [ ] Gate 6 shows locked source and exported PPT render side by side.


# Unified 3A Checklist

- [ ] After lock, the task entered Unified 3A Replica Flow.
- [ ] Original mode is used only to explain how the reference was created.
- [ ] Single/multi/full-PPT reconstruction is handled by batching, not by switching workflows.
- [ ] Max repair rounds and build attempts are respected unless the user explicitly requests strict mode.

---

# Restored Detail-Replica QA Checklist

## Screenshot-only rejection

- [ ] Final PPT is not a single full-slide screenshot when the reference contains editable content.
- [ ] Visible charts/tables/cards/icons/flows are represented as native/editable structures or appropriate separate assets.

## Background

- [ ] Textured / atmospheric background is preserved as a clean background asset when needed.
- [ ] Background is not flattened into a plain solid/generic gradient.
- [ ] Background asset contains no editable content.

## Hero / main visual

- [ ] Complex hero is present and visually close to the locked reference.
- [ ] Hero route is crop / transparent PNG-SVG regeneration / background-fused asset.
- [ ] Hero is not simplified into generic native circles/shapes.
- [ ] Cropped/fused hero edges are feathered or alpha-softened when needed.
- [ ] Hero asset contains no residual title, labels, pseudo-text, or duplicated numbers.

## Icons

- [ ] Every visible icon is represented.
- [ ] Simple filled/line/geometric icons are native shapes/freeforms or editable SVG when practical.
- [ ] Complex icons are clean PNG/SVG assets.
- [ ] Icon captions and labels remain editable text.

## Cards and PPT components

- [ ] Cards/panels/KPI blocks preserve size, position, border, shadow, radius, fill, padding, and text hierarchy.
- [ ] Arrows, connectors, chips, process nodes, progress bars, and conclusion bars are native editable components when practical.
- [ ] Simple components are not rasterized into image assets.

## Charts and tables

- [ ] Every visible chart is reconstructed.
- [ ] Native PPT charts are used when data is readable or recoverable.
- [ ] Every visible table is reconstructed.
- [ ] Readable real tables are native PPT tables when practical.

## Layout

- [ ] Major page composition matches the locked reference.
- [ ] No semantic re-layout after lock.
- [ ] Source vs PPT render comparison is shown before delivery.

---

# v5.0 强化版复原检查清单

## 背景图

- [ ] 有纹理 / 网格 / 点阵 / 光效 / 波纹背景被保留为干净背景资产。
- [ ] 背景资产没有文字、卡片边框、表格线、图表轴线、标签、页码和可编辑结构。
- [ ] 没有把有纹理背景简化成纯色或普通渐变。

## 视觉资产

- [ ] 主视觉没有被低保真原生形状重画。
- [ ] 主视觉采用透明 PNG/SVG、source-faithful 裁切或背景融合资产。
- [ ] 裁切资产无硬矩形边缘、无色差、无硬切光效。
- [ ] 资产里没有残留文字、伪文字、数字、卡片、图表或表格污染。

## 图标

- [ ] 所有可见小 icon 均已复原。
- [ ] 简单线性 / 面型 icon 使用原生 shape / line / editable SVG。
- [ ] 复杂发光 / 3D / 插画 icon 使用干净 PNG/SVG。
- [ ] icon 文字和标签是独立 PPT 文本。

## 卡片与组件

- [ ] 卡片颜色从参考图采样，而不是只按风格猜。
- [ ] 卡片尺寸、边框、投影、圆角、内边距、分割线和图文对齐接近参考图。
- [ ] 箭头、连接线、流程节点、标签、状态 chip 尽量是原生可编辑组件。

## 可编辑底线

- [ ] 最终 PPT 不是一张整页截图。
- [ ] 标题、正文、KPI、图例、标签是 PPT 文本。
- [ ] 可读表格为原生 PPT 表格。
- [ ] 标准图表为原生 PPT 图表或可编辑近似图表。
- [ ] 源图与 PPT 渲染对照中，视觉接近不是靠整图贴图实现的。

---

# Primary Asset and Component QA Checklist

## Background

- [ ] Textured / gradient atmosphere / light beam / glow / haze / grid / dot map / wave / curved-line background is a clean full-slide background asset.
- [ ] Pure color or simple gradient background uses native PPT fill.
- [ ] Background asset contains no editable text, KPI, cards, table lines, chart axes, labels, icons, or flow nodes.

## Hero edge blending

- [ ] Independent hero asset has no white edge, gray edge, color fringe, hard crop border, or background residue.
- [ ] Hero asset has no residual title, label, pseudo-text, duplicated number, or icon caption.
- [ ] Hero boundary uses light feathering / alpha soft edge when needed.
- [ ] Hero internal details remain sharp.
- [ ] Environment shadow/glow/contact light blends the hero with the page when needed.

## Icons

- [ ] No Unicode symbols, emoji, or icon-font characters are used as substitutes for visual icons.
- [ ] Every visible icon is represented.
- [ ] Icon base/background and icon body are handled separately.
- [ ] Simple line/filled/geometric icons are native shapes/lines/freeforms or editable SVG when practical.
- [ ] Complex icons are clean transparent PNG/SVG assets.
- [ ] Icon captions/numbers/labels are editable PPT text.


## Micro charts / sparklines

- [ ] Mini trend charts and KPI sparklines are not built from multiple disconnected straight line segments.
- [ ] Data-readable micro charts use native PPT line charts with axes/gridlines hidden when appropriate.
- [ ] Decorative sparklines use one continuous PPT freeform/curve, editable SVG path, or clean transparent SVG/PNG asset.
- [ ] Stroke color, opacity, line width, smoothing/angular style, glow, marker dots, endpoint style, and bounding box match the reference.
- [ ] Small trend graphics are not omitted, replaced by generic waves, or changed into unrelated arrows.

## Tables

- [ ] Native table line color matches the reference.
- [ ] Inner grid line color, width, and opacity match the reference.
- [ ] Header fill, row fill, row height, column width, and cell padding match the reference.
- [ ] Status dots and risk-level chips are reconstructed.

## Cards/components

- [ ] Cards, panels, KPI blocks, chips, process nodes, arrows, connectors, and progress bars preserve size, border, shadow, radius, fill, padding, and density.



---

# Title-Bar Fidelity Checklist

- [ ] Complex gradient/glow/glass title bars are treated as whole PNG assets.
- [ ] Title-bar border, glow, beam, and corner decorations match preview.
- [ ] If title text is fused into the complex title bar, it remains visually intact.
- [ ] Simple title regions only use native editable text when clearly separable.

---

# Current-Run Preview Lock Checklist

- [ ] Locked preview files come from the current run only.
- [ ] No older preview image was silently mixed into the lock registry.
- [ ] The confirmed preview list matches the newly generated files shown in the current conversation.
- [ ] Reconstruction reads the current lock set rather than historical preview files.


---

# v5.16 Light Main Constraint Checklist

## Image generation

- [ ] Gate 3 used a real image-generation capability.
- [ ] No tool-availability precheck, environment scan, tool enumeration, package check, or tool-registry lookup was performed.
- [ ] No unrelated system tool discovery was attempted before Gate 3.
- [ ] No local SVG/PNG/canvas/HTML/script fallback was used as the high-visual preview.

## Current-run preview lock

- [ ] Locked preview comes only from the current run / current conversation step.
- [ ] No old preview or stale locked reference was mixed in.

## Complex background

- [ ] Pure color/simple gradient may be native.
- [ ] Any texture/glow/grid/line/dot/particle/haze/beam/complex atmosphere background is preserved as a full-slide image.
- [ ] Complex background was not redrawn with many PPT shapes.

## Complex title bar

- [ ] Complex gradient/glow/glass/texture title bar is captured as PNG.
- [ ] Captured title-bar edges are feathered/softened when needed.

## Small icons

- [ ] Complex small icons use PNG/SVG assets.
- [ ] Unicode, emoji, icon-font, primitive-shape, or disconnected-line substitutes are not used.
- [ ] Captured icon edges are feathered/softened when needed.

## Captured assets

- [ ] Captured hero/title/icon/badge/card/label assets have no hard crop seams.
- [ ] White/gray/color fringe edges were removed.
- [ ] Internal details remain sharp.

## Charts

- [ ] Standard charts use native PPT chart components whenever practical.
- [ ] If chart and icon overlap, chart remains native and icon is separated as PNG/SVG.
- [ ] Shape-drawn chart downgrade is disclosed to the user for acceptance.

## Downgrade transparency

- [ ] If expected image assets or native charts were replaced by shape redraw, the user was asked to accept or reject the downgrade.


---

# v5.17 Stable Lock Checklist

## Visual priority

- [ ] Locked preview is treated as the only visual source.
- [ ] PPT render did not redesign from topic, outline, or style.
- [ ] Visual fidelity was prioritized before native-shape convenience.

## Layer A — Background

- [ ] Pure color/simple gradient only was native PPT background.
- [ ] Lines/dots/grid/glow/texture/haze/particles/technology patterns were fused into full background image.
- [ ] Complex background was not redrawn as many PPT shapes.
- [ ] If clean extraction was impossible, image generation was used to recreate clean background.

## Layer B — Complex assets

- [ ] Complex hero/main visual was not shape-redrawn.
- [ ] Complex title/header chrome was assetized if needed.
- [ ] Complex icon badges with glow/gradient/base/shadow were PNG/SVG or very faithful native.
- [ ] Complex pyramid/process/dashboard modules were assetized or matched faithfully.

## Edge treatment

- [ ] Hero/irregular cutouts use soft edge only when needed.
- [ ] Complex title bars keep crisp edges and are not feathered by default.
- [ ] Glass cards keep crisp rounded edges and are not feathered by default.
- [ ] Simple line/filled icons are not feathered.
- [ ] Small badges/label icons are not feathered.

## Layer C — Native editable objects

- [ ] Text and numbers remain editable where practical.
- [ ] Simple line/filled icons and small label icons use native PPT/SVG continuous paths.
- [ ] No Unicode/emoji/icon-font substitution for designed icons.
- [ ] Native tables are used for real tables where practical.

## Charts

- [ ] Standard charts use native PPT chart components whenever practical.
- [ ] If chart and icon overlap, chart stays native and icon/badge is separate.
- [ ] Chart + icon was not captured as a single image.
- [ ] Shape-drawn chart downgrade was disclosed to user.

## Downgrade confirmation

- [ ] Shape-first downgrade in complex visual areas was not silently delivered.
- [ ] User was asked to accept, reject, or mix downgraded implementation.
- [ ] Targeted repair was used instead of whole-slide redesign.


---

# v5.18 Mode 3 Clean Layer Lock Checklist

## Full-slide screenshot

- [ ] The locked preview was used as reference, not final full-slide background.
- [ ] No whole-page screenshot background was silently delivered.
- [ ] If whole-page screenshot overlay was used, the user explicitly approved it as a downgrade.

## Clean background

- [ ] Background asset contains only background/atmosphere elements.
- [ ] Background asset does not contain title/body text, KPI values, cards, charts, tables, icons, hero, process nodes, legends, or labels.
- [ ] If clean extraction was unreliable, image generation was used to recreate clean background or user approval was requested for downgrade.

## Layer A/B/C plan

- [ ] Each Mode 3 slide has a Layer A/B/C plan before PPT generation.
- [ ] Layer A route is recorded.
- [ ] Layer B visual assets are listed.
- [ ] Layer C editable native objects are listed.

## Foreground rebuild

- [ ] Hero/main visuals were independently rebuilt or explicitly classified.
- [ ] Complex icon badges were independently rebuilt or explicitly classified.
- [ ] Simple icons/small labels used native PPT or SVG continuous paths when appropriate.
- [ ] Foreground objects were not skipped just because they appeared in the screenshot.

## OCR icon quarantine

- [ ] OCR-derived icon-like text was not used as final icon.
- [ ] Icon-like placeholders were reclassified from source regions.
- [ ] No font-style icon substitutes were delivered.

## Charts and tables

- [ ] Standard charts were rebuilt as native PPT charts whenever practical.
- [ ] Real tables were rebuilt as native PPT tables whenever practical.
- [ ] Screenshot-backed or shape-drawn chart/table downgrades were disclosed.

## First 1–3 page check

- [ ] Background route was reported.
- [ ] Asset route was reported.
- [ ] Native chart/table status was reported.
- [ ] Any full-slide screenshot overlay or shape downgrade was reported for user approval.


---

# v5.19 Background and Icon Lock Checklist

## Background

- [ ] Pure solid background only uses native PPT fill.
- [ ] Any non-solid background was recreated by image generation as clean background.
- [ ] Background was not produced by erasing foreground from screenshot.
- [ ] Background contains no old text, cards, charts, tables, icons, hero, labels, or residue.
- [ ] Full-slide screenshot was not used as final background.

## Icons

- [ ] Simple line/filled icons are transparent PNG or SVG continuous paths.
- [ ] Simple icon backgrounds are native PPT shapes.
- [ ] Complex glowing/gradient/glass icon badges are combined transparent PNG when needed.
- [ ] No Unicode, emoji, icon-font, Chinese-character placeholder, or broken-line substitute.
- [ ] Icon crops are complete and not clipped.
- [ ] Simple icons are not feathered or shrunk.

## Chart/icon overlap

- [ ] Donut/ring/pie/bar/line/area/radar/sparkline charts are native PPT charts whenever practical.
- [ ] Icons are separated from charts.
- [ ] Chart + icon was not captured as one screenshot.
- [ ] Shape-drawn chart downgrade was disclosed to user.

## Downgrade

- [ ] If image generation was unavailable for non-solid background, user was asked for downgrade approval.
- [ ] If complete icon reconstruction was not possible, user was asked for downgrade approval.
- [ ] If native chart reconstruction was not possible, user was asked for downgrade approval.


---

# v5.20 Visual Asset QA Lock Checklist

## Background
- [ ] Pure solid background uses native PPT fill.
- [ ] Every non-solid background uses real image generation as raster clean background.
- [ ] Local SVG/canvas/script/PPT-shape background was not used unless user approved downgrade.
- [ ] Background prompt matched locked preview atmosphere.
- [ ] Clean background contains no foreground residue or content.

## Hero / main visual
- [ ] Slide hero/main visual was identified by role.
- [ ] Hero/main visual was assetized by default.
- [ ] No hero/main visual was natively redrawn merely because it contains geometry.
- [ ] Any native hero redraw is near-identical or user-approved as downgrade.

## Icons
- [ ] Simple line/filled icons are SVG continuous paths or transparent PNG.
- [ ] Simple icon bases are native PPT shapes when appropriate.
- [ ] Complex glowing/gradient/halo/glass/shadow badge icons are combined transparent PNG.
- [ ] Complex icon assets are complete, not clipped, and include badge/glow boundaries.
- [ ] No Unicode, emoji, icon-font, Chinese-character placeholder, broken fragment, or incomplete crop.

## Charts and tables
- [ ] Standard charts are native PPT charts whenever practical.
- [ ] Chart+icon regions are separated, not combined screenshots.
- [ ] Real tables are native PPT tables whenever practical.
- [ ] Shape-drawn or screenshot-backed charts/tables are marked as downgrade.

## Asset preview
- [ ] Complex slides include compact visual asset preview in the first 1–3 page checkpoint.
- [ ] Asset preview includes clean background, hero asset, complex icon badges, chart/table status, and downgrade list.
- [ ] Asset preview is compact and does not become a new workflow.

## QA summary
- [ ] First 1–3 page checkpoint includes explicit QA summary.
- [ ] QA uses pass/fail/downgrade labels.
- [ ] QA reports background route, hero route, icon route, chart route, table route, and downgrade list.
- [ ] Batch generation did not continue when QA was missing or unapproved downgrades remained.

---

# v5.21 Small Icon SVG Lock Checklist

## Small simple icons

- [ ] Small simple line icons use SVG continuous path first.
- [ ] Small simple filled icons use SVG continuous path first.
- [ ] Transparent PNG is used only when SVG is unreliable.
- [ ] Screenshot crop is not used by default for small simple icons.
- [ ] Any screenshot-cropped small icon is disclosed as downgrade.

## SVG quality

- [ ] SVG paths are continuous and complete.
- [ ] Stroke width matches the locked preview.
- [ ] ViewBox includes safe padding.
- [ ] No clipped edges.
- [ ] No broken/disconnected line fragments.
- [ ] No Unicode, emoji, icon-font, or Chinese-character placeholder.

## PNG fallback quality

- [ ] Transparent PNG fallback has complete contour.
- [ ] No dirty background fringe.
- [ ] Sharp at final display size.
- [ ] No feathering that shrinks or blurs the icon.

## Medium/large and complex icons

- [ ] Medium/large icon crops remain allowed when complete, sharp, and faithful.
- [ ] Complex glowing/gradient/glass/badge icons remain combined transparent PNG when appropriate.

## QA

- [ ] QA reports small icon route: SVG / transparent PNG / screenshot downgrade.
- [ ] Clipped, blurry, incomplete, or inconsistent small icons are marked fail/downgrade.
- [ ] Batch generation does not continue if small icon downgrade is unapproved.


---

# v5.22 Detail Fidelity Checklist

## Small icon likeness

- [ ] Important/repeated small icons have crop/bbox references or explicit visual notes.
- [ ] Icon silhouette, stroke weight, cap/join style, aspect ratio, negative space, badge/glow/halo, and color order match the locked preview.
- [ ] No generic same-meaning icon substitution is used when visually different.
- [ ] Any SVG/PNG fallback is sharp, complete, padded, and visually consistent with the preview icon family.

## Card / panel fidelity

- [ ] Card/panel bbox, radius, fill/gradient/opacity, border, shadow/glow, and elevation are sampled or matched from the locked preview.
- [ ] Equal sizes, row/column gaps, internal translucent bands, decorative dots/waves/dividers, icon positions, and text padding are preserved.
- [ ] No card has downgraded into a plain rectangle unless explicitly accepted as downgrade.

## Text position fidelity

- [ ] Title/subtitle/KPI/card/process/table/chart text preserves x/y anchors, baselines, alignment, size, weight, and line spacing.
- [ ] Icon-text distances and card-edge padding match the locked preview.
- [ ] No automatic reflow or convenience repositioning is visible in Gate 6 render.
