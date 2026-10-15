# Theme Pack · Business Navy

> Best for: **general business reporting** — proposals, bids, results reports, project summaries, technical proposals
> Master source: 62-page enterprise proposal document (16:9, 10.00 × 5.625 in)
> Character: **steady deep blue + bright blue accents + generous white space**, the most general-purpose business blue system, not tied to any one industry

---

## Why this style works as a general base

Style profile from measurements across 62 pages:

| Dimension | Measured result |
|---|---|
| Primary text colour | `0C5FAC` (deep blue), 177 occurrences — this is its "signature colour" |
| Secondary text | `6C6C6C` (mid grey), 163 occurrences |
| Accent colours | `0066CC`(58) / `0070C0`(55) / `11A4FF`(25) |
| Background | `FFFFFF` pure white (93 fills) |
| Fonts | Microsoft YaHei (1714) + Microsoft YaHei UI (625) |
| Body text sizes | 12pt(702) / 11pt(604) / 14pt(490) |

**Structural trait**: single-page information density is medium-high (proposal-type documents), but colour is **restrained** — only one blue family plus grey steps, with hierarchy coming from lightness rather than hue. This is the safest and most professional route.

---

## Palette

### Primary palette

| Role | HEX | Use |
|---|---|---|
| **Primary blue (brand)** | `0C5FAC` | Page titles, section names, key words, large numbers |
| Bright blue (accent) | `0066CC` / `0070C0` | Emphasis, icons, decorative rules |
| Sky blue (light layer) | `11A4FF` / `0686F1` / `0478E2` | Secondary emphasis, gradients |
| Deep blue (heavy block) | `0C63B4` / `0944C9` | Large solid-colour backgrounds |
| Pale blue (underlay) | `9BDDFB` / `B3F4FF` | Card backgrounds, light areas |
| Primary text | `0C5FAC` (titles) / `000000` (body) | — |
| Secondary text | `6C6C6C` | Notes, captions, minor information |
| Dark grey | `333333` / `4B5563` | Long body copy |
| Divider | `D8D8D8` | Hairlines, borders |
| Background | `FFFFFF` | Page base |

### Hierarchy logic

```
Title             0C5FAC   deep blue     ← strongest visual weight
Body              #000000 / 333333      ← neutral, readable
Notes/captions    6C6C6C   mid grey      ← recedes into the background layer
Blocks/decor      0066CC   bright blue   ← structured information
Underlay          B3F4FF   pale blue     ← weakest container
```

> **Key technique**: build the entire hierarchy from **shades of blue**, never introducing a second hue.
> Orange (`ED7D31` / `FF6B00`) is used only when "emphasis" is needed — at most one instance per page.

---

## Fonts

| Use | Font | Notes |
|---|---|---|
| Chinese | **Microsoft YaHei** | Main body, 1700+ instances |
| Chinese fallback | Microsoft YaHei UI | Same family, UI-optimised |
| Numbers/Latin | **Times New Roman** or Roboto | Serif numbers read as more formal (proposal type) |
| Large heading numbers | Sans-serif bold | e.g. "3 million copies" |

> ⚠️ Avoid mixing in SimHei / DengXian / FangSong — this breaks consistency.
> **Standardise on Microsoft YaHei**, and use Times New Roman for numbers only.

---

## Type scale (measured)

| Use | Size |
|---|---|
| Cover main title | 40–54pt |
| Page title | 20–24pt |
| Key large numbers | 44pt |
| Number unit | 14pt (1/3 of the number) |
| Subheading | 16–22pt |
| **Body** | **12–14pt** |
| Secondary notes | 11pt |
| Captions | 9–10pt |
| Data cutoff/source | 8pt (grey) |

**Baseline = 12–14pt**, slightly smaller than Deep Blue Tech (because information density is higher).

---

## Page structure (standard skeleton for a proposal deck)

The chapter structure of this 62-page proposal can serve directly as a template for **any business proposal**:

```
Cover                                   1 page
Contents (3 chapters)                   1 page
─────────────────────────────
Chapter 1  Organisation                 10 pages
  ├ Overview / strength (large numbers)   ← use 5W2H What/How much
  ├ Development history (timeline)        ← use a timeline
  ├ Business results (data comparison)
  ├ Technical capability / industry sectors
  ├ National footprint (map page)
  ├ Talent structure (large numbers)
  ├ R&D (large number group)
  ├ Technology platforms (matrix)
  ├ Qualifications and honours (certificate wall)
  └ Quality control
─────────────────────────────
Chapter 2  Core capabilities            30 pages
  ├ Capability overview
  ├ Resource distribution
  ├ Qualification evidence
  ├ Capability by discipline (1 page each)  ← capability summary + technical advantages + client cases
  └ Extended services
─────────────────────────────
Chapter 3  Scenario-based services      10 pages
  ├ By industry/scenario (1 page each)
  └ Digital services
─────────────────────────────
Service process and model               1 page
Acknowledgements                        1 page
```

### The three-chapter formula

| Chapter | Question it answers | Share of pages |
|---|---|---|
| **Ch.1 Who I am** | What gives you the right to do this? | 20% |
| **Ch.2 What I can do** | Your capability boundary and technical depth | 50% |
| **Ch.3 How I apply it to you** | Landing it in concrete scenarios | 25% |
| Closing | How we work together | 5% |

> This is the optimal structure for a bid/proposal, and the **order reviewers most want to see**: trust you first, understand you next, then want to use you.

---

## Layout patterns (distilled from measurements)

### Common header

| Element | Position | Notes |
|---|---|---|
| Page title "(1) Development history" | @(0.32, 0.03) | Top-left, 20–24pt, primary blue |
| Lead-in paragraph | @(0.16–0.30, 0.51–0.59), width 9.5in | 14pt, one paragraph summarising the page |
| Content area | y = 2.0–5.5 | Safe zone |

> **What sets this style apart**: the title sits in the **top-left** (not centred), and every page carries a one-sentence **lead-in paragraph**.
> The lead-in is the most worth learning from — it lets the audience read a sentence before entering the visuals, lowering the barrier to comprehension.

### Large-number page (strength showcase)

```
[Large number 44pt deep blue]  [unit 14pt]
[caption 11-12pt]

Example: 24 years      35            500,000 m²     3 million copies
         years in field  service bases  site area      annual output
```

Four numbers in a row, x ≈ 0.86 / 4.14 / 7.29 / 10.46, evenly spaced.

### Timeline page (development history)

- Baseline horizontal rule y ≈ 3.61
- Node circles **increase in size** (0.47 → 1.11in) to signal growth
- Each node: year (22pt) + event name (14pt) + description (11pt)
- A short rule `009DFF` 0.51×0.04 below each node as decoration

> The growing circles are the clever part — **shape size implies growth**, with no need for words.

### Capability detail page (main layout of Chapter 2)

```
(2) Capability - Mechanics
┌────────────────┬──────────────────┐
│  Capability    │  Core technical  │
│  overview      │  advantages      │
│  · metric 1    │  · advantage 1   │
│  · metric 2    │  · advantage 2   │
└────────────────┴──────────────────┘
        Client cases (table / name wall)
```

Three fixed blocks: **capability overview** (let the numbers speak) + **core technical advantages** (differentiation) + **client cases** (credibility).
Every page has an identical form → this is a textbook application of the "repetition principle".

### Scenario service page (main layout of Chapter 3)

```
(1) Scenario for a given industry
[lead-in paragraph]
┌────────┬────────┬────────┐
│ Cat. 1 │ Cat. 2 │ Cat. 3 │
│ · item │ · item │ · item │
└────────┴────────┴────────┘
```

Three card columns, each = category name + 3–5 concrete items.

---

## Reusable sentence patterns (proposal copy templates)

| Scenario | Pattern |
|---|---|
| Organisation overview | "XX was founded in YYYY, is ..., has grown into ..., the first in ... to ..." |
| Capability overview | "Equipped with advanced A, B, C and other equipment, we can provide end-to-end ... services" |
| Capability strengths | "Broad scope: ... | High precision: ... | Full coverage: ..." (three parallel clauses) |
| Client cases | "XX Company XX Project" — list the names directly, no description |
| Digitalisation | "From X to Y to Z, threading A, B and C through every step of the service" |
| Service commitment | "Completed same day | B issued within 5 working days" |

**Data note**: put "Data as of D MMM YYYY" in a page corner, 8pt grey.

---

## When to use it

| Scenario | Suitable for this theme? |
|---|---|
| State-owned / public institution reporting | ✅ Very suitable (steady, formal) |
| Technical proposals / bids | ✅ Very suitable |
| Project close-out / results reporting | ✅ Suitable |
| Government project applications | ✅ Suitable |
| Internet / creative pitches | ⚠️ Too conservative; add white space and larger type |
| Product launch | ❌ Use the minimal, high-whitespace style instead |

---

## Relationship to the general guidelines

This theme pack is **one concrete implementation of the general guidelines**. In use:
- Palette, fonts, type scale, header layout → **follow this theme pack**
- Logical framework, visual theory, structural models → **follow the main SKILL.md**
- If the two conflict, the theme pack wins (specific scenario rules > general advice)
