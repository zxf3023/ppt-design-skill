# PPT Design

An agent skill for designing and building PPT / deck presentations that actually communicate.

Most decks fail for the same reason: they are documents pretending to be slides. Slides are a **visual aid**, not a transcript. The audience came to listen to you, not to read your slides. Every page in this skill is built around one question — *this page says one thing, what is that thing?*

This skill is deliberately small and composable. It is plain Markdown plus one Python recipe for driving `python-pptx`, so it works with any model and any harness. Hack around with it. Make it your own.

## What it gives you

Three theory frameworks that answer three different questions, plus the hard numbers that make them land:

| Layer | Framework | Question it answers |
| --- | --- | --- |
| **Logic** | Pyramid Principle, MECE, SCQA | How is the argument organised? How does a claim hold up? |
| **Visual** | Gestalt, rule of thirds, Hick's law, CRAP | How is the page laid out? How does the eye move? |
| **Structure** | 5W2H, SWOT, funnel, timeline | Which container carries this particular page? |

Use them in that order: think with the logic layer, choose a container with the structure layer, then lay it out with the visual layer.

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

The skill is self-contained: `SKILL.md` plus `references/` and `themes/`. Nothing else in this repo is needed at runtime.

</details>

## Skills

### Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for it).

- **[ppt-design](./skills/productivity/ppt-design/SKILL.md)**: Design and build a deck from first principles — outline the narrative, structure the logic, lay out pages, pick colour and type, compress walls of text, and build chart and data pages. Ships three theory frameworks (logic: Pyramid Principle / MECE / SCQA; visual: Gestalt / rule of thirds / Hick's law; structure: 5W2H / SWOT / funnel / timeline) and pluggable colour themes.

## Layout

```
skills/productivity/ppt-design/
├── SKILL.md                  # the methodology: 10 chapters
├── agents/openai.yaml        # display name and short description
├── references/               # deep-dive docs, loaded on demand
│   ├── logic-frameworks.md
│   ├── visual-theories.md
│   ├── structure-models.md
│   ├── layout-patterns.md
│   ├── design-basics.md
│   └── checklist.md
└── themes/                   # pluggable colour themes
    ├── business-navy.md
    └── deep-blue-tech.md
```

## Licence

MIT — see [LICENSE](./LICENSE).
