## What it does

`ppt-design` is a working method for building a deck, in the order the work actually happens: decide what the argument is, choose the container that carries each page, then lay the page out. It is not a template gallery and it does not generate slides for you. It is the set of rules and frameworks that stop a deck from becoming a document with page numbers.

The skill ships three theory layers because decks fail at three different levels, and a fix aimed at the wrong level never works.

| Layer | Framework | Question | Typical failure it catches |
| --- | --- | --- | --- |
| **Logic** | Pyramid Principle, MECE, SCQA | How is the argument organised? | The deck has no through-line; every page is a peer |
| **Visual** | Gestalt, rule of thirds, Hick's law, CRAP | How is the page laid out? | The eye has nowhere to land; eight things compete at once |
| **Structure** | 5W2H, SWOT, funnel, timeline | Which container carries this page? | Content is forced into a shape it does not fit |

The order matters. Logic first, because a beautifully laid out deck with no argument is still a bad deck. Structure second, because the right container is decided by the shape of the content, not by what looks nice. Visual last, because layout is the cheapest thing to change and the least important thing to get right first.

On top of the frameworks, the skill carries the parts that are simply arithmetic: a type scale that produces visible hierarchy, minimum whitespace, how many words fit on a slide, how many items before a list should become a chart. These are given as numbers, not adjectives.

## When to reach for it

Type `/ppt-design`, or the agent reaches for it on its own when you ask for a deck, slides, a report, a proposal, or a review of one.

| Your situation | Reach for |
| --- | --- |
| You have a topic, an article, or a script and need it to become slides | `ppt-design`, starting at the logic layer |
| You already have slides and they feel wrong but you can't say why | `ppt-design`, running the chapter 9 checks |
| You have a wall of text on a page and need to compress it | `ppt-design`, chapter 5 (the four-step method) |
| You need to pick a palette or a font and don't want to guess | `ppt-design` plus a theme under `themes/` |
| You need the actual `.pptx` file produced | `ppt-design` for the design, then a `python-pptx` build script — chapter 8 covers the API and the pitfalls |

## Common questions

**Does it make the file, or just the design?**
The design. It tells you what the page should contain and how it should be laid out. Chapter 8 covers driving `python-pptx` — including the one pitfall that catches everyone, setting a Chinese font without also writing the `a:ea` element — but the skill's job is the decisions, not the file.

**Why three frameworks instead of one?**
Because they answer different questions and the failures are independent. A deck can have a sound argument (logic passes) that is laid out so badly nobody follows it (visual fails). It can look beautiful and argue nothing. One framework cannot catch both, and a reviewer who only has one will confidently pass a deck that fails on the other.

**Do I have to use all three on every deck?**
No. A five-page internal update needs the logic layer and maybe a type scale. A 60-page pitch needs all three. Start at the logic layer regardless — it is where the expensive mistakes are.

**Is the chapter 8 font recipe specific to Chinese?**
The `a:ea` pitfall is specific to East Asian text, but the section is worth reading for any deck built by script: it covers grouped shapes, reading the master theme, and why font size must be set on the run rather than the paragraph.

**How many words is too many?**
Chapter 4 gives the numbers rather than a feeling. If you are past them, chapter 5's four-step method is the fix — and the first of those steps is usually "delete this page".

## It's working if

- You can state what each page says in one sentence, and that sentence is not the title.
- The deck reads in the same order when the slides are printed as a handout, and when they are presented.
- A page that survives the four-step method is shorter than what you started with, and nothing was lost.
- The type scale produces a hierarchy you can see from the back of the room without being told where to look.
- Nobody asks "can you go back a slide" because the argument did not need re-reading.
