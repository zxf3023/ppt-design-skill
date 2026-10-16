Skills are organised into bucket folders under `skills/`:

- `productivity/`: daily non-code workflow tools
- `engineering/`: daily code work
- `misc/`: kept around but rarely used, not promoted
- `in-progress/`: beta: public on purpose, feedback wanted, not shipped in the plugin
- `deprecated/`: no longer used

Every skill in `productivity/` or `engineering/` (the **promoted** buckets) must have a reference in the top-level `README.md` and an entry in `.claude-plugin/plugin.json`'s `skills` array. Skills in `misc/`, `in-progress/`, and `deprecated/` must not appear in either.

Each skill entry in the top-level `README.md` must link the skill name to its `SKILL.md`.

Each bucket folder has a `README.md` that lists every skill in the bucket with a one-line description, with the skill name linked to its `SKILL.md`. Promoted bucket `README.md`s group entries into **User-invoked** and **Model-invoked**; non-promoted buckets use a flat list.

Skills in `productivity/` and `engineering/` also have a human-facing docs page at `docs/<bucket>/<skill-name>.md`. A finished page carries four sections: **What it does**, **When to reach for it**, **Common questions**, and **It's working if**. Skills in the non-promoted buckets get **no** docs page.

## Skill anatomy

```
skills/<bucket>/<skill-name>/
├── SKILL.md           # required; YAML frontmatter with `name` and `description`
├── agents/openai.yaml # required; display_name + short_description
├── references/        # optional; loaded on demand, one topic per file
├── themes/            # optional; pluggable variants
├── scripts/           # optional; the deterministic work the skill drives
├── assets/            # optional; libraries and images the scripts read
└── config.example.json # optional; configuration template
```

### Frontmatter

```yaml
---
name: <skill-name>          # must match the folder name
description: "<rich trigger phrasing: what it does, and when to reach for it>"
---
```

The `description` is the only thing the model sees before deciding to load the skill. Write it as trigger phrasing — name the user's situations, not the skill's internals.

### Body

- Open with the core belief of the skill in one or two lines, then get to the mechanics.
- Prefer tables of rules over prose. A rule the reader can scan beats a paragraph they must parse.
- Every rule that has a numeric form gets the number: font sizes, spacing, ratios, word counts.
- Keep `SKILL.md` to the working method. Anything that is a deep dive on one topic belongs in `references/` and gets one line in `SKILL.md` telling the model when to open it.
- No marketing language. No filler openers. Say the thing.

### User-invoked vs model-invoked

A skill is either user-invoked (reachable only when typed: `disable-model-invocation: true` in the frontmatter plus `policy.allow_implicit_invocation: false` in `agents/openai.yaml`) or model-invoked (rich trigger phrasing so the model can reach for it on its own).

## Manifests

`.claude-plugin/marketplace.json` is this repo's own marketplace. `.claude-plugin/plugin.json` lists the promoted skills in its `skills` array.

When you add, rename, or remove a promoted skill, update all four: the top-level `README.md`, the bucket `README.md`, `.claude-plugin/plugin.json`, and the docs page under `docs/`.

## Docs pages

`docs/<bucket>/<skill-name>.md` mirrors the promoted bucket folders. Four sections, in this order:

1. **What it does** — the mechanism, and the design decision behind it.
2. **When to reach for it** — including a table of "your situation → reach for".
3. **Common questions** — the questions a reader actually asks, answered plainly.
4. **It's working if** — observable signals that the skill is doing its job.
