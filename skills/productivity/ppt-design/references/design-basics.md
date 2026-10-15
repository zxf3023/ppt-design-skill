# Design Fundamentals

The four hands-on basics (CRAP) + underlying design principles + general numeric references.

---

## 1. The Four CRAP Principles

**Origin**: Fundamental principles of graphic design introduced in 1994, helping non-professional designers quickly grasp core design thinking. They are the cornerstone of graphic and UI design.

### Cognitive Psychology Basis

The human brain has four basic preferences when processing visual information, and these are precisely the underlying logic of CRAP:

| Preference | Corresponding principle |
|---|---|
| Preference for **difference** — more sensitive to "different" | Contrast |
| Preference for **pattern** — likes repeated patterns, which are easier to process | Repetition |
| Preference for **order** — neat arrangement feels reassuring | Alignment |
| Preference for **grouping** — treats nearby elements as a whole | Proximity |

> CRAP is not an arbitrary dogma, but a summary of **the laws of human visual cognition**. When you organise elements according to these principles, the work naturally feels comfortable, clear, and professional.

### C — Contrast

**Core: make the differences between distinct elements as obvious as possible.**

Contrast not only creates a visual focus, but also establishes information hierarchy and guides readers to read in the order you intend.

| Type | Approach | PPT application |
|---|---|---|
| **Size** | Main title 36pt / subtitle 20pt / body 12pt | Hierarchy |
| **Colour** | Dark background + white text; a warm block within cool tones | Highlight key data |
| **Weight** | Titles Bold/Black, body Regular/Light | Layering even at the same size |
| **Shape** | Introduce circles/curves among square straight lines | Break monotony, create focus |
| **Texture** | Smooth vs rough, solid vs transparent | Add depth |

> ⚠️ **Emphasis: do not use weak contrast.**
>
> "Weak contrast is worse than no contrast, because it implies 'these two things are different' yet is not strong enough for the audience to clearly perceive that difference. The result is a layout that looks unprofessional and unsure of itself."
>
> **Rather than a 14pt vs 16pt contrast, go straight to 14pt vs 28pt.**

**Anti-pattern**: All text at 16pt, all dark grey, with no distinction between title and body → the audience doesn't know what to read first and perceives "a pile of text".
**Example**: Main title 48pt in brand colour + subtitle 20pt black bold + body 14pt dark grey + divider lines → the hierarchy is obvious at a glance.

### R — Repetition

**Core: repeatedly use certain visual elements throughout the design.**

Dimensions that can be repeated:

| Dimension | Approach |
|---|---|
| **Colour** | The primary colour runs through titles, buttons, icons, and footer accent lines |
| **Font** | Use 2–3 fonts per design (one for titles, one for body) |
| **Spacing** | Constant spacing between title and body, constant spacing between cards |
| **Icon style** | If you use line icons, don't mix in filled icons |
| **Decorative elements** | Small dots, divider lines, and background blocks recurring to create rhythm |

**Anti-pattern**: Page 1 of a brochure has a blue title, page 2 green, page 3 red; some images are rounded, some have shadows, some have nothing; every page has different spacing → it looks like a pile of unrelated designs thrown together.
**Example**: The whole document uses a unified brand colour, unified corner radius, unified margins, and strictly identical body text size → every page is "part of the same book".

> **Repetition does not mean sameness**: you can vary the size, position, or combination of repeated elements, but keep their basic characteristics unchanged.
> This "**variation within unity**" is the essence of the repetition principle.

### A — Alignment

**Core: every element on the page should have some visual alignment relationship with other elements.**

Alignment is the **simplest way** to make a layout look professional and organised. Even with only text, good alignment makes it look highly refined.

| Alignment | Applies to | Note |
|---|---|---|
| **Left** | Large amounts of body text (safest) | Both Chinese and English reading habits go left to right |
| **Right** | Signature, date, annotations, and other supporting information | Rare, but can create a distinctive effect |
| **Centre** | Titles, short text, formal occasions | ⚠️ **Avoid centring long blocks of text**; ragged line endings severely hurt readability |
| **Justified** | Newspapers and magazines | ⚠️ Use with caution on web/PPT; word spacing becomes uneven |

> **Key idea: no element is placed at random.**
> Even when two elements are far apart (a title at the top of the page and copyright information at the bottom), there should still be an alignment relationship.

**The most common beginner mistake**: centring everything. Centring is safe, but centring every element makes the layout dull and directionless.
**Try a strong left or right alignment and the design immediately becomes more powerful and modern.**

**Anti-pattern**: On a business card the company name sits slightly top-left, the phone at bottom-right, the email centre-left, and the QR code placed randomly at top-right → every element is "roughly in the right place", but there is no clear reference line.
**Example**: All text is strictly left-aligned, and the left edge of the QR code is equidistant from the right edge of the text → clean and crisp.

**Practical tip**: Turn on guides and the grid system to ensure every element has a "home".

### P — Proximity

**Core: related elements should be placed close together, unrelated elements should be kept apart.**

**Theoretical basis**: The Gestalt principle of proximity — when multiple elements are close to one another, people naturally perceive them as a single whole. Just as paragraph spacing is larger than line spacing, we know "this paragraph has ended".

| Application | Correct approach |
|---|---|
| Title and body | The title hugs its body text, with a large gap from the preceding body text |
| Image and caption | The caption sits 5–8px from the image, with a large gap from other content |
| Forms | Labels hug their input fields, with a large gap between form items |
| Cards | Elements inside a card stay close, cards stay far apart |

> 💡 **Important technique**: Sometimes you don't need to "pull related elements closer" — you only need to **"push unrelated elements farther away"**.
> For three groups of information, rather than spacing them all 20px apart, use 10px within groups and 40px between groups — **even without divider lines, the audience can understand the grouping through the difference in spacing**.

**Anti-pattern**: The event title, time, location, and registration button are all spaced 30px apart → the relationships between the information are completely lost.
**Example**: 8px within the title group, 40px between the title group and the details group, 10px within the details group, 50px between the details group and the button → the hierarchy is obvious at a glance: title group → details group → call to action.

### CRAP Checklist

| Principle | Check question | Passing standard |
|---|---|---|
| **Contrast C** | Are primary and secondary information clearly distinguishable? | **You can tell the hierarchy even when squinting** |
| **Repetition R** | Are fonts, colours, and spacing consistent? | All similar elements use the same specifications |
| **Alignment A** | Does every element have a clear alignment basis? | You can find an alignment guide line for every element |
| **Proximity P** | Are related items close and unrelated items far? | Information groups are clearly distinguishable by spacing |

---

## 2. Underlying Design Principles

Higher-level design values, applicable to the overall control of a whole presentation deck.

| Principle | Meaning | Applied to PPT |
|---|---|---|
| **Purpose** | Make something meaningful | Each page has one clear purpose; delete decoration that doesn't serve that purpose |
| **Simplicity** | Clear and direct, **not minimalism** | **Every element must earn its place** |
| **Craft** | Care about every detail | Align to the pixel, use a systematic type scale, keep spacing consistent |
| **Familiarity** | Build on what is known | Use layout conventions the audience knows; don't sacrifice readability for novelty |
| **Flexibility** | Adapt to different scenarios | Prepare two versions of the same content, detailed and condensed (speaker version / reading version) |
| **Agency** | Let people act freely | A reading-version PPT must be understandable on its own, without relying on the speaker |
| **Delight** | Give people a feeling | One restrained highlight beats a page full of effects. **Don't treat delight as decoration** |
| **Responsibility** | Be accountable to people | Data is truthful, sources are cited, no misleading; confidential content is not shared |

### Two Key Clarifications

**Simplicity ≠ Minimalism**

> The goal is "focused and useful": keep what matters close at hand and let the rest naturally recede.

It is not about emptying the page, but about **giving every retained element a sufficient reason**. A page with a lot of information isn't the problem — the problem is whether there is any filler.

**Delight ≠ Decoration**

> People are here to get something done; don't let the pursuit of delight get in the way of the core purpose.

One carefully designed highlight (an outstanding transition page, one great image) beats a page full of animated effects. **A restrained highlight is the real highlight.**

---

## 3. General Numeric References

### Contrast Standards (Accessibility Guidelines)

| Level | Contrast ratio | Use |
|---|---|---|
| AA | ≥ 4.5:1 | Minimum requirement for body text |
| AA Large | ≥ 3:1 | Above 18pt or 14pt bold |
| AAA | ≥ 7:1 | High standard, **recommended for lecture-hall projection** |

> In a lecture-hall projection environment, due to ambient light interference, **a body-text contrast ratio of 7:1 is recommended**.

### Typographic Spacing

| Relationship | Recommended spacing |
|---|---|
| Title and subtitle | 0.3 × title font size |
| Title group and body | 1.5–2 × body font size |
| Line spacing | 1.3–1.5 × font size |
| Paragraph spacing | 0.75–1 × line height |
| Card padding | ≥ 0.3in |
| Card spacing | ≥ 1.5 × card padding |

### Image Guidelines

| Item | Standard |
|---|---|
| Resolution | ≥ 150 dpi (projection); ≥ 300 dpi (print) |
| Aspect ratio | Preserve the original aspect ratio; never stretch |
| Style | Image style consistent across the whole PPT (don't mix photography / illustration / icons) |
| Source | Avoid low-resolution images from search engines and watermarked images |
| Recommended stock sites | Unsplash, Pexels, and professional domestic design asset sites |

### Colour Usage

| Rule | Value |
|---|---|
| Colours per page | ≤ 3 (excluding black, white, and grey) |
| Primary colour share | 60% |
| Secondary colour | 30% |
| Accent colour | 10%, used only for the single most important point |
| Body text colour | Avoid pure black `#000000`; use a warm black from `#1F1F1F`–`#3F403F` |

### Animation and Transitions

| Rule | Description |
|---|---|
| Transition type | Use 1 type throughout (recommended: "Fade" or "Push") |
| Duration | 0.3–0.5 seconds; don't go slower |
| Purpose of animation | Only for **guiding the order of attention**, not for showing off |
| Avoid | Fly in, bounce, spin, blinds, random |

---

## 4. Relationship to Other Theories

| Content of this file | Relationship to other chapters of the main file |
|---|---|
| CRAP Contrast | Corresponds to the "figure/ground" law in `visual-theories.md` |
| CRAP Repetition | Corresponds to the "similarity" law |
| CRAP Alignment | Corresponds to the "continuity" law |
| CRAP Proximity | Corresponds to the "proximity" law |
| Purpose, Simplicity | Corresponds to "conclusion first" in Chapter 1, the pyramid principle |
| Flexibility, Agency | Corresponds to the scenario adaptation of "presentation version vs reading version" |
