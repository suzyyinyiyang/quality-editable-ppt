# Blueprint and Preview Templates


---

<!-- Source: templates/visual-blueprint-template.md -->


# Visual Blueprint Template

```json
{
  "slide": 1,
  "title": "",
  "style": "蓝黑科技运营风",
  "background": {
    "type": "solid|gradient|texture_image",
    "asset_needed": true,
    "must_not_contain_text": true
  },
  "color_blocks": [
    {"id": "block_01", "purpose": "header", "bbox": "x,y,w,h", "color": "#"}
  ],
  "text_regions": [],
  "cards": [],
  "charts": [],
  "icons": [],
  "hero_assets": [],
  "layer_plan": {"A": [], "B": [], "C": []},
  "complexity_budget": {
    "hero_count": 0,
    "complex_chart_count": 0,
    "card_count": 0,
    "icon_count": 0,
    "status": "pass|warn|fail"
  }
}
```


---

<!-- Source: templates/preview-prompt-template.md -->


# Preview Prompt Template

Use this after visual blueprint confirmation.

```text
Use image_gen / image2 to generate a 16:9 PPT slide preview from this blueprint.
The preview must be reconstructable: bold color blocks, flat icons, standard charts, clear modules, no tiny unreadable text, no text embedded in hero illustrations, background separated from content.
Follow the blueprint exactly. Do not create a poster-like page.
```
