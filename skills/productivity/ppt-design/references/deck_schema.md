# deck.json Field Reference

deck.json describes "what this PPT is saying" and is independent of style. The layout functions only read the fields documented here.

## Top level

```json
{
  "meta": {
    "title": "Muse",
    "series": "Beginner intro · 3 minutes",
    "footer": "Muse beginner intro",
    "total": 11,
    "topic": "Muse, an AI agent app that does tasks for you",
    "anchor": {
      "description": "a glossy mint-teal rounded-square app icon with a bold white letter M, gently held by a sleek white robotic hand",
      "glyph": "M"
    }
  },
  "slides": [ ... ]
}
```

| Field | Description |
|---|---|
| `series` | A series header centred at the top of content pages, with leaf decorations on either side. The small label on the source cover often belongs here. Leave it empty if not needed |
| `footer` | The footer text from the source. When there is a takeaway pill, it sits to the right of the pill; otherwise it goes in the bottom-left corner |
| `topic` | A one-sentence topic in English, referenced by the illustration prompts |
| `anchor` | The visual anchor, see `image_prompts.md`. `glyph` is the letter on the tile in procedural illustrations |
| `scenario` / `audience` / `density` | Used in generation mode: scenario (oral, talk, reading, report), audience, density (low / high) |
| `storyline` | Used in generation mode, a one-sentence storyline |
| `notes` | Used in generation mode; true means every page needs speaker notes |
| `auto_page` | When true, content pages automatically get an "03 / 11" style page number, so you don't have to write `page` on every page |
| `projection` | When true, layouts are set for projection: automatic font sizes are never below 14pt, body text starts at 18pt, and the capacity ceiling is counted at 65%; pages that don't fit are reported by QA and split |
| `date` / `issue` | The date or issue number in the top-right of the magazine-style header; also used at the top of the large-type cover |
| `auto_number` | Defaults to true: section pages without a `number` are numbered 01, 02… in order; false turns this off |

## Fields common to every page

| Field | Description |
|---|---|
| `n` | Page index, starting at 1, matching the source |
| `type` | Page type, which determines the default layout; see the table below |
| `layout` | Optional; specifies the layout directly, with lower priority than plan.json |
| `title` | The page title |
| `takeaway` | The one-sentence conclusion for this page, placed in the pill at the bottom (in the source, the emphasis bar or callout box at the bottom of a page is usually this) |
| `page` | The page number text, copied from the source, e.g. `"02 / 11"`; the cover and closing usually don't have one |
| `notes` | Speaker notes. When beautifying, copy them from `deck.draft.json`; when generating, write the spoken wording |
| `purpose` | Used in generation mode: what this page is responsible for in the story; it does not appear on the page |
| `source` | The data source, shown as small text at the bottom of the page, "Source: …" |
| `show_footer` | Content pages show the footer by default; set to false to hide it |

Within text, `**fragment**` marks a local bold run, which is rendered bold in the accent colour. `\n` marks a paragraph break.

## Small fields available on every page

| Field | Description |
|---|---|
| `kicker` | A small label above the title, such as "01 · DEVDAY Overview". Put the source's per-page section tape or small label here; it shows on covers, content pages, section pages and closing pages |
| `stamps` | Small images from the source to keep as they are, such as a logo or an "AI generated" badge: [{image, x, y, w, h}] (inches, 13.333×7.5 canvas) |
| `items[].num` | A number that belongs to the item, such as "01". If it is set, the item shows the number instead of an icon, and no style will drop it |
| `source` | The data source. Text that already starts with a source label (Chinese 来源 / 数据来源, or "Source") won't get another prefix |

## Optional fields on a few page types

- `stats`: each item can add `note` (a one-line footnote under the number); the page as a whole can add `body` (a paragraph of explanation under the cards) or `detail` {title, body} (an explanation box with a small heading)
- `definitions` (rows_side layout): `side` can add `number`, turning the sidebar into "label + big number + explanation"; the page can add `list_title` above the list on the right
- `compare`: items can be written as {num, text} to keep the numbering; set `"bullet": "dash"` on a column to use a dash instead of an icon; set `vs_label` to an empty string to remove the VS in the middle, which suits a two-column summary page
- `footnote`: a one-line note at the bottom of the page, shown as is, without a "Source" prefix

## Page types and their specific fields

| type | Default layout | Specific fields |
|---|---|---|
| `cover` | cover_hero or cover_type | `kicker` a small label, `subtitle`, `body` a one-sentence description, `items` the agenda or key points (each with `text`) |
| `big_number` | statement_number | `number` the big number, `lines` two or three lines of large text, `body` a supplementary explanation |
| `definitions` | rows_side | `side` {title, body} the lead-in on the left, `items` each {title, text, emphasis} |
| `stats` | stats_row | `items` each {value, label}, `takeaway` |
| `diagram_text` | media_text | `diagram` {title, icon, boxes:[{text, emphasis}], caption}, `point` the key point on the right, `body`, `callout` a callout box |
| `steps` | side_cards | `side`, `items` each {title?, text, emphasis} |
| `quotes` | quote_cards | `lead` a lead-in sentence, `items` each {text} |
| `statement` | statement_hero | `headline`, `body`, `pill` a small pill |
| `warnings` | cards_quote | `items` each {title, text}, `quote_lines` two lines of pull quote on the right |
| `side_cards` | side_cards | Same as steps |
| `list` | list_icons or grid_cards | `items` each {title?, text} |
| `grid` | grid_cards | `items` each {title?, text, emphasis} |
| `process` | steps_flow | `items` 2 to 5 steps, each {title, text}, automatically numbered 01, 02 |
| `compare` | compare_split | `left` / `right` each {title, items:[text…], icon?}, with the right side being the recommended one; `vs_label` changes the text in the middle |
| `cycle` | cycle | `center` the short word in the middle of the ring, `items` 3 to 6 {title, text} |
| `layers` | pyramid | `items` 3 to 5 layers from top to bottom {title, text}, with the top one narrowest |
| `section` | section | `number` the section number such as "01" (auto-numbered if omitted), `title`, `subtitle` |
| `ranking` | rank_grid | `items` 3 to 10 {num, title, text}, `findings` {title, items:[text…]} the conclusion box under the ranking |
| `explain` | explain | An explanation page for science and teaching content. `blocks` for a single column, or `columns` for two to four columns (each {blocks}); a block is {label} a small label, {text} body text, {formula} a formula (centred in a light-coloured bar, with all the formulas on a page at the same font size), {rule, tone} a judgement rule (tone takes up for green / down for red), {note} a footnote; `image` the diagram on the left; `boxed` whether to give each column a card (added by default when there are several columns) |
| `screenshot` | shot_notes | `image` the screenshot path (relative to the working directory), `items` 0 to 5 {title?, text, at?: [horizontal ratio, vertical ratio]}, where `at` is a position from 0 to 1 and stamps the matching number onto the screenshot; `caption` small text below the screenshot; `frame` the outer frame style |
| `screenshots` | shot_stack | `items` 1 to 4 {image, title?, text?, num?}, `flow` defaults to true (steps, with numbers and arrows), false for a side-by-side comparison; `frame` the outer frame style |
| `question` | question | `question` the big question (can carry a **stressed word**), `kicker` a short lead-in, `body` a one-sentence hint |
| `big_quote` | big_quote | `quote` the quotation, `by` the attribution, `note` supplementary context (time, occasion) |
| `toc` | toc or toc_row | `title` defaults to "Table of contents", `kicker` defaults to "CONTENTS", `items` each {title, text?}; if items is omitted, it automatically lists the titles and subtitles of all the section pages |
| `closing` | closing | `headline`, `body`, `cta` the button text |
| `timeline` | timeline | `items` 3 to 6 {date, title, text, emphasis}, written in chronological order |
| `funnel` | funnel | `items` 3 to 5 layers {label, value, text}, from wide to narrow; when all the values are numbers, the widths are proportional |
| `hub` | hub | `center` {title} the centre, `items` 3 to 6 {title, text}, connected to the left and right columns |
| `matrix` | matrix | `x_axis` / `y_axis` each {label, low, high}, `quadrants` four items in the order top-left, top-right, bottom-left, bottom-right, each {title, items:[text…], emphasis} |
| `table` | table | `columns` the header row, `rows` a two-dimensional array, `highlight_col` which column to highlight (counted from 0), `note` a note under the table; cells can use `**bold**` |
| `chart` | chart | `chart` see below, `insights` one to three conclusions on the right, `source` the data source |
| `framework` | framework | `framework` {kind, blocks, labels?}, see below |

How to write `chart`

- `type` takes column, bar, line, pie, doughnut, stacked
- `categories` the categories, `series` each {name, values}, with values the same length as categories
- `highlight` the index of the category to emphasise (works for single-series column, bar and pie charts), `unit` set to "%" makes pie labels carry a percent sign, `number_format` such as `"0"` `"0.0"` `"#,##0"`
- With several lines, label the numbers only at the ends, so the numbers don't crowd together
- Numbers must come from the material or a verified source, and `source` is required; if the data changes, the conclusions in `insights` and the title must be rewritten together

The blocks keys for `framework`

| kind | blocks keys | Items per block |
|---|---|---|
| swot | s, w, o, t | 1 to 4 |
| pest | p, e, s, t | 1 to 4 |
| five_forces | center, entrant, substitute, supplier, buyer | 1 to 3 |
| canvas | kp, ka, kr, vp, cr, ch, cs, cost, revenue | 1 to 3 |

Each block is an array of strings. To change a block name (for example writing "our strengths" instead of "Strengths"), override it in `labels` under the same key.

`emphasis: "primary"` marks this card as the key one (a solid accent-coloured card, or emphasis on a light background). In the source, the card filled with the accent colour is usually the key one.

## Lessons for mapping from a source draft

- In `deck.draft.json`, each text unit carries a guessed `role` (title, number, footer, page, decor, text), a font size, whether it is bold, and the fill of the colour block it sits in, `container.fill`. Text in the same colour block belongs to the same card.
- A lone CJK quotation mark such as 「 in the source is decoration; after beautification it is replaced by a quote icon, so it does not need to go into deck.json.
- Text inside images in the source (`pictures[].svg_texts`) has to land in `diagram`; QA raises a missing-text warning for this kind of text.
- When a page's content doesn't fit any layout, change the layout first (list_icons holds the most, for example); if there is really no option, lay it out by hand with the `free` layout — don't delete text.
- Don't invent text that isn't in the source. When a layout needs a label, you may only use text that already exists in the source.
- To emphasise the first half of "Recyclables: paper, plastic, metal", don't split it into title and text (the colon would be lost); write it as `"**Recyclables**: paper, plastic, metal"`. A bold marker doesn't count as changing the text — QA ignores it.
- In the source, each paragraph is one validation unit, so splitting a bulleted list into several cards is fine, but don't split a single paragraph or merge two paragraphs.

## Complete example (excerpt)

```json
{"n": 4, "type": "stats", "title": "The numbers behind its popularity are rock solid",
 "items": [{"value": "730K", "label": "downloads in the first 5 days"},
           {"value": "2.5M", "label": "total downloads across the web in 13 days"},
           {"value": "640K", "label": "US mobile daily active users"}],
 "takeaway": "Daily active users are nearly 3× ChatGPT at the same stage — people really are using it every day",
 "page": "04 / 11", "notes": "So how popular is it, really? ..."}

{"n": 5, "type": "diagram_text", "title": "Why it can still get work done with the screen off",
 "diagram": {"title": "Secure VM standalone cloud computer", "icon": "cloud",
             "boxes": [{"text": "Your login info · browser · accounts"}, {"text": "Sentinel supervisor", "emphasis": "primary"}],
             "caption": "Every outward action needs its approval"},
 "point": "Everyone gets their own cloud computer; tasks keep running with the screen off",
 "body": "Your account data is fully isolated from everyone else's, with a supervisor watching over it.",
 "callout": "The barrier is so low you can **just sign up and use it**, whereas that earlier kind of Agent had to be deployed locally.",
 "page": "05 / 11"}
```
