# Quality Editable PPT — Merged Distribution

This is the merged version of `quality-editable-ppt`. It preserves the final workflow and all optimization constraints while reducing file count.

## What is preserved

- Outline / strategy confirmation.
- Visual blueprint confirmation.
- image_gen / image2 reconstructable preview generation.
- Preview lock as the only visual source of truth.
- Phase 1 element inventory and Step 1.4 self-check.
- Chart Data Binding: standard charts should use native PPT charts with editable data when possible.
- Native Table Reconstruction: real data tables should use native PPT table components when possible.
- Detail Fidelity Optimization: card styles, transparent hero PNGs, icon badges, header beams, background purity, and detail density.
- Phase 2 asset confirmation.
- Phase 3 first 1-3 page PPT render confirmation.
- Final render comparison and QA.

## Important execution principle

This merge only consolidates supporting files. It must not be interpreted as permission to skip phases, gates, inventories, asset checks, native chart/table rules, or the 1-3 page checkpoint.

## Simple prompt

```text
使用 $quality-editable-ppt，做一份《终端安全行业的 AI 智能运营》PPT，风格自动推荐，先给我大纲确认。
```

## Validation

```bash
python scripts/validate_skill_package.py .
```

## v5.5 hero fallback optimization

This version strengthens the hero illustration rule. Complex hero visuals must not start as native PPT shape drawings. The skill should first use image_gen / image2 transparent PNG regeneration, then retry if the asset drifts, then use source-faithful crop fallback when regeneration is not close enough.

## v5.6 background integration, card sampling, and style palette update

This version adds background integration strategy, seamless source-crop integration, card color sampling, page-level card tokens, and final color patch pass. It also updates the built-in style palettes, including `#1135EA`, `#01B285`, `#5D08D8`, `#123371`, `#B81615`, `#E3E6ED`, `#61696A`, `#E9EDF1`, `#342D2B`, `#C9A24D`, and `#E8E2D8`.


## v5.0.1 Minimal Lock

This version keeps the v5.0 stable workflow intact and adds only a minimal priority clarification: all modes share the locked-reference reconstruction rule, Mode 1/2/4 switch to Mode 3-style reconstruction after preview confirmation, flat components are rebuilt by geometry, and Phase 3 checks approved asset binding before building.


## v5.0.2 Light Lock

This version keeps the lightweight v5.0 workflow but adds a small file-lock guard: confirmed preview/source images must be persisted as project-local files with SHA-256, Phase 3 must list locked references and asset inputs, and Gate 6 must show locked source beside exported PPT render. It intentionally avoids the heavy hard-lock runtime helper and mandatory diff heatmaps.


## v5.0.3 Unified 3A

This version keeps the lightweight file-lock approach and makes Unified 3A Replica Flow the only post-lock reconstruction path for single-image, multi-image, and full-PPT work. The original mode only creates locked references. After lock, reconstruction scales by slide batches, with default cost controls and no automatic multi-round repair.


## v5.1 Scope-Aware Replica Update

This version keeps the built-in style system and now uses 7 fixed styles + 1 automatic recommendation router, Layer A/B/C strategy, native chart/table reconstruction, complex hero asset handling, background asset handling, card sampling, and lightweight file lock.

The main change is workflow routing: modes only create locked references. After a reference is locked, every task enters the same scope-aware Unified 3A replica core. The core first decides scope, source quality, and asset roles, then builds only the required scope. This prevents single-slide image reconstruction from using multi-page deck wording or unnecessary phases.


## v5.1.1 Style Update

This version updates the style system to **7 fixed built-in styles + 1 automatic recommendation router**.

Fixed styles:

1. 蓝绿产品发布风
2. 蓝黑科技运营风
3. 紫色科技色块风
4. 紫蓝AI科技风
5. 深蓝深红攻防风
6. 深灰绿色监控风
7. 深灰金色年会风

`灰白极简咨询风` is removed. `自动推荐` is retained after the 7 fixed styles and is not counted as a fixed style.


## v5.12 Scientific Flow Consolidation

This version keeps the stable v5.10 workflow and adds scientific execution discipline without increasing public workflow burden.

Key points:

- Default output remains: high-visual preview + 90%+ high-replica editable PPT.
- Mode 2A fixed-wording outlines/documents must read full content and go directly to Gate 2.
- Mode 2B long-form material must extract outline first, then follow Mode 1.
- Gate 2 must happen before any background-only or hero-only draft generation.
- High-visual preview generation must use image_gen / image2 / equivalent image generation.
- After preview/source confirmation, locked references become the only visual source of truth.
- Post-lock build must be replica reconstruction, not local-script redesign.
- Existing primary rules remain: full background asset rule, hero feathering/blending, icon PNG/SVG rule, sparkline rule, native chart/table rule, card box-model rule, screenshot-only rejection.


## v5.13 Hard Asset Fidelity Gates

This version keeps the v5.10/v5.12 workflow and adds hard visual-fidelity gates:

- except pure solid or extremely simple gradient backgrounds, backgrounds are clean full-slide assets;
- complex hero visuals are Layer A assets and must not be low-fidelity native-shape redraws;
- hero assets must be transparent/cropped cleanly, feathered, and blended into the background;
- preview-styled icons default to SVG / transparent PNG; native shapes are allowed only for ultra-simple flat icons that match;
- rough shape fragments, disconnected line icons, font icons, emoji, and different-library icon substitutions fail QA;
- after preview lock, major layout regions must preserve relative bbox, size, spacing, and visual density;
- Gate 6 is a hard pass/fail gate, not only a side-by-side display.


## v5.14 Mode 2 Normalized-to-Mode-1 Flow

This version keeps the v5.13 hard asset fidelity gates and simplifies Mode 2:

- uploaded outline / fixed wording: read current content, preserve text and hierarchy, confirm recognized content as Gate 1, then follow Mode 1 flow;
- long-form material / extraction request: extract PPT outline, confirm it as Gate 1, then follow Mode 1 flow;
- no automatic environment setup, virtual environment creation, package installation, stale `phase0/phase1` reuse, or old locked-reference reuse for Mode 2 intake;
- no background, hero, preview, or PPT render before Gate 1 and Gate 2 confirmation.


## v5.15 Asset-Capture Fidelity Additions

This version adds four hard rules on top of v5.14:

- complex gradient / glow / glass title bars are captured as whole PNG title-bar assets instead of being redrawn;
- complex 3D / glow / gradient / glass hero visuals may keep intrinsic text inside the hero asset when separation would blur or degrade fidelity;
- small icons default to faithful PNG/SVG asset use and must not be redrawn with font glyphs or rough primitive shapes;
- preview lock reads only the newly generated current-run preview files, not older previews from previous runs.


## v5.16 Light Main Constraints — Based on v5.15

This version keeps the v5.15 main workflow unchanged and adds lightweight primary constraints:

- real image-generation preflight before Gate 3, without broad tool scanning or automation tools;
- no local SVG/PNG/canvas/script fallback as high-visual preview;
- complex backgrounds preserved as full-slide background images;
- complex title bars captured as PNG with feathered edges;
- complex small icons captured as PNG/SVG with feathered edges;
- all captured complex assets require soft-edge integration;
- charts stay native/editable when overlapping icons are present;
- standard charts prioritize native PPT chart components;
- preview lock reads only current-run newly generated previews;
- shape-based downgrades must be disclosed and confirmed by the user.


## v5.17 Stable Lock

This version keeps the v5.15/v5.16-light gate rhythm but locks execution priority:

- locked preview fidelity first;
- no redesign after preview lock;
- Layer A/B/C reconstruction;
- complex backgrounds fused into full background images;
- complex visual modules assetized instead of shape-redrawn;
- title bars and glass cards keep crisp edges rather than unnecessary feathering;
- simple line/filled icons and small badges prefer native PPT/SVG continuous paths;
- complex icon badges use PNG/SVG when native matching is not faithful;
- standard charts stay native, especially when overlapping icons;
- shape-based downgrades require user confirmation instead of silent delivery.


## v5.18 Mode 3 Clean Layer Lock

This version keeps v5.17 Stable Lock's main flow unchanged and adds Mode 3 image-to-PPT anti-overlay discipline:

- full-slide screenshot is reference only, not final clean background;
- clean background must not contain text/cards/charts/tables/icons/hero;
- if clean background cannot be extracted, use image generation to recreate it;
- whole screenshot + overlay is a downgrade requiring user approval;
- every Mode 3 slide needs an internal Layer A/B/C plan before PPT generation;
- foreground objects are not considered reconstructed just because they appear in the screenshot;
- OCR icon placeholders are quarantined and rebuilt from source regions;
- charts and tables remain native whenever practical;
- first 1–3 page comparison must report background route, asset route, chart/table status, and downgrades.


## v5.19 Background and Icon Lock

This version keeps v5.18's main flow unchanged and tightens only the remaining background/icon issues:

- pure solid background may use native PPT fill;
- every non-solid background must be recreated with image generation as clean background;
- no background should be created by erasing text/icons/cards/charts from screenshots;
- simple line/filled icons use transparent PNG or SVG continuous paths;
- simple icon backgrounds use native PPT shapes;
- complex glowing/gradient/glass icon badges can be one combined transparent PNG;
- icon crops must be complete;
- chart/icon overlaps keep charts native and icons separate;
- downgrades require user confirmation.


## v5.20 Visual Asset QA Lock

This version keeps v5.19's main flow unchanged and adds stricter execution locks:

- non-solid backgrounds require real image generation raster backgrounds, not local SVG/canvas/script/PPT-shape substitutes;
- background generation must match the locked preview atmosphere;
- hero/main visual role overrides geometry simplicity and is assetized by default;
- complex icons on complex backgrounds are combined transparent PNG assets;
- simple icons remain SVG/transparent PNG and simple icon bases remain native shapes;
- complex slides must include compact visual asset preview in the existing first 1–3 page checkpoint;
- Mode 3 and complex slides must include explicit QA summary before batch generation continues.

## v5.21 Small Icon SVG Lock

This version keeps v5.20's main flow unchanged and improves only small icon reconstruction:

- small simple line/filled icons are SVG-first;
- transparent PNG is the fallback;
- screenshot crops are downgrade-only for small simple icons;
- SVG icons must be complete, sharp, padded, and non-fragmented;
- medium/large complete icon crops remain allowed;
- complex glowing/gradient/badge icons remain combined transparent PNG;
- QA explicitly reports small icon route and blocks clipped/blurry/incomplete small icons.


## v5.22 Micro Icon, Card, and Text Precision Lock

This version keeps the v5.21 workflow unchanged and only strengthens three detail-fidelity checks: small icons must match the locked preview visual family and stroke/silhouette details; cards/panels must preserve sampled box-model tokens and internal decorative details; editable text must keep locked-preview anchors, baselines, alignment, and icon-text spacing.
