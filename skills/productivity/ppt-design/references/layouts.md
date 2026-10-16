# Layout Library

All layouts are drawn on a 13.333 × 7.5 inch canvas; if the source is another 16:9 size, everything is scaled proportionally.

Every page has a common part (added automatically by build_deck.py).

- Background image: `bg_content` for content pages, `bg_cover` for the cover, `bg_closing` for the closing page
- Series header: `meta.series` centered with two leaves, only on content pages; turn off with `style.decor.header=false`
- Bottom: when there is a `takeaway` it is a semi-transparent pill with an icon, with the footer and page number on the right; otherwise the footer sits bottom-left and the page number bottom-right
- Title: top-left, max 36pt, with a short bar, a dot, and two short bar segments below (`style.decor.title_mark=false` turns it off)

The content area runs from y 2.15 to 6.05 inches, with 0.8 inch left and right margins.

## Layout Overview

| Layout | Use for | Fields used | Illustration slot |
|---|---|---|---|
| `cover_hero` | Cover | kicker, title, subtitle (with brush highlight), body, items (full-width agenda cards), takeaway | Large image on the right |
| `statement_number` | One core number plus one sentence | number (brush behind it), lines, body | Large image on the right |
| `rows_side` | Term explanations, three or four parallel concepts | side, items{title,text,emphasis} | Side image bottom-left |
| `stats_row` | Two to four data points | items{value,label}, takeaway | Small image top-right |
| `media_text` | Diagram plus explanation | diagram or image, point, body, callout | Small image top-right |
| `side_cards` | Steps, methods, one heavy and one light card | side, items{title?,text,emphasis} | Side image bottom-left |
| `quote_cards` | Example sentences, prompts, actual quotes | lead, items{text} | Small image top-right |
| `statement_hero` | A single claim plus explanation | headline (with brush), body, pill | Large image on the right |
| `cards_quote` | Risks, pitfalls, counterexamples plus a one-line summary | items{title,text}, quote_lines | Image upper right |
| `list_icons` | Fallback, any list, holds up even with long entries | items{title?,text} | Small image top-right |
| `grid_cards` | Three to six short points, two or three columns of large cards | items{title?,text,emphasis} | Small image top-right |
| `closing` | Closing page, dark by default | kicker, headline, body, cta | Centered image at the top |
| `steps_flow` | Two to five sequential steps, numbered horizontally | items{title,text} | Small image top-right |
| `compare_split` | Two-way comparison, the right side is the recommended one | left, right, vs_label | None |
| `cycle` | Recurring stages of a loop | center, items{title,text} | None |
| `pyramid` | Hierarchy, narrowest at the top | items{title,text} | None |
| `section` | Section divider; with no illustration, an oversized pale section number fills the right side | number, kicker, title, subtitle | Large image on the right |
| `toc` | Table of contents, large type on the left and stacked chapters on the right, three to six chapters | title, kicker, items{title,text} | None |
| `cover_type` | Large-type cover, the title is the whole visual, no illustration | kicker, title (may contain an **emphasis word**), subtitle, body, items | None |
| `question` | One large question filling the page, for transitions or building suspense | kicker, question, body | None |
| `cover_center` | Centered cover, paired with a landscape at the bottom (background decoration scene) | kicker, title, subtitle (yellow brush), body, takeaway | The landscape in the background |
| `rank_grid` | TOP ranking, up to 10 entries laid out in two rows, with an optional "key findings" below | items{num,title,text}, findings{title,items} | None |
| `explain` | Explanation page: label, body, centered formula bar, decision rules with colored dots, small note; one to four columns, with an optional diagram on the left; without a conclusion bar the content is vertically centered on the page | image, blocks or columns[{blocks}], boxed, takeaway | None |
| `shot_notes` | One large screenshot with numbered notes; a landscape screenshot takes 60% of the width, a portrait phone screenshot is narrowed by height; if an entry has `at`, a numbered dot is placed at the corresponding position on the screenshot | image, items{title?,text,at?:[x,y]}, caption, frame | None |
| `shot_stack` | Two to four screenshots in a row, widths allocated by each one's aspect ratio; treated as steps by default, numbered automatically with arrows in between; `flow: false` turns it into a side-by-side comparison | items{image,title?,text?,num?}, flow, frame | None |
| `big_quote` | One quotation filling the page, with an oversized quotation mark as decoration | quote, by, note | None |
| `toc_row` | Table of contents, chapters in a single horizontal row, three to five chapters | title, kicker, items{title,text} | None |
| `timeline` | Three to six milestones arranged by time | items{date,title,text,emphasis} | None |
| `funnel` | Layer-by-layer conversion or filtering, three to five layers | items{label,value,text} | None |
| `hub` | One center connected to three to six parts | center{title}, items{title,text} | None |
| `matrix` | Two dimensions cutting out four quadrants | x_axis, y_axis, quadrants | None |
| `table` | Native table, one column can be highlighted | columns, rows, highlight_col, note | None |
| `chart` | Native chart with one to three conclusions | chart, insights, source | None |
| `framework` | SWOT, PEST, Porter's Five Forces, Business Model Canvas | framework{kind,blocks,labels} | None |
| `free` | Special pages, placed by hand | elements in plan | Custom |

## Rules of Thumb for Choosing a Layout

- Don't use the same layout on two adjacent pages; for similar content (say two consecutive `side_cards` pages) you can differentiate with illustrations and icons
- For content-heavy pages, consider `list_icons` first — its row height compresses automatically; when the points are few and short, use `grid_cards` for a fuller page (plan_deck picks this automatically for list page types)
- With no side and no illustration, the cards in `rows_side` automatically fill the whole row; when a cover has little content, the text block is automatically centered vertically
- When the source is already structured as "guide on the left + cards on the right", use `rows_side` or `side_cards` — that's where the information relationships are least likely to go wrong
- For a page with a single sentence, use `statement_hero` or `statement_number` with a large illustration to hold the page up
- When `stats_row` has more than four numbers, switch to `list_icons` or split into free
- Use `chart` when you need to compare magnitudes, see trends, or show proportions; use `stats_row` when you're just listing a few striking numbers
- Tables and charts are native objects, so users can edit the data directly in PowerPoint; once the chart data changes, the conclusions in the insights on the right must be rewritten to match
- When every value in a funnel is a number, each layer's width is drawn in proportion to its value; if one isn't a number, switch to equal-step narrowing
- The newer layouts have no illustration slot — the structure carries the page, so save the illustration budget for cover and statement-type pages
- The number style on TOC and section pages is decided uniformly by the style's `decor.number_style`, so the two are always consistent; a TOC without items pulls them from the section pages automatically, and editing a section title updates the TOC to match
- For decks of eight pages or more with chapters, put a TOC page after the cover and return to the cover's visuals at the end — only then is the set complete
- After several pages of cards in a row, insert a `question` or `big_quote` page to loosen the rhythm; the "rhythm" item in the five-dimension self-review looks at this
- For styles that carry the page with type (cobalt type, ink magazine, hard-edge grid), the cover defaults to `cover_type`, decided by the preset's `prefer_layouts`

## How Styles Affect Layouts

The same layout automatically changes a few details under different styles; there's no need to edit deck.json.

| style.json field | Values | Effect |
|---|---|---|
| `shape.depth` | flat / ring / whisper / shadow | Cards get just a fill, a thin outline, a very faint glow, or a classic drop shadow |
| `decor.bullet` | icon / dash / number | Each list entry is preceded by an icon, an accent-colored dash, or a 01, 02 number; on pages like big numbers and buttons the icons are dropped entirely |
| `decor.emphasis` | color / serif | The **emphasis word** in the title changes color, or changes color and switches to a serif face at the same time |
| `decor.chrome` | standard / editorial | Either a centered series name at the top plus a bottom pill bar, or a magazine-style top info bar, hairline rules, and a page number at the bottom right |
| `decor.number_style` | plain / badge / ring / block / diamond | The look of the numbers on TOC and section pages |
| `type_scale` | A list of font sizes, or false | The whole deck uses only this ladder of sizes; during layout, sizes are tried directly from the ladder, roughly 1.2× per step by default |

build_deck snaps every computed font size down to the nearest step, so the same kind of text is the same size across pages, and the whole deck usually ends up with only six to ten font sizes.

## How Much Each Layout Holds

Every layout has a capacity, counted in "reading units", where one Chinese character or one English word counts as 1. When the capacity is exceeded, plan_deck automatically switches to the next layout of the same page type or to the `list_icons` fallback, lists it under "capacity warnings" in design_spec.md, and outline_check also reports "doesn't fit" ahead of time.

```bash
python3 $S/layout_info.py              # all layouts, their page types, and uses
python3 $S/layout_info.py funnel        # capacity and deck.json example for a single layout
python3 $S/layout_info.py --check $W    # check page by page whether deck.json exceeds capacity
```

If you're unsure when writing deck.json, look it up first — that's easier than splitting pages after rendering. The capacity numbers live in `scripts/capacity.py`; remember to update them in step when you adjust layout dimensions.

## Adjustable Keys Per Page in plan.json

```json
{"n": 3, "layout": "rows_side", "hero": "hero_03",
 "icons": ["smartphone", "cpu", "message-circle"],
 "takeaway_icon": "globe", "lead_icon": "message-circle",
 "info": {"header": false}}
```

`icons` map to items in order; on pages with no items, the first icon is used for the callout, pill, or cta.
`info.header=false` turns off the series header for a single page.

## Element Format for the free Layout

```json
{"n": 7, "layout": "free", "master": "content", "elements": [
  {"t": "text", "x": 0.8, "y": 0.95, "w": 8, "h": 0.8, "text": "Title", "size": 36, "color": "text",
   "bold": true, "font": "heading", "align": "l", "valign": "m", "ls": 1.2, "spc": 0},
  {"t": "rect", "x": 0.8, "y": 2.2, "w": 5, "h": 1.2, "fill": "surface", "alpha": 0.88,
   "radius": 0.18, "line": "line", "shadow": true},
  {"t": "ellipse", "x": 1, "y": 2.4, "w": 0.6, "h": 0.6, "fill": "tint"},
  {"t": "icon", "x": 1, "y": 2.4, "size": 0.6, "name": "lightbulb", "color": "primary", "bg": "tint", "circle": true},
  {"t": "image", "x": 7.5, "y": 1, "w": 5, "h": 5, "path": "/abs/path/assets/hero_07.png", "fit": "contain"}
]}
```

Colors can be written as palette role names (primary, primary_dark, accent, tint, surface, text, muted, line, on_primary, bg_top, bg_bottom,
plus the automatically derived strong heading color and highlight colored-text color);
`primary@0.3` means a light color mixed from the primary color and white at 30%, and you can also write a hex value directly.
`font` takes one of heading, body, display. For the free layout you have to compute text sizes yourself with `common.fit_size`, or leave enough headroom — QA checks for overflow.
