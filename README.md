# PPT Design

An agent skill for designing **and producing** PPT / deck presentations that actually communicate.

Most decks fail for the same reason: they are documents pretending to be slides. Slides are a **visual aid**, not a transcript. The audience came to listen to you, not to read your slides. Every page in this skill is built around one question — *this page says one thing, what is that thing?*

The skill has two halves that share one set of standards:

- **Methodology** — how to think and how to lay out. Logic, visual and structure frameworks, the hard numbers that make them land, and the checks that catch a bad deck before an audience does.
- **Execution engine** — how to actually produce the file. Two routes, both emitting editable native `.pptx`: generate from a topic, article, script or outline; or beautify an existing deck against a reference image without changing a word of the text.

You can use the methodology alone for review, outlining and specification work, or run the whole thing end to end.

## What it gives you

Three theory frameworks that answer three different questions, plus the hard numbers that make them land:

| Layer | Framework | Question it answers |
| --- | --- | --- |
| **Logic** | Pyramid Principle, MECE, SCQA | How is the argument organised? How does a claim hold up? |
| **Visual** | Gestalt, rule of thirds, Hick's law, CRAP | How is the page laid out? How does the eye move? |
| **Structure** | 5W2H, SWOT, funnel, timeline | Which container carries this particular page? |

Use them in that order: think with the logic layer, choose a container with the structure layer, then lay it out with the visual layer.

The engine carries the parts that are arithmetic and the parts that are labour:

- **14 style presets** (Swiss grid, ink magazine, cobalt type, dark tech, warm orange and more), each with hard rules the layouts must obey
- **A layout library** with per-layout capacity, so content that does not fit is caught before it is rendered
- **An icon library**, a **five-dimension self-review** (unity, hierarchy, detail, communication, pacing), and a QA pass that checks for missing text, overflow, overlap and over-emphasis
- **Image generation is optional** — configure OpenAI, Gemini, Volcengine Ark or a custom endpoint, or let it fall back to programmatic illustration

## Installation

Pick **one** method per agent. Installing two gives you the skill twice.

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add zxf3023/ppt-design-skill
claude plugin install ppt-design-skills@zxf3023
```

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add zxf3023/ppt-design-skill
codex plugin add ppt-design-skills@zxf3023
```

</details>

<details>
<summary><strong>Any other agent (manual)</strong></summary>

Copy the skill folder into your agent's skills directory:

```bash
cp -r skills/productivity/ppt-design ~/.your-agent/skills/
```

The skill is self-contained. Before first use, run the environment check — it verifies Python, `python-pptx`, Pillow, numpy and lxml, and can install what is missing:

```bash
python3 scripts/setup_check.py --quick --install
```

LibreOffice is recommended (it renders the preview sheets) but not required: without it the engine falls back to `render_lite.py`, which draws an approximate preview straight from the layout data.

</details>

## Skills

### Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for it).

- **[ppt-design](./skills/productivity/ppt-design/SKILL.md)**: Design and produce a deck. Methodology: logic (Pyramid Principle / MECE / SCQA), visual (Gestalt / rule of thirds / Hick's law / CRAP), structure (5W2H / SWOT / funnel / timeline), type scale, whitespace, colour, wall-of-text handling, page templates and narrative pacing. Execution engine: generate a deck from a topic, article, script or outline with conclusion-style titles and speaker notes, or beautify an existing `.pptx` against a reference image without changing the text. Ships 14 style presets, an icon library and a five-dimension self-review chain.

## Layout

```
skills/productivity/ppt-design/
├── SKILL.md                  # the method: 11 chapters
├── agents/openai.yaml        # display name and short description
├── references/               # deep-dive docs, loaded on demand
│   ├── logic-frameworks.md   # methodology: logic layer
│   ├── visual-theories.md    # methodology: visual layer
│   ├── structure-models.md   # methodology: structure layer
│   ├── layout-patterns.md    # methodology: 38 page patterns
│   ├── design-basics.md      # methodology: CRAP, whitespace, contrast
│   ├── checklist.md          # methodology: delivery checklist
│   ├── generate.md           # engine: generation rules
│   ├── deck_schema.md        # engine: deck.json fields and page types
│   ├── layouts.md            # engine: layout library and capacity
│   ├── style_extraction.md   # engine: read style.json from an image
│   ├── critique.md           # engine: five-dimension scoring
│   ├── icons.md              # engine: icon catalogue
│   ├── image_prompts.md      # engine: illustration prompts
│   ├── imagegen_config.md    # engine: image backend configuration
│   ├── fonts.md              # engine: font choice and compatibility
│   └── styles/               # engine: 14 style presets (JSON)
├── themes/                   # methodology: pluggable colour themes
│   ├── business-navy.md
│   └── deep-blue-tech.md
├── scripts/                  # engine: 23 Python scripts
├── assets/                   # engine: icon library, style gallery
└── config.example.json       # engine: image backend template
```

The engine drives three intermediate files — `deck.json` (what each page says), `style.json` (palette, fonts, decoration) and `plan.json` (layout, icons and illustration prompts per page). Scripts do the deterministic work; the model does the judgement.

## Licence

MIT — see [LICENSE](./LICENSE). The execution engine is derived from [luobo-ppt](https://github.com/zhouwei713/luobo-ppt) by zhouluobo, also MIT — see [LICENSE-luobo-ppt](./LICENSE-luobo-ppt).
