# Generating a PPT from Scratch

The input can be an article or a spoken script, a topic, an outline, or .docx / .pdf / .pptx material.
Generation and beautification share the same design engine; they differ only in the first half of the process: beautification extracts deck.json from an existing draft, while generation writes deck.json itself.
In generation mode the text may be rewritten, condensed and reorganised — this is the biggest difference from beautification.

## Process Overview

| Step | What to do | Tool | Stop for confirmation |
|---|---|---|---|
| G1 | Clarify the requirements | one round of questions | Yes |
| G2 | Analyse the material | `analyze_source.py` | No |
| G3 | Write deck.json | per the rules in this document | No |
| G4 | Check the outline, show it to the user | `outline_check.py` → outline.md | Yes |
| G5 | Decide the style | with a reference image, run `extract_style.py`; without one, `style_previews.py --auto` produces three samples | Yes |
| G6 | Layout planning | `plan_deck.py` → design_spec.md | Yes (skipped in fast mode) |
| G7 | Render images, assemble, check | `pipeline.py` | No |
| G8 | Deliver | pptx + preview images + a one-sentence note | |

When the user says "just produce it" or "don't ask me", enter fast mode: G1 uses the defaults, G4, G5 and G6 don't stop, the first style sample is chosen automatically, and the choices that were made are listed at delivery.

## G1 Clarify the requirements

Ask everything in one round of questions; for anything not answered, use the default in parentheses.

- Where it will be used: spoken video / live talk / sent out to be read / work report (spoken video)
- Who it's for: beginners / some background / professional peers / the boss (beginners)
- How long: how many minutes or how many pages (estimated from the material)
- Style: is there a reference image; if not, produce three samples to choose from (produce samples)
- Whether speaker notes are needed (yes by default for spoken video and talks)

The scenario determines density: spoken video and talks use low (one idea per page, few words on screen, the expanded wording goes into the notes), while reading and reports use high (each page stands on its own and can carry several points).

## G2 Analyse the material

```bash
python3 $S/analyze_source.py $W --file article.md --scenario oral
python3 $S/analyze_source.py $W --topic "Topic" --minutes 3
```

You get analysis.md: word count, the heading structure of the source, numbers that can become data pages, style clues, and a suggested page count.
A rule of thumb for estimating pages is that one spoken page is about 25 seconds, corresponding to roughly 150 characters of source text; for an outline, allow "at least one page per second-level heading".

**When you only have a topic**, first decide "the one sentence the audience should remember after watching", then list three to five supporting points. For anything involving facts, data or the current state of a product, verify it with a search first; if you can't find it, don't write it — never make up numbers.

## G3 Write deck.json

See `deck_schema.md` for the field formats. Generation mode uses these fields in addition.

```json
{"meta": {"title": "…", "scenario": "oral", "audience": "beginner", "density": "low",
          "storyline": "One sentence that makes the whole deck's arc clear", "notes": true, "auto_page": true,
          "series": "Small header text, optional", "anchor": {"description": "…", "glyph": "M"}},
 "slides": [{"n": 2, "type": "big_number", "purpose": "Make the audience remember in one sentence what it is",
             "title": "…", "…": "…", "notes": "The spoken wording", "source": "Data source, optional"}]}
```

### Build the storyline first

Pick one main line according to the scenario, then fill in the pages.

- **Explanatory** (the default for spoken popular science): opening hook → what it is → why it's worth paying attention to (evidence, data) → how to use it → pitfalls and limits → call to action
- **Proposal** (reports): current situation and problems → goals → proposal → plan and resources → risks → decisions that need to be made
- **Listicle** (tips collection): why it's needed → item one through item N → how to combine them → call to action

Write the main line into `meta.storyline`, and give each page a `purpose` (what that page is responsible for in the story).

### Titles state conclusions

Each page title is a conclusion that stands on its own, not a topic name.

| Topic name (don't) | Conclusion style (do) |
|---|---|
| Data performance | The numbers behind its popularity are rock solid |
| How to use it | Start by changing permissions, then connect the account |
| Things to watch out for | It makes mistakes — don't hand over your judgement |

When you're done, read all the titles in order; they only pass if they read as one complete story. If they don't read smoothly, adjust the order or add pages — don't rush into the design. Keep titles between 4 and 22 characters.

### One thing per page

- One page carries one idea only. If it doesn't fit, split the page; don't shrink the font and force it in.
- low density: about 100 characters or fewer on screen, at most 4 points; high density: about 200 characters or fewer, at most 6 points.
- Put keywords and short phrases on screen, and the full sentences in `notes`.
- The closing page carries a conclusion or a call to action, not "thank you for watching".
- When there are more than 15 pages, add section dividers (type: section).

### Speaker notes

`notes` is the script to be read aloud: conversational, short sentences, matching this page's content one-to-one, 40 to 260 characters per page (about 15 to 60 seconds).
When rewriting from an article, keep the author's original sentences and tone in the notes as much as possible, then distil the on-screen text from the notes.
If the environment has the user's own writing-style skill, write the notes in that style.

### The shape of the content determines the page type

| What the content looks like | type | Default layout |
|---|---|---|
| One core number or a one-sentence definition | big_number | statement_number |
| Two to four data points | stats | stats_row |
| Two to five steps in a sequence | process | steps_flow |
| How-to advice, one key point plus one supplement | steps | side_cards |
| A contrast between two things, or before and after | compare | compare_split |
| A repeating cycle of stages | cycle | cycle |
| Layered structure, with a base and upper levels | layers | pyramid |
| Explanations of several parallel concepts | definitions | rows_side |
| Three to six short points | list / grid | grid_cards |
| Example sentences, prompts, original quotes | quotes | quote_cards |
| Risks and pitfalls, plus a one-line summary | warnings | cards_quote |
| One claim plus an explanation | statement | statement_hero |
| A diagram plus commentary | diagram_text | media_text |
| One screenshot explaining several points of action | screenshot | shot_notes |
| Several screenshots covering one flow, or a desktop-versus-mobile comparison | screenshots | shot_stack |
| Milestones or history arranged by time | timeline | timeline |
| Layer-by-layer conversion, filtering or drop-off | funnel | funnel |
| One core radiating out to several parts | hub | hub |
| Classifying or prioritising things along two dimensions | matrix | matrix |
| Comparing several options across several dimensions | table | table |
| Comparing magnitudes, spotting trends, or showing proportions | chart | chart |
| Strengths and weaknesses, external environment, competitive landscape, business model | framework | framework |
| Start of a chapter | section | section |
| A deck divided into chapters, right after the cover | toc | toc |
| Pose a question, answer it on the next page | question | question |
| A single quote worth a page of its own | big_quote | big_quote |

Don't use the same page type three times in a row — vary how you tell it. See `deck_schema.md` for each page type's fields, and use `python3 $S/layout_info.py <layout name>` to check how much each layout can hold; it also includes an example you can edit directly.

Choosing data pages: if you only want people to remember one or two numbers, use big_number or stats; only bring in chart when people need to see which is bigger, which way things are heading, or what share something takes. A chart's title is the single most important conclusion in the chart, and insights add one or two findings the title didn't cover.

Don't force an analysis framework in just to look professional. If one of the four SWOT boxes can only be filled with empty words, that page should become compare or warnings instead.

You can wrap the single most important word in a title with `**…**`, which turns it into the accent colour; mark at most one place per title — mark more and there is no emphasis left.

### Key points for the three kinds of input

- **An article or spoken script**: first cut the storyline by paragraph — one paragraph is often one page; turn numbers into data pages first; a striking line from the source can be used directly as a title or takeaway.
- **An outline**: at least one page per second-level heading; use process for ordered lists, warnings for "pitfalls" and "misconceptions", and turn "a final word" into the closing page. An outline usually has no expanded wording, so the notes need to be written out, and any facts you add must be verified.
- **A topic**: see the approach in G2 — verify first, then write.

## G4 Check the outline

```bash
python3 $S/outline_check.py $W
```

It prints a ghost draft (titles only) and checks for topic-style titles, density, number of points, note length, page count, repeated page types and the closing page. It also reports the pages that don't fit, based on layout capacity, and gives alternative layouts that do fit.
Keep fixing until there are no ERRORs and you have looked at every WARN, then send the "titles only" part of outline.md to the user for confirmation.

## G5 Decide the style

- The user provided a reference image: follow step 2 of the beautification process (`extract_style.py` + look at the image and write style.json + `style_card.py`).
- No reference image:
  ```bash
  python3 $S/style_previews.py $W --auto          # or --presets a,b,c to pick three sets yourself
  python3 $S/style_previews.py $W --apply <id>    # after the user chooses
  ```
  The three samples are one safe, one bold and one unexpected, all using the user's own cover and first page content. Send `previews/sheet.png` to the user and explain in the conversation what styles 1, 2 and 3 are and what each one suits. The preset list is in `styles/index.json`, and each set's hard rules are in its own json — follow them when laying out.

## G6 Layout planning

```bash
python3 $S/plan_deck.py $W --level full            # with an image model, add --sheets to slice one big image into several small illustrations
```

It writes plan.json and design_spec.md. Review them: do the layouts fit the content, is the visual focus of each page clear, are the illustration prompts specific (see `image_prompts.md`).
You can add a `relation` to each page in plan.json (its relationship to the pages before and after, for example "picks up the previous page's data and moves into how to do it") to help keep the rhythm consistent.
Send the tables in design_spec.md to the user for confirmation before rendering images — rendering is the most expensive step.

## G7 Render images, assemble, check

```bash
python3 $S/pipeline.py $W
```

In generation mode, QA is based on deck.json and checks that every piece of text made it onto a page; the other checks are the same as for beautification.
The final prompts for AI illustrations are written into `prompts/`. To change a particular image, edit its prompt file, then run `make_assets.py $W --only hero_05 --force`.

## G8 Deliver

The pptx, the preview images, and a sentence or two explaining: which style was used, where the illustrations came from (model or procedural), and whether there is anything the user needs to add or verify.
