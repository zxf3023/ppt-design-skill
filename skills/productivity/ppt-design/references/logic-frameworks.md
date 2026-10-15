# Logic Frameworks in Detail

Three major logic tools that answer "how should content be organised, and how do you make a point hold up."

| Framework | Problem it solves | When to use |
|---|---|---|
| **Pyramid Principle** | How to build the overall structure | Outline stage |
| **MECE** | How to split parallel items | Before finalising any parallel layout |
| **SCQA** | How to make the opening compelling | Designing the preface and section transitions |

---

## 1. Pyramid Principle

### 1.1 Core idea

**Conclusion first, each level summarises the one below, group related items, order logically.**

People have limited attention, and they naturally prefer to take in the conclusion before looking for reasons. The pyramid structure works with that cognitive habit—give the answer first, then the support.

```
        ┌────────────────┐
        │Core conclusion │  ← one central idea
        └───────┬────────┘
     ┌───────────┼───────────┐
┌────┴─────┐┌────┴─────┐┌────┴─────┐
│Argument 1││Argument 2││Argument 3│  ← 3–7 supports
└────┬─────┘└────┬─────┘└────┬─────┘
┌────┴─────┐┌────┴─────┐┌────┴─────┐
│   Fact   ││   Fact   ││   Fact   │  ← concrete evidence
└──────────┘└──────────┘└──────────┘
```

### 1.2 The four basic principles

| Principle | Meaning | What happens if you break it |
|---|---|---|
| **Conclusion first** | Give the conclusion at each level before the reasons | The audience is halfway through and still doesn't know your point |
| **Each level summarises the one below** | An upper level must be a summary of the level beneath it | Titles and content drift apart; the logic breaks |
| **Group related items** | Items in the same group belong to the same logical category | Causes and symptoms get mixed together |
| **Order logically** | Items within a group follow a clear order | The audience can't find a reading order |

### 1.3 The three logical orders

| Order | Basis | Example | Use for |
|---|---|---|---|
| **Chronological** | By sequence of occurrence | Kick-off → R&D → Testing → Launch | Processes, steps, phases |
| **Structural** | By space / composition | HQ → Region → Store | Organisation, geography, system composition |
| **Order of importance** | By weight | Most critical → Next most → Ordinary | Arguments, problems, recommendations |

> **How to choose**: use chronological order to explain "how to do it"; structural order to explain "what it is made of"; order of importance to explain "which one matters most."

### 1.4 Deduction and induction

**Deductive reasoning**: from the general to the specific—a syllogism.

```
Major premise:   all customers need faster response
Minor premise:   we are a customer
Conclusion:      we need faster response
```

- Strength: rigorous logic, highly persuasive
- Weakness: the audience loses the thread when the chain gets long
- Use for: **argument, proposals, cases that need rigorous reasoning**

**Inductive reasoning**: from the specific to the general—facts converging.

```
Fact 1: response time in East China is 2 hours
Fact 2: response time in South China is 1.5 hours
Fact 3: response time in North China is 2.5 hours
Conclusion: national average response time is about 2 hours
```

- Strength: direct, easy to read, high information density
- Weakness: the conclusion is weaker than deduction
- Use for: **reporting, summaries, quick communication**

### 1.5 Putting it to work in a deck

| Deck element | Pyramid equivalent |
|---|---|
| Slide title | The conclusion (apex) |
| Slide body | 2–4 supporting arguments (the body of the pyramid) |
| Charts / data | Factual evidence (the base) |
| Overall section structure | The highest-level pyramid |

**In practice**:

1. Write one sentence that summarises the whole deck (the apex)
2. Break it into 3–5 sections (second level)
3. Break each section into 3–5 slides (third level)
4. Write every slide title as a conclusion sentence
5. Make each slide's content support that conclusion

### 1.6 The title test

**Read every slide title in sequence—together they should tell a complete story.**

If they don't read as a coherent whole, the pyramid structure has a problem—usually a failure to make "each level summarises the one below" work.

```
❌ Company profile → Technical capability → Service process → Customer cases
   (reads as scattered)

✅ 24 years in the industry, nationwide coverage → Five technology platforms covering every domain
   → Delivered in 5 working days, traceable online end to end → 3000+ customers served
   (reads as a complete narrative)
```

---

## 2. MECE

### 2.1 Definition

**Mutually Exclusive, Collectively Exhaustive** — no overlap, no gaps.

Source: a standard analysis tool from McKinsey, and the foundation of all structured thinking.

| Requirement | Test question |
|---|---|
| **Mutually exclusive (ME)** | Can any single item belong to two groups at once? |
| **Collectively exhaustive (CE)** | Is there any content with nowhere to go? |

### 2.2 Five ways to classify

#### Method 1: Dichotomy

The most basic approach: split something in two along a single dimension.

| Dimension | Split |
|---|---|
| Internal / external | Internal factors / external factors |
| Physical / virtual | Online channels / offline channels |
| Nature | Qualitative metrics / quantitative metrics |
| Time | Short term / long term |
| Own / other party | Our resources / their resources |

#### Method 2: Process

Split by the order in which the business happens.

```
Input → Processing → Output
Pre-sales → Sales → After-sales
Kick-off → R&D → Testing → Launch → Operations
```

#### Method 3: Elements

List the constituent elements. Common combinations:

| Scenario | Element combination |
|---|---|
| Corporate management | People / Finance / Materials / Information / Process |
| Marketing | Product / Price / Place / Promotion |
| Project | Scope / Time / Cost / Quality |
| System | Hardware / Software / Network / Data |

#### Method 4: Formula

Break it down with a mathematical formula—MECE by construction.

```
Profit = Revenue − Cost
  Revenue = Customers × Average order value × Repurchase rate
  Cost = Fixed cost + Variable cost
```

#### Method 5: Matrix

Cross two dimensions to form four quadrants.

```
              Internal        External
      ┌───────────┬───────────┐
Positive│ Strength  │Opportunity│
      ├───────────┼───────────┤
Negative│ Weakness  │  Threat   │
      └───────────┴───────────┘
```

### 2.3 Common mistakes side by side

| ❌ Not MECE | Problem | ✅ Fix |
|---|---|---|
| Strengthen management, improve efficiency, optimise processes, perfect the system | All four overlap | Systems / Processes / People / Technology |
| Technical problems, funding problems, talent problems, other problems | "Other" is a catch-all, so it isn't independent | Switch dimension: Resources / Capabilities / Mechanisms |
| Good product, good service, low price | The first two overlap (service is part of the product) | Product / Service / Price |
| Large customers, mid-sized customers, important customers | "Important" conflicts with the size dimension | By size: Large / Medium / Small; or by importance: Strategic / Key / Ordinary |

### 2.4 Applying it in a deck

**When to use**: anywhere "parallel items" appear.

| Deck scenario | MECE checkpoint |
|---|---|
| Dividing table-of-contents sections | Do the sections overlap? Is anything missing? |
| Several points on one slide | Are the points independent of each other? |
| Card layouts | Is every card at the same level? |
| Table header design | Are the columns mutually exclusive? |
| SWOT | Are internal/external and positive/negative clear? |

**Key constraint**: **2–4 parallel items is best**; more than 5 means you haven't found the right classification dimension and should switch dimensions and split again.

> ⚠️ **Use five- and six-item parallel layouts with caution**—it usually means the items should be reclassified, not forced into six cards.

---

## 3. SCQA Preface Structure

### 3.1 The four elements

The Pyramid Principle's standard structure for an opening.

| Element | English | Meaning | Function |
|---|---|---|---|
| **S** | Situation | Situation | Establish common ground, get the audience nodding |
| **C** | Complication | Complication | Create tension, draw attention |
| **Q** | Question | Question | Turn the complication into a question |
| **A** | Answer | Answer | Give the solution—this is the through-line of the deck |

**Inner logic**: S puts people at ease → C makes them tense → Q makes them curious → A satisfies them.

### 3.2 A complete example

> **S Situation**: The company's business now covers 20 provinces nationwide and serves more than 3000 customers.
>
> **C Complication**: But as the customer base has grown, average response time has risen from 1.5 hours to 2.8 hours, and customer satisfaction has fallen 12% year on year.
>
> **Q Question**: How can response time be brought back under 1.5 hours while the customer base keeps growing?
>
> **A Answer**: This proposal puts forward a two-pronged model: "regional service centres + intelligent dispatch."

**Note**: A is the core conclusion of the whole deck; every section that follows expands on it.

### 3.3 Four variants

| Variant | Order | Characteristic | Use for |
|---|---|---|---|
| **Standard** | S-C-Q-A | Complete, steady | Routine reporting |
| **Straight to the point** | A-S-C-Q | Conclusion first | Tight schedule, conclusion already clear |
| **Lead with concern** | C-S-Q-A | Open with the complication | When you need to attract attention and win resources |
| **Lead with confidence** | Q-S-C-A | Open with the question | When the plan is solid and you need to get to the point fast |

### 3.4 Laying it out in a deck

**Placement 1: slides 2–3, right after the cover**

```
Slide 1  Cover
Slide 2  S Situation  ← industry background / company status
Slide 3  C Complication  ← problem / challenge
Slide 4  Q Question  ← core question (can be merged into C)
Slide 5  A Answer  ← solution overview (= table of contents slide)
```

**Placement 2: section transition slides**

Each section can also open with a miniature SCQA:

```
What this chapter is about (A)
  ← why it is needed (C)
```

**Placement 3: a lead-in paragraph within a single slide**

Write a 2–3 line lead-in at the top of the slide that carries the S + C function, so readers enter the context before reading the content.

### 3.5 Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Only S, no C | Flat and tensionless | Add a "but" |
| C is too weak | "There are some shortcomings" | Quantify the complication with concrete numbers |
| A doesn't match Q | The question asks about efficiency, the answer talks about cost | Make sure Q and A correspond exactly |
| S is too long | The background runs three slides | Keep S within half a slide |

---

## 4. Using the three together

```
Step 1  SCQA for the opening     → make the audience want to keep listening
Step 2  Pyramid for the skeleton → make the content well organised
Step 3  MECE for parallel items  → make the classification hold up
```

**The complete workflow**:

```
1. Write the opening with SCQA (half a slide)
2. Write the core conclusion with the Pyramid Principle (one sentence)
3. Break the core conclusion into 3–5 supporting arguments (second level)
4. Check each argument with MECE
5. Break each argument into 3–5 slides (third level)
6. Write every slide title as a conclusion sentence
7. Run the title test
```
