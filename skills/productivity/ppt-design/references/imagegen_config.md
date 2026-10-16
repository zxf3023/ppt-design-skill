# Image Generation API Configuration

It works without configuration — illustrations will use procedural generation. To get the AI illustration look shown in the attachment examples, configure an image generation model.

## Where to Put the Config File

Files are looked up in the order below, and the first one found is used.

1. Command line `--config path`
2. The file pointed to by the `LUOBO_PPT_CONFIG` environment variable
3. `luobo-ppt.config.json` in the current directory, then the file with the same name in the working directory
4. `~/.config/luobo-ppt/config.json`
5. `config.json` in the skill directory

The config file names and environment variables for the old names ppt-studio and ppt-beautify are still valid, so nothing needs to change after upgrading. If none of them exist, you can also use environment variables alone: `LUOBO_PPT_PROVIDER=openai` plus the corresponding key variable.

To check the currently active configuration: `python3 scripts/make_assets.py <working_dir> --status`

## Fields

| Field | Description |
|---|---|
| `provider` | `openai`, `gemini`, `ark`, `openai_compatible`, `command`, `none` |
| `api_key_env` | Name of the environment variable that holds the key (recommended; the key is never written to disk) |
| `api_key` | Write the key directly (not recommended; don't share the file) |
| `model` | Model name; the default is used if omitted |
| `base_url` | API endpoint; the provider default is used if omitted |
| `quality` | OpenAI gpt-image only; `low` / `medium` / `high` |
| `size` | Forced size; usually not needed |
| `use_for` | `{"hero": true, "background": false}`; by default AI is used only for illustrations, while backgrounds are procedural (cleaner, doesn't compete with the text) |
| `max_parallel` | Concurrency; default 3 |
| `timeout` / `retries` | Per-request timeout in seconds and retry count; defaults are 180 and 1 |
| `extra` | Extra parameters merged into the request body as-is |

## Examples per Provider

OpenAI (supports native transparent backgrounds)

```json
{"provider": "openai", "api_key_env": "OPENAI_API_KEY", "model": "gpt-image-1", "quality": "medium"}
```

Google Gemini

```json
{"provider": "gemini", "api_key_env": "GEMINI_API_KEY", "model": "gemini-2.5-flash-image"}
```

Volcengine Ark (Jimeng / Seedream)

```json
{"provider": "ark", "api_key_env": "ARK_API_KEY", "model": "doubao-seedream-4-0-250828"}
```

Other services compatible with the OpenAI image API (proxies, self-hosted services, etc.)

```json
{"provider": "openai_compatible", "api_key_env": "IMAGE_API_KEY",
 "base_url": "https://your-endpoint/v1", "model": "your-model"}
```

Local command (for example your own ComfyUI script). The command must write the PNG to `{out}`; the placeholders `{prompt_file}`, `{prompt}`, `{out}`, `{w}`, `{h}` are available.

```json
{"provider": "command", "command": "python my_gen.py --prompt-file {prompt_file} --out {out} --size {w}x{h}"}
```

Model names and default endpoints change as providers update them, so if a call fails, first verify the model name against the provider's documentation.

## What Happens on Failure

- If a single image fails, it automatically falls back to a procedural illustration; `assets/manifest.json` records `procedural (after AI error)` along with the error message
- In Claude's cloud environment, image generation requests must pass through a network allowlist; when they are blocked, the same fallback applies, and the user should be told honestly at delivery time
- If the runtime environment has its own native image generation tool (such as certain agent platforms), you can also use it directly with the prompts printed by `--dry-run`, save the output as `assets/hero_NN.png`, register it in the manifest, and then continue assembling
