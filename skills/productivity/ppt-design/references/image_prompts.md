# Illustration Prompts

## Visual Anchor

The illustrations in a deck look like one family because **the same protagonist appears over and over**. In the example it is "a robotic hand holding an M icon", and only the props around it change from page to page.

Follow three points when writing `meta.anchor.description`.

1. Pick a concrete object that represents the topic: for a product, use its app icon or mascot; for a course topic, it could be a book, a globe, or a plant
2. Be specific down to material and color, for example "a glossy mint-teal rounded-square app icon with a bold white letter M"
3. You can add an action carrier to leave room for variation across pages, for example "held by a sleek white robotic hand"

`glyph` takes a single letter, and the procedural illustration draws it on the main tile.

## Per-Page Prompt Formula

make_assets.py automatically appends the style, palette, composition, and negative constraints after every prompt, so in plan.json you only write **what this page depicts**.

```
{anchor or part of the anchor} + {props/actions related to this page's content} + {mood}
```

| Page content | Prompt example |
|---|---|
| Cover | hero shot of {anchor}, floating above a soft round pedestal, small chat bubble and chart badges orbiting around it |
| What it is | {anchor} presented alone, simple and iconic, gentle glow |
| Data growth | {anchor} next to a rising bar chart with an upward arrow, a few floating download icons |
| Cloud computer | a friendly cloud-shaped computer inside a transparent protective shield, a small {anchor} badge on it |
| Getting-started steps | a checklist card with a big check mark and a small lock, {anchor} peeking from behind |
| Example sentence prompt | a large speech bubble with quote marks, {anchor} typing on it |
| Low-risk tasks | {anchor} calmly reading a document with a magnifier |
| Risk reminder | a gentle caution sign and a closed shop door, {anchor} standing aside, not scary |
| Privacy | a padlock and a key beside a mailbox, soft protective glow |
| Ending | {anchor} waving hello, sparkles around, optimistic |

## Auto-Appended Parts (No Need to Write by Hand)

- `Visual style:` taken from `style.illustration.style_prompt`
- `Color palette:` taken from the palette's primary, primary_dark, accent, tint
- Composition: subject centered, fully visible, with margins around it; add "isolated on a plain pure white background" when a transparent background is needed
- `Do not include:` taken from `style.illustration.negative`

Use `python3 $S/make_assets.py $W --dry-run` to print the final prompts without calling the API.

## Transparent Background

- OpenAI `gpt-image-1` supports native transparent backgrounds, and the script requests them automatically
- Other models produce white-background images; the script removes the white background with rembg (when installed) or edge flood fill, which suits flat illustrations. For realistic styles, install rembg: `pip install rembg --break-system-packages`

## Procedural Fallback

When no image generation model is configured, the `fallback` field determines what the fallback illustration looks like.

| scene | Visual | Good for |
|---|---|---|
| `tile` | Glowing main tile (letter or icon), orbit, small satellite icons, pedestal | Cover, definition pages, ending |
| `badge` | Large circular badge with one icon | Concepts, principles, warnings |
| `cards` | Stacked cards with list lines | Lists, steps, document-style pages |
| `chart` | Bar chart card with a rising line | Data pages |

The fallback illustration's small icons default to that page's `icons`, or you can specify them separately in `fallback.icons`. All colors come from style.json, so just regenerate after switching styles.
