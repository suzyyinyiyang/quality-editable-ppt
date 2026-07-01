# Manifest — Merged Package

## Skill

- Name: `quality-editable-ppt`
- Distribution: merged v5.22-detail-fidelity-lock
- Purpose: reconstructable high-visual editable PPT generation and image-to-PPT reconstruction.

## Preserved requirements

1. Do not generate previews before outline and visual blueprint confirmation.
2. Do not generate PPTX before preview/source images are locked, Phase 1 inventory is complete, and Phase 2 assets are confirmed.
3. Build only slides 1-3 first, render them, and wait for user confirmation.
4. Standard charts should use native PPT charts with editable data when possible.
5. Real data tables should use native PPT table components when possible.
6. Complex hero illustrations should default to image_gen / image2 regenerated transparent PNG assets.
7. Background assets must be clean and must not contain card wireframes, table borders, labels, text, or other editable structures.
8. Card styles, icon badges, header decorations, shadows, glows, and detail density must be checked.
9. Final PPTX render must be compared with locked references before delivery.

## File consolidation

- workflows: merged into 3 files.
- templates: merged into 4 files.
- quality-control: merged into 2 files.
- style-profiles: merged into 1 file.
- examples: merged into 1 file.
- scripts: consolidated into 4 scripts.

## Optimization added in v5.5

- Hero Illustration Fallback / Escalation Rule.
- Native-shape drawing is prohibited as the first method for complex hero illustrations.
- Source-faithful crop fallback is required when image_gen/image2 regeneration drifts.
- Bad native hero illustrations detected in the 1-3 page render must return to Phase 2 for replacement.

## Optimization added in v5.6

- Background Integration Strategy.
- Source Crop Integration Rule.
- Asset Seamless Integration Check.
- Card Color Sampling Rule.
- Card Token System.
- Final Color Patch Pass.
- Updated built-in style palette tokens.


## Change Note

- v5.0.1-minimal-lock: retained all v5.0 constraints and added minimal universal locked-reference, flat geometry reconstruction, and Phase 3 binding-check clarifications without adding new stages or public gates.


## Change Note

- v5.0.2-light-lock: adds lightweight local-file + SHA-256 reference locking, small validator script, build-input summary, and source-vs-render Gate 6 comparison without heavy runtime evidence or mandatory heatmaps.


## Change Note

- v5.0.3-unified-3a: after locked references exist, all modes and all scopes use Unified 3A Replica Flow. Single-image, multi-image, and full-PPT tasks scale by batching rather than switching workflows. Default repair/build caps were clarified to control Codex load.

## Change Note

- v5.1-scope-aware-replica: keeps all existing capabilities, but changes post-lock execution into Reference Routing → Scope Detection → Source Quality Decision → Asset Role Plan → one-pass/batched Unified 3A Replica Build. It avoids extra heavy runtime checks and prevents single-slide jobs from using multi-page workflow language.

## Change Note

- v5.1.1-style-system: updated built-in style order to 7 fixed styles + 1 automatic recommendation router; removed `灰白极简咨询风`; renamed `蓝白科技色块风` to `紫色科技色块风`; updated style colors for purple block, attack-defense, and monitoring styles.


## Change Note

- v5.12-scientific-final: preserves the v5.10 main workflow, fixes gate-order drift, clarifies Mode 2A/2B routing, requires image-gen preview generation, forbids pre-Gate-2 background-only drafts, and enforces locked-preview-only replica reconstruction after Gate 3 lock.


## Change Note

- v5.13-hard-asset-fidelity: preserves the v5.10/v5.12 main workflow and upgrades asset fidelity guidance into hard failure gates. It strengthens full-slide background assets, hero asset binding and feathering, SVG/PNG icon fidelity, bbox-level preview replication, native-if-faithful implementation, and Gate 6 pass/fail enforcement.


## Change Note

- v5.22-detail-fidelity-lock: preserves v5.21 gate flow and constraints while adding focused checks for small-icon likeness, card/panel reconstruction fidelity, and editable text position accuracy.
