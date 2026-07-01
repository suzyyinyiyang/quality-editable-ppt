# Workflow

Merged from the original workflow files. The final workflow is preserved; this version makes the post-lock flow scope-aware without removing existing capabilities.


---

<!-- Source: workflows/01-company-simple-prompt.md -->


# 01 — Company Simple Prompt

Company users should be able to start with one sentence.

Example:

```text
使用 $quality-editable-ppt，做一份《主题》PPT，风格自动推荐，先给我大纲确认。
```

The skill must manage all steps. Users should only reply:

- `确认`
- `修改第 X 页`
- `换成某某风格`
- `继续`

Do not require users to know phase names, image generation tools, presentation plugin details, blueprint schemas, or Layer A/B/C.


---

<!-- Source: workflows/02-outline-gate.md -->


# 02 — Quick Outline Gate

Generate or optimize the deck outline before any visual or strategy work.

For Mode 1 topic/brief tasks, this gate must be outline only. Keep it short.

Output per slide:

- slide number;
- title;
- core message;
- 3–5 main content points.

Do not include page information structure, layout strategy, visual strategy, chart plan, asset plan, or reconstruction strategy in Gate 1.

Stop and ask:

```text
请确认大纲。确认后我将输出页面信息结构和视觉策略。
```


---

<!-- Source: workflows/03-visual-blueprint.md -->


# 03 — Page Information Structure and Visual Strategy

Run only after Gate 1 outline confirmation.

Before generating preview images, create a reconstruction-aware page information structure and visual strategy.

Each slide strategy must include:

- page module structure;
- content hierarchy;
- KPI / chart / table plan;
- main visual direction;
- background texture / atmosphere direction;
- card/module regions;
- icon/component plan;
- style and color strategy;
- expected editable objects;
- expected image assets;
- preview complexity notes when needed.

Stop and ask:

```text
请确认页面信息结构和视觉策略。确认后我将生成可复刻高视觉预览图。
```


---

<!-- Source: workflows/04-reconstructable-preview-generation.md -->


# 04 — Reconstructable Preview Generation

Run only after visual blueprint confirmation.

Use image generation first:

- image_gen;
- image2;
- GPT Image 2 / ChatGPT Images 2.0 / gpt-image-2;
- equivalent Codex image-generation capability.

Preview images must obey the blueprint.

Required visual style:

- bold blocks;
- flat icons;
- clear cards;
- standard charts;
- separate background and content;
- avoid text embedded in hero illustrations unless the hero is intentionally a complex fused asset whose intrinsic text must stay inside the asset for fidelity;
- no tiny unreadable pseudo-charts.

Stop for Gate 3 confirmation.


---

<!-- Source: workflows/05-preview-lock.md -->


## Restored Detail-Replica Checkpoints

Carry these checks through Phase 1 / Phase 2 / Phase 3 without adding public gates:

- background route: clean full-slide texture asset vs native gradient;
- hero route: clean crop / regenerated transparent PNG/SVG / background-fused asset;
- text contamination: assets checked for residual labels, title fragments, pseudo-text, duplicated numbers;
- edge treatment: cropped/fused assets use alpha/soft-edge when needed;
- icon route: simple native/SVG, complex PNG/SVG, none omitted;
- card box model: border, shadow, radius, size, padding, icon-text alignment;
- chart/table presence: every visible chart/table is reconstructed;
- editable floor: screenshot-only output is rejected.


## v5.0 强化版复原检查点

Phase 1 / Phase 2 / Phase 3 中必须继承 5.0 强化版的资产复原逻辑：

- 背景纹理优先干净整图背景资产；
- 主视觉优先透明 PNG/SVG 或 source-faithful 裁切；
- 裁切资产必须避免硬边和文字污染；
- 小 icon 不得省略；
- 卡片必须按盒模型复刻；
- 整页截图式输出必须失败重建。


## Primary Asset / Component Reconstruction Checkpoints

These checkpoints are part of the normal reconstruction path and do not create a new public gate:

- complex textured/glow/grid/dot/wave backgrounds route to one clean full-slide background asset;
- pure solid/simple gradient backgrounds route to native PPT fill;
- independent hero assets route through edge cleaning, light feathering, and background blending;
- visually inseparable hero/background regions route to a background-fused asset;
- every visible small icon is reconstructed; no Unicode/emoji/icon-font substitutes;
- icon base and icon body are handled separately;
- readable tables preserve native table styling, including line color and opacity;

- mini trend charts / KPI sparklines route to native hidden-axis line charts when data is readable, or one continuous smooth vector path / SVG / transparent asset when decorative; never multiple disconnected straight line segments;
- cards and components preserve box model, shadows, borders, radius, and size.

# 05 — Reference Lock and Scope Detection

Before confirmation, save every preview/source image to a real project-local file, preferably under `phase1/locked_references/`, and record `local_file` plus SHA-256 in `phase1/locked_reference_registry.json`.


## Current-Run Preview Lock Rule

When Gate 3 preview images are confirmed, only the preview files generated in the current run / current conversation step may be locked.

Do not:

- pull older preview files from previous runs;
- compare against earlier generated previews unless the user explicitly asks to reuse them;
- mix old `locked_references` with current preview outputs;
- lock a previous preview simply because it looks similar.

The lock registry for the current run must contain only the newly generated preview files that were just confirmed.

After Gate 3, confirmed preview/source images become locked references. The original mode stops controlling reconstruction behavior.

Immediately determine:

- `scope_type`: `single_slide`, `multi_slide`, or `deck_batch`;
- `source_quality`: clear enough for source crop, or blurry/low-resolution and reference-only;
- `checkpoint_range`: Slide 01 only, current batch, or first 1-3 pages.

After this point:

- do not redesign from outline;
- do not redesign from topic;
- do not rebuild from semantic meaning;
- do not use generic templates;
- do not build PPTX if `local_file` is null, missing, or hash-mismatched;
- do not use a blurry full-page source as the final background when clean rebuild is required.

Runtime folders may still be used as needed, but do not create unnecessary assets or reports for a simple one-page job.

---

# 05B — Scope-Aware Unified 3A Replica Core

Unified 3A is the only post-lock core path. It handles single-image, multi-image, and full-PPT reconstruction by changing scope, not by switching workflows.

Core path:

1. verify lightweight file lock;
2. detect scope;
3. judge source quality;
4. create asset role plan;
5. build only the required scope;
6. show locked source and PPT render;
7. stop for user confirmation.

Scope behavior:

- `single_slide`: analyze, build, render, and confirm Slide 01 only.
- `multi_slide`: process the current batch of locked pages.
- `deck_batch`: first build slides 1-3, then continue in 3-5 slide batches after confirmation.

Cost controls:

- no new preview generation after lock;
- prepare only necessary assets;
- max repair rounds: 1 by default;
- max build attempts per scope: 1 initial + 1 repair;
- strict/high-fidelity escalation requires explicit user request.

---

<!-- Source: workflows/06-phase1-analysis-and-selfcheck.md -->


# 06 — Reconstruction Plan and Step 1.4 Self-Check

For each locked slide in the active scope, output a compact reconstruction plan. Use a full element inventory only when the slide is complex or the user requests it.

Required decisions:

- scope and checkpoint range;
- source quality decision;
- background treatment;
- hero illustration treatment;
- native editable objects;
- regenerated clean assets;
- source crop assets;
- charts/tables/list-like structures;
- text contamination risks.

## Step 1.4 Self-Check

Before asking the user to confirm, run a missing-element check:

- small icons missed?
- chart missed?
- table or list-like data missed?
- card shadow/glow missed?
- card inset illustration missed?
- bottom bar missed?
- page number missed?
- connector node missed?
- background texture missed?
- blurry source used as final full-page background incorrectly?
- text accidentally included in image asset?

Stop for Gate 4 confirmation.

---

<!-- Source: workflows/07-phase2-asset-preparation.md -->


# 07 — Necessary Asset Preparation

Prepare only assets required by the reconstruction plan. Do not build PPTX in this phase.

Typical outputs when needed:

- `asset_plans/slideXX_asset_plan.json`;
- clean background asset for texture/glow/complex gradient;
- regenerated or source-faithful hero asset;
- icons only when native/SVG reconstruction is not practical;
- chart/table assets only for decorative or unrecoverable items.

Asset rules:

- background image must not contain editable text;
- blurry full-slide references should not be used as final backgrounds;
- hero image should be transparent PNG when practical, or a clean local background patch when visually fused;
- icons should be SVG/native when simple, PNG when complex;
- chart assets should not replace editable chart titles/labels unless unavoidable;
- any asset containing editable text must be recropped, regenerated, or split.

Gate 5 is optional. Stop for asset confirmation only when asset choices need user review. For ordinary pages with straightforward assets, skip separate Gate 5 and combine a short asset summary with the build input summary.

---

<!-- Source: workflows/08-phase3-presentation-build.md -->


# 08 — Phase 3 Presentation Build

Run only after the reconstruction plan and necessary assets are ready.

Use `presentation` plugin / `@presentations` / equivalent presentation generation tool first.

Build source of truth:

- locked references;
- reconstruction plan / element inventory;
- Layer A/B/C plan;
- necessary asset plan and assets;
- chart/table registries when applicable.

Before building, verify that the PPT build input references the approved locked reference and current asset files. Write a lightweight `phase3/build_input_summary.md` listing locked reference paths, asset paths, scope, and builder input source. Do not build with stale SVG/PNG assets or semantic reconstruction output.

## Scope-Aware Checkpoint

Build only the required scope:

- `single_slide`: Slide 01 only.
- `multi_slide`: current batch.
- `deck_batch`: first 1-3 pages, then 3-5 page batches after confirmation.

Render the built slides to images and show each locked source beside the exported PPT render. A heatmap is optional in lightweight mode. Stop for Gate 6 confirmation.

Do not continue beyond the active scope until the user confirms the restoration quality.

---

<!-- Source: workflows/09-render-compare-and-final-qa.md -->


# 09 — Render Compare and Final QA

After the 1-3 page checkpoint is approved, build the remaining slides.

For every slide, render the PPTX page and compare with the locked reference.

QA must check:

- layout match;
- visual density;
- background match;
- card styles and shadows;
- icons present;
- charts present;
- text not baked into assets;
- colors and spacing;
- page chrome and footer;
- editability of core elements.

Output:

- final PPTX;
- rendered images;
- contact sheet;
- QA report.


---

# v5.16 Lightweight Execution Discipline

This section preserves the v5.15 workflow and only clarifies execution discipline.

- Gate 3 must use real image generation for high-visual previews.
- Do not run tool-availability prechecks, environment scans, tool enumeration, package checks, or tool-registry lookups before Gate 3.
- Directly invoke the explicitly selected image-generation route; if it cannot be invoked, stop before Gate 3 instead of discovering fallback tools or using local fallback preview generation.
- Preview lock reads only the current run's newly generated and confirmed preview files.
- Complex backgrounds, title bars, and icons should be assetized instead of redrawn.
- Standard charts should stay native/editable whenever practical.
- If a downgraded shape-based implementation is produced, pause and ask the user whether it is acceptable instead of silently delivering.


---

# v5.17 Stable Lock Workflow Discipline

This section does not add new public gates. It clarifies execution inside the existing gates.

After Gate 3 preview lock:

1. Treat the current locked preview as the only visual source.
2. Do not redesign from outline or style.
3. Do not compare against older previews.
4. Build Layer A/B/C plan:
   - A: background image/atmosphere
   - B: complex assets
   - C: editable text/tables/charts/simple shapes
5. Use native drawing only for elements in the native allowlist.
6. Use PNG/SVG/image assets for complex visuals.
7. If shape-based downgrade occurs, pause for user confirmation instead of silently delivering.

Keep execution lightweight. Perform targeted repair only for the regions that fail visual fidelity.


---

# v5.18 Mode 3 Clean Layer Lock Workflow Discipline

This section does not change the main workflow. It only clarifies how Mode 3 executes inside the existing reconstruction plan.

For each Mode 3 slide:

1. Lock the current reference image only.
2. Treat the full-slide reference as visual reference, not final background.
3. Create a Layer A/B/C plan.
4. Build or generate a clean background asset for Layer A.
5. Independently rebuild Layer B assets and Layer C editable objects.
6. If full-slide screenshot overlay is used, pause and ask the user to approve the downgrade.
7. In the first 1–3 page render comparison, report background route, asset route, native chart/table status, and any downgrades.

Do not add broad scans, old preview comparisons, or extra public gates.


---

# v5.19 Background and Icon Lock Workflow Discipline

This section does not change the main workflow.

During the existing reconstruction plan:

1. Classify background:
   - pure solid → native PPT fill;
   - anything else → image-generated clean background.
2. Do not create background by erasing text/icons/cards/charts from screenshots.
3. Classify icon:
   - simple line/filled icon → transparent PNG or SVG continuous path;
   - simple icon background → native PPT shape;
   - complex fused icon badge → combined transparent PNG.
4. If chart overlaps icon, keep chart native and separate icon.
5. If any downgrade is needed, pause for user confirmation.

Do not add broad scans, old preview comparisons, or extra public gates.


---

# v5.20 Visual Asset QA Lock Workflow Discipline

This section does not change the main workflow.

During the existing reconstruction plan and first 1–3 page checkpoint:

1. For every non-solid background, require real image generation raster background. Local SVG/canvas/script/PPT shape background is a downgrade.
2. Treat hero/main visual as an asset by role, not by geometry simplicity.
3. Treat complex icons on complex backgrounds as combined transparent PNG assets.
4. Keep simple icons as SVG/transparent PNG and simple icon bases as native shapes.
5. For complex slides, include compact asset preview in the existing first 1–3 page checkpoint.
6. Output explicit QA summary with pass/fail/downgrade labels.
7. Do not continue batch generation until QA status and downgrade approvals are clear.

No extra public gate, broad tool scan, old preview comparison, or workflow reorder is allowed.

---

# v5.21 Small Icon SVG Lock Workflow Discipline

This section does not change the main workflow.

During the existing reconstruction plan and first 1–3 page checkpoint:

1. Classify icons by size and complexity.
2. Small simple line/filled icon → SVG continuous path first.
3. If SVG is unreliable → transparent PNG.
4. Screenshot-cropped small simple icon → downgrade requiring QA disclosure.
5. Medium/large complete icon crop remains allowed when sharp and faithful.
6. Complex glowing/gradient badge icon remains combined transparent PNG.
7. QA must report small icon route and block clipped/blurry/incomplete small icons unless user accepts downgrade.

Do not add new gates, broad scans, or workflow reorder.
