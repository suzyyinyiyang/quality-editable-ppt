# Registry Templates

All inventory and registry templates are consolidated here.


---

<!-- Source: templates/element-inventory-template.md -->


# Element Inventory Template

```json
{
  "slide": 1,
  "elements": [
    {
      "id": "title_01",
      "category": "text|card|chart|icon|background|hero|line|arrow|table|decor",
      "layer": "A|B|C",
      "bbox": "x,y,w,h",
      "implementation": "text_box|shape|native_chart|shape_chart|png_asset|svg_icon",
      "editable": true,
      "notes": ""
    }
  ]
}
```


---

<!-- Source: templates/chart-inventory-template.md -->


# Chart Inventory Template

```json
{
  "charts": [
    {
      "chart_id": "slide02_chart01",
      "slide": 2,
      "chart_type": "donut|pie|column|bar|line|area|progress|matrix|radar|kpi|decorative",
      "bbox": "x,y,w,h",
      "title": "",
      "categories": [],
      "series": [
        {
          "name": "",
          "values": [],
          "colors": []
        }
      ],
      "axis": {
        "x_label": "",
        "y_label": "",
        "min": null,
        "max": null,
        "unit": ""
      },
      "legend": [],
      "data_source": "visual_blueprint|visible_label|geometry_estimate|user_provided|unknown",
      "confidence": "high|medium|estimated|low",
      "editable_data_required": true,
      "implementation": "native_ppt_chart|native_chart_with_overlays|shape_chart_with_data_file|png_asset_plus_editable_labels",
      "fallback_reason": "",
      "must_not_omit": true
    }
  ]
}
```

Rule: standard charts with reliable data should use `native_ppt_chart` or `native_chart_with_overlays` whenever the available presentation tool supports it.


---

<!-- Source: templates/table-inventory-template.md -->


# Table Inventory Template

```json
{
  "tables": [
    {
      "table_id": "slide02_table01",
      "slide": 2,
      "bbox": "x,y,w,h",
      "table_type": "data_table|comparison_table|risk_list|asset_list|capability_matrix|decorative",
      "headers": [],
      "rows": [
        []
      ],
      "row_count": 0,
      "column_count": 0,
      "column_widths": [],
      "row_heights": [],
      "header_style": {
        "fill": "#",
        "font_color": "#",
        "bold": true
      },
      "body_style": {
        "fill": "#",
        "font_color": "#",
        "zebra_striping": false
      },
      "border_style": {
        "color": "#",
        "width": 1,
        "opacity": 1.0
      },
      "cell_badges_or_icons": [],
      "data_source": "visual_blueprint|visible_text|user_provided|unknown",
      "confidence": "high|medium|estimated|low",
      "implementation": "native_ppt_table|native_table_with_overlays|shape_table_with_data_file|png_asset_plus_editable_labels",
      "fallback_reason": "",
      "must_not_omit": true
    }
  ]
}
```

Rule: real tabular data should use `native_ppt_table` or `native_table_with_overlays` whenever the available presentation tool supports native tables.


---

<!-- Source: templates/icon-inventory-template.md -->


# Icon Inventory Template

```json
{
  "icons": [
    {
      "icon_id": "icon_01",
      "slide": 1,
      "bbox": "x,y,w,h",
      "style": "flat-line|flat-filled|complex-glow",
      "implementation": "svg_icon|native_shape|transparent_png|image_gen_png",
      "asset": "",
      "must_not_omit": true
    }
  ]
}
```


---

<!-- Source: templates/hero-illustration-inventory-template.md -->


# Hero Illustration Inventory Template

```json
{
  "hero_illustrations": [
    {
      "hero_id": "slide01_hero_ai_hub",
      "slide": 1,
      "bbox": "x,y,w,h",
      "visual_description": "glowing AI hub with endpoint nodes",
      "preferred_asset_method": "image_gen_transparent_png",
      "fallback_method": "clean_crop_if_needed",
      "must_be_transparent": true,
      "forbidden_content": ["editable text", "labels", "numbers", "cards", "chart axes", "page number", "module border"],
      "style_constraints": ["match locked preview composition", "match colors", "no text", "no background panel"],
      "asset_output": "assets/slide01/slide01_hero_ai_hub.png"
    }
  ]
}
```


---

<!-- Source: templates/card-style-registry-template.md -->


# Card Style Registry Template

```json
{
  "cards": [
    {
      "card_id": "slide01_card_01",
      "slide": 1,
      "bbox": "x,y,w,h",
      "fill": "#",
      "gradient": null,
      "border_color": "#",
      "border_opacity": 1.0,
      "radius": 8,
      "shadow": {"enabled": true, "color": "#000000", "opacity": 0.25, "blur": 8, "offset_x": 0, "offset_y": 4},
      "glow": {"enabled": false},
      "inner_highlight": null,
      "divider_lines": [],
      "state_color": null
    }
  ]
}
```


---

<!-- Source: templates/icon-badge-registry-template.md -->


# Icon Badge Registry Template

```json
{
  "icon_badges": [
    {
      "badge_id": "slide01_icon_badge_01",
      "slide": 1,
      "bbox": "x,y,w,h",
      "background_shape": "circle|rounded_rect|hex|none",
      "background_fill": "#",
      "gradient": null,
      "border": "#",
      "glow": null,
      "glyph": "shield|monitor|ai|custom",
      "glyph_method": "svg|native_shape|image_gen_png",
      "state_dot": null,
      "asset_output": ""
    }
  ]
}
```


---

<!-- Source: templates/header-decoration-registry-template.md -->


# Header Decoration Registry Template

```json
{
  "header_decorations": [
    {
      "decoration_id": "slide03_header_beam_01",
      "slide": 3,
      "type": "beam_line|separator|corner_bracket|short_line|glow_png",
      "bbox": "x,y,w,h",
      "color": "#00AEEF",
      "opacity": 0.8,
      "implementation": "native_line|gradient_shape|png_glow",
      "shadow_or_glow": true
    }
  ]
}
```

---

# Hero Escalation Registry Extension

```json
{
  "hero_id": "slide01_hero_ai_core",
  "complexity": "complex",
  "native_shape_allowed": false,
  "preferred_method": "image_gen_or_image2_transparent_png",
  "retry_if": ["composition drift", "wrong node count", "wrong device placement", "weak glow", "style drift"],
  "fallback_method": "source_faithful_crop",
  "crop_cleanup_required": true,
  "user_confirmation_required_if": ["both methods fail", "crop contains unavoidable background contamination"],
  "phase3_must_use_asset": true
}
```

---

# Background Integration and Card Token Registry Extension

```json
{
  "asset_integration": [
    {
      "asset_id": "slide01_soc_floor_ring",
      "type": "background_integrated_visual|independent_hero|structural_content",
      "method": "full_slide_background|local_background_patch|transparent_png|ppt_native",
      "seamless_integration_required": true,
      "fail_if": ["visible rectangle", "background color mismatch", "hard glow cutoff", "text pollution", "card pollution"]
    }
  ],
  "page_color_tokens": {
    "page-bg": "#...",
    "panel-bg": "#...",
    "card-bg": "#...",
    "card-border": "#...",
    "card-glow": "#...",
    "text-main": "#...",
    "text-sub": "#...",
    "accent-primary": "#...",
    "accent-secondary": "#..."
  }
}
```
