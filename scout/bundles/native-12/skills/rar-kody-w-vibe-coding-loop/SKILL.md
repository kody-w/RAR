---
name: "rar-kody-w-vibe-coding-loop"
description: "Returns prompt templates for the kody-w.github.io/learnwithkody publishing loop. Provider-agnostic \u2014 feed the returned templates to whatever LLM you have. Actions: ideate, worker, wrapper, ship, loop."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/vibe_coding_loop", "rar_sha256": "931c9224a42c1a609821a5d2fb5b7303a7434fb625d59eae8f8027a7ef7b046e", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "vibe_coding_loop_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/vibe-coding-loop:863fcb7d8c325a97690ff32cb05eb90dd71c7aacb8f98f8dcbd895a4479f76e2", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["publishing", "orchestration", "vibe-coding", "single-file-html", "loop"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/vibe_coding_loop`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `vibe_coding_loop_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
