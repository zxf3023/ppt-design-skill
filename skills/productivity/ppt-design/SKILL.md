---
name: ppt-design
description: "PPT design methodology plus an execution engine, producing editable native .pptx end to end. The methodology half answers \"how to think and how to lay out\": a logic layer (Pyramid Principle / MECE / SCQA), a visual layer (Gestalt / rule of thirds / Hick's law / CRAP), and a structure layer (5W2H / SWOT / funnel / timeline), plus type scale, whitespace, colour, wall-of-text handling, data pages and narrative pacing. The execution-engine half answers \"how to actually produce the file\": give it a topic, article, spoken script or outline and it generates a deck with conclusion-style titles, speaker notes and a consistent style; give it a plain .pptx plus one reference image and it swaps in a unified palette, master, layouts, icons and illustrations without changing a single word of the text. Use whenever the user asks to make, write, beautify, lay out, review or outline a deck or slides, a business report or proposal deck, or drops in a .pptx, article, outline or reference image. Ships fourteen style presets, an icon library and a five-dimension self-review chain; the image model is configurable and falls back to programmatic illustration when none is configured."
---

# PPT Design and Production (Methodology + Execution Engine)

**Core belief**: A PPT is not a document — it is a **visual aid**. The audience is here to listen to you speak, not to read your slides.

> "The presentation, the slides — all of it is nothing more than a vehicle for information, and a vehicle tends to be fastest when light and devoid of clutter."

Before making every page, ask: **this page covers only one thing — what is that thing?**

---

## How to Use This Skill

It has two parts: the methodology governs "how to think, how to arrange", and the execution engine governs "how to actually produce the file". You can use only the first half to make design decisions, or follow it all the way through to produce a `.pptx`.

| What you want to do | Where to look |
|---|---|
| Clarify how content should be organised and how arguments hold up | Chapters 1–3 · Logic layer, visual layer, structure layer |
| Set font sizes, whitespace, colour scheme, fonts | Chapter 4 · Hard numeric specifications |
| Handle a large block of text | Chapter 5 · Handling large blocks of text |
| Choose page types, write titles, build data pages | Chapter 6 · Page structure templates |
| Arrange narrative rhythm | Chapter 7 · Narrative rhythm |
| Use scripts to manipulate pptx | Chapter 8 · Manipulating PPT with Python |
| Check before delivery | Chapter 9 · Delivery checks |
| **Actually produce / beautify a .pptx file** | **Chapter 11 · Execution Engine** |

**Two paths**:

- **Design decisions only** (review, build an outline, set specifications, give advice) → read Chapters 1–10, no need to touch the scripts.
- **Produce an editable .pptx** → think it through per Chapters 1–7 first, then follow the execution engine in Chapter 11. The engine carries the complete generation and beautification workflow and does not repeat the methodology's content; the methodology's numeric specifications (Chapter 4) and checklists (Chapter 9) are exactly the standards the engine must follow.

---

## Theoretical Framework Overview

This methodology is built on three sets of long-validated theories, which respectively address "how to think", "how to draw" and "how to build":

| Layer | Framework | What it solves | Chapter |
|---|---|---|---|
| **Logic layer** | Pyramid Principle · MECE · SCQA | How content is organised, how arguments hold up | Chapter 1 |
| **Visual layer** | Gestalt · Rule of Thirds · Hick's Law | How the page is arranged, how the eye looks | Chapter 2 |
| **Structure layer** | 5W2H · SWOT · Funnel · Timeline | Which framework carries a specific page | Chapter 3 |

**Order of use**: first think it through with the logic layer → then choose the carrying form with the structure layer → finally land the arrangement with the visual layer.

# Chapter 1 · Logic Layer

## 1.1 Pyramid Principle

**Core**: conclusion first, each level summarises the one below, group like with like, advance logically.

### Four basic principles

| Principle | Meaning | Counter-example |
|---|---|---|
| **Conclusion first** | State the conclusion, then the reasons | Building up for ages before giving the point |
| **Each level summarises the one below** | The upper level generalises the lower level | Title does not match the content |
| **Group like with like** | Items in one group belong to the same logical category | Mixing causes and symptoms in one group |
| **Advance logically** | Items within a group follow a set order | Random piling up with no basis for order |

### Three logical orders

| Order | Applies to | Example |
|---|---|---|
| **Time order** | Processes, steps, phases | Initiation → R&D → testing → launch |
| **Structural order** | Space, composition, hierarchy | HQ → region → store |
| **Order of importance** | Ranked by weight | Most critical → next most critical → ordinary |

### Two modes of reasoning

| Mode | Logic | Applies to |
|---|---|---|
| **Deduction** | Major premise → minor premise → conclusion | Persuasion, argument, rigorous reasoning |
| **Induction** | Several like facts → common conclusion | Reporting, summarising, quick expression |

> **Advice for PPT**: **use induction for reporting** (fast, easy to read), **use deduction for argument** (strong, credible).

### Landing it on PPT

```
Page title   = the conclusion (top of the pyramid)
Page content = the 2–4 arguments that support the conclusion (body of the pyramid)
Argument detail = data / cases (base of the pyramid)
```

**Title test**: read every page title in sequence — together they should be the complete storyline. This is the direct application of the Pyramid Principle's "conclusion first" to PPT.

### Opening structure: SCQA

The Pyramid Principle's standard structure for an opening, **in four steps**:

| Element | Meaning | Example |
|---|---|---|
| **S**ituation | A fact both sides accept | "The company's business already covers 20 provinces" |
| **C**omplication | What change or problem has appeared | "But customer response speed is 30% below the industry average" |
| **Q**uestion | What therefore needs to be solved | "How do we speed up without adding headcount?" |
| **A**nswer | Your proposal (= the main line of the whole deck) | "Build a regional service-centre network" |

**Variants**:

| Variant | Order | Applies to |
|---|---|---|
| Standard | S-C-Q-A | Routine reporting |
| Straight to the point | A-S-C-Q | Tight on time, conclusion is clear |
| Highlight the worry | C-S-Q-A | Need to draw attention |
| Highlight confidence | Q-S-C-A | The proposal is a sure bet |

---

## 1.2 MECE Principle

**Mutually Exclusive, Collectively Exhaustive** — no overlaps, no gaps.

### Two requirements

| Requirement | Meaning | Test |
|---|---|---|
| **Mutually Exclusive (ME)** | Groups do not overlap | Can any item belong to two groups at once? |
| **Collectively Exhaustive (CE)** | Together they cover everything | Is there any item with nowhere to go? |

### Five common dimensions for grouping

| Dimension | Example |
|---|---|
| **Dichotomy** | Internal / external; online / offline; qualitative / quantitative |
| **Process** | Pre-sales / during sales / after sales; input / processing / output |
| **Elements** | People / money / materials / information / process |
| **Formula** | Profit = revenue − cost; break it down term by term |
| **Matrix** | Important / urgent; internal / external × positive / negative |

### Landing it on PPT

- Parallel items on a page **must pass the MECE test** before you lay them out
- The number of parallel items should be **2–4**; more than 5 means you have not found the right grouping dimension
- Be cautious with five- or six-column parallel layouts — they probably need to be split again

> ⚠️ **Common mistake**: "Strengthen management, improve efficiency, optimise processes, perfect systems" — these four overlap with one another and fail MECE.
> The right approach: switch to a non-overlapping dimension, such as "systems / processes / people / IT".

---

## 1.3 Logic Layer Checklist

- [ ] Every page title is a **conclusion**, not a topic
- [ ] Titles read in sequence form a complete storyline
- [ ] Arguments support the conclusion (each level summarises the one below)
- [ ] Parallel items pass the MECE test (no overlap, no gaps)
- [ ] Items within a group follow a clear order (time / structure / importance)
- [ ] The opening uses the SCQA structure

---

# Chapter 2 · Visual Layer

## 2.1 Gestalt Principles

**Core**: the human eye tends to organise visual elements into meaningful wholes, not into a collection of separate fragments.

### Seven key laws and their PPT application

| Law | Meaning | PPT application |
|---|---|---|
| **Proximity** | Elements close together are seen as one group | Related captions, titles and body text should sit close together |
| **Similarity** | Similar elements are seen as the same kind | Same-level content uses the same colour, size and shape |
| **Closure** | The brain completes an incomplete figure | An incomplete border can imply grouping and reduce visual load |
| **Continuity** | Elements arranged along a line or curve are seen as one group | Use alignment lines and flow arrows to guide the eye |
| **Common Region** | Elements inside one region are seen as one group | Wrap related content in a background colour block |
| **Figure-Ground** | Vision automatically separates foreground from background | Use contrast to float the key point and push decoration back |
| **Common Fate** | Elements that move together are seen as one group | Animate a group of elements to enter and leave together |

### The three most-used

**Proximity** is the first principle of layout — it directly determines whether the audience can see how content is grouped.

```
❌ Equal spacing        ✅ Tight within group, loose between groups
Title                   Title
Body                    ────
Subtitle                Body body
Body                    Body body

                        Title two
                        ────
                        Body body
```

**Similarity** is the psychological basis of the "repetition principle". Same-level elements must share the same specification, or the audience will mistake them for different categories.

**Common Region** is the basis of card-style design. Adding a light background panel expresses "this content belongs together" more effectively than drawing a divider line.

### Landing it on PPT

| What you want to say | Which law to use |
|---|---|
| This content is one group | Proximity (close together) + Common Region (background panel) |
| This content is the same level | Similarity (same specification) |
| This is the key point | Figure-Ground (pull apart with contrast) |
| Reading order is A→B→C | Continuity (alignment + arrows) |
| This is part of a whole | Closure (omit part of the border) |

---

## 2.2 Rule of Thirds and Composition

### Rule of Thirds

Divide the frame into a nine-square grid with **two horizontal and two vertical lines**; **the four intersection points are the best visual focal positions**.

```
┌──────┬──────┬──────┐
│      │      │      │
├──────┼──────┼──────┤
│      │      │      │
├──────┼──────┼──────┤
│      │      │      │
└──────┴──────┴──────┘
   ↑              ↑
Visual focus   Visual focus
```

**PPT application**:

| Scenario | Approach |
|---|---|
| Mixed image and text | Image takes the left 1/3 or right 1/3, text takes the other 2/3 |
| Full-screen image page | Title at the top-left intersection, main element at the bottom-right intersection |
| Three-column layout | Equal column widths, which naturally forms a vertical three-way split |
| Top/bottom split | Main content sits in the bottom 2/3, the top 1/3 is left for the title and whitespace |

> ⚠️ **Avoid placing the main element dead centre** — unless you are deliberately going for symmetry. Centring makes the page look stiff.

### Golden ratio (supplementary)

Ratio roughly **1:1.618**. A practical conversion: split the page **38% : 62%**.

It suits pages with more content that need a clear primary/secondary split better than the rule of thirds.

### Visual weight and whitespace

| Concept | Explanation |
|---|---|
| **Visual weight** | The centre of the page's distribution of "weight"; should sit slightly above centre or slightly left of centre (matching reading habits) |
| **Whitespace** | The content area should not exceed **70%** of the layout; keep a margin of ≥ 5% of the page width on all sides |
| **Breathing room** | Leave gaps between elements; avoid "touching the edge" or "crammed together" |

---

## 2.3 Hick's Law

**Core formula**: `T = a + b × log₂(n)`

**Decision time grows with the logarithm of the number of options.** The more options there are, the longer the audience needs to react — and in a PPT setting the audience has no time to "make a choice" at all; they simply give up reading.

### Direct guidance for PPT

| Element | Upper limit | Reason |
|---|---|---|
| Bullet points per page | **≤ 5** (3 recommended) | Beyond 5, the audience neither remembers nor wants to read |
| Agenda chapters | **3–5 chapters** | Beyond 5, consider merging |
| Data series in a chart | **≤ 3 lines / 5 pie slices** | Beyond that, change the chart type or split the chart |
| Colours per page | **≤ 3** | Colour is also a kind of "option" |
| Columns in a parallel layout | **≤ 5** | Five is the ceiling; six means it should be reclassified |
| Columns in a table | **≤ 7** | Beyond that, split the table or turn it into a chart |

### Three ways to reduce load

| Method | Approach |
|---|---|
| **Reduce options** | Delete unnecessary content (run the four-step "delete text" method) |
| **Group and categorise** | Collapse n options into 3 groups, so the audience only chooses among 3 |
| **Progressive disclosure** | Reveal step by step with animation, one new option per step |

> **In one line**: **the audience's cognitive bandwidth is limited; every extra option you give them is one more chance they give up.**

---

## 2.4 Visual Layer Design Principles (CRAP)

Four operational fundamentals, which corroborate the Gestalt principles:

| Principle | One-line rule | Corresponding Gestalt law | Test |
|---|---|---|---|
| **C**ontrast | **Either strong, or none at all** | Figure-Ground | Squint — can you still tell the levels apart? |
| **R**epetition | Seek variation within unity | Similarity | Do same-kind elements share the same specification? |
| **A**lignment | Every element belongs somewhere | Continuity | Can every element find an alignment line? |
| **P**roximity | Related content close, unrelated far | Proximity | Can you read the grouping from the spacing alone? |

> ⚠️ **Weak contrast is worse than no contrast**. 14pt vs 16pt is indecision; 14pt vs 28pt is contrast.

### Four dimensions of contrast

| Dimension | Approach |
|---|---|
| **Size** | Main title 40pt / subtitle 24pt / body 14pt |
| **Colour** | White text on a dark ground; a warm block inside cool tones |
| **Shape** | Introduce a circle among many squares to create a focal point |
| **Lightness** | Separate levels with light and dark shades of the same hue |

---

## 2.5 Visual Layer Checklist

- [ ] Is related content close together (proximity)?
- [ ] Do same-level elements share the same specification (similarity)?
- [ ] Do groupings use a background panel or region (common region)?
- [ ] Does the key point float up through contrast (figure-ground)?
- [ ] Does the main element avoid dead centre (rule of thirds)?
- [ ] Bullet points per page ≤ 5 (Hick's Law)?
- [ ] Colours per page ≤ 3 (Hick's Law)?
- [ ] Does content occupy ≤ 70% of the layout, with whitespace around it?
- [ ] Is the contrast strong enough (avoiding weak contrast)?

---

# Chapter 3 · Structure Layer

Four classic structural frameworks, used to carry different kinds of page content. **Choosing the wrong framework is more fatal than ugly layout.**

## 3.1 5W2H — Describe One Thing Completely

**Use**: proposal statements, problem definition, plan making, project explanation.

| Element | Question | PPT application |
|---|---|---|
| **What** | What is it / what to do | Proposal content, goal definition |
| **Why** | Why do it | Background, necessity, value |
| **Who** | Who does it / for whom | Team, owners, target audience |
| **When** | When | Milestones, cycle |
| **Where** | Where | Region, scenario, channel |
| **How** | How to do it | Method, path, technical approach |
| **How much** | How much cost / how much volume | Budget, resources, metrics |

**Landing it on PPT**: you do not have to use all seven; choose by scenario.

| Scenario | Required elements |
|---|---|
| Project initiation | Why + What + How + How much |
| Execution plan | What + Who + When + How |
| Problem analysis | What + Why + Where + How |
| Product introduction | What + Who + Where + How much |

> **Test**: if a page cannot make clear "what to do, why, and how", the information is not yet complete.

## 3.2 SWOT — Strategic Positioning Analysis

**Use**: competitive analysis, strategic choice, evaluating the pros and cons of a proposal.

```
┌──────────────────────┬──────────────────────┐
│   S Strengths        │   W Weaknesses       │
│   Internal · Positive│   Internal · Negative│
├──────────────────────┼──────────────────────┤
│   O Opportunities    │   T Threats          │
│   External · Positive│   External · Negative│
└──────────────────────┴──────────────────────┘
```

**Key: SWOT is not four parallel items; it is the pairwise combinations that produce strategy.**

| Combination | Strategy type | Meaning |
|---|---|---|
| **SO** | Growth | Use strengths to seize opportunities |
| **WO** | Turnaround | Fix weaknesses to seize opportunities |
| **ST** | Diversification | Use strengths to avoid threats |
| **WT** | Defensive | Reduce weaknesses and avoid threats |

> ⚠️ **The most common mistake**: listing only the four S/W/O/T items without giving a strategic conclusion. **The value of SWOT lies in the combinations, not the listing.**

## 3.3 Funnel — Conversion and Filtering

**Use**: conversion analysis, filtering processes, service tiers, marketing chains.

```
    ████████████      Entry / Total
     ██████████       Filter
      ████████        Convert
       ██████         Close
        ████          Retain
```

**Two ways to use it**:

| Type | Meaning | Example |
|---|---|---|
| **Filtering** | Narrow down layer by layer; the survivors win | Recruitment funnel, quality screening |
| **Conversion** | Attrition layer by layer; focus on conversion rate | Marketing funnel, sales funnel |

**PPT essentials**:
- Each layer **must be labelled with a number or ratio**, otherwise the funnel is meaningless
- Keep the number of layers to **3–5**
- Highlight **the layer with the worst attrition** (usually the focus for improvement)

## 3.4 Timeline — Evolution and Planning

**Use**: development history, project scheduling, roadmaps.

**Four forms**:

| Form | Applies to | Characteristics |
|---|---|---|
| **Horizontal linear axis** | Milestone display | Most common; 3–7 nodes |
| **Vertical timeline** | More content | Each node can carry a detailed explanation |
| **Gantt chart** | Project scheduling | Can express task parallelism and duration |
| **Stepped axis** | Emphasising phase-by-phase leaps | Uses height differences to express growth |

**Advanced technique**: make the node graphics **grow in size** to imply growth, with no need for text.

**PPT essentials**:
- Time points **≤ 7** (Hick's Law)
- **Clear time scale** must be labelled
- Distinguish "done / planned" with dashed lines or light colour for future nodes

---

## 3.5 Structure Selection Decision Tree

```
What does this page need to say?
├─ Describe one thing fully    → 5W2H
├─ Strategy / competition      → SWOT
├─ Conversion / filtering      → Funnel
├─ Time evolution / planning   → Timeline
├─ One point / a quote         → Single text block / full-screen image
├─ 2–4 parallel points         → MECE grouping + parallel layout
├─ Process / steps             → Progressive logic diagram (one-way)
├─ Closed loop                 → Cyclic logic diagram
├─ Data comparison             → Comparison layout / bar chart
├─ Trend                       → Line chart
├─ Composition                 → Pie / donut chart (≤5 slices)
└─ Hierarchy                   → Architecture diagram / pyramid diagram
```

---

# Chapter 4 · Hard Numeric Specifications

## 4.1 Type Scale (16:9, canvas 13.333 × 7.5in)

| Level | Size | Use |
|---|---|---|
| Cover main title | 40–54pt | Only on the cover |
| Section big number | 60–72pt | Transition pages |
| Page main title | 28–40pt | Top of every page |
| Second-level subheading | 18–24pt | Card titles |
| **Body** | **14–18pt** | Baseline 16pt |
| Caption / source | 10–12pt | Never below 10pt |

**The scale ratio must be ≥ 1.5×** to form a clear hierarchy: 40 → 24 → 16 ✅ / 18 → 16 → 14 ❌

> For projection settings (large auditorium), body text is no smaller than 18pt; for laptop reading, 14–16pt is fine.

### Traps when mixing type sizes

- **Mixed Chinese and English**: Chinese characters need to be one step larger than the English to look balanced. When English is 14pt, Chinese at 15–16pt is more harmonious.
- **All-caps English**: visually grows by about 10%, so go 1–2pt smaller than expected.
- **Numbers**: numbers on the same data page must share the same size and weight, otherwise they will be read as different magnitudes.

## 4.2 Whitespace

| Area | Recommendation |
|---|---|
| Top/bottom/left/right margins | ≥ 5% of page width (16:9 ≈ 0.6in) |
| Content share of layout | **No more than 70%** |
| Words per page | Chinese ≤ 100 characters |
| One assertion per page | Write the title as a **conclusion sentence** |

## 4.3 Colour

| Rule | Value |
|---|---|
| Colours per page | **≤ 3** (excluding black, white and grey) |
| Share of the primary colour | 60% |
| Secondary colour | 30% |
| Accent colour | **10%, used for the single most important spot only** |
| Body-to-background contrast | ≥ 4.5:1 |
| Contrast for auditorium projection | ≥ 7:1 |

**Three-colour method**: primary colour (brand) + neutral greys (60% of information) + one accent colour.

> For text on a dark background use `#FFFFFF` or 90% white; never put dark grey text on a solid colour block.

## 4.4 Fonts

| Use | Recommendation |
|---|---|
| Chinese headings | Source Han Sans Heavy / Microsoft YaHei Bold / PingFang Semibold |
| Chinese body | Source Han Sans Regular / Microsoft YaHei / PingFang |
| English headings | Arial Black / Helvetica Neue Bold / Inter Bold |
| English body | Arial / Helvetica / Inter / Roboto |
| Numbers | DIN / Roboto Mono (monospaced, easier to align) |

**Iron rule**: one deck uses **at most 2 font families**. More fonts means more amateur.
**Fonts must be embedded before delivery**. Chinese fonts not embedded = guaranteed mess on another computer.

---

# Chapter 5 · Handling Walls of Text

## 5.1 The Four-Step Method

| Step | Action | Key point |
|---|---|---|
| **01 Split into blocks** | Cut by meaning | Find the "general → specific" structure |
| **02 Layer it** | Sort out the logical relationships | Test the grouping with MECE |
| **03 Delete text** | Boldly cut five kinds | **Causes, explanations, repetitions, supporting detail, build-up** |
| **04 Convert the form** | Text → visual | See the order below |

### The five-item list of text to delete

- **Causes**: "because…", "due to…" — fill these in verbally when speaking
- **Explanations**: supplementary notes on content already made clear
- **Repetitions**: saying the same thing in different words
- **Supporting detail**: detailed enumeration of data sources (move to an appendix)
- **Build-up**: "in order to better…", "with the development of…" — just give the conclusion

### The order for converting the form (follow it)

1. Distil the remaining text into keywords
2. Adjust the positional relationships of the text (grouping)
3. Add lines to make the logic clear
4. Add icons to lower the cost of understanding
5. Add colour blocks as a background to set off the text
6. **Delete the superfluous lines from step 3**
7. Shrink the body size to widen the gap from the title
8. Enlarge the main element and centre it; spread the body text to the sides

---

# Chapter 6 · Page Structure Templates

## 6.1 Universal Header

```
┌──────────────────────────────────────────┐
│ [Company name block]  [Section name]_____│ y≈0.45
│                                          │
│  Page title (conclusion sentence)        │ y≈1.0–1.9
│  ───                                     │
│                                          │
│              Content area (inside safe zone) │ y≈2.0–6.6
│                                          │
│ ────────────────────────── Footer decoration │ y≈7.1–7.4
└──────────────────────────────────────────┘
```

Safe zone: `x ∈ [0.6, 12.7]`, `y ∈ [1.8, 7.0]` (inches)

## 6.2 How to Write Titles

| ❌ Noun phrase | ✅ Conclusion sentence |
|---|---|
| Business results | 30% average annual compound growth over twenty-three years, from laboratory to listed group |
| Technical capability | Five major technology platforms support ten key laboratories |
| Service process | Certificate issued within 5 working days, trackable online throughout |

## 6.3 The Data-Page Trio

1. **Big number** (40–72pt, the only accent colour)
2. **Unit** (1/4 the size of the number, immediately after it)
3. **One-line interpretation** (14pt grey, explaining what the number means)

> A data page must label the **data cut-off date** and the **source**. 8–10pt grey in the corner.

## 6.4 Chart Selection

| What you want to express | Use | Do not use |
|---|---|---|
| Compare sizes | Horizontal bar chart | Pie chart |
| See a trend | Line chart | Column chart |
| See composition (≤5 items) | Pie / donut chart | Stacked columns |
| See composition (>5 items) | Stacked bar chart | Pie chart |
| See correlation | Scatter plot | Line chart |
| See progress | Gantt chart / progress bar | Pie chart |

**Chart subtraction**: delete gridlines → delete the legend (label directly beside the series) → delete the border → fade the axes → use data labels directly.
**One conclusion per chart**: there must be a conclusion sentence above or below every chart.

---

# Chapter 7 · Narrative Pacing

## 7.1 Three-Part Skeleton

```
Opening (10%)  Cover + agenda + SCQA opening
Body (80%)     3–5 chapters, each = transition page + 3–5 content pages
Closing (10%)  Summary / next steps / thanks
```

**Chapter transition pages are mandatory.** They give the audience the signal to "change channel".

## 7.2 Tension Curve

The structure of a good presentation **swings back and forth between "reality" and "ideal"**, gradually widening the tension, and finally settles on the "new normal".

```
Ideal  ╱╲    ╱╲    ╱╲  ← each swing grows in amplitude
      ╱  ╲  ╱  ╲  ╱  ╲
Reality ╱   ╲╱   ╲╱    ╲___ New normal
```

**Landing it on PPT**: give the "reality dilemma" first, then the "ideal picture", repeat a few times, and finally settle on the "new normal after adopting the proposal".

## 7.3 Pacing Inside a Chapter

Each chapter follows this order: **state the point → give the evidence → give the data → give the conclusion → transition to the next chapter**.

## 7.4 Scenario Adaptation

| Scenario | Body size | Words per page | Bullet points per page |
|---|---|---|---|
| Auditorium talk | ≥ 24pt | ≤ 50 characters | ≤ 3 |
| Laptop / video conference | 14–18pt | ≤ 100 characters | ≤ 5 |
| Email / printed reading | 12–14pt | Can be more | Must be readable standalone |

> ⚠️ **Do not make one piece of content serve both purposes**. Make the reading version first (complete information), then cut it down into the speaking version.

---

# Chapter 8 · Working with PPT in Python

## 8.1 Environment

```bash
PY="C:/Users/zxf30/.workbuddy-ai/binaries/python/envs/default/Scripts/python.exe"
```

```python
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # prevent mojibake on Windows

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor

p = Presentation("template.pptx")
print(len(p.slides), p.slide_width/914400, p.slide_height/914400)
```

## 8.2 Setting Chinese Fonts (⚠️ The Most Common Pitfall)

**Verified by testing**: `run.font.name = "Microsoft YaHei"` **only** generates `<a:latin typeface="Microsoft YaHei"/>`.
Chinese is an East Asian font, so `<a:ea>` must be written **separately**, otherwise Chinese still falls back to the default font inside PowerPoint.

```python
from pptx.oxml.ns import qn

def set_font(run, name="Microsoft YaHei", size=None, bold=None, color=None):
    """Set all three of latin / ea / cs, or CJK text will not take effect"""
    run.font.name = name                              # → a:latin
    if size:  run.font.size = Pt(size)
    if bold is not None: run.font.bold = bold
    if color: run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()                     # Note: it is run._r, not run._element
    for tag in ('a:ea', 'a:cs'):                      # CJK / complex script
        el = rPr.find(qn(tag))
        if el is None:
            el = rPr.makeelement(qn(tag), {})
            rPr.append(el)
        el.set('typeface', name)
```

**The generated XML (correct)**:

```xml
<a:rPr sz="1600">
  <a:latin typeface="Microsoft YaHei"/>
  <a:ea  typeface="Microsoft YaHei"/>   <!-- critical: without this line CJK does not take effect -->
</a:rPr>
```

> ⚠️ Two pitfalls:
> 1. **Setting only `font.name` does not make Chinese take effect**; you must add `a:ea`
> 2. **The API is `run._r`**, not `run._element`

## 8.3 Other Key Points

| Pitfall | Solution |
|---|---|
| Cannot iterate over elements inside a grouped shape | Recurse: `if sh.shape_type == 6: walk(sh.shapes)` |
| Reading the master theme raises `no attribute 'element'` | Go through the zip: `zipfile.ZipFile(P).read('ppt/theme/theme1.xml')` |
| Copying a whole page is hard | Ctrl+D in PowerPoint, then batch-replace the text with a script |
| Changing the header page by page is tedious | Headers/footers live in **slideMaster / slideLayout**; change once for a global effect |
| Font size setting has no effect | It must be set on the **run**, not the paragraph |

## 8.4 Colour Reference

```python
TEXT_DARK = RGBColor(0x1F, 0x1F, 0x1F)   # body text (warm black, never pure black #000000)
```
> **Do not use pure black**: #000000 looks rigid on a projector. Use a warm black from `#1F1F1F`–`#3F403F`.

For the specific theme colour values see the `themes/` directory.

---

# Chapter 9 · Delivery Checks

## 9.1 Three Layers of Checks

### Logic layer
- [ ] Every page title is a conclusion sentence; read in sequence they form a storyline
- [ ] Every page says only one thing
- [ ] Parallel items pass the MECE test
- [ ] The opening has an SCQA structure

### Visual layer
- [ ] Grouping is distinguished by spacing (Gestalt proximity)
- [ ] Same-level elements share the same specification (similarity)
- [ ] The key point floats up through contrast
- [ ] Bullet points per page ≤ 5, colours ≤ 3 (Hick's Law)
- [ ] Type sizes fall on the scale, font families ≤ 2
- [ ] Content is inside the safe zone, with whitespace around it

### Delivery layer
- [ ] **Fonts are embedded** (Windows: File → Options → Save → Embed fonts in the file; macOS: Preferences → Save → Embed fonts in the file)
- [ ] Saved as a PDF backup
- [ ] No leftover placeholders
- [ ] File name is standardised (project name + date)

## 9.2 Three Quick Self-Checks

1. **Squint test**: squint at each page — is the hierarchy still clear?
2. **One-metre test**: print it out and look from a metre away; alignment problems will show themselves.
3. **Three-second test**: show it to someone who has not seen it for 3 seconds, then ask what they remember. If it matches your intent, it passes.

---

# Chapter 10 · Workflow Overview

**When you only want to think it through and not produce a file**, just follow steps 1 to 8:

```
1. Clarify the scenario    Auditorium talk / laptop reading / email sending? (determines font size and information density)
2. Build the logic skeleton    Organise content with Pyramid + MECE; design the opening with SCQA
3. Choose a structure framework    5W2H / SWOT / Funnel / Timeline —— choose by page content
4. Write the outline    Write titles as conclusive sentences, run the title test
5. Land the visuals    Gestalt grouping, Rule-of-Thirds composition, Hick's Law load control, CRAP refinement
6. Build page by page    One assertion per page; large text blocks use the four-step method; data uses the three-piece set
7. Unify the treatment    Unify the font-size ladder, colour scheme, card specifications
8. Delivery check    Run the Chapter 9 checklist; embed fonts; export PDF
```

**When you actually want to produce an editable `.pptx`**, after steps 1 to 4 hand it to the execution engine, which takes over the subsequent layout planning, asset generation, assembly and self-check:

```
1. Clarify the scenario    ┐
2. Build the logic skeleton    │ Handled by the methodology (Chapters 1–7)
3. Choose a structure framework    │
4. Write the outline    ┘
5. Hand to the execution engine    → Chapter 11: write deck.json, set the style, plan the layout
6. Generate assets and assemble    → pipeline.py runs it all in one command
7. Five-dimension self-review    → look at sheet.png, score per critique.md and fix the "must fix" items
8. Delivery    → out/*.pptx + overview sheet + score explanation
```

Both paths share the same set of design standards: the engine's layout library follows the font-size ladder and minimum whitespace of Chapter 4, and the pre-delivery self-check layers on the Chapter 9 checklist.

# Chapter 11 · Execution Engine

The methodology addresses "how to think, how to arrange"; this chapter addresses "how to actually produce the file". The two routes share one design engine: generation is "write the content then design it", beautification is "extract the content of the original then design it", and from layout planning onward they are exactly the same.

Three intermediate files thread through the whole flow; the scripts handle the deterministic work, and the model handles understanding the content and aesthetic judgement.

| File | Content | During beautification | During generation |
|---|---|---|---|
| `deck.json` | Each page's page type, title, key points, data, notes | Extracted from the original, text unchanged verbatim | Written per `references/generate.md` |
| `style.json` | Palette, fonts, corner radius, decoration, illustration style | Extracted from the reference image | Extracted from the reference image, or picked from the preset library |
| `plan.json` | Each page's layout, icons, illustrations and prompts | Drafted by `plan_deck.py`, revised by the model | Same as the left |

Below, `$S` refers to this skill's `scripts` directory, and `$W` refers to this run's working directory (e.g. `./ppt_work`). On Windows, replace `python3` with `python`.

## 11.1 Before You Start

1. **Determine the route**
   - The user gave a .pptx and wants it to look better → Route A beautification
   - What was given is a topic, article, spoken script, outline or other material, to be turned into a PPT → Route B generation
   - A .pptx was given but the content is to be rewritten and the structure adjusted → Route B, read the pptx as material
2. **Environment self-check**, which finishes within a second if it passed before, otherwise auto-installs missing dependencies. If the exit code is non-zero, tell the user the suggestion and stop; if only recommended components (such as LibreOffice) are missing you can continue, and the pipeline will switch to `render_lite.py` to draw an approximate preview directly from the layout data, so layout, colour scheme and overflow are still visible — state at delivery that the preview is an approximate image. To skip LibreOffice for speed you can also add `--lite`.
   ```bash
   python3 $S/setup_check.py --quick --install
   ```
3. **Image-generation status** `python3 $S/make_assets.py $W --status` — tell the user in one sentence which model is connected, or that procedural illustration will be used. For configuration see `references/imagegen_config.md`.
4. **Ask once** to clarify the choices the route needs, and use defaults for the rest. When the user says "just do it" or "no need to ask", or is not present, use all defaults and list the choices made at delivery.
5. **Fast mode**: when the user says "fast mode", "stop asking" or "in a hurry", skip the confirmation of the style card, outline and design specification; the five-dimension self-review fixes only one round of "must fix" items, and "nice-to-fix" items are written into the delivery notes without acting on them. For a deck of about 12 pages, normal is 15 to 25 minutes and fast mode is around 10 minutes; the bulk of the time goes into transcribing text and looking at images, while the scripts themselves take only a minute or two.
   - Beautification: strength light / standard / full (default full), whether to allow text refinement (default not allowed)
   - Generation: purpose, audience, duration, presence of a reference image, whether spoken notes are wanted; for defaults see `references/generate.md`

## 11.2 Route A Beautification

1. **Parse the original** `python3 $S/extract_deck.py original.pptx $W`, then look at `source_png/sheet.png`. The script repairs zips that LibreOffice cannot open, and can also read spoken notes hidden in the descr attribute.
2. **Read the reference image** `python3 $S/extract_style.py reference.png $W`, then look at the image yourself, write `$W/style.json` per `references/style_extraction.md`, then run `python3 $S/style_card.py $W` to produce a style card. If the user is present, send the style card for confirmation.
3. **Organise deck.json** — transcribe from `deck.draft.json` per `references/deck_schema.md`. Copy text verbatim, writing local bolding as `**fragment**`; rebuild text inside images as native structures such as `diagram`; carry `notes` over as-is; write the `meta.anchor` visual anchor. Small labels on the original pages (section tape like "01 · Overview") go into that page's `kicker`, and numbering carried by an item (01, 02) goes into the item's `num`, so that no characters are lost when switching to any list bullet. Formulas typed with the equation editor in the original are automatically converted to plain-text formulas during parsing (e.g. V′(x) = (a−2x)(a−6x)) and transcribed verbatim as usual; use the `explain` page type for explanation pages with many formulas. SVG images are also converted to a PNG copy along the way (the png field in raw.json), and the layout uses the PNG. Small images such as logos and "AI generated" badges go into `stamps` and are kept as-is. Software screenshots in the original (images under `media/`) use the `screenshot` or `screenshots` page type; screenshots are placed into a unified window frame, and annotation points can be placed on the screenshot with `at`.
4. Then follow "Layout, Asset Generation and Checks" below.

## 11.3 Route B Generation

Before starting, read `references/generate.md`, which contains all the rules for story line, conclusive titles, density, spoken notes and page-type selection.

1. **Analyse the material** `python3 $S/analyze_source.py $W --file article.md` (if there is only a topic use `--topic "…"`, and you may add `--minutes 3`). When there is only a topic or facts need supplementing, search to verify first, and do not write what cannot be found.
2. **Write deck.json**: define the story line first, then write page by page following "the shape of the content decides the page type" — write titles as conclusions, put keywords on screen, and put complete sentences in `notes`. For a deck with chapters, place a `toc` table of contents page after the cover (omitting items auto-lists the chapters); when too many card pages run in a row, insert a `question` big-question page or a `big_quote` big-quote page. When tool-tutorial material has screenshots, use `screenshot` for one image with a few operation points, and `screenshots` for several images showing a process. Besides the regular cards, steps and comparisons, there are also timeline, funnel, hub-and-spoke, 2x2 matrix, native tables, native charts and SWOT/PEST/Five Forces/Business Model Canvas; if unsure whether it fits, run `python3 $S/layout_info.py <layout-name>` to check capacity and examples.
3. **Check the outline** `python3 $S/outline_check.py $W`, fix it until there are no ERRORs, and send the "titles only" from outline.md to the user for confirmation.
4. **Set the style**: if there is a reference image, follow step 2 of Route A; if not, run `python3 $S/style_previews.py $W --auto` to produce three sample sheets (the user's own cover and content page), send `previews/sheet.png` for the user to choose, then `--apply <id>`. Presets are in `references/styles/`, fourteen sets in total, and each set's hard rules must be followed when laying out. For a meeting-room projection, write `"projection": true` in `meta`, and the minimum font size is raised.
5. Then follow "Layout, Asset Generation and Checks" below.

## 11.4 Layout, Asset Generation and Checks (Shared by Both Routes)

1. **Layout planning** `python3 $S/plan_deck.py $W --level full` (add `--sheets` when an image-generation model is available, cutting several small illustrations out of one large image, which is more consistent in style and cheaper).
   On a re-run, pages whose content has not changed keep their original plan (including hand-edited layouts and illustration prompts); to re-plan everything add `--reset`.
   Review plan.json: whether the layout fits the content (`references/layouts.md`), whether the icons convey the meaning (`references/icons.md`), whether the illustration prompts are specific (`references/image_prompts.md`). When content exceeds the layout's capacity the script automatically switches layouts and writes it into the "capacity reminders" of design_spec.md; handle these before generating assets.
   Send the generated design_spec.md to the user for confirmation before generating assets, since asset generation costs the most. Fast mode skips the confirmation.
2. **Asset generation, assembly, self-check** in one command:
   ```bash
   python3 $S/pipeline.py $W
   ```
   It runs make_assets (illustrations, backgrounds, decorations; AI prompts are first written to disk under `prompts/`), build_deck, render, qa_check, compare_sheet and review in sequence.

   | Check | Level | Handling |
   |---|---|---|
   | During beautification, original text is missing or altered; during generation, text from deck.json did not make it onto the page | ERROR | Fix against the original text or deck.json |
   | Text overflow, overlapping text boxes, text crossing the bottom line (pressing onto the capsule bar or footer) | ERROR | Switch layout, split the page, or place manually with the `free` layout |
   | More than 3 accent uses on one page, or accent area over 8% | WARN | Keep only one accent |
   | Text pressing on an illustration, insufficient contrast, out of bounds, body text too small | WARN | Judge by looking at the image; most need fixing |
   | Newly added header, page number, step number | INFO | Normal |

3. **Five-dimension self-review**: look at `out/sheet.png` and the per-page PNGs, cross-reference the evidence counted by the scripts in `out/review.md`, and per `references/critique.md` score consistency, hierarchy, detail, communication and rhythm each from 0 to 10, writing three lists: keep, must fix, nice-to-fix. The "must fix" items are fixed before delivery; after fixing, re-run only the affected steps, at most three rounds.

## 11.5 Delivery

- `out/beautified.pptx`; the file name uses `original-name_beautified.pptx` or `theme.pptx`
- Beautification attaches `out/compare.png` as a before/after comparison; generation attaches `out/sheet.png` as an overview sheet
- Report the five-dimension self-review scores and the weakest dimension in one sentence
- Explain in one or two sentences the style, the illustration source (which model or procedural illustration) and the fonts; for beautification state whether text was refined, and for generation state which content the user needs to verify further
- When the user has connected a local folder, write back to where the material is located

## 11.6 Hard Rules

General
1. All text is an editable text box; cards, capsule bars and dividers use native shapes; only backgrounds, illustrations, icons and brushes are images.
2. The reference image is used only to extract the style — never cropped or pasted into the PPT.
3. No text appears inside AI illustrations (graphical letters such as a product initial are the exception); prompts always carry negative constraints.
4. Procedural illustration is the fallback; state it truthfully at delivery and do not present it as AI-generated.
5. Do not modify the skill's own files while working on a deck. If you hit a problem with the skill, work around it to complete the delivery, then write the problem into the delivery notes and let the user decide whether to change the skill.

Beautification
6. By default, change no text; when the user allows refinement, list the changes one by one for the user to review.
7. The page order and page count match the original, and notes are kept.

Generation
8. Use only data and facts from the material or that have been verified, and mark them with `source`; if you cannot find it, do not write it — never invent numbers. If chart data is changed, rewrite the titles and insights conclusions accordingly.
9. Do the design only after the outline (titles only) is confirmed by the user; the same applies to the style and design specification, except in fast mode.

## 11.7 Partial Edits

- **Redo a single page**: change that page's `layout` and `icons` in plan.json, or edit `prompts/hero_NN.md`, then run `make_assets.py $W --only hero_NN --force` and `pipeline.py $W`
- **Switch style**: swap style.json (a reference image or `style_previews.py --apply`), regenerate illustrations with `--force`; deck.json and plan.json can be reused
- **Special page**: set that page's layout to `free` and write `elements` directly in plan (for the format see `references/layouts.md`)
- **Light beautification only**: `plan_deck.py $W --level light`, no illustrations

## 11.8 Common Problems

- `soffice` conversion fails: rendering only affects the preview, not the delivered file; first confirm that the `source.pptx` produced by `extract_deck.py` opens
- Preview fonts differ from the user's computer: the preview uses Source Han Sans in place of Microsoft YaHei, and the layout leaves margin — see `references/fonts.md`
- Image generation fails: it automatically switches to procedural illustration, the error is recorded in `assets/manifest.json`, and at delivery state which pages use fallback images

## 11.9 Execution Engine File Index

| Path | Purpose |
|---|---|
| `references/generate.md` | Complete rules for the generation route (must-read before generating) |
| `references/deck_schema.md` | deck.json fields and all page types |
| `references/critique.md` | Scoring rules and common fixes for the five-dimension self-review |
| `references/layouts.md` | Layout library, applicable scenarios, capacity, free-layout element format |
| `scripts/layout_info.py` | Check layout capacity and deck.json examples; `--check $W` checks page by page for over-capacity |
| `references/style_extraction.md` | Read style.json out of a reference image |
| `references/styles/` | Fourteen style presets (index.json + one json per set, containing hard rules and imagery tags); samples are in `assets/style_gallery.jpg` (row N corresponds to gallery_row in index.json) |
| `references/image_prompts.md` | Visual anchors and illustration prompts |
| `references/imagegen_config.md` | Image-generation interface configuration |
| `references/fonts.md` | Font selection and compatibility |
| `references/icons.md` | Built-in icon list |
| `INSTALL.md` / `install.sh` / `install.ps1` / `install.bat` | The execution engine's original installation instructions and scripts (used for standalone installation) |
| `config.example.json` | Image-generation configuration template |

# Reference Files

## Methodology (Chapters 1–10)

| File | Content |
|---|---|
| `references/logic-frameworks.md` | Detailed explanation and examples of the Pyramid Principle, MECE and SCQA |
| `references/visual-theories.md` | Detailed explanation of the seven Gestalt laws, Rule-of-Thirds composition and Hick's Law |
| `references/structure-models.md` | Detailed explanation and layout landing of 5W2H, SWOT, Funnel and Timeline |
| `references/layout-patterns.md` | 38 page layout patterns + decision tree + pitfall checklist |
| `references/design-basics.md` | The four CRAP principles, whitespace and contrast data |
| `references/checklist.md` | Complete delivery checklist and self-check methods |

## Execution Engine (Chapter 11)

| File | Content |
|---|---|
| `references/generate.md` | Complete rules for the generation route |
| `references/deck_schema.md` | deck.json fields and all page types |
| `references/layouts.md` | Layout library, capacity and free-layout format |
| `references/style_extraction.md` | Extract the style from a reference image |
| `references/critique.md` | Five-dimension self-review rules |
| `references/icons.md` | Built-in icon list |
| `references/image_prompts.md` | Visual anchors and illustration prompts |
| `references/imagegen_config.md` | Image-generation interface configuration |
| `references/fonts.md` | Font selection and compatibility |
| `scripts/*.py` | 23 execution scripts (parsing, planning, asset generation, assembly, checking, rendering) |
| `assets/` | Icon library, style samples, third-party licences |

## Themes and Styles

| Path | Content |
|---|---|
| `themes/*.md` | Methodology colour themes (human-readable design specifications, including colour values, font sizes and layout rules) |
| `references/styles/*.json` | The execution engine's fourteen style presets (machine format read by scripts) |

## Other

| Path | Content |
|---|---|
| `agents/openai.yaml` | Display name and default prompt |
| `INSTALL.md` / `install.sh` / `install.ps1` / `install.bat` | The execution engine's original installation instructions and scripts (used for standalone installation) |
| `config.example.json` | Image-generation configuration template |
| `LICENSE-luobo-ppt` | MIT licence for the execution engine part ((c) 2026 zhouluobo (Zhou Luobo)) |
