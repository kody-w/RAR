---
name: "rar-kody-w-vibe-coding-loop"
description: "Returns prompt templates for the kody-w.github.io/learnwithkody publishing loop. Provider-agnostic \u2014 feed the returned templates to whatever LLM you have. Actions: ideate, worker, wrapper, ship, loop."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/vibe_coding_loop", "rar_sha256": "c0329a49a1dccb8873b83964d0fa8ce231a24ede94051343162b37bef7149b1f", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["publishing", "orchestration", "vibe-coding", "single-file-html", "loop"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/vibe_coding_loop`. The original RAPP
agent is preserved byte-for-byte in `vibe_coding_loop_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

vibe_coding_loop_agent.py — RAPP agent that runs the kody-w.github.io/learnwithkody publishing loop.

Drop into any RAPP brainstem's agents/ directory. Returns templates that
the host LLM (or another agent) executes. The agent is stateless and
provider-agnostic — it does NOT make LLM calls itself; it generates the
exact prompts you feed to your model so you can run the loop with any
backend (GitHub Copilot SDK, Azure OpenAI, Anthropic, Ollama, etc.).

Loop documented at: https://kody-w.github.io/loop/

Actions:
  ideate(domain)              → ideation prompt for your LLM (returns 10 demo concepts)
  worker(prompt, lib, path)   → worker brief to dispatch to a sub-agent
  wrapper(demo_path, prompt)  → Jekyll example-post template to fill in
  ship(slugs)                 → shell command sequence for commit/push/verify
  loop(domain)                → full step-by-step plan for one round

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Which template to generate.",
      "enum": [
        "ideate",
        "worker",
        "wrapper",
        "ship",
        "loop"
      ],
      "type": "string"
    },
    "category": {
      "description": "simulator|game|tool|prompt",
      "type": "string"
    },
    "demo_filename": {
      "description": "Filename of the demo (e.g. '42-foo.html'). Used by wrapper.",
      "type": "string"
    },
    "difficulty": {
      "description": "beginner|intermediate|advanced",
      "type": "string"
    },
    "domain": {
      "description": "Domain for ideation (action=ideate or loop). E.g. 'first-person 3D environments'.",
      "type": "string"
    },
    "highlight": {
      "description": "Signature term to highlight in prompt block.",
      "type": "string"
    },
    "lesson1": {
      "type": "string"
    },
    "lesson2": {
      "type": "string"
    },
    "lesson3": {
      "type": "string"
    },
    "lib": {
      "description": "Approved external library for the worker. Default: 'three.js'.",
      "type": "string"
    },
    "order": {
      "description": "Sort order in catalog.",
      "type": "integer"
    },
    "output_path": {
      "description": "Absolute path where the worker writes the HTML demo (action=worker).",
      "type": "string"
    },
    "prompt": {
      "description": "Creative brief for a worker (action=worker).",
      "type": "string"
    },
    "slug": {
      "description": "Kebab-case identifier.",
      "type": "string"
    },
    "slugs": {
      "description": "Space-separated slugs (action=ship).",
      "type": "string"
    },
    "stack": {
      "description": "Comma-separated stack components.",
      "type": "string"
    },
    "tagline": {
      "type": "string"
    },
    "tags": {
      "description": "Comma-separated tags.",
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "what_this_is": {
      "type": "string"
    },
    "why_mind_blowing": {
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vibe_coding_loop_agent.py` and embedded as the fenced Python below (sha256 c0329a49a1dccb88…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vibe_coding_loop_agent.py` first:

```bash
python3 vibe_coding_loop_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vibe_coding_loop_agent.py   # or on stdin
python3 vibe_coding_loop_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/vibe_coding_loop_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/vibe_coding_loop_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/vibe_coding_loop/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
vibe_coding_loop_agent.py — RAPP agent that runs the kody-w.github.io/learnwithkody publishing loop.

Drop into any RAPP brainstem's agents/ directory. Returns templates that
the host LLM (or another agent) executes. The agent is stateless and
provider-agnostic — it does NOT make LLM calls itself; it generates the
exact prompts you feed to your model so you can run the loop with any
backend (GitHub Copilot SDK, Azure OpenAI, Anthropic, Ollama, etc.).

Loop documented at: https://kody-w.github.io/loop/

Actions:
  ideate(domain)              → ideation prompt for your LLM (returns 10 demo concepts)
  worker(prompt, lib, path)   → worker brief to dispatch to a sub-agent
  wrapper(demo_path, prompt)  → Jekyll example-post template to fill in
  ship(slugs)                 → shell command sequence for commit/push/verify
  loop(domain)                → full step-by-step plan for one round
"""

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent
    except ModuleNotFoundError:
        class BasicAgent:
            def __init__(self, name, metadata): self.name, self.metadata = name, metadata

import json


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/vibe_coding_loop",
    "version": "1.0.1",
    "display_name": "Vibe Coding Demo Loop",
    "description": (
        "Returns prompt and shell-command templates for shipping batches of single-file HTML demos to a Jekyll site; makes no LLM or network calls itself."
    ),
    "author": "kody-w",
    "tags": ["publishing", "orchestration", "vibe-coding", "single-file-html", "loop"],
    "category": "workflow",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "action": "loop",
        "domain": "first-person rooftop scenes",
    },
}


_CONSTRAINTS = """CONSTRAINTS (non-negotiable):
- ONE HTML file. All CSS/JS inline.
- Approved external lib: {lib} from CDN. Nothing else.
- No API keys, no backend, no fetch() to external services.
- Must run instantly. Visible / playable within 1 second of load.
- DO NOT modify any other file. DO NOT touch git. DO NOT spawn subagents."""


_IDEATION_PROMPT = """You are helping a human grow a vibe-coding examples catalog
(reference: https://kody-w.github.io/learnwithkody/). Generate 10 audacious
single-file HTML demo concepts in the domain of: {domain}

Constraints per concept:
- Runs in a browser tab from one HTML file
- Approved external lib: three.js from CDN (or pure web platform)
- No API keys, no backend, no fetch() to external services
- Beautiful within one second of load — no setup screens
- Ambition that makes the viewer say "I can't believe this is one HTML file"

Format each entry as:
- Bold title
- One-line italic hook (what the viewer sees)
- Blockquote of the actual prompt I'd send a worker, with one bold
  signature technical term that names the demo's defining trick

End with a four-tier ranking:
- Highest hit-rate (likely nailed first try)
- Hardest but most spectacular
- Best for a video / Twitter clip
- Best educational reach"""


_WORKER_BRIEF = """You are building one mind-blowing single-file HTML demo for
kody-w.github.io/learnwithkody — a vibe coding examples site.

{constraints}

THE DEMO TO BUILD:
{prompt}

WRITE TO: {output_path}

After writing, report back in under 150 words: what's beautiful about it,
key implementation details, any compromises you made."""


_WRAPPER_TEMPLATE = """---
title: "{title}"
slug: {slug}
order: {order}
featured: true
tagline: "{tagline}"
category: {category}
difficulty: {difficulty}
status: live
tags: [{tags}]
stack: [{stack}]
demo: /learnwithkody/demos/{demo_filename}
repo: https://github.com/kody-w/kody-w.github.io
highlights:
  - {highlight}
prompt: |
{prompt_indented}
lessons:
  - "{lesson1}"
  - "{lesson2}"
  - "{lesson3}"
---

<section class="lwk-section">
  <h2>What this is</h2>
  <p>{what_this_is}</p>
</section>

<section class="lwk-section">
  <h2>Why this is mind-blowing</h2>
  <p>{why_mind_blowing}</p>
</section>

<aside class="lwk-try-embed">
  <div class="lwk-try-embed-head">
    <span class="lwk-try-embed-label">Live demo</span>
    <a href="/learnwithkody/demos/{demo_filename}" target="_blank" rel="noopener" class="lwk-try-embed-open">Open in new tab ↗</a>
  </div>
  <iframe src="/learnwithkody/demos/{demo_filename}" title="{title} — live demo" loading="lazy" sandbox="allow-scripts allow-same-origin allow-pointer-lock"></iframe>
</aside>"""


_SHIP_SEQUENCE = """# Validate every YAML
for f in _examples/{slugs}.html; do
  ruby -ryaml -e "YAML.load(File.read('$f')[/---\\n(.*?)\\n---/m, 1])"
done

# Tests
python3 -m unittest discover -s tests -p 'test_*.py'

# Check for concurrent commits before pushing
git fetch origin master
git rev-list --left-right --count HEAD...origin/master

# If divergent: git pull --rebase origin master  (no destructive force-push)

# Stage, commit, push
git add _examples/ learnwithkody/demos/
git commit -m "learnwithkody: round N — <table of demos + signature tricks>

Co-Authored-By: <your-llm-id> <noreply@example.com>"
git push origin master

# Watch CI
gh run list --branch master --limit 1 --json databaseId --jq '.[0].databaseId' \\
  | xargs -I {{}} gh run watch {{}} --exit-status

# Verify each URL returns 200
for slug in {slugs}; do
  printf "%-50s " "/learnwithkody/examples/$slug/"
  curl -s -o /dev/null -w "%{{http_code}}\\n" "https://kody-w.github.io/learnwithkody/examples/$slug/"
done"""


class VibeCodingLoopAgent(BasicAgent):
    def __init__(self):
        self.name = "VibeCodingLoop"
        self.metadata = {
            "name": self.name,
            "description": (
                "Returns prompt templates for the kody-w.github.io/learnwithkody publishing loop. "
                "Provider-agnostic — feed the returned templates to whatever LLM you have. "
                "Actions: ideate, worker, wrapper, ship, loop."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["ideate", "worker", "wrapper", "ship", "loop"],
                        "description": "Which template to generate.",
                    },
                    "domain": {
                        "type": "string",
                        "description": "Domain for ideation (action=ideate or loop). E.g. 'first-person 3D environments'.",
                    },
                    "prompt": {
                        "type": "string",
                        "description": "Creative brief for a worker (action=worker).",
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Absolute path where the worker writes the HTML demo (action=worker).",
                    },
                    "lib": {
                        "type": "string",
                        "description": "Approved external library for the worker. Default: 'three.js'.",
                    },
                    "demo_filename": {
                        "type": "string",
                        "description": "Filename of the demo (e.g. '42-foo.html'). Used by wrapper.",
                    },
                    "slug": {"type": "string", "description": "Kebab-case identifier."},
                    "title": {"type": "string"},
                    "tagline": {"type": "string"},
                    "category": {"type": "string", "description": "simulator|game|tool|prompt"},
                    "difficulty": {"type": "string", "description": "beginner|intermediate|advanced"},
                    "tags": {"type": "string", "description": "Comma-separated tags."},
                    "stack": {"type": "string", "description": "Comma-separated stack components."},
                    "order": {"type": "integer", "description": "Sort order in catalog."},
                    "highlight": {"type": "string", "description": "Signature term to highlight in prompt block."},
                    "lesson1": {"type": "string"},
                    "lesson2": {"type": "string"},
                    "lesson3": {"type": "string"},
                    "what_this_is": {"type": "string"},
                    "why_mind_blowing": {"type": "string"},
                    "slugs": {
                        "type": "string",
                        "description": "Space-separated slugs (action=ship).",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get("action", "").lower()

        if action == "ideate":
            domain = kwargs.get("domain") or "single-file HTML demos"
            return json.dumps({
                "status": "success",
                "action": "ideate",
                "instruction": "Feed the following prompt to your LLM. It will return 10 demo concepts.",
                "prompt": _IDEATION_PROMPT.format(domain=domain),
            })

        if action == "worker":
            prompt = kwargs.get("prompt") or "[insert creative brief]"
            output_path = kwargs.get("output_path") or "[insert absolute path /.../learnwithkody/demos/NN-slug.html]"
            lib = kwargs.get("lib") or "three.js"
            constraints = _CONSTRAINTS.format(lib=lib)
            return json.dumps({
                "status": "success",
                "action": "worker",
                "instruction": (
                    "Dispatch this brief as a sub-agent (parallel to other workers). "
                    "DO NOT have the worker spawn its own subagents."
                ),
                "brief": _WORKER_BRIEF.format(constraints=constraints, prompt=prompt, output_path=output_path),
            })

        if action == "wrapper":
            prompt_text = kwargs.get("prompt") or "[verbatim worker brief]"
            indented = "\n".join("  " + line for line in prompt_text.splitlines())
            tags = kwargs.get("tags") or "fps, three-js, game"
            stack = kwargs.get("stack") or "HTML, JavaScript, three.js"
            return json.dumps({
                "status": "success",
                "action": "wrapper",
                "instruction": "Fill in the placeholders, then write to _examples/{slug}.html",
                "template": _WRAPPER_TEMPLATE.format(
                    title=kwargs.get("title") or "[Title]",
                    slug=kwargs.get("slug") or "[slug]",
                    order=kwargs.get("order") or 99,
                    tagline=kwargs.get("tagline") or "[Tagline — quote if it has colons]",
                    category=kwargs.get("category") or "game",
                    difficulty=kwargs.get("difficulty") or "advanced",
                    tags=tags,
                    stack=stack,
                    demo_filename=kwargs.get("demo_filename") or "NN-slug.html",
                    highlight=kwargs.get("highlight") or "[signature technical term]",
                    prompt_indented=indented,
                    lesson1=kwargs.get("lesson1") or "[Lesson 1 — one specific technical sentence]",
                    lesson2=kwargs.get("lesson2") or "[Lesson 2]",
                    lesson3=kwargs.get("lesson3") or "[Lesson 3]",
                    what_this_is=kwargs.get("what_this_is") or "[What this is — one paragraph, concrete]",
                    why_mind_blowing=kwargs.get("why_mind_blowing") or "[Why this is mind-blowing — end on a punchline]",
                ),
            })

        if action == "ship":
            slugs = kwargs.get("slugs") or "demo1 demo2 demo3"
            slug_brace = "{" + ",".join(slugs.split()) + "}"
            return json.dumps({
                "status": "success",
                "action": "ship",
                "instruction": "Run this shell sequence to validate, commit, push, and verify.",
                "shell": _SHIP_SEQUENCE.format(slugs=slug_brace),
            })

        if action == "loop":
            domain = kwargs.get("domain") or "[a specific domain — e.g. 'first-person rooftop scenes']"
            return json.dumps({
                "status": "success",
                "action": "loop",
                "instruction": "Execute these steps in order. Each step gives you what to do AND what to feed your LLM.",
                "plan": [
                    {
                        "step": 1,
                        "title": "Ideate",
                        "what_to_do": (
                            "Feed your LLM the ideation prompt. It returns 10 demo concepts. "
                            "Present them to the human and wait for approval."
                        ),
                        "call": {"action": "ideate", "domain": domain},
                    },
                    {
                        "step": 2,
                        "title": "Dispatch",
                        "what_to_do": (
                            "For each of the 10 concepts, generate a worker brief and dispatch "
                            "as a parallel sub-agent. Number demo files NN-slug.html (next "
                            "available NN). Send all 10 dispatches in ONE message — true "
                            "parallelism. CRITICAL: include 'DO NOT spawn subagents' in every brief."
                        ),
                        "call": {"action": "worker", "prompt": "<one of the 10>", "output_path": "<path>"},
                    },
                    {
                        "step": 3,
                        "title": "Wrap",
                        "what_to_do": (
                            "When each worker reports back, write a Jekyll example post in "
                            "_examples/{slug}.html using the wrapper template. Quote any tagline "
                            "with embedded colons — Jekyll YAML strict mode will reject unquoted ones."
                        ),
                        "call": {"action": "wrapper", "demo_filename": "NN-slug.html", "...": "..."},
                    },
                    {
                        "step": 4,
                        "title": "Ship",
                        "what_to_do": (
                            "Validate YAML, run tests, fetch remote, commit, push, watch CI, verify URLs."
                        ),
                        "call": {"action": "ship", "slugs": "slug1 slug2 slug3 ..."},
                    },
                ],
                "reference": "https://kody-w.github.io/loop/",
                "skill_md": ".github/skills/vibe-coding-demo-loop/SKILL.md",
            })

        return json.dumps({
            "status": "error",
            "message": f"Unknown action: {action!r}. Try: ideate, worker, wrapper, ship, loop.",
        })
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
