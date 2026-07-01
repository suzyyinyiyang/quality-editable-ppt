# Primary Asset and Component Reconstruction Rules
These are primary reconstruction rules, equal in priority to locked-reference fidelity, native charts, native tables, and screenshot-only rejection. They are not optional patch rules.

### Full Background Asset Rule

When the locked reference background contains any of the following, treat it as a clean full-slide background asset:

- texture;
- gradient atmosphere;
- light beams;
- glow / bloom / haze;
- grid;
- dot map;
- wave lines;
- curved technology lines;
- layered background patterns.

Do not redraw these background details one line at a time. Preserve them as one clean background image whenever they are part of the page atmosphere.

Use native PPT fill only for:

- pure solid backgrounds;
- simple gradients without texture, glow, beam, grid, dot, wave, line, particle, haze, bloom, decoration, overlay, or atmosphere.

The full background asset must be clean: it must not include titles, body text, KPI values, cards, table lines, chart axes, labels, legends, icons, process nodes, or other editable content.


### Complex Title-Bar Asset Rule

If a title bar / header chrome contains compound visual treatment such as complex gradient, glassmorphism, glow, atmospheric stroke, decorative beam lines, corner devices, layered borders, or fused styling, do not redraw the entire title bar with native PPT shapes.

Required handling:

- capture the whole title-bar region as a faithful PNG asset;
- preserve its gradient, glow, beams, corner details, and border treatments;
- if the title text is visually fused into that complex bar, keep the title text inside the title-bar asset;
- only rebuild title text as separate editable text when the bar is visually simple and clearly separable without quality loss.

A title bar that loses its preview gradient logic, glow, or compound header styling fails QA.

### Hero Asset Edge Blending Rule

Independent hero / main visual assets placed as PNG/SVG must be cleaned and blended into the page background.

Required handling:

- remove white edges, gray edges, color fringes, hard crop borders, and old background residue;
- remove residual text, labels, pseudo-characters, duplicated title fragments, numbers, and icon captions from the asset **only when they are contamination and not part of the intended hero design**;
- use light feathering / soft alpha edge only on the asset boundary;
- keep the internal hero details sharp;
- add subtle environment shadow/glow/contact light when needed to match the background;
- if the hero and background are visually inseparable, use a background-fused asset instead of hard-cutting the hero.
- If the hero is a complex 3D / glow / gradient / glass-style visual and includes intrinsic text, keep that text inside the hero asset when separating it would blur or degrade the visual.
- Do not force OCR-style extraction of hero text when the source-faithful crop/regenerated asset is visually more accurate.

A hero asset with visible hard rectangular edges, text contamination, or pasted-on sticker feeling fails QA.

### Icon Reconstruction Rule

Do not use Unicode symbols, emoji, or icon-font characters as substitutes for visual icons in the locked reference.

For every visible small icon:

- the default route is a faithful transparent PNG or SVG asset, not redraw;
- preserve the icon base/background separately from the icon body when that improves fidelity, or keep them together as one PNG/SVG asset when separation degrades fidelity;
- icon base/background may be native PPT only when it visually matches the preview precisely;
- the icon body itself must not be redrawn with font glyphs, emoji, Unicode symbols, rough primitive approximations, or discontinuous line segments;
- if a faithful SVG is available, use it; otherwise use a clean transparent PNG crop;
- icon captions, numbers, and labels should remain separate editable PPT text unless they are intrinsically fused inside the icon artwork.

Do not omit visible icons. Do not replace icons with unrelated circles, dots, emoji, font glyphs, or alternate library icons.

Additional small-icon precision constraints:

- record icon-level crop/bbox references for repeated or important icons;
- preserve silhouette, stroke thickness, stroke cap/join, aspect ratio, negative space, viewBox padding, badge/glow/halo, and color order;
- do not use generic same-meaning icons from another library when their visual family differs;
- if native/SVG reconstruction drifts, switch to transparent PNG or regenerated asset that better matches the locked preview;
- an icon that is semantically correct but visually different fails Gate 6.


### Micro Chart and Sparkline Reconstruction Rule

Mini trend charts, KPI sparklines, tiny decorative line charts, and card-level micro charts must not be drawn as many disconnected straight line segments.

Classify each small trend graphic before reconstruction:

- If it is a real data chart and the data is readable, use a native PPT line chart with axes/gridlines/legend hidden as needed, matching stroke color, line width, markers, smoothing, and chart bounds.
- If it is a decorative sparkline or the data is not readable, use one continuous smooth vector path: PPT freeform/curve, editable SVG path, or clean transparent SVG/PNG asset.
- If the reference sparkline is angular by design, use one continuous polyline path with consistent joins, not multiple independent line objects.

Required visual fidelity:

- preserve the sparkline bounding box and baseline position inside the card;
- preserve stroke color, opacity, thickness, glow, marker dots, and endpoint style;
- preserve whether the line is smooth, angular, stepped, or dotted;
- preserve any small area fill, under-line glow, or mini axis baseline when visible.

Forbidden:

- separate disconnected line segments that create visible seams;
- generic zigzag lines unrelated to the locked reference;
- replacing a sparkline with a plain arrow or decorative wave;
- omitting the mini trend graphic because it is small.

A sparkline with visible segment seams or an unrelated generic shape fails visual reconstruction.

### Native Table Styling Rule

Native tables must preserve visual style, not only editable text.

For readable tables, reconstruct as native PPT tables and match:

- table border color;
- inner grid line color;
- line width;
- line opacity;
- header fill;
- row fill / zebra fill when present;
- row height;
- column width;
- cell padding;
- status dots;
- risk-level chips;
- text alignment and hierarchy.

A native table with generic black/gray lines fails visual reconstruction when the reference uses colored or low-opacity table lines.

### Card and Component Box Model Rule

Cards, panels, KPI blocks, icon badges, status chips, process nodes, arrows, connectors, and progress bars must preserve their visual box model:

- relative size and position;
- fill / opacity / gradient;
- border color and thickness;
- shadow / glow / elevation;
- corner radius;
- inner padding;
- icon-text alignment;
- title/body spacing;
- component density.

A card is not complete just because text exists.

Additional card/panel fidelity constraints:

- sample fill, opacity, gradient, border, glow, and shadow from the locked preview;
- preserve equal-width/equal-height relationships, group alignment, row/column spacing, internal translucent bands, decorative waves/dots/dividers, and icon/text padding;
- if native card reconstruction cannot match glass/glow/depth, use a card background asset with editable text/icons layered above;
- cards fail Gate 6 when they become plain rectangles or when size, spacing, depth, or internal content placement visibly differs.

### Editable Text Position Anchor Rule

After lock, text must follow the locked reference anchors rather than auto-layout convenience. For title, subtitle, KPI label/value, card text, process labels, table text, and chart labels, preserve relative bbox, anchor point, baseline, alignment, font size, weight, line spacing, and distance to paired icons/cards/dividers. Visible text drift, reflow, or hierarchy changes fail Gate 6.


---


## v5.0 强化版复原约束合并

以下规则来自 5.0 强化版中已经验证有效的复原能力，必须作为 5.7 主线的一部分执行，不是额外补丁。

### 1. 背景资产分层

当锁定参考图中存在统一的背景纹理、网格、点阵、光效、波纹、地图或大面积渐变氛围时，背景应作为**干净整张背景图资产**保留。

背景资产只能包含：

- 颜色；
- 渐变；
- 纹理；
- 网格；
- 点阵；
- 光效；
- 波纹；
- 地图轮廓；
- 氛围装饰。

背景资产不得包含：

- 标题 / 正文；
- KPI 数字；
- 卡片边框；
- 表格线；
- 图表坐标轴 / 图例 / 标签；
- 流程节点 / 箭头；
- 按钮 / 状态标签；
- 页码；
- 任何应可编辑的结构。

如果背景资产中混入这些内容，必须重新裁切、重绘或拆分，不能直接进入 PPT 构建。

### 2. 主视觉资产复原

复杂主视觉不能用低保真原生形状强行重画。

AI 中枢、SOC 环、发光大脑、盾牌、芯片、终端设备集群、节点网络、决策引擎、复杂安全场景等，优先进入视觉资产路径：

1. 参考图约束下重新生成透明 PNG / SVG；
2. 如果生成漂移，使用更严格提示重试；
3. 仍然漂移时，使用 source-faithful 高保真裁切；
4. 裁切包含文字、卡片、标签、坐标轴、背景污染时，必须清理 / 蒙版 / 拆分；
5. 两种方式都不理想时，让用户选择。

主视觉资产不能残留标题、标签、伪文字、数字、图表轴线或卡片边框。需要保留的标签必须用独立 PPT 文本重建。

### 3. 裁切与融合边缘

source-faithful crop fallback 不能是生硬矩形截图。

必须使用：

- 透明抠图；
- 羽化边缘；
- 背景匹配裁切；
- 局部背景补丁；
- alpha mask；
- 柔边过渡。

失败特征包括：

- 可见矩形边缘；
- 与 PPT 背景颜色不一致；
- 光效被硬切；
- 资产内有文字 / 卡片 / 图表 / 表格污染；
- 看起来像贴了一块截图。

### 4. 卡片颜色采样与盒模型

卡片和面板颜色必须从锁定参考图采样，不能只根据风格名推断。

需要记录或内部遵循：

- 页面背景色；
- 面板背景色；
- 卡片背景色；
- 卡片边框色；
- 卡片投影 / 发光；
- 主文字色；
- 副文字色；
- 主强调色；
- 辅助强调色。

卡片必须复刻视觉盒模型：

- 尺寸；
- 位置；
- 圆角；
- 边框；
- 投影；
- 发光；
- 高光线；
- 分割线；
- 内边距；
- 图标与文字对齐；
- 标题和正文间距。

如果参考图卡片有阴影 / 发光 / 边框，而 PPT 渲染成普通白色矩形，则该页失败。

### 5. 图标徽章复原

每个可见 icon 都必须进入图标登记和复原，不得省略。

处理规则：

- 简单线性 / 面型 / 单色几何 icon：优先 PPT 原生 shape / line / freeform 或 editable SVG；
- 复杂渐变 / 发光 / 3D / 插画型 icon：透明 PNG / SVG 资产；
- icon 底座、圆环、徽章背景、状态点、光晕应按参考图复刻；
- icon 旁的文字、数字、标签必须独立 PPT 文本，不得烘焙进 icon 图片。

### 6. 构建层级顺序

推荐 z-order：

1. 背景色；
2. 干净整张背景纹理；
3. 主视觉 / 复杂视觉资产；
4. 卡片阴影 / 光晕；
5. 卡片主体；
6. 图表；
7. 图标徽章底座；
8. 图标 glyph；
9. 顶部装饰线 / 标题分割线；
10. 可编辑文字和页面标识。

不要把第 4–10 层提前烘焙进第 2 层背景图。

### 7. 可编辑结构底线

整页截图式输出不是合格结果。

如果锁定参考图里有图表、表格、卡片、icon、流程、文字，而最终 PPT 只有一张大图或少量文本对象，该页必须判定失败并重建。

最低要求：

- 标题 / 正文 / KPI / 标签必须是 PPT 文本；
- 标准图表必须尽量是 PPT 原生图表或可编辑近似图表；
- 可读表格必须是 PPT 原生表格；
- 卡片、面板、箭头、连接线、流程节点必须尽量是 PPT 原生组件；
- 背景、主视觉、复杂 icon 可以是图片资产，但不能包含应可编辑内容。


# Restored Detail-Replica Mainline

This package restores the earlier detail-replica behavior that worked better than screenshot-only hard-lock output.

## Historical fixes kept in mainline

- v5.0 strong lock: locked reference is the visual source of truth.
- v5.1 scope-aware: decide full-background asset, local asset, or native component by visual role.
- detail fidelity branch: background purity, seamless assets, card color sampling, icon badge registry, header decoration registry.
- hero fallback branch: complex hero uses source-faithful crop / regenerated transparent PNG-SVG / background-fused asset.
- chart/table branch: standard charts and readable tables remain native/editable when practical.
- shape/icon branch: simple shapes and simple icons remain native/editable; complex icons are assets.
- v5.4 flow branch: quick outline first; asset confirmation optional.

## Background standard

Use a clean full-slide background asset when the reference has coherent texture, glow, grid, dot map, waves, or atmospheric pattern.

Do not flatten textured backgrounds into plain solid/generic gradients.

Background assets must not include editable text, KPI values, cards, charts, tables, flow nodes, legends, labels, or page numbers.

## Hero / central visual standard

Complex hero visuals must match the locked reference and should not be simplified into generic native circles/shapes.

Choose the most faithful method:

1. clean source-faithful crop when source quality is good;
2. reference-guided transparent PNG/SVG regeneration;
3. background-fused asset when the hero and background light are inseparable.

Remove or avoid residual reference text, labels, pseudo-characters, duplicated title words, and numbers. Keep required labels as separate editable PPT text.

Apply soft-edge/feathering or alpha mask when a cropped/fused asset sits over a background. Do not leave hard rectangular crop edges.

## Icon standard

Every visible icon must be accounted for.

Simple filled icons, line icons, single-color icons, and geometric icons should be native shapes/lines/freeforms or editable SVG when practical.

Complex gradient, glowing, 3D, skeuomorphic, illustration-style, or dense composite icons should be clean transparent PNG/SVG assets.

Do not omit icons, replace them with unrelated dots, or bake icon captions into images.

## Card / component box model

Cards, KPI blocks, panels, chips, badges, process nodes, arrows, connectors, and progress bars must preserve:

- relative size and position;
- fill / opacity / gradient;
- border color and thickness;
- shadow / glow / elevation;
- corner radius;
- inner padding;
- icon-text alignment;
- title/body spacing;
- density.

A card is not complete just because the text exists.

## Chart and table standard

Every visible chart/table in the locked reference must be represented.

Charts preserve chart type, panel geometry, title placement, legend position, axis density, series colors, and plot weight. Use native PPT charts when data is readable or recoverable.

Tables preserve row/column proportions, header styling, fills, borders, status chips, and text hierarchy. Use native PPT tables when readable.

## Screenshot-only failure

A rendered PPT with one large screenshot plus minimal editable text is not a valid high-replica editable PPT.

Reject final delivery if the visible reference includes charts, tables, cards, icons, or flow components that are only present inside one full-slide image.

---

# Scope-Aware Unified 3A Rules

These rules are a flow-level clarification, not a new heavy workflow. They preserve the existing style system, Layer A/B/C, native chart/table rules, hero/background asset rules, card sampling, and detail fidelity rules.

## Reference routing

Mode 1 / 2 / 3 / 4 only decide how references are created. Once preview/source/reference images are locked, reconstruct from the locked image instead of topic, outline, semantic meaning, or generic template logic.

## Scope detection

Before post-lock reconstruction, determine scope:

- `single_slide`: exactly one source image or one target slide. Only build Slide 01; do not use 1-3 page wording.
- `multi_slide`: multiple locked images. Work in the current batch.
- `deck_batch`: full deck or many pages. Use first 1-3 pages as checkpoint, then 3-5 page batches.

Scale by batching slides, not by switching to another workflow.

## Source quality decision

A locked reference is not automatically a final image asset.

- Clear source: source-faithful crops may be used when they improve fidelity and do not contain editable text contamination.
- Blurry / low-resolution source: treat as reference-only for layout and content. Rebuild clean background and regenerate/redraw key hero or icon assets instead of using the blurry full-slide image as the final background.

## Asset role plan

Assign each visible region one role before building:

- `reference_only`;
- `native_editable_object`;
- `regenerated_clean_asset`;
- `source_crop_asset`;
- `background_asset`.

Flat PPT-like components must be reconstructed by visual geometry: position, size, fill, border, radius, shadow, opacity, z-order, text, font size, and alignment. This includes cards, KPI blocks, step cards, progress bars, conclusion bars, icon badges, arrows, lists, and title blocks.

Before Phase 3, verify that the PPT build references the approved locked reference, current reconstruction plan / element inventory, and current approved assets.

---

# Reconstruction Rules

Merged optimization rules for charts, tables, hero assets, card styles, icon badges, header decorations, and detail fidelity. These rules are additive and must not reorder the main workflow.


---

<!-- Source: workflows/06b-chart-data-binding.md -->


# 06b — Chart Data Binding Optimization

This is a safe optimization layer on top of the existing Phase 1 analysis. It must not replace, reorder, or weaken the existing high-fidelity reconstruction workflow.

## Goal

When a slide contains standard charts, bind the chart visual to editable chart data whenever possible.

## Standard chart priority

Use native editable PPT charts for:

- donut / pie charts;
- column charts;
- bar charts;
- line / area charts;
- simple radar charts;
- simple scatter charts.

Progress bars and KPI cards may remain PPT shapes, but their numbers should still be editable text.

## Data source priority

1. `visual_blueprint.json` chart data.
2. Visible chart labels and values in locked reference.
3. Geometry-based estimation when data labels are missing.
4. User-provided correction if confidence is low.

## Required output

Create or update:

```text
chart_registry.json
charts/slideXX_chartYY_data.csv
charts/slideXX_chartYY_config.json
```

## Implementation priority

1. Native PPT chart with editable data.
2. Native PPT chart + overlay shapes for exact visual styling.
3. Shape-based chart + editable CSV/JSON data fallback.
4. PNG chart only for decorative or unrecoverable charts.

Do not convert a recoverable standard chart into pure shapes without data binding.


---

<!-- Source: workflows/06c-native-table-reconstruction.md -->


# 06c — Native Table Reconstruction Optimization

This is a safe optimization layer on top of Phase 1 analysis. It must not replace or reorder the existing high-fidelity reconstruction workflow.

## Goal

When a slide contains real tabular data, use native PowerPoint table components whenever possible so cell data remains editable.

## Native table priority

Use native PPT tables for:

- data tables;
- comparison tables;
- risk lists;
- asset lists;
- event records;
- capability matrices that are truly tabular;
- status tables with rows/columns.

## Data source priority

1. `visual_blueprint.json` table data.
2. Visible headers and cell values from locked reference.
3. User-provided corrections when OCR/visual extraction is uncertain.

## Required output

Create or update:

```text
table_registry.json
tables/slideXX_tableYY_data.csv
tables/slideXX_tableYY_config.json
```

## Implementation priority

1. Native PPT table with editable cell data.
2. Native PPT table + overlay icons/badges for visual fidelity.
3. Shape-based table only if native table construction is unavailable, plus CSV/JSON data fallback.
4. PNG table only for decorative or unrecoverable tables.

Do not convert a recoverable real data table into pure rectangles and lines.


---

<!-- Source: workflows/07b-detail-fidelity-optimization.md -->


# 07b — Detail Fidelity Optimization

This is an additive optimization layer. It must not replace the existing reconstruction workflow.

## Goal

Improve the last 5-15% of visual fidelity while preserving the current high-fidelity pipeline.

## Runs inside

- Phase 1: identify detail fidelity items.
- Phase 2: prepare clean assets and style registries.
- Phase 3: build objects in the correct z-order.
- QA: compare detail fidelity before delivery.

## Required inventories

Create or update:

```text
hero_illustration_inventory.json
card_style_registry.json
icon_badge_registry.json
header_decoration_registry.json
background_purity_report.md
detail_fidelity_report.md
```

## Hero illustration policy

Complex hero illustrations must default to image_gen / image2 regenerated transparent PNG assets.

Fallback to crop only when:

- regenerated asset is too different from the locked reference;
- the crop is clean;
- the crop does not contain editable text, labels, card borders, chart axes, or background contamination.

## Build order

Recommended z-order:

1. background color;
2. clean full-slide background texture;
3. regenerated transparent hero PNG;
4. card shadows/glows;
5. card bodies;
6. charts;
7. icon badge backgrounds;
8. icon glyphs;
9. header beam lines and separators;
10. editable text and page chrome.

---

# Hero Illustration Fallback / Escalation Rule

Complex hero illustrations must not be rebuilt first with low-fidelity native PPT shapes. They must enter an asset escalation path before Phase 3.

## Priority

1. image_gen / image2 regenerated transparent PNG.
2. Retry with stricter prompt if composition, glow, node layout, or device placement differs.
3. Source-faithful high-fidelity crop if regeneration still drifts.
4. Crop cleanup/masking/splitting if the crop contains text, cards, labels, axes, or background pollution.
5. User choice if both regenerated and cropped assets are unsatisfactory.

## Native-shape prohibition

Native PPT reconstruction is allowed only for simple geometric illustrations. It is not allowed as the first method for AI hubs, SOC rings, glowing brains, endpoint node networks, decision engines, or complex security hero visuals.

## Failure trigger

If the first 1-3 page render shows a bad native hero illustration, return to Phase 2 and replace it with an image_gen/image2 PNG or a source-faithful crop before continuing.

---

# Background Integration and Asset Seamless Integration

Classify visual elements before asset creation:

- Background-integrated visuals: SOC rooms, environment photos, floor rings, global glow, wall screens, large atmosphere. Use full-slide background assets or local background patches.
- Independent hero visuals: AI core, device node cluster, shield, glowing brain, badge-like hero object. Use transparent PNG.
- Structural content: text, cards, charts, tables, labels, legends, arrows, page numbers. Keep PPT-native/editable whenever practical.

Source-faithful crop fallback must not be a raw rectangle. It must use transparent cutout, feathered edge, background-matched crop, or local background patch.

Failed crop indicators:

- visible rectangular seam;
- color mismatch with PPT background;
- hard-cut glow;
- text/card/chart/table pollution;
- pasted screenshot appearance.

# Card Color Sampling and Token System

Card and panel colors must be sampled from the locked preview. Do not infer them only from the style name.

Record page-level tokens:

```json
{
  "page-bg": "#...",
  "panel-bg": "#...",
  "card-bg": "#...",
  "card-border": "#...",
  "card-glow": "rgba(...) / #...",
  "text-main": "#...",
  "text-sub": "#...",
  "accent-primary": "#...",
  "accent-secondary": "#..."
}
```

Run a final color patch pass before showing the first 1-3 page render.


---

# v5.16 Light Primary Reconstruction Constraints

These constraints are based on v5.15 and do not modify the main workflow.

## Lightweight Image Generation Preflight

Before Gate 3, verify only whether a real image-generation capability is available in the current run. Do not scan all tools, do not call automation tools, and do not use local SVG/PNG/canvas/script fallback as the high-visual preview.

## Complex Background Full-Image Rule

Use native PPT background only for pure color or simple gradient. Any texture, glow, haze, beam, technology line, grid, dot, particle, wave, circuit line, decoration, complex gradient, or translucent atmosphere means the background must be preserved as a full-slide clean image asset. Do not redraw complex backgrounds.

## Complex Title-Bar Capture Rule

Complex title bars/header strips with gradient, glow, glass, texture, lines, borders, or layered effects must be captured as whole PNG assets. Feather/soften edges when needed. Keep fused title text inside the asset when separation harms fidelity.

## Complex Small Icon PNG/SVG Rule

Complex small icons default to faithful PNG/SVG assets. Do not redraw them with Unicode, emoji, icon fonts, primitive shapes, disconnected line fragments, or alternate library icons. Captured icons require feathering/soft edges when needed.

## Captured-Asset Feathering Rule

Every captured complex asset must avoid hard crop edges, white/gray/color fringes, and sticker-like placement. This applies to title bars, icons, hero visuals, glow badges, glass cards, labels, and local patches.

## Chart/Icon Separation Rule

When chart and icon overlap, keep the chart native/editable whenever practical and place the icon/badge as a separate PNG/SVG asset. Do not capture chart+icon together as one image.

## Standard Chart Native Priority

Donut, pie, bar, column, line, area, radar, sparkline, and KPI charts should use native PPT chart components whenever practical. Shape-drawn charts are a downgrade and require user confirmation before final delivery.

## Downgrade Transparency Rule

If an implementation falls back to shape redraw where PNG/SVG assets or native charts were expected, pause and ask the user whether to accept the downgrade. Do not silently deliver a downgraded implementation.


---

# v5.17 Stable Lock Reconstruction Rules

These rules are primary reconstruction rules and override convenience-based shape redraw.

## Visual Priority Lock

Locked preview fidelity is higher priority than editability and higher priority than native-shape convenience. Do not reconstruct a slide by redesigning it. Reconstruct it by matching the locked preview.

## Layered Reconstruction

Split every slide into:

- Layer A: full background/atmosphere image when the background is not pure color or simple gradient;
- Layer B: PNG/SVG/crop/generated assets for complex visual modules;
- Layer C: editable native objects for text, tables, standard charts, simple icons, simple shapes.

## Complex Background Full-Image Rule

Only pure solid and simple gradient backgrounds can be native PPT fills. If background contains lines, dots, grids, glow, texture, particles, map/circuit/technology patterns, haze, or light beams, fuse those elements into the full background image. Do not redraw them. If a clean background cannot be extracted, recreate the clean background using image generation.

## Complex Visual Assetization Rule

Do not shape-redraw complex visuals. Assetize them when they use glow, 3D, glass, gradient atmosphere, composite badge construction, depth, perspective, or fused decoration.

Applies to complex hero visuals, title decoration, complex icon badges, glowing card backgrounds, complex pyramids/process blocks, and dashboard visual modules.

## Correct Edge Treatment

- Complex hero / irregular cutout: transparent asset with light soft-edge only when needed.
- Complex title bar: PNG asset, crisp edges, no feather unless original edge is soft.
- Glass card: native translucent card if faithful; otherwise PNG with crisp round corners and borders, no feather by default.
- Simple line/filled icon: native/SVG continuous path, no feather.
- Small badge / label icon: native PPT drawing when simple, no feather.
- Complex icon badge: PNG/SVG, clean crop artifacts only, no size-reducing feather.

## Simple Icon Native Rule

Simple line icons, simple filled icons, small badges, and small label icons should be native PPT drawing or SVG continuous paths when they can match the preview. Do not use Unicode, emoji, icon fonts, or broken line fragments.

## Complex Icon Badge Rule

If an icon includes a circular/rounded base, glow, gradient, shadow, inner layer, or badge composition, treat it as a complex icon badge. Use PNG/SVG asset unless native reconstruction can match almost exactly.

## Chart / Icon Separation

When charts overlap icons or badges, keep chart as native PPT chart whenever practical and separate the icon/badge as its own object. Do not combine chart + icon into one screenshot. Shape-drawn standard charts require user downgrade confirmation.

## No Silent Downgrade

If the output uses shape-first redraw for a complex visual area or shape-drawn charts instead of expected native charts, pause and ask the user to accept, reject, or mix the downgrade.


---

# v5.18 Mode 3 Clean Layer Lock Reconstruction Rules

These rules apply to Mode 3 image-to-PPT reconstruction and override any shortcut that treats a full-page screenshot as a final clean background.

## Full-Slide Screenshot Rejection for Final Background

The locked preview full-page image is a reference only. It must not be used as the final full-slide background unless the user explicitly accepts full-slide screenshot overlay downgrade.

A full-slide screenshot is not a clean background asset.

## Clean Background Asset Rule

Clean background may include base color, gradient, texture, grid, dots, lines, glow, beams, haze, particles, map/circuit/technology patterns, and atmosphere.

Clean background must not include title/body text, KPI values, cards, chart/table content, icons, hero visuals, process nodes, legends, or labels.

If foreground content remains inside the background, the asset is not clean.

## Background Route

For Mode 3 slides:

- extract a clean background when reliable;
- otherwise use image generation to recreate clean background;
- if image generation is unavailable, ask whether the user accepts full-slide screenshot overlay downgrade;
- never silently fall back to whole screenshot background.

## Mandatory Mode 3 Layer Plan

Before PPT generation, every Mode 3 slide must have a Layer A/B/C plan:

- Layer A: clean background route;
- Layer B: independent visual assets;
- Layer C: editable native objects.

This is an internal reconstruction-plan requirement, not a new public gate.

## Foreground Object Independence

Foreground objects visible in the screenshot are not considered reconstructed. Each must be independently classified and rebuilt:

- hero/main visual;
- title/header decoration;
- complex icon badge;
- simple icon;
- charts;
- tables;
- cards;
- process nodes;
- text and numbers.

## OCR Icon Quarantine

OCR-extracted icon-like text/symbols must not be used as final icons. Quarantine them and rebuild from the original source region as native/SVG simple icon or PNG/SVG complex icon badge.

## Native Chart/Table Priority

Standard charts and real tables should be rebuilt as native PPT components whenever practical, even if the same chart/table is visible in the screenshot.

Screenshot-backed charts/tables are downgrades and must be disclosed.

## Full-Slide Overlay Downgrade Confirmation

If the final implementation uses whole screenshot background plus overlays, pause for user approval. Provide choices: reject and rebuild, accept downgrade, or mix selected pages/regions.


---

# v5.19 Background and Icon Lock Reconstruction Rules

## Background Route

Only pure solid-color backgrounds may use native PPT fill.

All other backgrounds must be recreated as clean background images with image generation, including simple gradients, complex gradients, lines, dots, grids, glow, haze, texture, particles, circuit/technology patterns, and all decorative background elements.

Do not erase foreground content from screenshots to create background. Do not use dirty inpainted backgrounds. Do not use full-slide screenshots as final backgrounds. Do not redraw background atmosphere as PPT shapes.

## Clean Background Generation

Clean background should be generated/recreated, not wiped. It must not contain foreground residue, text, cards, charts, tables, icons, hero visuals, legends, labels, or process nodes.

If image generation is unavailable, ask the user whether to accept a downgrade.

## Simple Small Icons

Simple line icons and filled icons should be transparent PNG or SVG continuous path. They should not be font glyphs, Unicode, emoji, Chinese character placeholders, broken line fragments, or incomplete crops. Do not feather simple icons.

## Simple Icon Backgrounds

Simple icon backgrounds are native PPT shapes: solid/gradient circles, rounded rectangles, border rings, translucent chips. Place PNG/SVG icon body above the native background.

## Complex Icon Badges

For glowing, gradient, glass, multi-ring, inner-shadow, or fused badge icons, combine icon body and background as one transparent PNG asset. Do not force separation if it reduces fidelity.

## Icon Crop Completeness

Icon crops must include the entire visible icon, badge boundary, halo/glow, and border ring. No clipped or partial icons.

## Chart/Icon Overlap

Charts stay native whenever practical. Icons are separate PNG/SVG or native background plus PNG/SVG body. Do not combine chart and icon into one screenshot. Donut/ring charts must be native chart when practical, not shape-drawn, unless user accepts downgrade.

## Downgrade Confirmation

If non-solid background image generation, complete icon extraction, or native chart reconstruction cannot be achieved, pause and ask the user to accept or reject downgrade.


---

# v5.20 Visual Asset QA Lock Reconstruction Rules

## Real Image Generation Background Rule
Only pure solid-color backgrounds may use native PPT fill. All non-solid backgrounds must be recreated by real image generation as clean raster image assets such as PNG, JPG, or WebP. Local SVG, canvas, HTML, Python/script-generated backgrounds, PPT shape-drawn backgrounds, screenshot erasing, and dirty inpainted backgrounds are downgrades requiring user approval.

## Background Fidelity Rule
The generated clean background must match the locked preview's background atmosphere: color direction, glow direction, density of lines/dots/grid/particles, texture scale, contrast, and visual mood. The clean background must contain no foreground residue or content.

## Hero Role Priority Rule
Hero/main visual role overrides geometry simplicity. Slide hero, central AI hub, security shield, operation platform, architecture core, glowing ring, 3D platform, and visual center elements are visual assets by default. Do not native-redraw main visuals merely because they contain simple geometry. Native redraw is allowed only when near-identical and approved or when clearly simple.

## Complex Icon Combined PNG Rule
Complex icons on complex backgrounds should be combined transparent PNG assets when they include glow, gradient, halo, glass effect, shadow, badge base, multi-layer ring, or fused background. Do not split complex icons if separation reduces fidelity.

## Simple Icon Rule
Simple line and filled icons should be SVG continuous paths or transparent PNG. Simple pure-color/gradient icon bases may be native PPT shapes. No Unicode, emoji, icon fonts, Chinese-character placeholders, broken fragments, or incomplete crops.

## Compact Visual Asset Preview
For complex slides, provide a compact asset preview inside the existing first 1–3 page checkpoint: clean background, hero/main visual asset, complex icon badge assets, native chart/table status, and downgrade list. This is quality control, not a new workflow gate.

## Explicit QA Summary
For Mode 3 and complex slides, the first 1–3 page checkpoint must include an explicit QA summary with pass/fail/downgrade labels for background route, hero route, icon route, chart route, table route, and downgrade list. Do not continue batch generation when QA is missing or downgrades need approval.

---

# v5.21 Small Icon SVG Lock Reconstruction Rules

## Small Simple Icons Are Vector-First

Small-size simple line icons and small-size simple filled icons should be rebuilt as SVG continuous paths first. Transparent PNG is the second route. Screenshot crop is a downgrade route for small simple icons and requires disclosure.

## Priority

```text
small simple icon → SVG continuous path
if SVG is unreliable → transparent PNG
if both fail → screenshot crop only with user-approved downgrade
```

## No Default Screenshot Crops for Small Icons

Do not crop small simple icons from the screenshot by default. Cropped small icons commonly become clipped, blurry, incomplete, or inconsistent.

## SVG Quality

Small icon SVG assets must have complete paths, correct stroke width, safe viewBox padding, no clipped edges, no broken fragments, and no font/emoji/Unicode/Chinese-character placeholders.

## PNG Fallback Quality

Small icon PNG fallback must be transparent, complete, high-resolution for final size, sharp after scaling, and free of background fringe.

## Preserve Existing Good Routes

Medium/large icons may remain complete sharp transparent PNG crop assets. Complex glowing/gradient/glass/halo/shadow/fused badge icons may remain combined transparent PNG assets.

## QA Reporting

For pages with small icons, QA must report small icon route and flag clipped, blurry, incomplete, or screenshot-cropped small icons as fail/downgrade.


---

# v5.22 Micro Icon, Card, and Text Precision Lock Reconstruction Rules

These rules keep the v5.21 workflow unchanged and only improve detail-level visual similarity.

## Small Icon Likeness

Small icons must match the locked preview silhouette, stroke weight, stroke cap/join, internal negative space, badge/glow/halo, color order, and viewBox padding. Same-meaning substitutions from another icon set are not acceptable when visually different.

## Card / Panel Fidelity

Cards and panels must preserve bbox, radius, fill/gradient/opacity, border, shadow/glow, internal translucent bands, decorative dots/waves/dividers, padding, and group spacing. Native reconstruction is allowed only when the rendered card remains faithful.

## Text Position Fidelity

Editable text must preserve locked-preview anchors, baselines, alignment, size, weight, line spacing, and icon-text relationship. Automatic reflow or convenience repositioning is not allowed after lock.
