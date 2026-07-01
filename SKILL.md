---
name: quality-editable-ppt
description: "v5.22 detail-fidelity-lock edition. Preserves the v5.21 main flow and adds focused constraints for small-icon similarity, card/panel reconstruction fidelity, and text-position accuracy without changing gates or workflow."
---

# Quality Editable PPT

## Merged Package Note

This is the merged distribution. The execution workflow and all constraints are preserved, but supporting files are consolidated to reduce package size.


Create high-quality editable PPTX decks from a short prompt, an outline, or slide images.


## v5.12 Scientific Flow Consolidation

This version keeps the **v5.10 main workflow** and consolidates all later validated constraints into one scientific execution path. It does **not** add extra public stages or heavy runtime burden. It only fixes routing and execution discipline so Codex does not run off-course.

### Default Operating Principle

- Default output is always **high-visual preview + 90%+ high-replica editable PPT**.
- Users do **not** need to mention “high visual”, “high fidelity”, “image gen”, or “strong lock”.
- Preview generation must use **image_gen / image2 / GPT Image 2 / equivalent image generation** capability.
- After preview/source confirmation, the locked preview/source becomes the **only visual source of truth**.
- Post-lock reconstruction must not fall back to topic-based redesign, outline-based redesign, or local-script low-fidelity redraw.

### Scientific Gate Discipline

Never create background assets, hero crops, local-script previews, or PPT render **before the correct gate**.

Correct gate order:

```text
Gate 1  内容/大纲确认（only when needed）
→ Gate 2 页面信息结构与视觉策略确认
→ Gate 3 调用 image_gen / image2 生成高视觉预览图并确认
→ Gate 4 锁定预览图后的重建计划确认
→ Gate 5 必要时资产确认（默认可跳过）
→ Gate 6 图片级高复刻可编辑 PPT 渲染对照确认
```

### Mode-Specific Routing

- **Mode 1 — topic / brief**: generate outline first, confirm outline in Gate 1, then continue.
- **Mode 2A — existing outline / document, text must remain unchanged**: read the full content immediately, preserve wording and hierarchy, output the recognized content as Gate 1 confirmation, then continue through the same Mode 1 flow.
- **Mode 2B — long-form material to be distilled into outline**: extract key information into an outline, confirm outline in Gate 1, then continue exactly like Mode 1.
- **Mode 3 — existing slide image**: if the source is clear, lock and reconstruct directly; if blurry, first generate a **same-structure HD replica image**, confirm it, then lock and reconstruct.
- **Mode 4 — mixed inputs**: use documents as content source and visual references as visual constraints, then continue through Gate 2 → Gate 3 → lock → reconstruct.

### Non-Negotiable Execution Rules

- Mode 2A must not silently rewrite, shorten, flatten, or paraphrase user text.
- Mode 2A must preserve title/subtitle/body/bullet hierarchy, not just chapter titles.
- Gate 2 must happen **before** any background-only draft, hero-only draft, or preview asset generation.
- Generated preview must be a **complete reconstructable page**, not a pure background image or low-fidelity local drawing.
- After Gate 3 lock, PPT construction must be **preview-faithful replica build**, not local-script redesign.
- The local builder may reconstruct editable structures, but it may not invent a different layout or visually downgrade the page.

This skill is not a generic “make a PPT” workflow. It is a **reconstructable high-visual PPT pipeline**:

```text
brief / outline / images
→ create or select locked references
→ scope-aware Unified 3A replica core
→ editable PPTX
```


## v5.13 Hard Asset Fidelity Gates

This version does not change the v5.10/v5.12 gate flow. It upgrades previously stated visual-fidelity guidance into hard execution gates so Codex cannot pass a low-fidelity native-shape redraw as a replica.

### Visual-First Priority Rule

The default priority is:

```text
locked-preview visual fidelity
→ then editable structures
→ then native implementation convenience
```

Native PPT shapes are a method, not the goal. If native shapes do not closely match the locked preview, the element must be upgraded to SVG / transparent PNG / high-fidelity crop / generated asset.

Do not sacrifice preview fidelity merely to make an object editable.

### Full Background Hard Asset Rule

Except for pure solid backgrounds and extremely simple gradients, every slide background must be treated as one clean full-slide background asset.

This includes any background with texture, glow, bloom, haze, light beams, color atmosphere, dot matrix, grid, particles, wave lines, circuit lines, map texture, radial light, or sci-tech decorative line fields.

Forbidden:

- decomposing complex backgrounds into many PPT lines;
- redrawing dot grids, particles, circuit lines, and glow fields manually;
- replacing a textured background with a flat color;
- generating only a blank background before Gate 2;
- baking title, cards, chart axes, table lines, labels, icons, or flow nodes into the background asset.

Gate 6 fails if the PPT render background is visibly flatter, cleaner, or structurally different from the locked preview because the background was redrawn instead of used as a full-slide asset.

### Hero Asset Hard Binding Rule

Complex hero visuals must be treated as Layer A visual assets, not native-shape drawings.

This applies to AI hubs, AI cores, glowing brains, shields, cylinders, platforms, 3D rings, device clusters, node networks, cyber operation centers, circular data platforms, and multi-layer glow systems.

Allowed hero methods:

1. image_gen / image2 transparent PNG;
2. clean SVG asset;
3. source-faithful high-fidelity crop with transparent cutout;
4. local background patch when the hero cannot be separated from the background.

Forbidden hero methods:

- low-fidelity PPT shape redraw;
- raw rectangular crop pasted on top of a different background;
- simplified local-script illustration;
- replacing the preview hero with a different but semantically similar illustration.

Required hero integration:

- remove white edge, gray edge, color fringe, and hard crop border;
- remove residual title/text/label/number/card/chart pollution;
- use feathered edge / soft alpha on the asset boundary;
- match local background color, glow, and atmosphere;
- preserve preview size, position, lighting intensity, node/ring structure, and visual role.

Gate 6 fails if the hero has hard edges, visible rectangle boundaries, weak glow, different composition, wrong size/position, or sticker feeling.

### Icon PNG/SVG Fidelity Rule

Small icons must default to SVG or transparent PNG when the locked preview icon has any style complexity.

Use SVG / transparent PNG for icons with glow, gradient, multi-layer circular badge, halo, shadow, complex line geometry, multiple strokes, filled + outlined mixed style, 3D/skeuomorphic style, or custom product/security visual style.

Native PPT shapes are allowed only for ultra-simple single-color flat icons and only when the rendered result visually matches the locked preview.

Forbidden:

- Unicode symbols;
- emoji;
- icon-font glyphs;
- low-fidelity primitive-shape approximation;
- disconnected line-segment icon construction;
- replacing a preview icon with a different library icon;
- simplifying an icon just because it is small;
- omitting visible icons.

Icon badge backgrounds and icon bodies must be treated separately. If a preview icon sits in a glowing circular badge, the badge fill/glow/border and the glyph must both match. Use transparent PNG/SVG for the combined badge when separate reconstruction is not faithful enough.

Gate 6 fails if icons are visibly from a different icon set, lack preview glow/gradient, are made of rough shape fragments, or do not match preview silhouette and color.

Additional small-icon precision requirements:

- create icon-level reference crops or bbox notes for each repeated/important small icon before reconstruction;
- preserve silhouette, stroke cap/join style, stroke thickness, aspect ratio, internal negative space, badge boundary, glow/halo, and color order;
- do not swap a target-like icon, brain-like icon, shield-like icon, or workflow icon with a generic same-meaning icon from another library;
- if native/SVG reconstruction drifts, use a transparent PNG or regenerated asset that visually matches the locked preview instead of accepting a symbolic substitute;
- Gate 6 fails if a small icon is only semantically correct but visibly different from the locked preview.

### BBox-Level Preview Replica Rule

After a preview/reference is locked, create a lightweight internal layout-region map before PPT construction. This is not a new public gate.

Record approximate relative bounding boxes for title area, subtitle area, main hero visual, major cards/KPI groups, tables, charts, process bars, side panels, and footer/header decorations.

The PPT render must preserve the locked preview's relative positions, sizes, and visual density. Do not rebalance the slide, resize major groups, or shift the hero/cards/charts for local-script convenience.

Gate 6 fails if the render looks like a new layout rather than a preview replica, including title shift/scale changes, hero resize/move, card reflow, chart visual-weight shrinkage, bottom process bar spacing changes, or left/right balance changes.

### Native-If-Faithful Rule

The following elements should remain native/editable only when native reconstruction stays visually faithful:

- cards;
- panels;
- simple shapes;
- arrows;
- connectors;
- flow nodes;
- tables;
- standard charts;
- simple icon bodies.

If a native reconstruction is visually poor, the element must be patched with sampled colors/effects, overlaid with SVG/PNG visual asset while keeping editable text, or rebuilt with a better asset route.

Do not deliver a slide that is editable but obviously unlike the locked preview.

### Gate 6 Hard Failure Rule

Gate 6 render comparison is not just a display step. It is a pass/fail gate.

Fail and repair before delivery if any of these are true:

- overall slide looks like a local-script redesign;
- complex background is flatter or manually redrawn;
- main hero is a low-fidelity redraw or hard-edged crop;
- hero size/position/glow differs noticeably;
- small icons do not match the preview icon style;
- icons use fonts, emoji, rough primitives, or disconnected line segments;
- KPI cards or process components change major size/spacing;
- chart/sparkline styling differs obviously;
- table line color/opacity/chips are not restored;
- card borders, glow, radius, shadows, and density are lost;
- editable-native implementation clearly damages preview fidelity.

If Gate 6 fails, the next action must be targeted repair: background asset, hero asset, icons, layout bbox, chart/table/card styling, or sparkline—not a full redesign.

### Do Not Reinterpret This as More Workflow

These hard gates do not add new user confirmations. They only strengthen internal execution and QA within the existing v5.10/v5.12 flow.


## v5.14 Mode 2 Normalized-to-Mode-1 Flow

This version keeps the v5.10/v5.12/v5.13 visual fidelity and asset rules, but simplifies Mode 2 so it no longer becomes a separate, fragile workflow.

Mode 2 is only an **input normalization step**. After normalization, it must enter the same standard flow as Mode 1:

```text
confirmed outline/content source
→ Gate 1 outline/content confirmation
→ Gate 2 page information structure and visual strategy confirmation
→ Gate 3 image_gen / image2 high-visual preview
→ locked preview
→ high-fidelity editable PPT reconstruction
→ render comparison and editability QA
```

### Mode 2A — Uploaded Outline / Text Must Not Change

When the user uploads or pastes an existing outline, PDF outline, document outline, page-by-page text, or structured content and says the wording must not change:

1. Read the current uploaded/pasted content directly.
2. Extract the full visible text and hierarchy.
3. Preserve all original wording, numbers, titles, subtitles, bullet ownership, paragraph ownership, and page/section relationship.
4. Do **not** summarize, rewrite, expand, reduce, merge, flatten, or reorder.
5. Output the recognized outline/content as Gate 1 confirmation.
6. After the user confirms, continue exactly like Mode 1:
   - Gate 2 page information structure and visual strategy confirmation;
   - Gate 3 high-visual preview generation;
   - locked-preview reconstruction.

Mode 2A must not skip directly to asset generation, background generation, PPT rendering, or reconstruction.

### Mode 2B — Long Text Needs Key-Information Extraction

When the user provides long-form text and asks to extract key information, summarize, organize, or generate a PPT outline:

1. Read the current source text directly.
2. Extract key information into a PPT-ready outline.
3. Preserve factual meaning, names, numbers, scope, conditions, and conclusions.
4. Output the extracted PPT outline as Gate 1 confirmation.
5. After the user confirms, continue exactly like Mode 1:
   - Gate 2 page information structure and visual strategy confirmation;
   - Gate 3 high-visual preview generation;
   - locked-preview reconstruction.

Mode 2B must not create visuals before the user confirms the extracted outline.

### No Environment Bootstrapping Rule

Mode 2 must not automatically create, activate, or rely on a separate runtime environment merely to read uploaded content.

Forbidden unless the user explicitly asks:

- creating or activating virtual environments;
- installing packages;
- starting broad environment setup steps;
- running unrelated shell setup;
- scanning stale `phase0`, `phase1`, `locked_references`, or previous project files as the current source;
- continuing from old cached previews or old extraction outputs.

Use the current uploaded/pasted content as the only source. If extraction is not possible with available capabilities, stop and ask the user to paste the text or provide a clearer/exported file. Do not invent content and do not continue with partial headings only.

### Fresh Input Rule

For every Mode 2 run, treat the latest user-provided outline/text/file as the active source of truth.

Do not mix it with:

- old outlines;
- old previews;
- previous `phase0/phase1` files;
- previous locked references;
- previous extracted text;
- previous generated backgrounds.

If any stale file is detected, ignore it unless the user explicitly says to reuse it.

### Mode 2 Gate Discipline

For Mode 2, the only valid next visible step after reading/extracting content is Gate 1 confirmation of the recognized or distilled outline/content.

Do not generate:

- background images;
- hero assets;
- preview images;
- PPT renders;
- reconstruction plans;
- asset registries;

before Gate 1 confirmation and Gate 2 confirmation.



## v5.15 Asset-Capture Fidelity Additions

This version keeps the v5.14 normalized Mode 2 flow and adds four primary asset-fidelity rules. These rules are first-class constraints, not optional patches.

### Complex Title-Bar Asset Rule

If a title region / header bar contains complex gradient, glow, glass, decorative beams, corner chrome, layered strokes, or other compound styling, do not redraw it with native shapes.

Required route:

- capture the whole title bar as a faithful PNG asset;
- preserve its original gradient, glow, border, corner treatment, and integrated decorations;
- if the title text is visually integrated into that complex title bar, keep the text inside the captured title-bar asset;
- only use editable native title text when the title region is visually simple and separable without fidelity loss.

### Complex Hero With Intrinsic Text Rule

If the main visual / hero asset is complex (for example 3D, luminous, gradient, glass, volumetric, holographic, or other rich-rendered style) and contains text that is visually inside the hero composition, do not force text extraction.

Required route:

- keep the hero and its intrinsic text together as one faithful asset when separation would blur, damage, or visually downgrade the hero;
- remove only accidental contamination or duplicated page text that is not part of the intended hero design;
- do not over-cut, over-mask, or over-extract text from a complex hero if that causes blur or halo artifacts.

### Small-Icon Hard Asset Rule

Visible small icons must default to faithful PNG/SVG asset use, not redraw.

Required route:

- do not redraw small icons with font symbols, Unicode glyphs, emoji, primitive-shape approximations, or discontinuous line fragments;
- use source-faithful transparent PNG or SVG assets for small icons so the rendered icon matches the locked preview exactly;
- icon holder/badge background may be native only when it visually matches, but the icon body itself must still be matched faithfully;
- if an SVG is available, use it; otherwise use a clean transparent PNG crop.

### Current-Run Preview Lock Rule

When locking preview images after Gate 3, only the newly generated preview files from the current run / current conversation step may be read and locked.

Forbidden:

- comparing against older generated previews from earlier turns unless the user explicitly requests reuse;
- silently mixing current previews with old locked references;
- picking an earlier preview because it is visually similar;
- searching previous runs for alternate preview images during lock.

The lock registry must contain only the current newly generated preview files confirmed by the user.


## v5.16 Light Main Constraints — Based on v5.15

This version is based on v5.15 and **does not change the main workflow**. It only promotes recurring implementation problems into primary execution constraints. These are not optional patch notes and must be treated as main constraints.

### Preserve v5.15 Main Flow

Do not add new public workflow stages, heavy tool scans, broad structural audits, or extra confirmation loops.

Keep the existing gate rhythm:

```text
Gate 1 content / outline confirmation
→ Gate 2 page information structure and visual strategy confirmation
→ Gate 3 real high-visual preview generation
→ current-run preview lock
→ high-fidelity editable PPT reconstruction
→ render comparison and QA
```

### 1. Lightweight Image Generation Preflight

Before Gate 3, perform only a lightweight check that the current run has a real image-generation capability.

Allowed names include:

- `image_gen`;
- `image2`;
- `GPT Image 2`;
- `ChatGPT Images`;
- `gpt-image-2`;
- `openai image generation`;
- `Product Design` only if it clearly exposes real image generation in the current run;
- `Superpowers` only if it clearly exposes real image generation in the current run.

Do not enumerate all tools. Do not scan unrelated tools. Do not call or inspect:

- `automation_update`;
- automation / reminder / schedule tools;
- broad environment setup;
- package installation;
- historical tool registries.

If real image generation is unavailable or cannot be safely confirmed, stop before Gate 3 and tell the user. Do not create a local SVG / PNG / canvas / HTML / script fallback as a high-visual preview.

### 2. High-Visual Preview Source Constraint

For Mode 1 and Mode 2, Gate 3 high-visual preview must come from a real image-generation capability, not from local-script redraw.

Local scripts may support later PPT reconstruction, asset cleaning, cropping, or validation, but they must not replace the high-visual preview generator.

### 3. Complex Background Full-Image Constraint

Use native PPT background only for:

- pure solid color;
- simple gradient with no texture, glow, line, grid, dot, particle, haze, beam, decoration, or atmospheric overlay.

If the background contains even one of the following, keep it as a full-slide clean background image and do not redraw it:

- texture;
- glow;
- haze / bloom / light;
- beam;
- technology line;
- grid;
- dot matrix;
- particle field;
- wave line;
- circuit line;
- decoration pattern;
- complex layered gradient;
- translucent atmospheric layer.

This improves both fidelity and speed. Do not spend time recreating complex backgrounds with many PPT shapes.

### 4. Complex Title-Bar Capture Constraint

If a title bar, header strip, section heading region, or top chrome has complex gradient, glow, glass, texture, technology line, decorative border, or layered effects, capture the whole title-bar region as a PNG asset.

Do not redraw complex title bars with native PPT shapes.

If text is visually fused into the title bar, keep the text inside the PNG. Separate title text only when the title region is simple and separation does not harm fidelity.

Captured title bars must use feathered / softened crop edges when needed.

### 5. Complex Small Icon PNG/SVG Constraint

Complex small icons default to faithful PNG/SVG assets, not redraw.

Priority:

1. source-faithful transparent PNG crop;
2. clean SVG asset;
3. native redraw only for ultra-simple flat icons that can match almost exactly.

Forbidden:

- Unicode symbols;
- emoji;
- icon-font glyphs;
- font-like icons;
- rough primitive-shape redraw;
- disconnected line fragments;
- alternate library icon substitution;
- low-fidelity approximations.

Captured small icons must also use feathered / softened edges when needed.

### 6. Unified Captured-Asset Feathering Constraint

Any directly captured complex visual asset must be blended into the slide, not only hero illustrations.

This applies to:

- hero illustrations;
- complex title bars;
- complex small icons;
- glow badges;
- decorative labels;
- glass cards;
- local background patches;
- complex chips / tabs / buttons.

Required:

- remove white / gray / color fringe edges;
- avoid hard rectangular crop boundaries;
- apply light feathering or soft alpha where needed;
- keep internal details sharp;
- match local background light and color.

### 7. Chart and Icon Separation Constraint

If a chart overlaps with a small icon, badge, or decorative element, separate by role:

1. chart stays native/editable whenever practical;
2. icon / badge / decoration becomes a separate PNG/SVG asset;
3. do not screenshot chart + icon together as one icon or one chart image.

This applies to donut, pie, column, bar, line, area, radar, sparkline, KPI charts, and other standard chart types.

### 8. Standard Chart Native Priority

Standard business charts should be reconstructed as native PPT chart components whenever practical:

- donut / ring chart;
- pie chart;
- column chart;
- bar chart;
- line chart;
- area chart;
- radar chart when structure is clear.

Shape-drawn charts are a downgrade. If native chart generation is not possible or the result is intentionally shape-drawn, pause and ask the user whether the downgraded shape-based chart is acceptable. Do not silently deliver it as if it were native.

### 9. Current-Run Preview Lock Constraint

At preview lock time, only read and lock the new preview generated and confirmed in the current run / current conversation step.

Do not:

- read old preview images;
- compare with previous preview generations;
- search previous `phase` folders for similar previews;
- mix old `locked_references` with the current preview;
- reuse a historical preview unless the user explicitly asks.

### 10. Downgrade Transparency Constraint

Do not silently pass downgraded implementations.

If complex visual assets were expected but the PPT was built mostly from shapes, or if native charts were expected but charts were shape-drawn, pause and ask the user whether the downgrade is acceptable.

Offer choices:

```text
A. 不接受：返回修复为 PNG/SVG 资产或原生图表
B. 接受：继续交付当前图形绘制版本
C. 混合处理：指定哪些元素必须资产化/原生化，哪些元素可图形绘制
```

This is a pause-and-confirm rule, not an automatic hard failure.


## v5.17 Stable Lock — Visual Priority and Layered Reconstruction

This version is a **stable-lock edition**. It does not add a heavier public workflow. It clarifies execution priority so the skill does not fall back into shape-first redesign.

### Stable Main Principle

The locked preview is the only visual source of truth.

The first goal of PPT reconstruction is:

```text
visual replica fidelity first
→ then editable content
→ then native implementation convenience
```

Native PPT objects are implementation tools, not the goal.

### Do Not Redesign Rule

After preview lock, the PPT render stage must not reinterpret the locked preview as a design reference.

Forbidden:

- redesigning the page from topic, outline, or style words;
- replacing the locked preview with a visually similar template;
- simplifying complex UI because it is easier to draw;
- rebuilding complex visual modules as generic PPT cards;
- using shape-first reconstruction for complex background/title/hero/card/icon badge areas;
- reducing glow, lighting, gradients, badge depth, or card atmosphere without user approval.

The task is **replica reconstruction**, not redesign.

### Three-Layer Reconstruction Model

Every slide must be reconstructed by separating the locked preview into three layers:

```text
Layer A — Background and atmosphere
Layer B — Visual assets and complex modules
Layer C — Editable native structures
```

#### Layer A — Background and atmosphere

Use native background only for pure solid color or simple gradient with no visual decoration.

If the background includes any line, dot, grid, glow, texture, particle, haze, light beam, map texture, circuit line, technology line, wave, decorative pattern, or atmosphere overlay, keep those elements fused with the background as one full-slide background image.

Do not redraw complex background decoration. If the background cannot be cleanly separated from foreground content, use image generation to recreate a clean background, then place editable foreground content on top.

#### Layer B — Visual assets and complex modules

Assetize rather than redraw visual modules that rely on high-fidelity appearance:

- complex hero / main visual;
- 3D, glow, glass, holographic, volumetric, or gradient illustration;
- complex icon badge, such as icon + circular base + glow + gradient + shadow;
- complex title decoration / header chrome;
- complex decorative card background when native shapes cannot match;
- complex pyramid / process block / dashboard module with glow, depth, perspective, or glass effects;
- fused decorative strip or line glow that cannot be matched with simple native shapes.

Layer B can use PNG/SVG/crops/generated assets. Text may stay editable when separation does not harm fidelity. If text is intrinsically fused inside a complex hero, keep it in the asset.

#### Layer C — Editable native structures

Use native PPT objects for content that can be faithfully editable:

- text;
- numbers;
- labels;
- simple solid or simple-gradient rectangles;
- simple borders and dividers;
- native tables;
- standard PPT charts;
- simple line icons and simple filled icons;
- small badges and small label icons when they are simple enough to match with native PPT shapes.

Do not use Unicode, emoji, or icon-font glyphs as substitutes for designed icons.

### Asset Edge Treatment Rules

Do not apply one feathering rule to every asset.

1. **Complex hero / irregular visual cutout**: use transparent PNG/SVG or faithful crop. Apply light soft-edge treatment only when needed to remove hard crop seams, white/gray/color fringes, or sticker-like edges.
2. **Complex title bar / header strip**: capture as PNG when complex, but keep edges crisp. Do not feather normal rectangular title bars. Preserve sharp borders, lines, and text clarity.
3. **Glass card / UI card**: prefer native translucent shape if it can match. If captured as PNG, keep rounded edges and border crisp. Do not feather the card edge unless the original edge is intentionally blurred/glowing.
4. **Simple line / filled icon**: prefer native PPT drawing or SVG continuous path. Do not feather. Keep strokes crisp and icon size unchanged.
5. **Small badge / small label icon**: prefer native PPT drawing when simple. Do not feather. Keep edges crisp.
6. **Complex icon badge**: use PNG/SVG asset when it includes glow, gradient, circular base, inner shadow, or composite layers. Usually do not feather; only clean obvious crop artifacts.

### Background Fusion Rule

Except for pure solid or simple gradient backgrounds, background decoration belongs to the full background image.

This includes line work, dot matrix, grid, glow, light beams, texture, particles, map/circuit/technology patterns, haze/atmosphere, and complex gradient overlays.

Do not separate and redraw these background elements as shapes. If a clean background cannot be extracted, generate a clean background with image generation.

### Chart / Icon Separation Rule

Charts and icons must be separated by role.

If a standard chart overlaps an icon, badge, or decoration:

- chart remains native PPT chart whenever practical;
- icon / badge / decoration is built separately as native simple icon or PNG/SVG complex badge;
- do not screenshot chart + icon as one image;
- do not turn chart into shape drawing merely because an icon overlaps it.

Standard charts include donut, pie, column, bar, line, area, radar, sparkline, KPI micro chart, and similar business charts.

If a standard chart is implemented as shapes instead of a native chart, this is a downgrade. Pause and ask the user whether it is acceptable instead of silently delivering.

### Native Drawing Allowlist

Native PPT drawing is allowed only when the element is visually simple and can match the locked preview:

- simple text;
- simple solid/gradient cards without complex glow or depth;
- simple borders/dividers;
- simple line icons;
- simple filled icons;
- small simple badges / label icons;
- native charts;
- native tables.

Native PPT drawing is not allowed as the default for complex UI modules.

### Shape-Based Downgrade Confirmation

If reconstruction uses shape drawing where assetization or native chart components were expected, pause and ask:

```text
当前实现为了可编辑性使用了图形绘制，可能降低视觉还原度。
请选择：
A. 不接受，返回资产化 / 原生图表修复
B. 接受当前图形绘制版本
C. 混合处理，指定哪些区域必须资产化或原生化
```

Do not silently deliver downgraded shape-first output.

### Lightweight Execution Constraint

Keep this version fast:

- do not add broad tool scans;
- do not compare against old previews;
- do not read historical phase folders unless explicitly requested;
- do not run heavy multi-round audits by default;
- use targeted repair for only the failed regions.


## v5.18 Mode 3 Clean Layer Lock — Image-to-PPT Anti Overlay Rules

This version is based on v5.17 Stable Lock and **does not change the main workflow**.

It only clarifies Mode 3 image-to-editable-PPT execution so the skill does not misuse a full-page screenshot as the final background.

### Main Flow Preservation

Do not add a new public gate. Do not reorder the existing gates. Do not convert this into a heavier workflow.

Keep the existing flow:

```text
image input / locked preview
→ current reference lock
→ page structure and reconstruction plan
→ PPT reconstruction
→ first 1–3 page render comparison
→ continue batch build
```

The following Mode 3 rules apply inside the existing page structure / reconstruction plan and QA steps.

### 1. Full-Slide Screenshot Is Not a Clean Background Asset

In Mode 3, the uploaded page image / locked preview is a visual reference, not a final background layer.

Forbidden by default:

- placing the whole locked preview image as the final full-slide background;
- using the whole screenshot as a background and overlaying editable text/cards/charts on top;
- treating the original screenshot as a clean background asset;
- claiming foreground elements are complete because they already exist in the screenshot.

Allowed uses of the whole locked preview:

- visual reference;
- positioning reference;
- bbox measurement reference;
- render comparison reference;
- temporary guide layer that must be removed before final delivery;
- downgrade mode only after user approval.

### 2. Clean Background Definition

A clean background asset may contain only background/atmosphere elements:

- base color;
- simple or complex gradient;
- texture;
- grid;
- dot matrix;
- line work;
- circuit / technology pattern;
- glow;
- light beam;
- haze;
- particles;
- map-like background texture;
- atmospheric overlay.

A clean background asset must not contain foreground content:

- title text;
- body text;
- KPI values;
- chart;
- table;
- card content;
- card foreground text;
- icon;
- icon badge;
- hero/main visual;
- process nodes;
- labels;
- legends;
- decorative badges attached to content.

If the extracted background contains foreground content, it is not clean and must not be used as the final background.

### 3. Background Extraction Route

For each Mode 3 slide:

1. Try to create a clean background asset by removing foreground content from the locked preview.
2. If clean separation is not reliable, use image generation to recreate the clean background atmosphere.
3. If image generation is unavailable, pause and ask whether the user accepts full-slide screenshot overlay as a downgrade.

Do not fall back silently to a full-slide screenshot background.

### 4. Mandatory Layer A/B/C Plan for Mode 3

Before building a Mode 3 slide, the reconstruction plan must include a per-slide Layer A/B/C plan.

This is not a new user-facing gate. It is an internal execution requirement inside the existing reconstruction plan.

Required format:

```text
Slide X Layer Plan

Layer A — Clean background
- clean background route: extracted / image-gen recreated / user-approved downgrade
- must not include: text, charts, tables, cards, icons, hero

Layer B — Visual assets
- hero / main visual
- complex title/header decoration
- complex icon badges
- complex card backgrounds
- glow decorations
- non-native visual modules

Layer C — Editable native objects
- title and body text
- numbers and KPI values
- native charts
- native tables
- simple line/filled icons and small labels when suitable
- simple shapes/borders/dividers
```

If this plan is missing, do not proceed directly to PPT generation.

### 5. Foreground Objects Are Not Reconstructed Just Because They Exist in the Screenshot

Even if the full-slide reference image contains hero visuals, icons, charts, tables, cards, or process nodes, they are not considered reconstructed.

Each foreground object must still be classified and rebuilt independently:

- complex hero/main visual → independent PNG/SVG/crop/generated asset;
- complex icon badge → independent PNG/SVG asset or highly faithful native reconstruction;
- simple line/filled icon or small label icon → native PPT drawing or SVG continuous path;
- standard chart → native PPT chart whenever practical;
- real table → native PPT table whenever practical;
- text/numbers → editable PPT text whenever practical;
- simple card frame → native PPT shape if faithful;
- complex card background → assetize or use faithful native translucent card.

### 6. OCR Icon Quarantine Rule

OCR-extracted icon-like text must not be used directly as icons.

If OCR returns icon-like words or symbols such as `盾`, `表`, `库`, `机`, `策`, `镜`, `禁`, `修`, `AI`, `C`, `☠`, `⌘`, `◎`, `▣`, `▭`, or similar placeholders, quarantine them.

Reclassify the original source region:

- simple icon → native PPT drawing or SVG continuous path;
- complex icon badge → PNG/SVG/crop asset;
- uncertain icon → crop the source region as transparent PNG/SVG asset.

Do not deliver font-style icon substitutes.

### 7. Chart and Table Native Priority in Mode 3

In image-to-PPT mode, standard charts and real tables must be rebuilt as native components whenever practical, even if they are visible in the screenshot.

The screenshot does not satisfy chart/table reconstruction.

Default routes:

- standard chart → native PPT chart;
- KPI micro chart / sparkline → native chart or continuous SVG path when native chart is not practical;
- real table / list table → native PPT table;
- chart-overlapping icon → separate the icon, keep chart native.

Shape-drawn charts and screenshot-backed charts are downgrade implementations and require user confirmation.

### 8. Full-Slide Screenshot Overlay Is a Downgrade Mode

Full-slide screenshot overlay means:

```text
whole original page image as background
+ semi-transparent mask / overlay
+ editable text/cards/charts added on top
```

This is not the default high-replica editable PPT route.

If the implementation uses this route, pause and ask the user:

```text
当前方案使用了“整页截图打底 + 可编辑元素叠加”的降级方案。
这能快速接近原图，但背景未干净分离，主视觉/icon/图表可能没有真正重建。
请选择：
A. 不接受，重新做 clean background + assets + native objects
B. 接受当前整页截图叠加版
C. 混合处理，指定哪些页或区域必须拆分重建
```

Do not silently deliver this downgrade.

### 9. Mode 3 First 1–3 Page Check

For Mode 3, the first 1–3 page check must explicitly report:

- whether any slide used full-slide screenshot overlay;
- whether clean background was extracted or image-generated;
- which hero/assets/icons were independently rebuilt;
- which charts are native PPT charts;
- which tables are native PPT tables;
- any downgrade that requires user approval.

Continue batch building only after the preview/render comparison and downgrade status are clear.


## v5.19 Background and Icon Lock — No Dirty Background, No Broken Icon

This version is based on v5.18 and **does not change the main workflow**.

### Main Flow Preservation

Do not add new public gates. Do not reorder existing gates. Do not change Mode 1 / Mode 2 / Mode 3 routing.

### 1. Background Rule — Pure Solid Native, Everything Else Image-Generated

Only pure solid-color backgrounds may use native PPT fill.

All non-solid backgrounds must be recreated as clean background images with image generation. This includes simple gradient, complex gradient, line work, dots, dot matrix, grid, glow, light beam, haze, texture, particles, circuit/technology patterns, wave lines, map-like texture, and any decorative background element.

Do not attempt to erase foreground text, icons, cards, or charts from the source screenshot to manufacture a background.

Forbidden:

- dirty inpainted/erased backgrounds with foreground residue;
- manually redrawing background lines/dots/grids/glow as PPT shapes;
- using the full-slide screenshot as final background;
- using a screenshot after imperfect foreground removal as clean background.

Required route:

```text
pure solid background → native PPT fill
all other backgrounds → image generation recreates clean background
```

### 2. Clean Background Must Be Generated, Not Wiped

For Mode 3 image-to-PPT reconstruction, clean background should be a newly recreated background atmosphere, not a screenshot with content erased.

Clean background may contain only background atmosphere: base color, generated gradient, generated texture, generated grid/line/dot system, generated glow, atmosphere, haze, and particles.

Clean background must not contain title/body text, KPI values, cards, charts, tables, icons, hero/main visuals, process nodes, labels, legends, or old foreground residue.

If image generation is unavailable, pause and ask whether the user accepts a downgraded fallback. Do not silently use a dirty background.

### 3. Simple Small Icon Rule — PNG/SVG, Not Font

Simple line icons and simple filled icons must be exported or rebuilt as transparent PNG or SVG continuous path.

Do not use Unicode, emoji, icon-font glyphs, Chinese character placeholders such as `盾`, `表`, `库`, `机`, `策`, `镜`, broken line fragments, or incomplete crops.

Small icons must remain visually complete and sharp. Do not feather simple icons.

### 4. Simple Icon Background Rule — Native Shape

If an icon background/badge base is visually simple, build the background natively: solid circle, solid rounded rectangle, simple gradient circle, simple gradient rounded rectangle, simple border ring, or simple translucent chip.

Required layering:

```text
icon background/base → native PPT shape
simple icon body → transparent PNG or SVG
```

### 5. Complex Icon Badge Rule — Combined Transparent PNG

If an icon and its background are visually fused, keep them together as one transparent PNG asset.

Use combined transparent PNG for icons with glow, complex gradient, glass effect, inner shadow, multiple rings/layers, strong highlight, composite badge depth, or icon-body/background that is difficult to separate cleanly.

Do not force separation when it causes blur, missing edges, or incomplete crop.

### 6. Icon Crop Completeness Rule

Any cropped icon asset must include the complete visible icon and any intended glow/badge boundary.

Forbidden: clipped icon edges, missing halo, missing border ring, cropped partial icon, size-reducing feather, or font-like placeholder.

### 7. Chart and Icon Overlap Rule

When a chart overlaps or sits close to an icon:

- chart remains native PPT chart whenever practical;
- icon is separated as SVG/transparent PNG;
- simple icon background is native shape;
- complex icon badge may be combined transparent PNG;
- do not screenshot chart + icon together;
- do not make a donut/ring chart from PPT shapes unless the user accepts downgrade.

For donut/ring, pie, bar/column, line, area, radar, and sparklines, native chart is the default route when practical.

### 8. Downgrade Confirmation

If image generation is unavailable for a non-solid background, a background would have to be dirty-erased from screenshot, a standard chart would be shape-drawn, chart+icon would have to be combined as a screenshot, or an icon cannot be rebuilt/cropped completely, pause and ask the user before continuing.

Do not silently deliver downgrade output.


## v5.20 Visual Asset QA Lock — Real Image Background, Hero Asset, Explicit QA

This version is based on v5.19 and **does not change the main workflow**. Do not add public gates, reorder phases, or change Mode routing. The asset preview and QA summary are part of the existing first 1–3 page checkpoint.

### Main Flow Preservation

Keep the existing flow:

```text
input / locked preview
→ current reference lock
→ page structure and reconstruction plan
→ PPT reconstruction
→ first 1–3 page render comparison
→ continue batch build
```

### 1. Real Image Generation Background Rule

Only pure solid-color backgrounds may use native PPT fill. Every non-solid background must be recreated by **real image generation** as a clean raster background asset, such as PNG, JPG, or WebP.

Non-solid background includes simple gradient, complex gradient, lines, dots, dot matrix, grid, glow, light beam, haze, texture, particles, circuit/technology pattern, wave lines, map-like texture, and any decorative background element.

The following are **not** valid substitutes for image generation: local SVG background, canvas-rendered background, HTML-generated background, Python/script-generated background, PPT shape-drawn background, screenshot with foreground erased, or dirty inpainted screenshot background.

Required route:

```text
pure solid background → native PPT fill
all non-solid backgrounds → real image generation clean raster background
local SVG/canvas/script/PPT-shape background → downgrade, requires user approval
```

If real image generation is unavailable for a non-solid background, pause and ask whether the user accepts a downgraded local-generated background. Do not silently deliver it.

### 2. Background Fidelity Prompting

When recreating a non-solid background, the image generation prompt must reference the locked preview background atmosphere. Do not freely redesign the background.

Match the locked preview in dominant color direction, light source/glow direction, density of lines/grids/dots/particles, texture scale, atmospheric depth, contrast, and visual mood. The clean background must contain no foreground text, card content, charts, tables, icons, hero visuals, process nodes, labels, legends, or old foreground residue.

### 3. Hero/Main Visual Role Overrides Geometry Simplicity

Main visual role is more important than geometry simplicity. If an element acts as the slide hero, central visual, AI hub, security shield, operation platform, architecture core, visual center, glowing ring, 3D platform, AI engine, or product architecture centerpiece, treat it as a visual asset by default.

Do not redraw the hero/main visual with native PPT shapes merely because it contains circles, lines, rings, platforms, shields, cards, or other geometric components.

Allowed routes: crop/extract as transparent PNG; recreate as high-fidelity transparent PNG/WebP with image generation; use SVG only when it preserves original fidelity; use native PPT shapes only when near-identical and approved. If a hero/main visual is rebuilt natively, report it in QA as a potential downgrade unless near-identical.

### 4. Complex Icon on Complex Background Rule

Complex icons on complex backgrounds should be exported as one transparent PNG asset. If an icon includes glow, gradient, halo, glass effect, shadow, badge base, multi-layer ring, inner highlight, or is visually fused with its background, keep icon body and icon background together as a transparent PNG.

Do not split complex icons into native base + SVG icon unless near-identical. The transparent PNG must include the complete icon, badge edge, glow, halo, visible shadow, and intended boundary.

### 5. Simple Icon Rule Remains

Simple line icons and simple filled icons should be transparent PNG or SVG continuous paths. Simple pure-color or simple-gradient icon backgrounds may be native PPT shapes. Do not use Unicode, emoji, icon fonts, Chinese-character placeholders, broken line fragments, or incomplete crops.

### 6. Compact Visual Asset Preview for Complex Slides

For complex slides, show a compact visual asset preview before or together with the first 1–3 page checkpoint. This is not a new public gate; it is part of the existing checkpoint.

A slide is complex if it contains any non-solid background, hero/main visual, complex icon badge, complex title/header decoration, chart-icon overlap, glass card, glow card, complex gradient module, or 3D/depth visual module.

The compact preview should include: clean background preview, hero/main visual asset preview, complex icon badge preview, native chart/table status, and downgrade list. Do not produce a large exhaustive asset dump unless requested.

### 7. Explicit QA Summary Is Mandatory for Mode 3 and Complex Slides

For Mode 3 and complex slides, the first 1–3 page checkpoint must include an explicit QA summary. Do not continue batch generation until QA status is clear.

The QA summary must report background route, hero route, icon route, chart route, table route, and downgrade list with pass/fail/downgrade labels.

### 8. Batch Continuation Rule

Do not continue from the first 1–3 pages to the remaining slides when any unapproved downgrade remains, any main visual was natively redrawn and not near-identical, any complex icon badge was split or cropped incorrectly, any chart+icon region was combined into one screenshot, any standard chart was shape-drawn without approval, or the QA summary is missing. Pause and ask the user whether to repair or accept downgrade.


## v5.21 Small Icon SVG Lock — Small Icons Are Vector-First

This version is based on v5.20 and does not change the main workflow.

Keep the existing flow:

```text
input / locked preview
→ current reference lock
→ page structure and reconstruction plan
→ PPT reconstruction
→ first 1–3 page render comparison with compact asset preview and QA
→ continue batch build
```

### Small Simple Icon Size Rule

For small-size simple line icons and small-size simple filled icons, the primary route is SVG continuous path. Transparent PNG is the second route. Screenshot crop is not the default route for small simple icons.

Small icon means a compact UI symbol, KPI icon, label icon, list icon, module icon, or tiny decorative icon where edge sharpness and complete contour matter more than photographic fidelity.

### Required Priority

```text
small simple line/filled icon
→ SVG continuous path first
→ transparent PNG second
→ screenshot crop only if SVG/PNG reconstruction is impossible and user approves downgrade
```

Do not choose screenshot crop merely because the icon is visible in the locked preview.

### No Default Screenshot Crops for Small Icons

Small screenshot crops often cause clipped edges, missing strokes, incomplete contours, blurry scaling, dirty background fringe, inconsistent optical size, and poor alignment. If a small simple icon is delivered as a screenshot crop, mark it as downgrade in QA.

### SVG Quality Requirements

Small simple icon SVG assets must have complete continuous paths, correct stroke width, safe viewBox padding, no clipped edges, no broken/disconnected fragments, no Unicode/emoji/icon-font/Chinese-character placeholders, and no rough primitive approximation when SVG path is feasible.

### Transparent PNG Fallback

Small icon PNG fallback must have transparent background, complete contour, no clipped edge, no dirty background fringe, enough resolution for final size, and sharp scaling. Do not feather simple icons if it shrinks or blurs them.

### Medium/Large Icon Asset Rule Remains

Medium or large icons may remain screenshot/crop-based transparent PNG assets when the crop is complete, sharp, clean, and visually faithful.

### Complex Icon Badge Rule Remains

Complex glowing, gradient, glass, halo, shadow, multi-ring, fused badge-style icons may remain combined transparent PNG assets. Do not force complex badge icons into SVG.

### Icon QA Additions

The first 1–3 page QA summary must explicitly report small icon route when small icons are present: SVG / transparent PNG / screenshot downgrade. Do not continue batch generation when small icons are clipped, blurry, incomplete, or screenshot-cropped without user approval.

## Primary Goal

Default target: **90%+ high-detail editable reconstruction**.

This is the only default fidelity target. Do not expose quick/standard/strict/95% mode choices to ordinary users.

The goal is not “looks similar as a screenshot”. The goal is:

- locked preview/source image is the visual source of truth;
- background texture, hero visual, charts, tables, icons, cards, and component geometry are preserved;
- core content and standard structures remain editable;
- high-visual background/hero/complex icons are clean assets;
- screenshot-only PPT is rejected as fake fidelity.

## v5.22 Micro Icon, Card, and Text Precision Lock

This version keeps the v5.21 gate flow, mode routing, and all existing constraints unchanged. It only tightens final visual matching for three recurring detail issues: small-icon likeness, card/panel fidelity, and editable text placement.

- Small icons must match the locked preview silhouette, stroke weight, viewBox padding, badge/glow style, color, and visual family. SVG/PNG assets may not be substituted with generic library icons that only share the same meaning.
- Cards and panels must preserve measured box-model tokens from the locked preview: bbox, radius, fill/gradient/opacity, border, shadow/glow, inner decorative strips, placeholder areas, padding, and group spacing.
- Editable text must preserve position anchors from the locked preview: title/subtitle/KPI label/value x/y, alignment, baseline, line spacing, font weight, and icon-text relationship. Automatic reflow or convenience repositioning is not allowed after lock.
- These checks run inside the existing inventory, build, and Gate 6 QA steps. They add no new public gate and must not change the workflow.


## Restored Detail-Replica Core

This version is based on the earlier branch that successfully restored:

- clean full-slide texture/background assets;
- complex hero / visual asset handling;
- source-faithful crop and transparent PNG/SVG hero fallback;
- chart data binding and native PPT charts;
- native PPT table reconstruction;
- icon badge registry and visible icon preservation;
- card color sampling, border, radius, shadow, glow, and box-model fidelity;
- background purity and asset seamless integration checks;
- simple PPT shapes / simple icons as native editable objects.

These are part of the mainline, not optional patches.


## v5.0 强化版复原能力已合并

本版本已合入 5.0 强化版中验证有效的复原规则：

- 有纹理 / 网格 / 点阵 / 光效背景作为干净整张背景图资产；
- 复杂主视觉优先透明 PNG/SVG 或 source-faithful 裁切，不允许低保真形状重画；
- 视觉资产不得残留文字、标签、数字、卡片边框、图表轴线等污染；
- 裁切资产必须羽化 / 柔边 / alpha 处理，避免硬边截图感；
- 卡片必须按颜色采样和盒模型复刻边框、投影、圆角、尺寸、内边距；
- 小 icon 必须登记并还原，简单 icon 原生/SVG，复杂 icon PNG/SVG；
- 最终 PPT 不能是一张整页截图，必须保留足够的可编辑文本、图表、表格、卡片、流程和组件。


## Primary Asset and Component Reconstruction Rules

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
- very simple linear gradients;
- backgrounds without texture, glow, beam, grid, dot, wave, or atmosphere.

The full background asset must be clean: it must not include titles, body text, KPI values, cards, table lines, chart axes, labels, legends, icons, process nodes, or other editable content.

### Hero Asset Edge Blending Rule

Independent hero / main visual assets placed as PNG/SVG must be cleaned and blended into the page background.

Required handling:

- remove white edges, gray edges, color fringes, hard crop borders, and old background residue;
- remove residual text, labels, pseudo-characters, duplicated title fragments, numbers, and icon captions from the asset;
- use light feathering / soft alpha edge only on the asset boundary;
- keep the internal hero details sharp;
- add subtle environment shadow/glow/contact light when needed to match the background;
- if the hero and background are visually inseparable, use a background-fused asset instead of hard-cutting the hero.

A hero asset with visible hard rectangular edges, text contamination, or pasted-on sticker feeling fails QA.

### Icon Reconstruction Rule

Do not use Unicode symbols, emoji, or icon-font characters as substitutes for visual icons in the locked reference.

For every visible small icon:

- preserve the icon base/background separately from the icon body;
- icon base/background should be native PPT circles, rounded rectangles, chips, or color blocks when practical;
- simple line icons, filled icons, single-color icons, and geometric icons should be native PPT shapes/lines/freeforms or editable SVG when practical;
- complex gradient, glow, 3D, skeuomorphic, illustration-style, or dense composite icons should be clean transparent PNG/SVG assets;
- icon captions, numbers, and labels must be separate editable PPT text.

Do not omit visible icons. Do not replace icons with unrelated circles, dots, emoji, or font glyphs.


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

Additional card/panel precision requirements:

- sample and record card/panel color tokens from the locked preview rather than guessing from style names;
- preserve group alignment, equal-width/equal-height relationships, row/column gaps, internal title/value positions, icon positions, and decorative details such as dot matrices, waves, divider lines, highlight bars, and translucent content bands;
- use native shapes only when fill, opacity, radius, border, glow, shadow, and density can match the preview; otherwise use card background PNG/SVG assets with editable text/icons layered above;
- Gate 6 fails if cards become plain rectangles, lose glass/glow/depth, or visibly change size, spacing, or internal content placement.


### Editable Text Position Anchor Rule

After preview/source lock, editable text must be positioned from the locked reference instead of auto-layout convenience.

For each title, subtitle, KPI label/value, card title/body, process label, chart label, table text, and footer/header text, record or infer:

- relative bbox and anchor point;
- alignment;
- baseline/vertical position;
- font size, weight, and line spacing;
- distance to paired icon, divider, card edge, or process node.

Do not move text to make local reconstruction easier. Do not let text drift because card groups or icon groups were rebuilt with different geometry. Gate 6 fails if visible text shifts, resizes, or reflows enough to break the locked preview alignment or hierarchy.


## Screenshot-Only Output Rejection

High fidelity must not be achieved by placing a full-slide screenshot over the slide.

A PPT fails delivery if:

- a full-slide image contains title/text/KPI/chart/table/cards/flow content;
- the slide has too few editable objects for its visible content;
- charts/tables/cards/flow/text visible in the reference are not present as native/editable objects when practical;
- source-vs-render looks close only because the whole reference was pasted as one image.

Full-slide images are allowed only for clean background texture/glow/gradient/dot-map/grid/wave atmosphere with no editable content.

## Company-Friendly Simple Prompt

Normal users may start with one short prompt:

```text
使用 $quality-editable-ppt，做一份《主题》PPT，风格自动推荐，先给我大纲确认。
```

Users do not need to mention phases, image_gen, image2, blueprint, Layer A/B/C, assets, SVG, or presentation plugin. The skill manages the steps and asks for confirmation when needed.

## Mode Routing

Modes only decide **how content is prepared and how locked references are created**:

- **Mode 1 — short topic / brief**: create outline → Gate 1 confirm outline → Gate 2 confirm page information structure and visual strategy → Gate 3 generate preview images → locked references.
- **Mode 2A — existing outline / document with fixed wording**: read the full content immediately and preserve the original text and hierarchy → Gate 1 confirm recognized content/outline → Gate 2 confirm page information structure and visual strategy → Gate 3 generate preview images → locked references.
- **Mode 2B — long-form material to be distilled**: extract key information into PPT outline → Gate 1 confirm outline → Gate 2 confirm page information structure and visual strategy → Gate 3 generate preview images → locked references.
- **Mode 3 — existing slide images**: determine source quality. Clear image → locked source references directly. Blurry image → generate same-structure HD replica image first, confirm it, then lock as source reference.
- **Mode 4 — outline + reference images + brand assets**: separate content source from visual constraint source → Gate 1 only when outline still needs confirmation → Gate 2 → Gate 3 → locked references.

After locked references exist, the original mode must stop controlling reconstruction behavior. All modes switch into the same **Scope-Aware Unified 3A Replica Core**.

## Scope-Aware Unified 3A Replica Core

Unified 3A is the **only post-lock reconstruction core**. It is not a single-image-only mode. Use it for:

- one image → one editable PPT slide;
- multiple images → matching editable PPT slides;
- a full PPT page set → batched editable reconstruction;
- Mode 1 / Mode 2 generated previews after user confirmation;
- Mode 3 uploaded source slide images;
- Mode 4 mixed reference workflows.

Unified 3A starts with three lightweight decisions before any build work:

1. **Scope Detection** — determine `single_slide`, `multi_slide`, or `deck_batch`.
   - `single_slide`: only discuss, analyze, build, render, and confirm Slide 01.
   - `multi_slide`: process the current batch of locked pages.
   - `deck_batch`: build the first 1-3 pages first, then continue in 3-5 page batches after confirmation.
2. **Source Quality Decision** — decide whether each locked reference is clean enough for direct crop use.
   - clear source: crops may be used as source-faithful assets when appropriate.
   - blurry / low-resolution source: treat it as layout/content reference only; rebuild clean background and regenerate/redraw key visual assets instead of using the blurry full-page image as final background.
3. **Asset Role Plan** — assign each visible region one role before building:
   - `reference_only`;
   - `native_editable_object`;
   - `regenerated_clean_asset`;
   - `source_crop_asset`;
   - `background_asset`.

This is a dispatcher, not an extra heavy workflow. It decides which existing abilities to use and prevents running the entire deck pipeline when the task is only one page.

## Reference Role vs Asset Role

A locked reference is the visual source of truth, but it is not automatically a final asset.

- Do not use a blurry full-slide reference as both final background and hero illustration.
- If the reference is blurry, use it for layout, proportions, text content, and visual relationships only.
- Rebuild clean backgrounds with native gradients, simple texture assets, or regenerated background assets.
- Regenerate or redraw complex hero illustrations as clean PNG assets when the source crop is too blurry.
- Keep text, cards, arrows, charts, tables, labels, and page chrome as editable/native objects whenever practical.

## Lightweight File Lock Rule

This is a lightweight guardrail, not the full hard-lock workflow.

Before preview/source/reference images can become locked references, save each one as a real project-local image file, preferably under `phase1/locked_references/`. Create or update `phase1/locked_reference_registry.json` with at least:

- slide ID;
- project-local `local_file`;
- SHA-256;
- width and height when available;
- confirmation state.

`local_file: null`, conversation-only previews, temporary URLs, or unreadable images must block Phase 1 / Phase 2 / Phase 3. Ask the user to regenerate or re-upload instead of falling back to outline, semantic reconstruction, or template redesign.

Use `scripts/light_lock_check.py` when available; otherwise perform the same checks with basic shell/Python commands. This check is intentionally small and does not require Node runtime, render heatmaps, or runtime evidence files.

## Flat Component Geometry Rule

Flat PPT-like components must be reconstructed by visual geometry, not redesigned from meaning.

This applies to cards, KPI blocks, step cards, number blocks, progress bars, conclusion bars, icon badges, divider lines, arrows, labels, title blocks, and list-like structures. Recover position, size, fill, border, radius, shadow, opacity, z-order, text, font size, and alignment from the locked reference.

## Phase 3 Binding Check

Inside Unified 3A, before Phase 3, verify that the PPT build uses the approved locked reference, current reconstruction plan / element inventory, and approved asset files. A short `phase3/build_input_summary.md` is enough; do not add heavy runtime evidence unless the user requests hard-lock mode. Do not build with stale SVG, old PNG assets, old blueprint layouts, or semantic reconstruction output.

## Mandatory Gates

The gates are scope-aware. Use single-slide wording for one-page work, batch wording for multi-page work, and deck wording only for full decks.

### Gate 1 — Quick Outline Confirmation

Gate 1 exists only when an outline still needs to be confirmed.

Use Gate 1 for:

- Mode 1 topic / brief tasks;
- Mode 2B long-form text that must first be distilled into a PPT outline;
- Mode 4 mixed-input cases where the outline is still not confirmed.

Gate 1 must be **outline only**.

Do not combine outline with page information structure, layout strategy, visual strategy, chart plan, asset plan, or reconstruction strategy.

Gate 1 output should be short:

- slide count / active scope;
- slide number;
- slide title;
- core message;
- 3–5 main content points.

End with:

```text
请确认大纲。确认后我将输出页面信息结构和视觉策略。
```

Use Gate 1 for Mode 2A fixed-wording outline/document tasks as a quick confirmation of the recognized original content. Do not generate a new outline; simply confirm that the extracted text and hierarchy are correct, then continue to Gate 2.

For Mode 3 image reconstruction, skip Gate 1 and use image reconstruction strategy.

### Gate 2 — Page Information Structure and Visual Strategy Confirmation

Run Gate 2:

- after Gate 1 for Mode 1 / Mode 2B / outline-unconfirmed Mode 4;
- directly for Mode 2A fixed-wording outline/document tasks;
- as a reconstruction-structure confirmation for Mode 3 only when needed.

Gate 2 defines:

- page module structure;
- content hierarchy;
- KPI / chart / table plan;
- main visual direction;
- background texture / atmosphere direction;
- icon / component plan;
- style and color strategy;
- expected editable objects;
- expected image assets;
- reconstruction complexity notes when needed.

Gate 2 is the **last confirmation step before high-visual preview generation**.

Forbidden before Gate 2 confirmation:

- generating background-only drafts;
- generating hero-only drafts;
- generating local-script preview substitutes;
- generating PPT renders;
- preparing a pure background image as if it were the preview.

End with:

```text
请确认页面信息结构和视觉策略。确认后我将调用 image_gen / image2 生成可复刻高视觉预览图。
```

For Mode 3 with an existing image, do not generate a new creative visual strategy unless the user asks. Use a reconstruction plan based on the locked source image or on the HD replica image when the original source is blurry.

### Gate 3 — Reference / Preview Confirmation

For generated previews, save each preview to a project-local file before asking for confirmation. Generated previews at Gate 3 must come from **image_gen / image2 / equivalent image generation**, not from local-script redraw.

For uploaded source images, save or register the local file before starting reconstruction.

Gate 3 confirmation creates locked references and triggers Scope-Aware Unified 3A Replica Core.

After Gate 3 lock:

- do not return to topic-based design;
- do not return to outline-based design;
- do not redraw a new low-fidelity page with local scripts;
- do not let the local builder replace the locked preview with a semantically similar but visually different PPT.

End with scope-aware wording:

```text
请确认参考图/预览图。确认后我将锁定图片并进入图片级高还原复刻流程。
```

For single-slide work, do not mention “修改第 X 页” or “构建 1-3 页”.

### Gate 4 — Reconstruction Plan Confirmation

After references are locked, output a compact reconstruction plan instead of a long default inventory unless the user requests a full element list.

The plan must include:

- scope: `single_slide`, `multi_slide`, or `deck_batch`;
- source quality decision;
- asset role plan;
- Layer A/B/C split;
- charts/tables/list-like structures to keep native when practical;
- elements that must be regenerated as clean assets.

End with scope-aware wording:

```text
请确认重建计划。确认后我将准备必要资产并构建。
```

### Gate 5 — Optional Asset Confirmation

Gate 5 is **not a default mandatory stop** for ordinary work.

Prepare only necessary assets. For normal one-page work, if asset choices are straightforward, skip separate asset confirmation and proceed directly to Phase 3 build with a short asset summary.

Trigger Gate 5 only when asset choices materially affect quality or need user review:

- complex hero illustration regeneration;
- blurry source requiring clean rebuild;
- brand logo / product image / specific icon confirmation;
- multiple asset options;
- background texture asset uncertainty;
- source-faithful crop fallback decision;
- any asset that may contain non-editable text or key data.

If Gate 5 is skipped, say:

```text
资产方案明确，跳过单独资产确认，直接进入构建并渲染对照。
```

If Gate 5 is triggered, end with:

```text
请确认资产方案。确认后我将构建并渲染对照图。
```

### Gate 6 — Render Confirmation

Build only the requested scope:

- `single_slide`: build and render Slide 01 only.
- `multi_slide`: build and render the current batch.
- `deck_batch`: build and render slides 1-3 first, then continue in 3-5 page batches.

Show the locked source and PPT render side by side. Diff heatmaps are optional in lightweight mode.

End with scope-aware wording:

```text
请确认还原效果。确认后我再继续下一步；如果需要修改，请指出具体区域。
```

## Absolute Rule After Locked Reference Creation


### Locked-Preview Replica Rule

Once a preview/source image is locked, PPT reconstruction must be a **replica build from the locked reference**.

Allowed after lock:

- native reconstruction of editable structures;
- asset regeneration/replacement when needed to better match the locked reference;
- source-faithful crops or clean HD regenerated assets;
- chart/table/icon/card rebuilding that visually follows the locked reference.

Forbidden after lock:

- semantic redesign with local scripts;
- generating a new page layout “based on the same meaning”;
- replacing preview-confirmed hero, background, or component relationships with simpler local-script drawings;
- showing a pure-background draft as if it were the real preview or real reconstruction.

After preview/source/reference images are confirmed or designated, they become locked references. This rule is shared by all modes and all scopes.

Forbidden after locked reference creation:

- Do not rebuild from the outline.
- Do not rebuild from the topic.
- Do not rebuild from semantic meaning.
- Do not create a new deck in a similar style.
- Do not continue from a pre-lock blueprint if it conflicts with the locked reference.
- Do not simplify visual density without approval.
- Do not skip chart/icon/card-effect/background checks.
- Do not use a full finished preview screenshot as the final slide.
- Do not let style names, outlines, or pre-lock blueprints override the locked reference.
- Do not use a blurry full-page reference as final background when clean rebuild is required.

## Tool Priority

### Preview Generation

After blueprint confirmation, use image generation first:

1. `image_gen` / `image2` / GPT Image 2 / ChatGPT Images 2.0 / `gpt-image-2`.
2. Equivalent image generation capability in the current Codex environment.
3. Configured image-generation API.
4. SVG/HTML/canvas only as fallback.

Preview images must be **reconstructable**, not freeform posters.

### Final PPTX Construction

After assets are confirmed, use presentation tooling:

1. `presentation` plugin / `@presentations` / equivalent presentation tool.
2. PptxGenJS or presentation-skill workflow.
3. SVG-to-DrawingML conversion if available.
4. python-pptx / manifest-based builder as fallback.

The presentation tool must build from the blueprint, locked references, element inventory, asset plan, and assets — not directly from the outline. After a locked reference exists, the locked reference overrides topic/outline intent whenever they conflict.

## Reconstructable Preview Rules

The preview-generation stage must control complexity from the beginning.

Required:

- Use bold color blocks and clear content areas.
- Prefer flat icon systems.
- Use pure color, PPT-native gradients, or full-slide texture backgrounds.
- Keep background and content separate.
- Use standard chart types: donut, line, bar, progress, matrix, simple radar, KPI cards.
- Keep charts readable and reconstructable.
- Keep card boundaries clear.
- Keep text outside illustrations and background assets.
- Use at most one complex hero illustration per slide.

Avoid:

- Poster-like fused backgrounds.
- Text embedded in illustrations.
- Tiny unreadable pseudo-charts.
- Excessive micro-icons.
- Overly complex glow/particles/texture behind editable content.
- AI-generated decorative charts that have no chart spec.

## Preview Complexity Budget

Default per-slide budget:

- Complex hero illustration: max 1.
- Complex charts: max 2.
- Cards: max 8.
- Small icons: max 20.
- Main color families: max 3.
- Font hierarchy: max 4.
- Background type: solid / gradient / full-slide texture background.

If the design exceeds this budget, warn the user and recommend splitting or simplifying.

## Visual Blueprint Requirements

Before preview generation, create one blueprint per slide.

Each blueprint must include:

- Slide layout.
- Background type.
- Main color blocks.
- Text regions.
- Card/module regions.
- Chart inventory.
- Icon inventory.
- Hero illustration plan.
- Layer A/B/C plan.
- Expected editability.
- Complexity score.

## Layer A/B/C Rules

| Layer | Contents | Implementation | Editability |
|---|---|---|---|
| Layer A — Visual Assets | background texture, glow, large decorative background, hero illustration, complex icons, complex dashboards, dense charts | full-slide background PNG / transparent PNG / SVG / source-faithful crop with feathering | movable / resizable / replaceable |
| Layer B — Editable Structures | color blocks, cards, panels, circles, lines, arrows, connectors, tables, matrices, progress bars, conclusion bars | PPT native shapes/tables/connectors when practical | editable |
| Layer C — Editable Text | titles, subtitles, body, page numbers, labels, numbers, chart labels, KPI values | PPT native text | editable |

Default: background glow, texture, waves, and atmosphere are Layer A assets, not native PPT shapes.

## Chart Reconstruction Rule

Every visible chart must be inventoried and implemented.

Each chart must choose one implementation:

1. Native PPT chart with editable data.
2. Native PPT chart + decorative overlay shapes for visual fidelity.
3. Shape-based chart + linked editable chart data file when native charting is unavailable.
4. PNG chart asset + editable title/labels/data note only when the chart is decorative, non-standard, or data cannot be reliably recovered.

Missing a visible chart is a failure.

## Chart Data Binding Optimization

This is a **safe optimization layer**. It must not disrupt the existing high-fidelity reconstruction workflow, gates, assets, or 1-3 page checkpoint. It runs inside Phase 1 / Gate 4 rather than adding a new default public gate.

For standard charts, prefer editable native PPT charts whenever data is available or can be generated from the blueprint.

Standard chart types include:

- donut / pie;
- column / bar;
- line / area;
- scatter when simple;
- radar when simple;
- progress and KPI charts when suitable.

Data source priority:

1. Use chart data defined in `visual_blueprint.json` when the deck is generated from an outline or brief.
2. Use visible numeric labels from the locked reference image when restoring from slide images.
3. Estimate data from geometry only when labels are unavailable, and mark `confidence: estimated`.
4. Ask for user confirmation in Gate 4 if chart data is uncertain.

For every standard chart, output:

- `chart_id`;
- chart type;
- categories;
- series;
- values;
- axis range;
- legend;
- colors;
- implementation;
- data confidence;
- whether native editable chart is possible.

Do not use shape-only charts for column, bar, line, donut, or pie charts when reliable data exists and native chart construction is available. If a shape-based chart is used as a fallback, also output the editable data in `chart_registry.json` or CSV so users can rebuild the chart manually.

## Table Reconstruction Rule

Every visible data table must be inventoried and implemented. For tabular data, use **native PowerPoint table components** whenever the available presentation tool supports them.

Do not rebuild real tables as a group of rectangles and lines unless native table construction is unavailable or the table is purely decorative.

A real table includes:

- header row;
- data rows;
- columns with aligned values;
- row/column separators;
- status chips inside cells;
- data labels arranged in a grid.

For every table, output:

- `table_id`;
- slide number;
- row count and column count;
- header values;
- cell values;
- column widths;
- row heights;
- header style;
- body style;
- border style;
- zebra striping, if present;
- cell badges/icons, if present;
- implementation method.

Implementation priority:

1. Native PPT table with editable cell data.
2. Native PPT table + overlay badges/icons for visual fidelity.
3. Shape-based table only when native table construction is unavailable, and the editable table data must still be exported as CSV/JSON.
4. PNG table asset only for decorative or unrecoverable tables, with editable title/labels outside the asset.

Missing a visible table is a failure. A real data table drawn only with rectangles/lines while native PPT table support is available is also a failure.

## Icon Reconstruction Rule

Every visible icon must be inventoried.

Implementation choices:

- Default for preview-styled icons: SVG icon / transparent PNG.
- Ultra-simple flat icon only: native PPT shape is allowed only when it visually matches the locked preview.
- Complex, glowing, gradient, multi-layer, badge, or product-style icon: image_gen/image2 generated transparent PNG or clean SVG.
- Hero icon/illustration: PNG/SVG asset.

Missing a visible icon is a failure. Low-fidelity primitive-shape redraw, disconnected-line construction, or mismatched icon library substitution is also a failure.

## Card Effect Rule

Each card/panel must record:

- fill,
- border,
- opacity,
- radius,
- shadow,
- glow,
- highlight line,
- divider,
- padding.

If the reference has shadows/glow and the PPT render has plain rectangles, the slide fails.

## Text Contamination Rule

Layer A assets must not contain editable text, numbers, labels, or page numbers unless unavoidable.

If an asset contains editable text:

1. Recrop it.
2. Regenerate a clean PNG with image_gen/image2.
3. Split it into background/illustration asset + editable text.

## Detail Fidelity Optimization

This is a safe optimization layer. It must not disrupt the existing workflow, gates, chart data binding, assets, or 1-3 page checkpoint. It runs inside Phase 1, Phase 2, Phase 3, and final QA.

The goal is to improve the final 5-15% visual similarity: card colors, shadows, glows, hero illustrations, icon badges, header beams, clean backgrounds, and small decorative details.

## Hero Illustration Asset Rule

For complex hero illustrations, use **image_gen / image2 to regenerate a clean transparent-background PNG by default**.

This applies to:

- AI hubs;
- glowing shields;
- security operation centers;
- endpoint-network hero illustrations;
- decision engines;
- futuristic platforms;
- complex decorative technology objects;
- SOC floor rings;
- AI core network diagrams;
- glowing brain/AI platform illustrations;
- multi-device node clusters.

Do not recreate complex hero illustrations with native PPT shapes unless the illustration is very simple. Native PPT reconstruction is allowed only for simple geometric illustrations.

## Hero Illustration Fallback / Escalation Rule

Complex hero illustrations must enter an asset escalation path before Phase 3. Do not start with low-fidelity native shapes for complex hero art.

Implementation priority:

1. Generate a clean transparent PNG with image_gen / image2 while preserving the locked preview's composition, style, colors, glow, node layout, and visual role.
2. If regenerated output is too different from the locked preview, retry with a stricter prompt.
3. If regeneration still causes style drift, structural mismatch, wrong node count, wrong device placement, or weak glow, use a high-fidelity crop from the locked preview as fallback.
4. If the crop contains text/card/background contamination, recrop, clean, mask, or split into asset + editable text.
5. If both regeneration and crop fail, stop and ask the user which asset version to use before Phase 3.

Hero PNG assets must not contain editable text, labels, numbers, cards, chart axes, page numbers, or module borders unless the user explicitly approves a source-faithful crop.

A complex hero illustration is considered failed if:

- the subject composition is different from the locked reference;
- key rings, nodes, devices, shields, AI core, brain, platform, or glow are missing;
- the node count or device positions are clearly different;
- the lighting/glow style is significantly weaker;
- the generated asset looks like a new design instead of a reconstruction;
- native shape reconstruction looks simplified or low-fidelity.

When failure is detected in the first 1-3 page render, return to Phase 2 asset preparation and replace the bad native/asset version with image_gen/image2 PNG or source-faithful crop before continuing.

## Background Integration Strategy

Classify complex visuals before asset creation:

1. Background-integrated visuals: SOC room, environment, floor rings, large glow fields, wall screens, and spatial atmosphere. Use full-slide background assets or local background patches.
2. Independent hero visuals: AI core, device cluster, glowing brain, shield, or badge-like hero object. Use transparent PNG assets.
3. Structural content: text, cards, charts, tables, legends, labels, arrows, page numbers. Keep editable with PPT-native objects whenever practical.

Do not force background-integrated visuals into transparent cutouts if they naturally belong to the background. Do not bake structural content into background assets.

## Source Crop Integration Rule

Source-faithful crop fallback must not be pasted as a raw rectangular screenshot.

If source crop is used, integrate it with one of these methods:

- transparent cutout;
- feathered-edge crop;
- background-matched crop;
- full local background patch when the hero and background cannot be separated.

A crop fails if it shows visible rectangular edges, background color mismatch, hard cut-off glow, or background pollution.

## Asset Seamless Integration Check

Before Phase 3 and again during the 1-3 page render check, inspect image assets for:

- visible rectangular boundaries;
- mismatch against PPT background color;
- hard glow cutoff;
- text/card/chart/table pollution;
- poor local blending;
- screenshot-like pasted appearance.

Failed assets must return to Phase 2 for transparent cutout, feathering, background matching, or local background patch replacement.

## Card Color Sampling Rule

Card colors must be sampled from the locked preview, not guessed from the style name.

For every card, record sampled values:

- fill color;
- gradient start/end;
- border color;
- border opacity;
- shadow color;
- glow color;
- background contrast.

If rendered PPT card colors, borders, gradients, or glows visibly differ from the locked reference, patch them before delivery.

## Card Token System

Create page-level color tokens from the locked preview before PPT construction:

- `page-bg`;
- `panel-bg`;
- `card-bg`;
- `card-border`;
- `card-glow`;
- `text-main`;
- `text-sub`;
- `accent-primary`;
- `accent-secondary`.

Use these tokens consistently across cards, panels, icon badges, and charts.

## Final Color Patch Pass

Before showing the first 1-3 page render, run a final patch pass for:

- image asset blending;
- background color mismatch;
- card color mismatch;
- card border/glow mismatch;
- icon badge color mismatch;
- header beam color mismatch.

Do not show the first render if obvious asset seams or card color mismatches are still present.

## Card Style Registry

Cards and panels must be treated as style components, not plain rectangles. For every visible card, record:

- fill color;
- gradient, if any;
- border color and opacity;
- radius;
- shadow;
- glow;
- inner highlight;
- divider lines;
- state color;
- padding.

If card colors or shadows are visibly different from the locked reference, the slide requires patching.

## Background Purity Check

Full-slide background assets may contain only:

- solid color;
- gradient;
- texture;
- grid/dot pattern;
- glow;
- atmosphere;
- abstract decorative technology lines.

Background assets must not contain:

- card borders;
- table lines;
- chart axes;
- buttons;
- labels;
- title text;
- page numbers;
- any editable structure.

If a background image contains card wireframes or content structure, it fails the purity check and must be regenerated or split.

## Header Decoration Registry

Header beams, title separators, corner brackets, short glowing lines, and decorative top rules must be inventoried and reconstructed.

Implementation can be:

- native PPT lines;
- semi-transparent shapes;
- gradient line overlays;
- small PNG glow assets;
- line + shadow/glow combination.

Do not omit visible header decoration lines.

## Icon Badge Registry

Icons with backgrounds must be reconstructed as icon badges, not just glyphs.

For every visible icon badge, record:

- icon background shape;
- icon glyph;
- badge fill/gradient;
- badge border;
- glow/shadow;
- state dot;
- size and placement.

Simple glyphs can be SVG/native shapes. Complex gradient or glowing icon badges can be transparent PNG assets generated with image_gen / image2.

## Detail Density Check

Before final delivery, compare detail density against the locked reference:

- small status dots;
- tiny labels;
- chart legends;
- card inner details;
- header beams;
- footer icons;
- decorative lines;
- background texture intensity;
- icon badge details.

If the PPT render looks cleaner but less detailed than the locked reference, patch it instead of delivering.


## Required Internal Pipeline

1. Intake and mode routing.
2. Determine which mode applies:
   - Mode 1: topic / brief;
   - Mode 2A: existing outline / document, wording must remain unchanged;
   - Mode 2B: long-form material to be distilled into an outline;
   - Mode 3: existing slide images;
   - Mode 4: mixed inputs.
3. Run Gate 1 as the content/outline confirmation step:
   - required for Mode 1;
   - required for Mode 2A as recognized-content confirmation without rewriting;
   - required for Mode 2B as extracted-outline confirmation;
   - skipped for Mode 3;
   - conditional for Mode 4.
4. Run Gate 2:
   - confirm page information structure, content hierarchy, and visual strategy;
   - for Mode 2A, this runs after the user confirms the recognized original content in Gate 1.
5. Only after Gate 2 confirmation, create or select preview/source references:
   - Mode 1 / Mode 2A / Mode 2B / Mode 4: generate full high-visual reconstructable preview images with image_gen / image2 / equivalent image generation;
   - Mode 3 clear source: register the source image;
   - Mode 3 blurry source: generate same-structure HD replica preview first, then confirm it.
6. Save/register references as project-local files and run the lightweight file lock check.
7. Gate 3 confirmation creates locked references.
8. Enter Scope-Aware Unified 3A Replica Core for every mode.
9. Run Scope Detection: `single_slide`, `multi_slide`, or `deck_batch`.
10. Run Source Quality Decision:
   - clear source → direct crop/rebuild allowed;
   - blurry source → use for layout/content reference only, regenerate clean background and key visual assets.
11. Run Asset Role Plan: `reference_only`, `native_editable_object`, `regenerated_clean_asset`, `source_crop_asset`, `background_asset`.
12. Prepare a compact reconstruction plan using Layer A/B/C:
   - Layer A: clean background, glow, complex hero/illustration assets, complex icons;
   - Layer B: native shapes, cards, tables, charts, lists, arrows, connectors, progress bars, conclusion bars;
   - Layer C: editable text, values, labels, page numbers.
13. Bind standard charts and tables to native PPT components when data is available or recoverable.
14. Prepare only necessary assets; avoid generating assets not required by the plan.
15. Run Phase 3 Binding Check with `phase3/build_input_summary.md`.
16. Build once for the requested scope, always as a **locked-preview replica build**, not a local redesign:
   - single slide: Slide 01 only;
   - multi-slide: current batch;
   - full deck: first 1-3 pages, then 3-5 page batches.
17. Render locked source vs PPT render for user confirmation.
18. Default to at most one automatic repair. Further repair requires user confirmation.
19. Final color patch pass, render compare, and QA for the delivered scope.

## Built-In Bold Color-Block Styles

The package uses **7 fixed built-in styles + 1 automatic recommendation router**.

1. `蓝绿产品发布风`
2. `蓝黑科技运营风`
3. `紫色科技色块风`
4. `紫蓝AI科技风`
5. `深蓝深红攻防风`
6. `深灰绿色监控风`
7. `深灰金色年会风`
8. `自动推荐`

Use the detailed merged style file in `style-profiles/STYLES.md`.

Style color tokens must follow `style-profiles/STYLES.md`, including `#1135EA`, `#01B285`, `#5D08D8`, `#123371`, `#B81615`, `#E3E6ED`, `#61696A`, `#E9EDF1`, `#342D2B`, `#C9A24D`, and `#E8E2D8` where specified.

`自动推荐` is not a fixed style. It routes the task to one of the 7 fixed styles based on topic, scenario, and audience.

## Native Table Reconstruction Rule

Readable real tables must be reconstructed as native PPT tables when practical. Table screenshots are not acceptable when table text and structure are readable.

## Editable Fidelity Delivery Gate

Before final delivery, inspect the PPTX structure and the exported render.

Reject and rebuild if the slide is screenshot-only.

Minimum expectations for a page with these visible elements:

- visible title/body/KPI text → PPT text objects;
- visible cards/panels/chips/arrows/connectors → native editable shapes/lines when practical;
- visible standard charts → native PPT charts or editable chart approximations with data files;
- visible readable tables → native PPT tables;
- visible simple icons → native shapes/freeforms or editable SVG when practical;
- visible complex hero/background/complex icons → clean image assets without editable text contamination.

A slide with one large image plus a few labels is not acceptable when the reference contains charts, tables, cards, icons, and flow components.

## Failure Conditions

A slide fails if:

- It looks like a new slide rather than reconstruction.
- The preview was too complex but no warning was given.
- A visible chart is missing.
- A visible data table is missing.
- A real data table is drawn only with rectangles/lines while native PPT table support was available.
- A standard chart with reliable data is rendered only as shapes while native editable chart construction was available.
- A visible icon is missing.
- A complex hero illustration was redrawn with low-fidelity native shapes instead of entering the hero asset escalation path.
- A regenerated hero PNG drifts from the locked preview and no retry/crop fallback is attempted.
- A source-faithful crop fallback is needed but not used after generation fails.
- A source crop is pasted as a raw rectangle with visible color mismatch or hard edges.
- A hero illustration PNG contains editable text, card borders, chart axes, or page numbers.
- Card shadows/glow are missing.
- Card/panel internal text, icon, decorative band, padding, or group spacing differs visibly from the locked preview.
- Card colors, gradients, or borders are clearly different from the locked reference.
- Card colors are guessed from style names instead of sampled from the locked preview.
- Text is baked into assets unnecessarily.
- Editable text position, baseline, alignment, or spacing drifts from the locked preview.
- Background/content layers are fused incorrectly.
- Background-integrated visuals are forced into transparent cutouts when they should be background assets.
- A background asset contains card wireframes, table borders, buttons, labels, or other editable structures.
- Header beam lines, title separators, or icon badge backgrounds are visibly omitted.
- Final PPTX render is clearly lower density than the preview.
- First 1-3 pages were not rendered and confirmed before continuing.
- Single-slide work uses multi-page wording or builds pages outside Slide 01.
- The workflow uses a blurry full-page reference as final background instead of clean rebuild.
- Mode 3 reconstruction returns to topic/outline/visual-style generation after the source image is locked.
- Mode 1 / Mode 2 / Mode 4 did not switch into locked-reference reconstruction after preview confirmation.
- Flat components were redesigned from meaning instead of reconstructed by visual geometry.
- Phase 3 used stale SVG/PNG assets, old blueprint layouts, or semantic reconstruction output after assets were confirmed.
- `local_file` is null, missing, unreadable, or does not match the recorded SHA-256.
- Gate 6 does not show locked source and exported PPT render side by side for the first 1-3 slides.
- The workflow uses a different post-lock reconstruction path instead of Unified 3A.
- Multi-image or full-PPT reconstruction switches back to outline/topic/semantic generation after lock.
- Codex starts automatic multi-round repair beyond the allowed repair round without explicit user approval.

Do not deliver known low-fidelity slides as final output.


---

# v5.22 Micro Icon, Card, and Text Precision Lock Reconstruction Rules

These rules preserve the existing workflow and only tighten execution inside the current inventory, build, and Gate 6 QA steps.

## Micro Icon Likeness

Small icons must be visually faithful, not only semantically similar. Preserve silhouette, stroke weight, stroke cap/join, internal negative space, badge/glow/halo, color order, and viewBox padding. Generic same-meaning icon substitutions fail when the locked preview icon has a different visual family.

## Card / Panel Fidelity

Cards and panels must be reconstructed from measured preview tokens: bbox, radius, fill/gradient/opacity, border, shadow/glow/elevation, internal translucent bands, decorative waves/dots/dividers, padding, and group spacing. A card that loses its depth, glass feeling, internal band, or aligned spacing fails even when the text is present.

## Editable Text Position Fidelity

Editable text must keep the locked preview anchors, baselines, alignment, size, weight, line spacing, and icon/text relationship. Automatic reflow, title drift, subtitle drift, KPI value movement, and process-label repositioning fail Gate 6 when visually noticeable.
