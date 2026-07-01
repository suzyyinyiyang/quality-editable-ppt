# Asset and Prompt Templates


---

<!-- Source: templates/asset-plan-template.md -->


# Asset Plan Template

```json
{
  "slide": 1,
  "assets": [
    {
      "id": "slide01_background",
      "type": "full_slide_background",
      "layer": "A",
      "output": "assets/slide01/slide01_background.png",
      "allowed_content": "texture, glow, gradient, atmosphere",
      "forbidden_content": "title, body text, cards, chart labels, numbers",
      "needs_user_check": true
    }
  ]
}
```

## Detail-fidelity asset extension

For complex hero illustrations, prefer this asset record:

```json
{
  "id": "slide01_hero_ai_hub",
  "type": "hero_illustration",
  "layer": "A",
  "method": "image_gen_transparent_png",
  "fallback": "clean_crop_only_if_generation_fails",
  "output": "assets/slide01/slide01_hero_ai_hub.png",
  "transparent_background": true,
  "forbidden_content": "editable text, labels, numbers, cards, chart axes, page numbers, module borders"
}
```


---

<!-- Source: templates/asset-contact-sheet-template.md -->


# Asset Contact Sheet Template

The asset contact sheet must include:

- slide number;
- asset id;
- asset preview;
- intended placement;
- whether the asset contains any text;
- action needed if contaminated.


---

<!-- Source: templates/hero-generation-prompt-template.md -->


# Hero Generation Prompt Template

Use with image_gen / image2 for complex hero assets.

```text
Generate a clean transparent-background PNG asset for this PPT hero illustration.
Match the locked preview's composition, style, colors, lighting, and visual role as closely as possible.
The asset must contain only the hero illustration itself.
Do not include any text, labels, numbers, cards, tables, chart axes, page numbers, background panels, or slide decorations.
Use transparent background. Keep edges clean. Make it suitable for placement on top of a PPT background.
```

---

# Hero Fallback Asset Prompt and Crop Policy

## Strict regeneration prompt

```text
Generate a transparent-background PNG that matches the locked reference hero illustration as closely as possible. Preserve composition, node count, device positions, ring layout, glow intensity, color palette, and visual role. Do not include text, labels, cards, chart axes, page numbers, or slide background. Use clean transparent edges.
```

## Source-faithful crop fallback

Use source crop only when regeneration causes style drift, structural mismatch, wrong device placement, or weak glow. The crop should be cleaned or masked when possible. If the crop contains unavoidable background glow that is essential to fidelity, mark it as `source_faithful_crop_approved` in the asset plan.

---

# Source Crop Integration Prompt

When source-faithful crop fallback is used, do not paste a raw rectangle. Prepare one of the following asset forms:

1. transparent cutout;
2. feathered-edge crop;
3. background-matched crop;
4. local background patch when the visual is inseparable from the background.

The final asset should not show a rectangular edge or color mismatch when placed on the PPT background.
