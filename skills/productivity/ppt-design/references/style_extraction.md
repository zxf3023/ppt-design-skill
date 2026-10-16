# Reading style.json out of a reference image

The reference image is there to supply "vibe"; none of its content is used. Run `extract_style.py` first to get the colour clusters, then fill in the rest by looking at the image yourself.

## Questions to answer while looking at the image

1. What is the primary colour? Usually the hue with medium area and the highest saturation. It has to work as a heading colour and as a solid card background, so its contrast against white must be at least 3.4; if it falls short, darken it (the script already handles this).
2. The dark version of the primary colour, `primary_dark`, is used for large headings and dark closing pages; its contrast against white must be at least 7.
3. The accent colour `accent` is the most eye-catching spot colour in the reference image (in the example, the yellow brush label). It is used for brush highlights, illustration accents and the background of warning icons.
4. The background gradient `bg_top` / `bg_bottom` comes from the large areas of light colour at the top and bottom of the reference image. The background must be light enough that body text `text` placed on it has a contrast of 7 or more.
5. Body colour `text` is a dark shade in the primary hue, close to black, which looks more harmonious than pure black. `muted` is for explanatory text and needs a contrast of at least 4.5 against the background.
6. `tint` is a very light version of the primary colour, used for icon backdrops and emphasis cards; `line` is slightly darker than tint and is used for card strokes.
7. Shape language: if the reference image is rounded, set `shape.radius` to 0.18 to 0.24; for a harder-edged business look use 0.06 to 0.1. Whether cards cast a shadow depends on whether the reference image has soft shadows.
8. Pick background decoration `background.decor` from the motifs you see in the reference image; the cover `cover_decor` can be richer than the content pages.

   | What you see in the reference image | Choose | Related parameters |
   |---|---|---|
   | Soft large colour blobs, light dots, pale arcs | `blobs` `bokeh` `arcs` | |
   | Clouds, rolling hills along the bottom | `clouds` `hills` | |
   | Dot grids, grainy texture | `grid` `grain` | |
   | Large soft mist gradients in two colours | `mist` | uses the two colours primary and accent |
   | Concentric ripple lines, thin coils like sound waves | `rings` | `line_color`, defaults to accent |
   | Flowing silk threads, golden light bands | `silk` | `line_color`, defaults to accent |
   | Dark bands with torn-paper or brush edges | `torn` | `band_color`, defaults to primary_dark |
   | Red, yellow, blue and green circles, half-circles, triangles, squares | `geo` | `geo_colors` colour list |
   | A solid colour bar spanning the page | `band` | `band_color`, defaults to primary |
   | A full flat landscape strip along the bottom (windmills, houses, hills, trees, solar panels) | `scene` | drawn only on the cover and closing pages; `scene_teal`, `scene_dark`, `scene_sky` adjust the colours; pair the cover with the `cover_center` layout |

   Pick only one or two motifs. If the reference image relies on photography to carry the visuals, you can only reproduce the colour scheme and layout here; say so clearly when delivering.
9. Other decoration `decor`: `leaf` header leaf (turn on only for nature, eco or fresh styles), `brush` brush highlight (hand-drawn, playful styles), `title_mark` small bar under the title, `sparkles` starlight in illustrations, `closing_dark` dark primary background on the closing page.
   The look of section numbers is set by `number_style`, shared by the table of contents and section pages; options are `plain` (large numeral), `badge` (solid circle), `ring` (hollow circle), `block` (solid square), `diamond` (outlined diamond).
   When a section page has no illustration, an oversized pale section number is laid across the right side; `number_watermark: false` turns it off, and `watermark_color` adjusts its colour, e.g. `primary@0.1`.
   The screenshot frame is set by `shot_frame`: `window` (a narrow title bar with three dots, the default), `card` (card only), `none` (no frame). A single page can override it with `frame` in deck.json.
10. Fonts: if the reference image uses a Song-style serif for Chinese headings and a serif for Latin text (common in high-end, artistic and Chinese-style decks), set `heading_ea` to `Source Han Serif SC`, `heading_latin` and `display_latin` to `Georgia`, and keep a sans-serif for body text. If the recipient's machine does not have Source Han Serif installed it will be substituted, so mention this when delivering.
11. Write the illustration style `illustration.style_prompt` in English, describing technique, material, lighting, colour tone and mood. For example "clean flat vector illustration with soft gradients, mint green and teal tones, rounded friendly shapes, light airy mood, subtle soft shadows".

## Full style.json fields

```json
{
  "name": "mint-eco-flat",
  "reference": "ref.png",
  "palette": {
    "primary": "17806D", "primary_dark": "0F5A4D", "accent": "F5D76E",
    "bg_top": "C3EDDB", "bg_bottom": "F4FBF8", "surface": "FFFFFF",
    "tint": "DDF3EA", "text": "1E3A33", "muted": "50655E", "on_primary": "FFFFFF", "line": "CDE8DD"
  },
  "fonts": {"heading_ea": "Microsoft YaHei", "body_ea": "Microsoft YaHei",
            "heading_latin": "Arial", "body_latin": "Arial", "display_latin": "Arial Black"},
  "shape": {"radius": 0.18, "shadow": true, "card_alpha": 0.88},
  "decor": {"header": true, "leaf": true, "brush": true, "brush_color": "accent",
            "title_mark": true, "sparkles": true, "closing_dark": true},
  "background": {"decor": ["blobs", "bokeh", "arcs"],
                 "cover_decor": ["blobs", "clouds", "hills", "bokeh"],
                 "closing_decor": ["blobs", "bokeh", "arcs"]},
  "illustration": {"style_prompt": "…", "negative": "text, letters, words, watermark, logo, …"},
  "emphasis_color": "primary"
}
```

`emphasis_color` is the colour of `**bold**` runs in body text.

Two more roles are derived automatically by the script and usually do not need to be written. `strong` is the large-heading colour: on a light background it equals primary_dark, on a dark background it is a brightened primary;
`highlight` is the coloured text colour (big numbers, sidebar headings): on a light background it equals primary, on a dark background it is a brightened primary. You can also set them explicitly in palette to override when needed.
`card_alpha` is the opacity of white cards; the busier the background, the higher it should be.

## When the reference image is dark

Dark reference images (tech style, night scenes) can still be used, but there are two things to watch.

- `bg_top` / `bg_bottom` use dark colours, `text` becomes near-white, `muted` uses light grey, `surface` uses a dark colour slightly lighter than the background, `card_alpha` around 0.7
- `on_primary` is black or white depending on how dark the primary colour is; the contrast between primary and on_primary must reach 4.5, otherwise QA will flag small text inside solid cards
- Change `decor.brush_color` to `primary` — a light brush turns grey on a dark base; `leaf` is usually turned off
- `closing_dark` can be turned off, and the closing page keeps the dark background
- Programmatic illustration tiles are light, which actually stands out on a dark background, so they can stay

## Preset styles

When the user provides no reference image, pick from the fourteen presets in `references/styles/`.

- The original six lean towards soft illustration styles: Mint Fresh, Business Blue, Warm Orange Energy, Dark Tech, Misty Purple Soft, Paper Notes
- Six rely on decorative motifs and typography: Black Gold Report, Geometric Colour Blocks, Cobalt Type, Black Grey Neon Green, Blue Pink Soft Mist, Blue Line Launch
- Two are magazine editorial styles with almost no decoration: Ink Magazine (Song-style serif, paper tones, fine rules), Hard Edge Grid (right angles, black and white plus one signal orange)

`index.json` tags each preset along four dimensions — texture, mood, typographic feel and density — and notes the scenarios it suits and does not suit, plus an `imagery` tag saying what carries the visuals in that style. With no image-generation model configured, `--auto` will not recommend `photo`-type styles and will push `illustration`-type ones further down the list.
`style_previews.py --auto` picks three presets — safe, bold and unexpected — based on the material keywords and renders samples using the user's own content; `--apply <id>` writes the chosen preset out as style.json.
The `rules` in a preset are hard rules for that style and must be respected even when adjusting the layout by hand; when `illustration.fallback_look` is flat, programmatic illustrations switch to an outlined sticker style.
There are two more optional keys. `prefer_layouts` makes a given page type prefer a given layout, for example `{"toc": "toc_row"}`; `illustration.skip_layouts` lists the layouts that get no illustration — styles carried by typography often include the cover, section pages and closing page.

### Typography rule fields

These fields decide *how* colours and type are used; read them off the reference image, or set them according to the style's character.

| Field | Description |
|---|---|
| `palette.secondary` / `palette.subtle` | The second and fourth levels of text grey; derived automatically if omitted. The four levels in order are body text, secondary, muted captions, and subtle metadata (page numbers, sources, footers) |
| `shape.depth` | Card depth: flat is fill only, ring is a single thin border, whisper is a very faint halo, shadow is a classic drop shadow. If the reference image's cards have no shadow, do not use shadow |
| `decor.bullet` | Bullet style: icon, dash, number |
| `decor.emphasis` | Heading emphasis: color changes the colour, serif changes the colour and switches to a Song-style serif |
| `title_emphasis_color` | Colour of the emphasised word in headings, defaults to highlight |
| `decor.chrome` | standard or editorial (magazine-style header and footer) |
| `type_scale` | Custom type scale; false disables snapping |
| `accent_max` | Accent colour ceiling, default `{"uses": 3, "area": 0.08}`; QA warns if exceeded |
| `forbid` | Red lines for this style, checked by QA: `pure_white` no pure white backgrounds, `pure_black` no pure black, `shadow` no shadows, `radius_over` corner-radius ceiling |

Rules of thumb from reading reference images: papery, magazine-like references are usually ring plus dash plus editorial; tech launch and dark styles are mostly ring plus number; soft illustration styles keep shadow or whisper plus icon.

## Common mistakes

- Treating the largest light-coloured area in the reference image as the primary colour, which leaves headings looking washed out. Judge the primary by saturation, not by area.
- Using the accent colour too much. accent should appear only on brushes, a few icon backdrops and illustration accents.
- Treating the LOGO, specific illustrations or specific text in the reference image as elements to be reproduced. Extract the style only.
