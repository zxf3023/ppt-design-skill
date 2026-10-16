# Five-dimension self-review after rendering

QA only covers mechanical problems: text overflow, contrast, missing text. Whether the whole deck looks like it was made by one person, and whether it rises and falls as you page through, are judgements a script cannot make — you have to look at the images.
The last step of `pipeline.py` runs `review.py`, which writes the countable evidence into `out/review.md`; you fill in the scores and conclusions after looking at the images.

## How to do it

1. Look at the overview `out/sheet.png` first, then examine three pages closely: the cover, the page with the most text, and the closing page
2. Against the numbers in `review.md`, score each of the five dimensions from 0 to 10
3. Write three lists: keep, must fix, quick fix
4. Fix the "must fix" items before delivery and re-run the pipeline afterwards; do the "quick fix" items where you can
5. Give the conclusion in a sentence or two at delivery, for example "unity 8, hierarchy 7, detail 8, communication 7, pacing 6 — the pacing is flat, four pages in the middle are all cards"

Score bands: 0 to 4 is failing, 5 to 6 is usable, 7 to 8 is solid, 9 to 10 is outstanding.
The five dimensions are scored independently — do not average them. A deck can score 9 for unity and 4 for pacing, and you should write it as it is.

## The five dimensions

### 1 Unity

Does the whole deck commit to one direction, from cover to closing page, without drifting?

What to look at
- Do the colour scheme, fonts, corner radii and decorative motifs follow the same rules on every page
- Do the header, footer, section numbers and page numbers look consistent throughout
- Is the accent colour used by one consistent rule, rather than highlighting numbers on one page and filling backgrounds on another

Deduction signals: more than 10 font sizes across the deck, colours outside the palette, three or more card corner radii, a page that suddenly switches illustration style.

### 2 Hierarchy

Can someone who has not heard the presentation tell at a glance what to look at first and what next?

What to look at
- Is the largest text on each page the most important information on that page
- Are the three levels of heading, key point and caption clearly separated; the ratio of the largest font size to the median body font size should generally be 1.5 or more
- Is the accent colour overused — if everything is highlighted, nothing is

Deduction signals: five or more font sizes on one page, numbers as large as the heading and competing with it, captions more prominent than key points.

### 3 Detail

Have the small things — alignment, spacing, edges — come loose?

What to look at
- Are the left edges of the same column actually aligned; a one or two millimetre offset hurts the look more than anything
- Is the padding inside cards consistent, and is any text touching the edge
- Do the icons convey the right meaning, does any illustration cover text, has the footer been squeezed by the content

Deduction signals: "slightly misaligned" entries in review.md, QA contrast, rail and accent warnings, and one or two characters left dangling at the end of a line.

### 4 Communication

Does each page get its own point across clearly?

What to look at
- Do the titles alone read as a complete story
- Are the slides showing keywords or whole paragraphs; whole paragraphs belong in the notes
- Do data pages cite a source, and is the chart's conclusion written in the title

Deduction signals: pages with more than 160 characters on screen, topic-style titles ("Market Analysis", "Summary"), and spoken pages with no notes.

### 5 Pacing

Does paging through have tension and release, or is it one tone all the way?

What to look at
- Do the layouts vary; is a big-type, big-number or image page slipped in between full pages of cards
- Does the density vary; a standard deviation of character count divided by the mean between 0.3 and 0.7 gives a better sense of breathing room
- Do the section pages and the conclusion page act as pauses

Deduction signals: three consecutive pages with the same layout, every page with three cards, every page with an illustration.

## Common "must fix" items and how to fix them

| Problem | Fix |
|---|---|
| Too many scattered font sizes | Use the same `grp` for text of the same kind, or switch to a level that already exists in the layout |
| A page with flat hierarchy | Shorten the title, enlarge the number, or switch to `statement_number` / `statement_hero` |
| Several pages of cards in a row | Break it up with a `statement_hero`, `chart` or section page |
| Too much accent colour | Keep one emphasis and change the rest to primary or muted |
| Too much text | Split the page, or move the explanation into `notes` |
| Slightly misaligned | Lay it out by hand with the `free` layout, or adjust the coordinates in the layout |
