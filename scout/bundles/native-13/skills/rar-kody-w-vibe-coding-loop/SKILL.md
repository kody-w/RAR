---
name: "rar-kody-w-vibe-coding-loop"
description: "Returns prompt templates for the kody-w.github.io/learnwithkody publishing loop. Provider-agnostic \u2014 feed the returned templates to whatever LLM you have. Actions: ideate, worker, wrapper, ship, loop."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/vibe_coding_loop", "rar_sha256": "c0329a49a1dccb8873b83964d0fa8ce231a24ede94051343162b37bef7149b1f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["publishing", "orchestration", "vibe-coding", "single-file-html", "loop"]}
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
