## What it does

`ppt-master` is a complete deck workflow written in Chinese, and it is tool-neutral: it works with whatever the environment provides, with implementation guidance for both pptxgenjs and python-pptx. Start from a request (a topic, material to restyle, or an existing `.pptx` to edit), and it runs six steps in order: clarify the request, structure the content, set the design system, build the file, run QA, deliver.

The request step is deliberately minimal. Known dimensions are skipped, and it asks at most one to three questions, only when the answer would change the output. When the request is vague but inferable, it builds the deck and states the assumptions in one line at delivery.

The two parts that carry most of the quality:

**The design system comes before any page.** Palette (one dominant colour at 60–70%, one or two supporting, one accent that is spent only on the key point), fonts from the cross-platform safe list, a type scale (page title 36–44pt, section 20–24pt, body 14–16pt, caption 10–12pt, big number 60–72pt), margins of at least 0.5", uniform block spacing of 0.3–0.5", and one recurring visual motif chosen per deck. Ten reference palettes ship as inspiration, to be adjusted to the actual topic; a palette that would still work for a different topic is too generic.

**Layouts rotate.** Ten patterns (text-plus-image either side, icon rows, 2x2 and 2x3 card grids, full-bleed image with overlay, stat callout, comparison columns, timeline or flow, chart plus insight sidebar, quote, section divider) are cycled so no two consecutive pages share one, and every page carries at least one visual element. Cards are separated by light background panels, subtle shadow or icons, never by edge colour bars, and a colour bar or accent line is never used as the deck's motif.

Content rules are numeric rather than advisory: one point per page, titles written as conclusions ("Renewals drive 60% of East region growth", not "Sales analysis"), bullets as phrases of two lines at most and five per page at most, body text left-aligned, long text compressed by distilling and regrouping instead of shrinking the font.

Data pages follow fixed rules: native charts stay native and editable, one chart makes one point, the key series is emphasised and the rest greyed, a single series drops its legend, pie charts stay at five slices or fewer, gridlines are thin and faint, and the conclusion is written on the page instead of left for the reader to find.

Implementation covers the two common tools with their pitfalls. For new decks the default is a structured build: a theme object (colours, title and body fonts) referenced everywhere so a theme swap re-skins the deck, a section per chapter, a layout per page framework with named placeholders carrying position, size, weight and colour, then pages filled by name. The pptxgenjs section lists the traps that corrupt files or silently break: `pres.layout` must be set before adding pages, no `#` prefix and no 8-digit hex in colours, shadow offsets of zero or more, `charSpacing` rather than `letterSpacing`, `bullet: true` rather than hand-typed bullets, fresh option objects per call, `rectRadius` only on rounded rectangles, gradient fills unsupported (use a gradient image), notes via `slide.addNotes`, and stacked bar `dataLabelPosition` limited to `ctr`/`inEnd`/`inBase`. For existing decks and templates it unpacks the `.pptx`, edits `ppt/slides/slideN.xml` with a safe parser, copies pages with a dedicated script, and repacks inside the unpacked directory.

QA is mandatory, in three layers: export the text and check content, run the file validation, then render every page to an image and look at it. The render chain is LibreOffice to PDF, `pdftoppm` to JPG, and all four commands are re-run after any fix, since the PDF must come from the new pptx. The per-page checklist is ordered by how often failures actually occur, text overflow first, then overlap, spacing, margins, alignment, contrast, inconsistent labels across similar pages, and leftover placeholder text. The first render almost always has a real problem on it, so a deck whose pages were never looked at is not finished. The advice to look with fresh eyes is taken literally: staring at the generating code too long makes you imagine the result.

## When to reach for it

The model reaches for it when the request involves producing, editing, beautifying, restyling or reviewing a deck, and the environment offers pptxgenjs or python-pptx rather than a dedicated slides tool.

| Your situation | Reach for |
| --- | --- |
| You want a deck built in Chinese from a topic, script or outline | `ppt-master`, steps 1 to 6 |
| You have an existing deck that needs restyling, not rewriting | `ppt-master`, section 6.5 (diagnose, then change form, keep content) |
| You have a company template to fill | `ppt-master`, section 6.4 (unpack, edit the XML, repack) |
| You are about to generate a deck with pptxgenjs | `ppt-master`, section 6.3 (the pitfalls, before the code) |
| A deck exists but nobody has looked at the rendered pages | `ppt-master`, section 7 (QA three-piece set) |
| You want the English methodology route with a Python engine and 23 scripts | `ppt-design` instead |

## Common questions

**Which tool should I generate with?**
pptxgenjs by default, python-pptx when the environment is Python-only. python-pptx cannot copy pages, and assigning `text_frame.text` wipes formatting, so edit `run.text` instead. Neither reads SVG or EMF.

**Does it need an image-generation model?**
No. Abstract diagrams are drawn from basic shapes, which beats a low-quality stock image. The skill is tool-neutral by design and has no model dependency.

**What if the target machine lacks the font?**
Pick from the cross-platform safe list (Arial, Calibri, Cambria, Times New Roman, Courier New, Bookman Old Style, Century Schoolbook), keep the deck to one or two families, and for Chinese leave 10% or more width redundancy since Chinese renders wider. Do not trust the preview to tell you whether text overflowed.

**Why is the visual QA step not optional?**
Because overflow, overlap and misalignment only exist in the render, not in the code that produced it, and the first render almost always has at least one. Fix in the generator and rebuild rather than hand-patching the packaged XML.

**How does it differ from `ppt-design` in this repo?**
`ppt-design` is an English methodology plus a Python execution engine with 23 scripts, 14 style presets and a five-dimension self-review. `ppt-master` is a Chinese workflow that runs on whatever tool is installed, edits existing decks at the XML level, and ends at a mandatory page-by-page visual QA. Use `ppt-design` for the engine and the presets, `ppt-master` when the job is a full production run in a pptxgenjs or python-pptx environment.

## It's working if

- Read the titles in sequence, they tell the whole story, and each title is a conclusion rather than a topic.
- No two consecutive pages share a layout, and no page is a title plus bullets with nothing else on it.
- Every page's type sizes sit on the scale, margins are at least 0.5", and nothing overflowed a text box or shape.
- Charts are native and editable, labelled directly, with one conclusion written beside each, and single-series charts carry no legend.
- Every rendered page was looked at, and overlap, collision with the footer, inconsistent labels and leftover placeholder text are all absent.
- The deck's motif appears on every page, and no colour bar or accent line is doing that job.
- The delivery is short: page count, structure, style in one line, assumptions made, and what can be adjusted.
