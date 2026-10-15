# Visual Theories in Detail

Three visual tools that answer "how should the page be laid out, and how does the eye read it".

| Theory | Problem it solves | When to use |
|---|---|---|
| **Gestalt principles** | How elements are grouped | Content organisation on every page |
| **Rule of thirds** | Where elements go | Page layout planning |
| **Hick's Law** | How many elements to keep | Content triage and trimming |

---

## 1. Gestalt Principles

### 1.1 The Basic Idea

**Core proposition**: the eye does not see isolated elements — it sees **a meaningful whole**.

> "The whole is other than the sum of the parts." — Kurt Koffka

The brain automatically organises scattered visual information into structured patterns rather than processing it item by item. The designer's job is to **exploit this automatic organisation so that the audience grasps grouping and hierarchy without conscious effort**.

**Historical background**: Gestalt psychology originated in Germany in the early 20th century and is one of the cornerstones of cognitive psychology. Its laws of visual organisation are widely applied in graphic design, UI design, and data visualisation.

### 1.2 Seven Key Laws

#### Law 1: Proximity

**Definition**: elements that sit close together are seen as one group.

**This is the single most important law in layout** — it directly determines whether the audience can read the content's grouping.

```
❌ Even spacing, grouping unclear    ✅ Tight within a group, loose between groups

  Title                              Title
  Body                               ────
  Subtitle                           Body body
  Body                               Body body

                                     Title two
                                     ────
                                     Body body
```

**PPT applications**:

| Scenario | Practice |
|---|---|
| Title and body | Keep the title tight to its body; leave a large gap above |
| Caption and image | Caption 5–8px from the image; large gap from everything else |
| Inside a card | Elements inside a card sit close; cards sit far apart |
| List items | Spacing within an item < spacing between items |

> 💡 **Key technique**: sometimes you don't need to pull related elements "closer" — you only need to push unrelated elements "further away".
> Three blocks of information are better served by 10px within a group and 40px between groups than by 20px everywhere — **the audience reads the grouping from the spacing difference even with no divider lines**.

#### Law 2: Similarity

**Definition**: elements that look alike are taken to be the same kind.

**This is the psychological basis of the "Repetition" principle.**

| Dimension of similarity | Application |
|---|---|
| Same colour | All headings of the same kind share one colour |
| Same size | Text at the same level uses the same size |
| Same shape | Cards of the same kind share one shape |
| Same icon style | All line icons or all filled icons |

> ⚠️ **Counterexample**: two cards at the same level, one rounded and one square, make the audience assume they sit at different levels.

#### Law 3: Closure

**Definition**: the brain automatically completes incomplete shapes.

**Application**: suggest grouping with an incomplete border or colour block to lighten the visual load.

```
┌                    ┐
   Content area (corner missing)
└                    ┘
```

Lighter than a full rectangle, yet it still says "this is one region".

**Note**: closure only suits **weak grouping**. If you need strong grouping, use a complete boundary.

#### Law 4: Continuity

**Definition**: elements arranged along a line or curve are seen as one group, and the eye follows the line.

**Applications**:
- Use alignment lines to lead the eye
- Use flow arrows to express order
- Nodes on a timeline read as one sequence because they lie along a straight line

```
① ──── ② ──── ③ ──── ④
(arranged along a line → the audience reads it automatically as a sequential flow)
```

#### Law 5: Common Region

**Definition**: elements inside the same visual region are seen as one group.

**This is the theoretical basis of card-based design.**

**Application**: adding a light backing or a rounded rectangle expresses "these belong together" more effectively than drawing a divider line.

| Grouping device | Strength | Suited to |
|---|---|---|
| Increase spacing | Weak | Little content, clean page |
| Add a divider line | Medium | Ordinary grouping |
| **Add a backing colour block** | **Strong** | Grouping must be explicit |
| Add a full border | Strongest | Emphasising independence |

#### Law 6: Figure-Ground

**Definition**: vision automatically separates the "figure" (foreground) from the "ground" (background).

**Applications**:
- Use contrast to lift the focus forward and push decoration back
- Dark background + white text makes the text the figure
- Light grey backing + dark text makes the colour block the ground

> ⚠️ **Common mistake**: a background pattern so loud it steals attention from the figure. The background always serves the figure.

#### Law 7: Common Fate

**Definition**: elements that move together are seen as one group.

**Application**: animate elements of one group in and out together. This is the theoretical basis of animation design — **animation is not for showing off; it expresses grouping and order**.

### 1.3 Seven Laws Quick Reference

| What you want to say | Which law to use | How |
|---|---|---|
| These belong together | Proximity + common region | Move closer + add a backing |
| These are the same level | Similarity | Make the specs uniform |
| This is the focus | Figure-ground | Separate it with contrast |
| The reading order is A→B→C | Continuity | Alignment + arrows |
| This is one region | Closure | Border with a missing corner |
| These move together | Common fate | Synchronised animation |

### 1.4 Mapping to the CRAP Principles

| CRAP | Gestalt root |
|---|---|
| Contrast | Figure-ground |
| Repetition | Similarity |
| Alignment | Continuity |
| Proximity | Proximity |

**CRAP is the operational rulebook; Gestalt is the cognitive principle behind it.**

---

## 2. Rule of Thirds and Composition

### 2.1 Rule of Thirds

**Definition**: divide the frame with two horizontal and two vertical lines into a 3×3 grid; **the four intersection points are the best visual focal points**.

```
┌──────┬──────┬──────┐
│      │      │      │
│  ●   │      │   ●  │  ← four intersections = visual focal points
├──────┼──────┼──────┤
│      │      │      │
├──────┼──────┼──────┤
│  ●   │      │   ●  │
│      │      │      │
└──────┴──────┴──────┘
```

**Why it works**: a perfectly symmetrical composition (subject dead centre) reads as static and dull. Placing the subject near a thirds intersection creates tension and movement, which feels more comfortable to the eye.

### 2.2 Concrete PPT Applications

#### Image and text side by side

```
┌────────┬─────────────────┐
│        │                 │
│ Image  │  Title + body   │
│  (1/3) │     (2/3)       │
│        │                 │
└────────┴─────────────────┘
     33%          67%
```

The image takes the left or right 1/3, the text the other 2/3. This is the most classic image-text layout.

#### Full-screen hero image page

```
┌──────────────────────────┐
│ ●                        │  ← title at the top-left intersection
│                          │
│                          │
│                    ●     │  ← subject at the bottom-right intersection
└──────────────────────────┘
```

#### Three-column layout

Three equal columns naturally form a vertical thirds split.

```
┌───────┬───────┬───────┐
│ Col 1 │ Col 2 │ Col 3 │
└───────┴───────┴───────┘
```

#### Top and bottom split

```
┌──────────────────────────┐
│      Title area (top 1/3) │
├──────────────────────────┤
│                          │
│   Content area (bottom 2/3)│
│                          │
└──────────────────────────┘
```

#### Visual focal point page

```
┌──────────────────────────┐
│  Explanatory text         │
│                          │
│        Core element       │  ← put big numbers / key info at the focal point
│                          │
│                    Footnote│
└──────────────────────────┘
```

### 2.3 Golden Ratio

**Ratio**: about **1 : 1.618** (roughly 0.618)

**Practical conversion**: split the page at **38% : 62%**.

Better than the rule of thirds for pages with more content that need a clear primary-secondary split. The rule of thirds is 33:67, the golden ratio is 38:62 — the latter is a subtler difference.

**No precise calculation needed** — just remember the two ideas "1/3 and 2/3" and "0.618".

### 2.4 Visual Centre of Gravity

The centre around which the page's "weight" is distributed.

| Principle | Explanation |
|---|---|
| **Position** | The centre of gravity should sit slightly above the middle (about 45%) or slightly left (matching the left-to-right reading habit) |
| **Sense of weight** | Dark > light, large > small, dense > sparse, complex > simple |
| **Balance** | Put heavy elements on the left; balance the right with whitespace or several light elements |

**Asymmetrical balance** is more lively and more modern than perfect symmetry.

### 2.5 Whitespace

**Whitespace is not waste — it lets the content breathe.**

| Area | Recommendation |
|---|---|
| Top, bottom, left, right margins | ≥ 5% of page width (16:9 ≈ 0.6in) |
| Content footprint | **No more than 70%** |
| Between elements | Leave gaps; avoid "hugging the edge" or "cramming together" |
| Whitespace across pages | Keep the margin spec consistent |

> 💡 **Rule of thumb**: if a page looks "full", it is definitely too full. Delete something, or split the page.

### 2.6 Common Composition Mistakes

| ❌ Mistake | Problem | ✅ Fix |
|---|---|---|
| Subject dead centre | Dull, no tension | Move it to a thirds intersection |
| Equal margins on all four sides | No rhythm | Split with 1/3 : 2/3 |
| Heavy left, empty right | Unbalanced | Add light elements on the right to balance |
| Elements hug the edge | Cramped | Leave a 5% margin |
| Content fills the whole page | Suffocating | Cut it to under 70% |
| Image centred with no connection | Disconnected from the text | Re-lay it out with the rule of thirds |

---

## 3. Hick's Law

### 3.1 The Law

**Hick's Law**

**Formula**: `T = a + b × log₂(n)`

| Variable | Meaning |
|---|---|
| T | Time required to decide |
| n | Number of options |
| a, b | Constants related to the task |

**Core conclusion**: **decision time grows with the logarithm of the number of options.**

### 3.2 What It Implies for PPT

**Key difference**: in a PPT, the audience **has no time to choose**.

Web or app users will spend 1–2 seconds weighing options, because their goal is to "choose". But a PPT audience's goal is to "understand" — if a page offers too many options, they can neither finish reading nor judge what matters, and the end result is that they **give up reading altogether**.

**So Hick's Law in PPT form reads: every extra element is one more chance to be ignored.**

### 3.3 Ceiling Table

| Element | Ceiling | Recommended | Rationale |
|---|---|---|---|
| Bullet points per page | 5 | **3** | More than 5 won't be remembered |
| Chapters in an agenda | 5 | **3–4** | More than 5 chapters should be merged |
| Lines in a chart | 3 | **2–3** | More than 3 lines can't be told apart |
| Pie slices | 5 | **3–4** | More than 5 slices are hard to compare |
| Colours per page | 3 | **2–3** | Colour is also an option |
| Side-by-side layout blocks | 5 | **3–4** | 6 blocks should be reclassified |
| Table columns | 7 | **4–5** | More than 7 columns needs horizontal scrolling |
| Number of charts (per page) | 3 | **1** | One page, one chart, one conclusion |
| Font families | 2 | **2** | Heading family + body family |

### 3.4 Three Ways to Reduce Load

#### Method 1: Cut options

The most direct route — delete what isn't needed.

**How**: work through the five-category "delete text" checklist (reasons, explanations, repetition, aids, preamble).

#### Method 2: Group and classify

Fold n options into 3 groups. The audience then chooses between 3 groups rather than between n items.

```
❌ 12 parallel bullet points
✅ 3 groups of 4 items each
   (cognitive load drops from 12 to 3)
```

**This answers Hick's Law and applies MECE at the same time.**

#### Method 3: Progressive disclosure

Reveal with stepped animation, introducing only one new option at each step.

**Note**: the point of animation is to **lower the instantaneous load**, not to show off. So it should be "fade out" or "appear", not "fly in" or "bounce".

### 3.5 Working with Gestalt

**The two theories solve opposite problems**:

| Theory | Role | Direction |
|---|---|---|
| **Gestalt** | Helps the audience **group**, reducing cognitive burden | Organise |
| **Hick's Law** | Limits the **count**, avoiding overload | Constrain |

**Using them together**:
1. First use Hick's Law to set the **ceiling** (this page gets at most 5 bullet points)
2. Then use Gestalt to **organise** those items well (group with proximity and common region)
3. Finally use the rule of thirds to **lay out** (place elements at visual focal points)

### 3.6 A Practical Check

**Three-second test**: show the PPT to someone who hasn't seen it for 3 seconds, then ask "what is this page saying?"

- They can state the point → load is acceptable
- They can't, or get it wrong → too many options or unclear hierarchy; simplify

---

## 4. How the Three Work Together

```
Hick's Law   decides "how many"    → subtract first
Gestalt      decides "how to group" → organise next
Rule of thirds decides "where"      → lay out last
```

**Standard workflow**:

```
1. What does this page say? (a one-sentence conclusion)
2. How many supporting points? (Hick's Law: ≤ 5, 3 recommended)
3. How are those points grouped? (Gestalt: proximity + common region)
4. Where do the elements go? (rule of thirds: visual focal points)
5. How do you lift the focus out? (Gestalt: figure-ground + CRAP contrast)
6. Verify with the squint test / three-second test
```

---

## 5. Other Fundamentals: CRAP

Four operational basics, covered in detail in `design-basics.md`. Their mapping to the Gestalt principles:

| CRAP | Gestalt root | One-line rule |
|---|---|---|
| **C**ontrast | Figure-ground | Either strong, or none at all |
| **R**epetition | Similarity | Variation within unity |
| **A**lignment | Continuity | Every element belongs somewhere |
| **P**roximity | Proximity | Related close, unrelated far |

> ⚠️ **Weak contrast is worse than no contrast**. 14pt vs 16pt is indecision; 14pt vs 28pt is contrast.
