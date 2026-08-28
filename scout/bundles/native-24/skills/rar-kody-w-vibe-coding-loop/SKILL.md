---
name: "rar-kody-w-vibe-coding-loop"
description: "Returns prompt templates for the kody-w.github.io/learnwithkody publishing loop. Provider-agnostic \u2014 feed the returned templates to whatever LLM you have. Actions: ideate, worker, wrapper, ship, loop."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/vibe_coding_loop", "rar_sha256": "931c9224a42c1a609821a5d2fb5b7303a7434fb625d59eae8f8027a7ef7b046e", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["publishing", "orchestration", "vibe-coding", "single-file-html", "loop"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vibe_coding_loop_agent.py` and embedded as the fenced Python below (sha256 931c9224a42c1a60…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vibe_coding_loop_agent.py` first:

```bash
python3 vibe_coding_loop_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vibe_coding_loop_agent.py   # or on stdin
python3 vibe_coding_loop_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
