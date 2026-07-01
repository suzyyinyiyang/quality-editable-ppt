# Quality Gates

## Gate 1 — Quick Outline

For topic/brief tasks, confirm outline only before any visual or strategy work.

Output only:

- slide count / active scope;
- slide number;
- title;
- core message;
- 3–5 main content points.

For image reconstruction, skip the outline gate and use image reconstruction strategy.

## Gate 2 — Page Information Structure and Visual Strategy

Run only after Gate 1 outline confirmation.

Confirm module structure, content hierarchy, KPI/chart/table plan, main visual direction, background texture / atmosphere direction, icon/component plan, style/color strategy, expected editable objects, and expected image assets.

## Gate 3 — Preview Image / Locked Reference

Persist preview/source images, record file metadata and SHA-256, show exact persisted files, confirm them, and lock them.

After Gate 3, reconstruct from locked reference pixels. Do not rebuild from topic, outline, semantic meaning, or generic template logic.

## Gate 4 — Element / Chart / Table / Detail Fidelity Confirmation

Confirm or internally verify:

- background purity and texture route;
- hero illustration method;
- chart data binding and native chart feasibility;
- native table data binding;
- icon badge registry;
- card styles and box model;
- header decoration;
- asset text-contamination risk;
- editable fidelity floor.


Gate 4 must also verify primary asset/component rules:

- textured backgrounds use clean full-slide background assets;
- pure backgrounds use native fill;
- hero assets are cleaned, feathered/blended, and text-free;
- no Unicode/emoji/icon-font substitutes for visual icons;
- table line color, line opacity, header fill, row/column sizing, and chips are restored;
- KPI sparklines and mini trend charts are native hidden-axis line charts or one continuous smooth vector path/SVG/transparent asset; no disconnected line-segment stitching;
- card/component box model is represented.

## Gate 5 — Optional Asset Confirmation

Gate 5 is not a default mandatory stop.

Confirm assets only when asset choices materially affect quality or need user review:

- complex hero regeneration;
- blurry-source clean rebuild;
- brand/product image confirmation;
- multiple asset options;
- background texture uncertainty;
- source-crop fallback;
- possible text/data contamination.

For ordinary pages with straightforward assets, skip Gate 5 and proceed directly to build with a short asset summary.

## Gate 6 — Render Confirmation

Build the active scope, export the PPTX, render exported slides, and show source/render/diff evidence.

For single-slide work, build and render Slide 01 only.

Continue only after source-vs-render comparison, structural QA, and user confirmation.

## Final QA

Final delivery fails if:

- screenshot-only output is used for a page with editable content;
- background texture is missing or flattened;
- hero visual is missing, simplified, hard-edged, or text-contaminated;
- visible icons are omitted;
- card border/shadow/radius/size/padding are not represented;
- small-icon silhouette/stroke/badge style is semantically similar but visually different;
- card/panel fill, glow, internal bands, decorative details, or group spacing visibly drift;
- editable text anchors, baselines, alignment, or line spacing visibly drift;
- visible charts/tables are missing;
- standard charts/readable tables are not native when feasible;
- main layout composition is semantically re-built instead of reconstructed.


## v5.0 强化版复原检查

Gate 4 / Gate 6 / Final QA 必须检查：

- 背景纹理是否作为干净背景资产保留；
- 主视觉是否用透明 PNG/SVG、source-faithful 裁切或背景融合资产复原；
- 资产边缘是否羽化 / 柔边 / alpha 处理；
- 资产内是否残留标题、标签、伪文字、数字、卡片边框、图表轴线；
- 小 icon 是否全部还原；
- 卡片边框、投影、圆角、尺寸、内边距是否接近参考图；
- 图表 / 表格是否存在且可编辑性达标；
- 是否存在整页截图式伪高还原。
