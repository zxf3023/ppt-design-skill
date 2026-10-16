## What it does

`ppt-design` is a working method for building a deck, in the order the work actually happens: decide what the argument is, choose the container that carries each page, then lay the page out — and, if you want the file, produce it.

The skill has two halves that share one set of standards.

**The methodology** is the set of rules and frameworks that stop a deck from becoming a document with page numbers. It ships three theory layers because decks fail at three different levels, and a fix aimed at the wrong level never works.

| Layer | Framework | Question | Typical failure it catches |
| --- | --- | --- | --- |
| **Logic** | Pyramid Principle, MECE, SCQA | How is the argument organised? | The deck has no through-line; every page is a peer |
| **Visual** | Gestalt, rule of thirds, Hick's law, CRAP | How is the page laid out? | The eye has nowhere to land; eight things compete at once |
| **Structure** | 5W2H, SWOT, funnel, timeline | Which container carries this page? | Content is forced into a shape it does not fit |

The order matters. Logic first, because a beautifully laid out deck with no argument is still a bad deck. Structure second, because the right container is decided by the shape of the content, not by what looks nice. Visual last, because layout is the cheapest thing to change and the least important thing to get right first.

On top of the frameworks, the methodology carries the parts that are simply arithmetic: a type scale that produces visible hierarchy, minimum whitespace, how many words fit on a slide, how many items before a list should become a chart. These are given as numbers, not adjectives.

**The execution engine** is what turns those decisions into a file. It has two routes and they converge early:

- **Generate** — give it a topic, an article, a spoken script or an outline, and it writes the content, then designs it.
- **Beautify** — give it a plain `.pptx` and a reference image, and it extracts the content without altering a word, then re-designs it in the reference's style.

Both routes emit **editable native `.pptx`**: every piece of text is a real text box, cards and dividers are native shapes, and only backgrounds, illustrations, icons and brush strokes are images. Both drive the same three intermediate files — `deck.json` (what each page says), `style.json` (palette, fonts, decoration) and `plan.json` (layout, icons and illustration prompts per page). Scripts do the deterministic work; the model does the judgement.

The engine ships 14 style presets, a layout library with per-layout capacity, an icon library, a five-dimension self-review (unity, hierarchy, detail, communication, pacing) and a QA pass that checks for missing text, overflow, overlap and over-emphasis. Image generation is optional — configure OpenAI, Gemini, Volcengine Ark or a custom endpoint, or let it fall back to programmatic illustration and say so in the delivery note.

## When to reach for it

Type `/ppt-design`, or the agent reaches for it on its own when you ask for a deck, slides, a report, a proposal, or a review of one.

| Your situation | Reach for |
| --- | --- |
| You have a topic, an article, or a script and need it to become slides | `ppt-design`, generate route — start at the logic layer |
| You have a plain `.pptx` and a reference image, and you want the style but not a rewrite | `ppt-design`, beautify route |
| You already have slides and they feel wrong but you can't say why | `ppt-design`, chapter 9 checks |
| You have a wall of text on a page and need to compress it | `ppt-design`, chapter 5 (the four-step method) |
| You need to pick a palette or a font and don't want to guess | `ppt-design` plus a theme under `themes/`, or a preset under `references/styles/` |
| You only want design advice — an outline, a review, a spec — and no file | `ppt-design`, chapters 1–10 only; skip the engine |

## Common questions

**Does it make the file, or just the design?**
Both, and you choose. The methodology stands alone for review, outlining and specification work. When you want the file, the engine takes over from layout planning onward and produces an editable `.pptx`.

**Will beautifying my deck change my text?**
Not by default. The beautify route copies text character for character, keeps the page order and page count, and preserves speaker notes. Refining the wording is opt-in, and when it is on, every change is listed for you to approve.

**Why three frameworks instead of one?**
Because they answer different questions and the failures are independent. A deck can have a sound argument (logic passes) that is laid out so badly nobody follows it (visual fails). It can look beautiful and argue nothing. One framework cannot catch both, and a reviewer who only has one will confidently pass a deck that fails on the other.

**Do I have to use all three on every deck?**
No. A five-page internal update needs the logic layer and maybe a type scale. A 60-page pitch needs all three. Start at the logic layer regardless — it is where the expensive mistakes are.

**How many words is too many?**
Chapter 4 gives the numbers rather than a feeling. If you are past them, chapter 5's four-step method is the fix — and the first of those steps is usually "delete this page".

**What if image generation is not configured?**
The engine falls back to programmatic illustration, and the delivery note says which pages used it. It never claims a fallback image was model-generated.

**What does the engine need installed?**
Python with `python-pptx`, Pillow, numpy and lxml. `scripts/setup_check.py --quick --install` verifies and installs them. LibreOffice is recommended for rendering preview sheets; without it the engine draws an approximate preview from the layout data instead.

## It's working if

- You can state what each page says in one sentence, and that sentence is not the title.
- The deck reads in the same order when the slides are printed as a handout, and when they are presented.
- A page that survives the four-step method is shorter than what you started with, and nothing was lost.
- The type scale produces a hierarchy you can see from the back of the room without being told where to look.
- Nobody asks "can you go back a slide" because the argument did not need re-reading.
- The delivered `.pptx` opens in PowerPoint with every word still editable, and nothing overflowed a text box.
