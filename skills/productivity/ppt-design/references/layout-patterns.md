# Layout Pattern Library

38 battle-tested page layouts, grouped into Opening and navigation / Text / Image and text / Data and charts / Diagrams and models / Special pages.
Each pattern gives **when to use it + structure + arrangement rules + cautions**.

> Before choosing a layout, run through the decision tree in `structure-models.md` — **picking the wrong framework is more fatal than ugly typesetting**.

---

## I. Opening and Navigation

### 1. Cover

```
┌──────────────────────────────────┐
│                                  │
│        [Main title 40–54pt]      │
│        ─────                     │
│        [Subtitle 20–24pt]        │
│                                  │
│                                  │
│ [Author/Dept]            [Date]  │
└──────────────────────────────────┘
```

- One page of information: main title + subtitle + entity + date
- Name the main title as a **conclusion** (e.g. "XX Technical Service Proposal", not "An Introduction to XX")
- Add one visual element: a full-bleed background image / a large colour block / a geometric shape. **Do not** place 5 logos

### 2. Table of Contents

```
Table of Contents        01  ─── Part One
CONTENTS                 02  ─── Part Two
                         03  ─── Part Three
```

- **3–5 chapters** (Hick's Law); more than 5 and you should merge
- Numbering is a natural visual anchor; use 01/02/03 rather than 1/2/3
- A bilingual Chinese-and-English title adds formality
- Two columns: large title + decoration on the left, item list on the right
- The chapter breakdown must pass the MECE test (no overlap, no gaps)

### 3. Section Divider

```
             01
        ─────────
        Part One
```

- Minimal: only the **chapter number + chapter name**
- A large number at 60–72pt creates a strong rhythm
- This set of "pre-chapter dividers" is a required feature of a professional deck
- Visually it can echo the cover (same colour block, same position)

### 4. Closing Page

```
        Thank You for Listening
     Thanks for Your Time
```

- Do not write "Thanks for watching" (watching is a video word)
- You may add contact details / a QR code
- **Never** pile up "Your comments are welcome" + 5 contacts + 3 QR codes

---

## II. Text-Only Layouts

### 5. Single Passage

```
   ❝
   [One complete passage, 14–20pt]
   ───────────────────────
```

- Use a quotation-mark graphic as the visual anchor
- Close with a horizontal rule at the bottom
- Good for: core philosophy, a memorable line, mission and vision
- **≤ 80 characters**

### 6. Two Parallel Columns

```
[Subhead]        │   [Subhead]
────             │   ────
[Body text]      │   [Body text]
```

- Two columns separated by a vertical rule in the gutter
- Equal width (4.14in each, gutter at 6.66in)
- Good for: comparing two options, explaining two dimensions
- The two columns must be MECE (mutually exclusive and collectively exhaustive)

### 7. Three / Four Parallel Columns

- **3 columns**: one above the other on the left + one block on the right (breaks symmetry)
- **4 columns**: a 2×2 grid
- Every column has the same structure: subhead + divider + body
- Spacing between columns > spacing inside a column (Gestalt proximity)

### 8. Five-Card Row

```
   ●──────●──────●──────●──────●
  ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐
  │T│  │T│  │T│  │T│  │T│
  │i│  │i│  │i│  │i│  │i│
  │t│  │t│  │t│  │t│  │t│
  │B│  │B│  │B│  │B│  │B│
  │d│  │d│  │d│  │d│  │d│
  └──┘  └──┘  └──┘  └──┘  └──┘
```

- Timeline dots + a horizontal line on top, equal-width cards below
- Card size: 2.14 × 3.45in, gap 0.29in
- **5 is the ceiling** (Hick's Law); at 6 consider grouping or splitting the page

### 9. Subhead + Multiple Items

```
This is a subhead (48pt)
──────────────────
· Item one
· Item two
· Item three
```

- A large 40–54pt title gets straight to the point
- Keep it to 3–5 items, each ≤ 25 characters
- **Avoid piles of bare bullets** — consider an icon list or cards instead

---

## III. Image-and-Text Layouts

### 10. Single Image

```
┌────────┐  ┌──────────────────┐
│        │  │                  │
│ Image  │  │   Body text      │
│        │  │                  │
└────────┘  │                  │
 [Caption]  └──────────────────┘
```

- Image takes 1/3, text 2/3 (rule of thirds)
- The caption sits tight under the image (Gestalt proximity)
- Good for: a detailed look at one product or one case

### 11. Two Images

- Left: a body-text block (on a colour panel)
- Right: two images stacked vertically + captions
- Both images share the same specification (Gestalt similarity)

### 12. Three Images

```
┌──────────────────────────────┐
│  Body text (full-width block) │
└──────────────────────────────┘
┌────────┐  ┌────────┐  ┌────────┐
│ Fig 1  │  │ Fig 2  │  │ Fig 3  │
└────────┘  └────────┘  └────────┘
 [Caption]   [Caption]   [Caption]
```

- Split top and bottom: lead-in text above, three images below
- The three images **must be equal in width and height** (alignment + similarity)

### 13. One Image + N Points

```
┌────────────┐   ● Point 1
│            │   ● Point 2
│    Image   │   ● Point 3
│            │   ● Point 4
└────────────┘
```

- Image takes the left 40%, four points on the right
- Points are introduced with icons or dots

### 14. Image Wall (multi-image display)

- A grid of 6–12 images
- **Image style must be consistent** (all real photos / all the same tone)
- Give each image a short label, not a long description
- Good for: case collections, partners, credentials

### 15. Full-Screen Image + Overlay Text

```
┌──────────────────────────────┐
│                              │
│      [Dark overlay 30–50%]   │
│          Main title          │
│                              │
└──────────────────────────────┘
```

- The image fills the screen, with a 30–50% black overlay on top
- White text for maximum visual impact
- Good for: section transitions, memorable lines, mood pages
- Use it 2–3 times per deck; more than that and it wears thin

---

## IV. Data and Chart Layouts

### 16. Big-Number Page (KPI)

```
   24 yrs      35 sites     500k m²      3M copies
   Domain      Service base Site area    Annual output
```

- 4 numbers in a row, evenly spaced (x ≈ 0.9 / 4.1 / 7.3 / 10.5)
- Number 44–72pt + unit 14pt + caption 11–12pt
- **Numbers must share the same size and weight**
- A data cut-off date is mandatory (8pt grey)

### 17. Three-Line Table

```
Table 3.2  Table title must be informative
┌──────────────────────────────┐
│ Hdr  │ Hdr  │ Hdr  │ Hdr      │  ← thick line
├──────┼──────┼──────┼──────────┤
│      │      │      │          │
├──────┼──────┼──────┼──────────┤
│      │      │      │          │  ← thin line
└──────────────────────────────┘
```

- The academic three-line table: thick top rule + thin rule under the header + thick bottom rule, with **no vertical rules and no internal grid**
- The table title goes **above** the table
- A light blue header fill is acceptable
- Numbers **right-aligned**, text left-aligned
- Columns ≤ 7 (Hick's Law)

### 18. Bar / Column Chart

- **Horizontal bars** beat columns (labels are easier to read, ranking is obvious)
- Sort by value, not alphabetically or chronologically
- Remove gridlines, remove borders, mute the axes
- Put data labels directly on the bars and drop the legend

### 19. Line Chart

- For **trends**, not for comparing magnitudes
- Line 2–3px, in the primary colour
- Label key turning points with numbers
- **At most 3 lines** (Hick's Law); more means splitting the chart

### 20. Pie / Donut Chart

- **≤ 5 slices** (Hick's Law); beyond that use a stacked bar chart
- Start at 12 o'clock and go clockwise **largest to smallest**
- The largest slice gets the accent colour
- Small items under 3% may be merged into "Other"

### 21. Percentage Rings (multiple metrics)

```
   ◯        ◯        ◯
  85%      62%      40%
 Subhead  Subhead  Subhead
 Caption  Caption  Caption
```

- 3 rings in a row, evenly spaced
- Each ring has a subhead + caption beneath it
- Good for: completion rates across items, satisfaction, share

### 22. Gantt Chart / Progress Bar

- Time runs horizontally, tasks vertically
- Duration bars are rounded rectangles and can be dragged
- Completed portions in the primary colour, incomplete in light grey
- Time ticks are mandatory

### 23. Data Comparison

```
     Option A     Option B
      85%          62%
      ████████     ██████
      Pros: …      Pros: …
```

- Symmetrical left and right, same structure
- Distinguish with colour (primary vs mid-grey)
- Clearly mark "better/worse" or a "recommended" label

---

## V. Diagram and Model Layouts

### 24. Timeline (horizontal)

- Baseline + node dots + labels alternating above and below
- **≤ 7 nodes** (Hick's Law)
- Increasing node size can show growth (an advanced move)

### 25. Development History (advanced timeline)

- Large circles + year + event name + description
- Circles shrinking (or growing) imply evolution
- Suits company history and project milestones

### 26. Three-Stage Cyclic Diagram

```
    A → B
    ↑   ↓
      C
```

- Head meets tail to express "cycle, closed loop"
- Three equal nodes joined by arrows
- Good for: management cycles, service loops

### 27. Three-Stage Progressive Diagram

```
 1 ───→ 2 ───→ 3
```

- One-way arrows express "progression, process"
- Numbers 1/2/3 reinforce the sequence
- Good for: implementation steps, development phases

### 28. Four Parallel Columns

```
  01        02        03        04
  Title     Title     Title     Title
  Body      Body      Body      Body
```

- Four equal-width columns, identical specification
- Each column = number + title + body
- Good for: four key points, four dimensions

### 29. SWOT Matrix

```
┌────────────┬────────────┐
│  S         │  W         │
│ Strengths  │ Weaknesses │
├────────────┼────────────┤
│  O         │  T         │
│ Opportunity│ Threats    │
└────────────┴────────────┘
```

- A 2×2 four-quadrant grid in four colours (internal/external × positive/negative)
- ⚠️ **You must add the four SO/WO/ST/WT strategies**, otherwise it is just a list (see `structure-models.md`)

### 30. Architecture Diagram

```
        ┌─────────┐
        │  Top    │
        └────┬────┘
    ┌────────┼────────┐
┌───┴──┐ ┌───┴──┐ ┌───┴──┐
│Module│ │Module│ │Module│
└──────┘ └──────┘ └──────┘
```

- Clear levels; elements at the same level are equal-sized and aligned
- Connectors show relationships; **more than 4 levels means splitting the page**
- Use colour to distinguish levels (darker higher up)

### 31. Coordinate Matrix

- A four-quadrant scatter with two dimensions on the axes
- Suits positioning analysis (e.g. "importance vs urgency")
- Each quadrant carries an explicit recommended action

### 32. Pyramid / Funnel

- Pyramid: layered progression, wide base (foundational/general) and narrow top (core/few)
- Funnel: layer-by-layer filtering, wide top (entry) and narrow bottom (result)
- **Every layer must be labelled with data** (see `structure-models.md`)

---

## VI. Special-Purpose Pages

### 33. Blank Page

- Plain white or solid background, no decoration at all
- For writing live, discussion, thinking on your feet
- Place it between chapters as a "thinking interlude"

### 34. Credentials / Awards

- A grid of certificate images
- Uniform size, uniform border
- Category labels may be added (national / provincial / industry)

### 35. Client Case Wall

- A grid of logos
- Group by industry or size
- Rendering logos in grey strengthens the sense of unity

### 36. Patents / Standards List

- A table with number + name + status
- Citation format is consistent
- When there are many, list only representative entries and move the rest to an appendix

### 37. Service Process

```
 ① ──→ ② ──→ ③ ──→ ④ ──→ ⑤
 Consult Sign  Execute Deliver Support
```

- 3–7 steps, one verb each
- A horizontal process with numbered circles and arrows
- You may annotate each step with its **time limit**

### 38. Appendix Page

- Detailed data, complete lists, references
- Type may be smaller than the body (10–12pt)
- Clearly label it "Appendix"

---

## VII. Layout ↔ Structure Model Mapping

| Page layout | Structure model it carries |
|---|---|
| Seven-cell grid / three-column | 5W2H |
| SWOT matrix | SWOT |
| Funnel chart / horizontal funnel bar | Funnel |
| Timeline / development history / Gantt chart | Timeline |
| Progressive logic diagram | Process (chronological) |
| Cyclic logic diagram | Closed loop |
| Four parallel columns | MECE classification |
| Pyramid chart | Pyramid Principle (hierarchy) |
| Big-number page | The How much of 5W2H |
| Data comparison / bar chart | Comparative analysis |

---

## VIII. General Pitfall Checklist

| ❌ Common mistake | ✅ Correct approach |
|---|---|
| More than 5 key points on one page | Split the page, or distil to one point |
| Title is a noun phrase | Write the title as a conclusion sentence |
| Body text copies whole paragraphs from a document | Use the four-step method to cut and convert |
| Mixing 5 fonts | At most 2 font families |
| 6 colours on one page | ≤ 3 |
| Weak contrast (14pt vs 16pt) | Strong contrast (14pt vs 28pt) |
| Elements "roughly aligned" | Align precisely with guides |
| Everything centred | Try left alignment; it carries more force |
| Low-resolution images | Use a professional stock library, ≥150dpi |
| Fly-in animations all over the screen | Use a consistent fade, 0.3–0.5s |
| Pure-black text `#000000` | Use warm black `#1F1F1F`–`#3F403F` |
| Long passages centred | Left-align |
| Footer crammed with information | Keep only what is necessary |
| Forgot to embed fonts | Always embed before delivery |
| Parallel items not MECE | Choose a new classification dimension |
| SWOT lists without strategies | Add SO/WO/ST/WT |
| Funnel without values | Label each layer with volume and conversion rate |
