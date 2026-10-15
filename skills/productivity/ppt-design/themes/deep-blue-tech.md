# Theme Pack · Deep Blue Tech

> Best for: technical proposals and product reporting by technology, manufacturing and energy companies
> Master source: 96-page enterprise general layout library (16:9)
> Character: **deep brand blue + lots of white + linear decoration**, formal without being too traditional, suited to scenarios that emphasise "technical strength"

---

## Palette

### Theme colour scheme

| Slot | HEX | Use |
|---|---|---|
| dk1 | `3F403F` | Primary text colour (warm black, not pure black) |
| lt1 | `FFFFFF` | Page base |
| dk2 | `413F3F` | Secondary text |
| lt2 | `E7E6E6` | Light grey fill |
| **accent1** | **`005AA6`** | **Primary colour · deep blue** |
| accent2 | `00B0EF` | Bright cyan-blue · accent |
| accent3 | `006FBF` | Mid blue |
| accent4 | `206DB1` | Grey blue |
| accent5 | `689CCB` | Pale blue · large solid areas |
| accent6 | `25A3EF` | Sky blue · highlight |
| hlink | `0563C1` | Hyperlink |
| folHlink | `6D84CE` | Followed link |

**High-frequency deep blues measured in body text**: `0559A7` / `035AA7` / `0370C0` / `0070C0` (slightly deeper than accent1, used for titles and colour blocks).
**Accent colour**: orange (reserved for special callouts, do not overuse).

### Colour rules

- Choose **blue theme fill colours** wherever possible
- Special callouts may only use **orange**
- **No more than three colours** per page

---

## Fonts

| Level | Latin | Chinese |
|---|---|---|
| Heading font | Arial Black | Microsoft YaHei |
| Body font | Arial | SimHei |
| **Actually used** | — | **Microsoft YaHei** |

**Font list**: Chinese = Microsoft YaHei / Source Han Sans / PingFang SC; Latin = Arial / Microsoft YaHei.

> When filling in content, always **explicitly specify Microsoft YaHei**; do not rely on inheritance.
> Never use multiple fonts, and keep font sizes as uniform as possible.

---

## Type scale (measured)

| Use | Size |
|---|---|
| Chapter large numbers (01/02…) | 66pt |
| Transition-page large numbers | 60 / 48 / 44pt |
| Page numbers / decorative numbers | 40 / 51pt |
| Page title | 40pt (bold) |
| Card keyword large numbers | 36 / 32pt |
| Level-2 heading | 28 / 24pt |
| Subheading | 20 / 22pt |
| Body standard | 14pt |
| Body secondary | 16pt |
| Notes / captions | 12pt |
| Tables and footnotes | 10 / 8pt |

**Body baseline = 14pt, never below 12pt.**

---

## Layout index (96 pages)

The template has two parts:
- **Pages 1–55 = layout library** (copy directly)
- **Pages 56–96 = PPT production training deck** (teaching pages, **do not** copy for content)

### Cover and contents (1–7)

| Page | Use |
|---|---|
| 1 | General cover |
| 2–4 | Covers for three business entities (swap in the entity name as needed) |
| 5 | Contents CONTENTS (4 items) |
| 6 | Level-1 transition page (large number 66pt) |
| 7 | Closing page |

### 01 Text-only layouts (8–15)

| Page | Use |
|---|---|
| 8 | Chapter transition page |
| 9 | Single paragraph (quote mark decoration + closing rule) |
| 10 | Two paragraphs (left/right columns + centre vertical rule) |
| 11 | Three paragraphs |
| 12 | Four paragraphs |
| 13 | Five paragraphs (5 rounded rectangles in a row + timeline dots) |
| 14 | Subheading + multi-item body |
| 15 | Data emphasis page (large number + caption) |

### 02 Image and text (16–21)

| Page | Use |
|---|---|
| 16 | Chapter transition page |
| 17 | Single-image product introduction (image left, text right) |
| 18 | Two-image product introduction |
| 19 | Three-image product introduction (upper/lower zones) |
| 20 | One image + four points |
| 21 | Multi-image product introduction (image wall) |

### 03 Charts (22–28)

| Page | Use |
|---|---|
| 22 | Chapter transition page |
| 23 | Three-line table (table name above, operation hint below) |
| 24 | Percentage chart (3 doughnut charts) |
| 25–26 | Bar chart |
| 27 | Line chart |
| 28 | Pie chart |

> Table pages must have a table name; to change chart data go to "Chart Tools → Design → Edit Data".

### 04 Diagram models (29–46)

| Page | Use |
|---|---|
| 29 | Chapter transition page |
| 30 | Development history |
| 31 | Timeline planning (year axis) |
| 32 | Timeline planning (Gantt chart, actually a table) |
| 33 | Creative timeline |
| 34 | Current progress (dark = completed) |
| 35 | Two-item comparison |
| 36 | Progress planning (simplified) |
| 37 | Three-part **cyclic** logic diagram |
| 38 | Three-part **progressive** logic diagram |
| 39 | Four-part summary with highlighted key point |
| 40 | SWOT matrix (large version) |
| 41 | SWOT matrix (compact version) |
| 42 | Four parallel points diagram |
| 43 | Five parallel points diagram |
| 44 | Six parallel points diagram |
| 45 | Simple architecture diagram |
| 46 | Coordinate matrix |

### 05 Special-purpose pages + appendix (47–55)

| Page | Use |
|---|---|
| 47 | Chapter transition page |
| 48 | Whiteboard page |
| 49 | Award showcase |
| 50 | Honours showcase |
| 51 | Patent and standard showcase |
| 52 | Partner showcase |
| 53 | Appendix · applicable entities / notes |
| 54 | Appendix · theme colours + fonts + guides |
| 55 | Notes page |

---

## Layout list (slideLayout)

| # | Name |
|---|---|
| 0 | Title Slide |
| 1 | Blank |
| 2 | Title and Content |
| 3 | Title Only |
| 4 | Content |
| 5 | 1_Title and Content (for training deck) |

---

## Header motif geometry (inches)

| Element | left | top | width | height |
|---|---|---|---|---|
| Entity name colour block | 0.00 | 0.45 | 2.64 | 0.37 |
| Section name text | 2.64 | 0.47 | ~1.8 | 0.34 |
| Section underline | 2.66 | 0.82 | ~1.5 | 0 |
| Subtitle decorative vertical block | 0.43 | 1.24 | 0.11 | 0.31 |
| Page subtitle | 0.54 | 1.18 | ~2.7 | 0.40 |
| Bottom decorative bar | 0.00 | 7.38 | 13.43 | 0.12 |

**Safe zone**: x ∈ [0.50, 12.83], y ∈ [1.80, 7.10]
Title zone y ≈ 1.95–2.60; body zone y ≈ 2.20–6.60

### Key layout coordinates

**Contents page (page 5)**: left decoration 0–5.28in; "Contents" @(1.76, 3.04); item numbers @x=6.44, item text @x=7.75, vertical y = 1.21 / 2.73 / 4.12 / 5.51

**Single paragraph (page 9)**: quote mark decoration @(0.77, 2.31) 1.08×0.92; body box @(1.84, 3.23) 9.93×1.55; closing rule @(1.84, 5.03)

**Two paragraphs (page 10)**: left column x=0.74 width 4.14; centre vertical rule x=6.66; right column x=8.45 width 4.14; subheading y=2.18, body y=3.21

**Five paragraphs (page 13)**: card 2.14×3.45 @y=3.26, horizontal x = 3.25 / 5.60 / 8.03 / 10.46

**Three-line table (page 23)**: table name @(0.73, 1.95); table @(0.73, 2.52) 11.88×3.14; hint @(0.73, 6.05)

**Percentage chart (page 24)**: three doughnut charts 2.35×2.22 @y=2.18, x = 0.76 / 5.33 / 9.93; subheading y=4.28; body y=5.30

---

## Workflow

1. **Copy pages, don't create new ones**. Select a layout page → Ctrl+D → drag to the target position. Master, header and guides are all inherited.
2. **Replace text only, don't touch shapes**. When text grows longer, shrink the font size first (≥12pt) or trim the copy.
3. **Replacement checklist**:
   - [ ] Top-right LOGO is correct (to change it go to View → Slide Master)
   - [ ] Entity name replaced (header colour block + cover + footer)
   - [ ] Level-1 / level-2 heading contents text replaced
   - [ ] Chapter numbers match chapter names
   - [ ] Data is the latest version
   - [ ] All content is inside the guides (ALT+F9 to show guides)
   - [ ] Fonts are uniformly Microsoft YaHei
   - [ ] No more than three colours, emphasis uses orange only
4. **Embed fonts**: Windows = File → Options → Save → Embed fonts in the file; macOS = Preferences → Save → Embed fonts in the file
5. **Images**: use high-resolution images; avoid low-resolution and watermarked images

---

## Notes

- ⚠️ Don't use the wrong top-right LOGO; to change it go to View → Slide Master
- ⚠️ The text on level-1 and level-2 heading contents pages must be replaced
- ⚠️ The entity name must be replaced
- ⚠️ Remember to copy the auxiliary lines along with the rest
- ⚠️ Only the area inside the guides is the safe zone; View → Guides, shortcut ALT+F9
