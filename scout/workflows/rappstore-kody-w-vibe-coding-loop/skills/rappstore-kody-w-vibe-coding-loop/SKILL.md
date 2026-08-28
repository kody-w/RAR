---
name: "rappstore-kody-w-vibe-coding-loop"
description: "Returns prompt templates for the kody-w.github.io/learnwithkody publishing loop. Provider-agnostic \u2014 feed the returned templates to whatever LLM you have. Actions: ideate, worker, wrapper, ship, loop."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/vibe-coding-loop", "rar_sha256": "fcbba7d2b73f340e1bdcf27a263e9f7a50b9d5ae117af80496cfcda287847b1d", "source_kind": "federated-rapplication", "source_commit": null, "author": "kody-w", "tags": ["publishing", "orchestration", "vibe-coding", "single-file-html", "loop"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/vibe-coding-loop`. The original RAPP
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vibe_coding_loop_agent.py` and embedded as the fenced Python below (sha256 fcbba7d2b73f340e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vibe_coding_loop_agent.py` first:

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
    "name": "@kody-w/vibe-coding-loop",
    "version": "1.0.0",
    "display_name": "Vibe Coding Demo Loop",
    "description": (
        "Ship batches of 10 single-file HTML demos to a Jekyll site via parallel sub-agents. "
        "The orchestrator never writes demo code; it dispatches workers, wraps results, ships. "
        "This agent returns the templates you feed to your LLM/sub-agents — provider-agnostic."
    ),
    "author": "kody-w",
    "tags": ["publishing", "orchestration", "vibe-coding", "single-file-html", "loop"],
    "category": "workflow",
    "quality_tier": "core",
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
