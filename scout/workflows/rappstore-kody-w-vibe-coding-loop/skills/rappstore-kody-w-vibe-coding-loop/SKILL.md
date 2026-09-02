---
name: "rappstore-kody-w-vibe-coding-loop"
description: "Returns prompt templates for the kody-w.github.io/learnwithkody publishing loop. Provider-agnostic \u2014 feed the returned templates to whatever LLM you have. Actions: ideate, worker, wrapper, ship, loop."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/vibe-coding-loop", "rar_sha256": "fcbba7d2b73f340e1bdcf27a263e9f7a50b9d5ae117af80496cfcda287847b1d", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "vibe_coding_loop_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/vibe-coding-loop:31b7449735d04b9f87f902fb7de46eead5b6ea26c35ba1e98393f1419300b573", "kind": "skill"}, "author": "kody-w", "tags": ["publishing", "orchestration", "vibe-coding", "single-file-html", "loop"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/vibe-coding-loop`. The
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/718eZfaSLLvV+HV/aPti10CCQnk+/zO0wYSSEIrAsZ93FqR0IoWQOrp734zRVW57Krq9syZGR93lUgyIyIjIiN+kSH373d2U4d5effpLs699uPl7sOd51duGRV1lGdgWPPrpsyqQVHmaVEPaj8tErv2q0GQl4M69Ae3dfeHqA4b5z7KkcS3y+wCPsJvBkXjJFEVRtlhkOR5cT9QyvwceX750T5keVVH7uBLg47Gk0Hg+15PsexZwg9PzOp8cAnB09kvB6IoDdq8GYT22b8fUC4UtPo0ADTBhA+DS17Gfgl+l3ZRwAfAvPhwYw52519tQNSv7j797dcPdxF4vvv0+52b2BUYuttEjs/kHpBWBPOpg5/VYE1iZwfwZdECVWXgMyALdp+CIc8PBg+f3lV+EnwY/Pd/xxe7PFTvP33JBg9/7F7GwefB7av7g1+/+3J3G/1y92Hw5e7L3fv7JL/45bv3X7JvC6Pgae1nMOu2xS93z0jDP16e2tEL8rdRQHgADPXlrgJ7SvyPQZT4A96QxIHnp3kFOH9H6qb6wbHKs3uvSYvq3e/fT4B/ALHarhuw+BN8blzXr8CHD6/NfNzkp2fivzoxyqq6bJ7Nnj+6Q5AnQDXQgR59MIf27x3hfiDUg0uUJI+Sj0f9xgZunrl+UVf3b7C7kYKcvgosRxnCWv6qaGtJMe6hMe363U1/n2+/3v9A5I8/M9PNA1+Y6UH6H8z0KMiDmf4G9OCX9cAtga6isz9wysgPfv3RTnlTF039tbDr8EeCz756QdV2qjxpan/QL0Tu7++/P61I7xSILH+skuZwH9Zp8oJ1Ejk/sgRDT6zqsPT9++MLzwIGAQYGqqwrsPwrs5Z1Q6ME2dAfFQ6ofAb/vf8PeuSjpX7GI9+9nHObx0YVUKcbAmeNqpu9BnY1sAdV44AgB0LI4F1hl3aS+An03Rw4dfkQpqr394MfNfWM8nogr40+0PUn4bZmANhdskEEFJmD34BLzwS6+ktC71/dWi9k7/zWWltx2ldaE7j5oyGemerzs+cPDx78+fbrw3Mn/Pzs+R87K7co/cZh+Vr71788MSAnOOCspI/qef3ERJkHlARCCuT6BUh0d3/MowzQgwoZDIFfZ36f1PoHEE+fiXBfFUlUwy+qd+9/cNDaPlQ/igjHngQMCqC6/lh8PIKng536PwoHvNeNfyTSDz5RgTH7w2Bpn229z84PJF85af/eE/Nor58M4jA0A11C7wWp3PXDPAG5v1eIn4EcHYFgBM7E18e0jPwOI88ffeh5g8kjKrj5r0YpCnBgg5MUkTK4Rx9+/UjVwIj+5+9NBYe+OZMBP/76KufeUEC479fDkW/L4ae3V+cl2Pv3y/uhh/Uk+cY64E7Q9z7/6GNw8Jnot4FHOHVqcqBbcNyiGkSQCgTgBJzlt4VzgUoPedl+z+Vx9InNzX3foOFFQRC5TVL/QOXb+BMd2zvbIEV7b9KCZ+gz/PGWKeDx+Nz/fEsakMy+QsCTAZl/EOj5V08yPc97b8oVRocwAf/V31N8Gn7mDNEhA2esBB7uu2EWuTaI/36Zvm2Dh5DzGKs+Pz68MR2cF3DIx98L8jD4TQyxHxiMHx0jBz5SFb4bAZM8k6yCnIBF3pbuRhl9jR36gh36V3Sw1+hgL+hgb9OBFcFXmHS/RtX3xJ5/842iBUZvSRr8faYMmJwPIK6FH3rYCOKn/2dM268psMtX5wZKf2T8/bfPmbdPvOGMjw8zHgXxMw8IA1BD0WRuCA/y6zL8Q9kVlj4vUit08RcZqx98khYej3F/ftD+J/YiYYHpX50SBPQ+n/7eZ1Ao70NW7cndsiZImP13f/xH89Rt5z+XpLQmu5mmCv0EHoRTAw8CzEtnO4m8vqx08zSNQNYtmgr4iQ2sBXBHFLRvFRg9rT5F6bygfNU51eRk5ik/9Qr6/E2N/5BZYS37z1WBf7O/Hf2HBY/+d3+4H/wSRGVVfwQJHh69Ms+DOi8GlesD4PPLr/9RA972+HMG5K6+C6sagCkqENtqv6gg6Ohz6/2AswE2h4ODAyioqv7u4NKHghzoYEDJ7NPH/griqbZ8q3RM7J7v314PEL+/PvyoCx9abjD+8GezHjAJ3Jrwds38bf4t3OVfvfxPCpVv0+fPd9lDs74yh+51S0B9VV0+XPy8qKjfLFi+cVBKH6YTSDuFeoU8wia1s/7gXGwASSDSBlCyzMERu/8ziu//dOsgc/Wn7Pc3rhoG347ApweP/+MNgm+N/5RB0Z816GO1+C82KdCmD/08D3plA6M92gtUHOD4lkAdILk8L5F6W3iPxetfG7WvaZ8K2afi9n4gN6kDiPZeAjFVNXgOpAbvMljE/QT9sx0ltpP4YDkoi3WYEQGv3gEfpPT7c72WuUEKoghg/xi9QDzwf4LFo/RRld4PGE0wBIYSPwGabtJ4/uCXh4L7VmA/Fda/QKbw6rG9Ke5f765P9xDf3Ux9ufu/EJ48mfT/3SZ8d8HTz4KP4Mt/i2NjP+vYFkBQ/1qntmCJ2Hv1g9uWfpGXdTVwIOZ/KB7twdKPW+AmDxXkoMirGhrsr73h1aJz0MCb0tt1y63WfbqGvh+ofU1lZ+1jSfYTXODd2sAHJ8TzQNi9VWGPbvsg+o6SRJChysitB2kOHPHhRvPog4Em6ys5iA796t/gek8F/eBFWfTpZU0ERu7v729f9Q//Fqeb/KzT6W/BvH/a6TYPiK83yodBCbGhX8EwGvgwTpZARS/x4KWPoYzw4QEVDkxN/DcY6wHVDp7w+qeHx3GPyNH+Jzb4hw3z66tAp/QDv4RI+MYnrOui+oQgLxs+AKohb8HgGLjy19R78JjbIqQfrZBz5Pgf3b7d8hG63seekr4SRPE+fXkz8D0m/kv0+T3y9Msyf3lt9eXuIZHAScGXOzOLM3ipelM60P/t4f+Uf9wPjLL9uS7Td1z+eA8s8RyywjbTf/3XQIrcMq8AwB7oLojo0NHqCBw6sEMD1iJGblfw1P/2qI7fYOUIw5LnB3aT1INFCfIlRGwwTEDwBhLFb///Zp3vVAuF+g3IHwLqeRkdogyU+/DebHC7nQZ0QWp146pJP54hacD24c5OY4SBaxdVk/j/M/gNEv16I/oVEv16AwBFC2X7kgGLAHj10LfLS7uMkvZ2E+60tf8RRFsQzso8SWD87oN4A5QFNtwH+psaXIAR/Qc4n+TwXqJHFOAg+lWe9PfgsFCD/gNQQQl2noO0DJEMUOAnSOy3335z7Cr8kt3addjg1s2sEDDhSeDBx48FcO/bhU3mu2E++OX3P34Z/H3wZ6t64pCHYlfVQ6sSSLjU1/IA1FxNCtHCANrat73eHL//cVM8lA6AsFt0iPx+MaD2zbZwBzdrPJqiv2+HJ/CB0/d6AyUL7OQBIO1fIxievmSQRN9buESgCnpQ4m3xTfWPtr3xgTapHnQI7BQA2NHP7d0KGtMF9ROoBILBk6aeErA9CGGW9fzChzdULrzasOtvJszyelCBiqIK2g8goYKtQsq/ObCRAJSTfnXB9N8GEqOA6iDvuyJ9oAWTwOr8diH14Jy3YUCk/AX4GP1IAsDOvhsMIV0RlnZ1a5EE9s0jYHXxsB4QtweZfxnAZq8PbdTXOr3nvenRjxn62THptwjErP6ZtjdkxpagmL7JAxBET/lJI79UNy4V8s2t7wePzfdnjXAgxE2bvQVgAfcO7jW7dZV6Gu+fjH/zvadTDuOhDy/aoLuBA/JWJx54lZdDGA+wcGrHfs8GpqQKdp38JPgfOOWxrHhw5puP3dDrrci+NfQfmrUQ14Cqof/Un/JHg0P1DHqQBLTyJYPuDZH/u0VU840zYPIiSoA76ezqw4Dq4G3qGngdBVItBfQAVBq5HwbrJLFT+8MApOj7972yYf8e7MLtDyV0+vrT4C8yGFj1+DYBjN+3UP/QB37/Q2Jr0DGJ/lg390XtU2H97q0Kum8g3RLIu8deWhI5H/qu7Ptv1L8r1uBlxVOjMX/eXeyp3dLQux7AQTKPzbr3T9S+h8kfe5j86Ff93cetVQOpwVx2u6F6/xKb3KjdrsogCIJh5+nKDCrghowQCIyQGxqCNKGKX9flE82ggbdvAAJ+dNqP/YUNvGrpacI6qMybzINvY0Sun1X+3acMzP9wB6Hqizc34EsaIDCkfg3iJ3zBA2gD6KeO/P7TLavDp+9fdrHCCKr3mVYenbx/dSRr0rtPf3u4XAADNwPBh5v6wRNUHZQRyvDrh7u6LaBwENtnBwgEHvspL3lXUdoArnn5d9hi+TuMi3+/2fDuFTrfIfWXxOYP3zwWj73/vbvd8U3Qj0Ge94D+F1BnmxU4HU776EL3r3J76t+8ZOX4AFAAJf0dRDa/TH0vAlv8+2N751VqvRe8pMTeLiShvZ8O1rubqT7fdA7DOlQtEJt7eV+JsQMfRPQyz/pE/MurW3nq07zkrz/r15T9vdXT5G/94IEDYEn8KumHzgsk/MZ36J98h73+XeS8FJTq782A2fwrkBSiOTAN4K326aWsm2feD9gbVvw0+OWxW/y6Vvqr0lc0ArL97RoVKgD4rp3kh2cEoMkPYCGk8O1W4hWBv3vv5AIy1XcvNPSV/C2tPr2a9GT525z3r4r9cD5e8GO+e3vmdtf4yOxn6MLY95Lqynds56MLoUYE+3IQyZVvrq9eUWdhu/7HyoehCeakWyfmUSAYOt4QBzY5X9kljL7PyfVvEYDwW4BwCV8IeY3Ww8XFq84Gu61/zQbOep00rMtfJfy8H/fGhO/7Zq9MArNKkGYAOPJgEH4I4d9ibO7AOqj3ChBGb+/n/Q7Ku9oG5bwNn2/I+QbxwII3sd8dDNMPKPTrrV8D5YA1R/96ZH+kvtogm0C0+eyrA4TOX2/I+e4TvJP8cAcWgxxoJ1HXv3N4d+P+a++7D4UboAAO78cKomdkfD8ClGAshiLHQCfPGMDhyOvnw4dPb1V7n7CxM51MyCmGe6OJQwazaUCO0MCZev6E8EF1gjuEb6OEi+GOPfbJGUZiwXgyJrHRyMGnGMxkoBBJ7QdeyBgqFkj5pL23WN/dplWhjeIEmBe4jmNPPdSZYgE2Gfljx3MDdAp4Yz4ZTG185JAebvvj8dQOZqMJSbiB69nobDqbTJ0xTCCPpc+N99fHMvNRwxUAXC60JIQdj6jgYfBBf4Hv9Vnc+wg3AwBEn1x6nypgq6I8Q3K/PxgHugoxAcv4SSVQtz8MMt042FZ0WnExvI4VSd0uV7iwo0S9wSNGKFajui3n470bafhWT8/RxWRUjKs4iY4oKZW6VdElqjvx7HI9HKIGvm58Sg3VnNnUjuw3rEWDrFUQwyYosxNfNhUhL6paS7ndqdHKub0/yYeo2c/5CTqfIsMOGS5nyAhzLhrCueZoxWn+MiwUM2mzkddOSZs0JR3jz/GJr9SuxWn7PGZWrRteSkXdaKqpkdcuk0ajNi+4cB5LFxnbcv6JU7duaYeddiVWzGrTTmlhNo3PXbrR8KPuZYvN1eSOssgeRsPO2ITGAff1MWGrOLFypkkYa0HLzVpR5p05HuT2NtxazYFZLlaFtDH19Sb1sVMo4Al+SXaMxWTp+BTSWpQl666dzkUxshTO3F3F+SLGnSvOICataYlzTrXj+WKGgkmdN4lls3NF7xaaFC53SxzvJLM6LtSz7LTMJqa0/YFRLTUQIt84HgWxtXRdI4KxMj9hQsXWS+lqxaF4wBFeOJIBbuPzhb83FFuZ7XemOQv1UJWv8yqgRfogWDttyHfCUNgX2qLYdSJdSLRkoSm9nwP/4S9I5YQVzl7JWGFwE8ScSqMOIl1lhbau1kOS25YdgSDDBDGOFY7WlsBMAinyda9txqjTjdR4T8TCqNXNmIuDZIEYyLxMFUNuhIUw5vNDtVrtSZ1MR2q7MLMlmwunrcZz02KtMQTPN7PjSC3YqSAVi2jF7bmdtZgSYS0osyz3r2OGobj8eN5dzGIjHPLjXrPn5nLFcdMKJ9Zt25BVYogxjq88CjNQ9bISpsas2Gs7jhnayqmI0uWGWJet1uxLSd0hMaqPpipK6oewHSmBsnAnyHBuUafdtiiE2PKTmhbnV6eYK6lbx2uB2exT0ZUCenyaC8R5XbWdzCALRmnQbrdWs7jcTDJzn4gcYkyijbaelZ3M+qZdCGNUR4wcnSgjW0V2WkflxY5NWmy0nC2bY7w7me4mHzPKdLE7xKmU0qkUR5EgRMRiJg6b1imR607eZV7iEOsdmc1OssK5+05j6Oa4TFbsmi2Dmds27Mlr5+XRuUSbuWTlHaboQaMqhnHUC3JbH9mR3AY4fg2u03onmwpKnEKiVjc5Hhx1QznuWOJEKMD7HdpaRLO17o+VRaxGJ1d2gVuF41WdTMY4RU4pdsTTk3irMfJJpik1F5G9EY39bcl1u8hRO2pVbqzRmnPmLj1yj4dkFjWbvcs6jXluceWoZ8Jh6841teK0SHEoT9tMRSt1Y3Rfb4p8t9hNNsSFs1NNx8cLzZsszXqfmfQ+aUenqvWD+myYJHI5bCXt0urjKYpVQ5R1O3KFjQ7lalcc4yXqXzdLz4waWZwMa9yjwwQT5C45xJk7lNmdlRU1I0fOvFzvzufFOpjSIxWjh6EbshIu5MtsbndIIi5c/ZQKs9Vynx4laZyM9w4r6/SJ2M8lJ4/OLLJtLqjMu3SxWmQEssRNVz6056w+EacrP19kOmmNcoJZYWhDYbW8NvbjDStqa4uYranNTjtehGEaq/RRFdyVWR8ki0I9epnJFy8rrr6DIwFf4NR+TVdoMiSYTTGJTFW1F4yrd1N0Msm6mFCOrK2jfHtl29GsEQ87JKNo/noqNaXMKxzRjHR1xm2PweNYjTEQOs4sdjlH9mEmG9sZw0o0oVb+PiyIbBdgUlU2prsq7PiS76mgmBzyeDwNvJWfniJruAMh23OvZGYVi10lXA4kbVY6xXSzonQZdLFcBpknrdZie9IW10hcLTVtubOK0ZybU1PFWOq8H3cpy8VSxLJlvRrPrQhEC8uwtihV1pd0nzkmQdbBGuzsYitIO1xfR+TamU0Vy9FbxQlm1II6aM11uZDmISHYarpd2tOWpHdnNrCqS2Eu1Chi1uK45bhRJp18akaYApZr7mU6OSOprTFBauRCy5grK/GOOalfUV8wV+jWltccPUe745XdXQiKpQrG9g88YueL2LJd7ipyB4rW1lNsjueHaLE810VGW6vZmKDVhRR7InJaVN7O0LecZ+OJpdhXVaRdz0FYTJ2rY1IY0ov5ZF4XFMZvx4cA1U5MPHFLwZVoS40VbI8qc1/wQ/EyZybDfZOI3dzPzMt8OLkenJOs5tekXNPxSJ0qkULaUs6sz5K2Ujl1YTJhbhwIb9QaizkaS0siXs1rbS8c0XZ1DpNmWakS65Pzcuyk5Qgvcd0OFSEyKqXcznJzCNK0SbkTBokKpph4zpWuLobAEmTM0+lMt1FZ0q+hsNU3tKoJ5z0bynPlomTn1d4y+PlalKNRcZCj8GLQvJLb+KKcycX1GLOuOj9SKStiLdusFC5qRjvXIkeFF5uVZY43k3Lpk9YcE31quoq5PEZ5TpNPfHKmyjZiT4o+i+zd8ryOqZjbaTG/9odHOY8MkfH1ld/NuEzaFkvr2p5yX4oK9nigd7o51evQIaZNN7sSSjfanbsJsd46geQmbZEKrY53c1X3LWkSnEvVMY6HyzY+DNs5KR12zeaAurtjpA4TdFIz3Q71rVLA5hNSKaTtkljO0aFiXAgsM5ouQsOZh+Ezf6dai8XenifJXlrj8wtCxNWc88xLe9kKe35P13FK0aUtY7NRp9iIGZ4ZUjg669VEzsMDy5dqvePYSyuoC65e8VS3OF6Y6Ya6dgI5Ey7cuVotxuywbYX9ejvFEq6hybnPl+OhOxUUI0mJrHHxUrYFAwtmFU95al3v6ADtXIkxu0Uik2uESc3QulLhUNCHyaGllaRijp2uAKTE2TlR8qEq8UrCq3EuDMXxzGLTzWzp7bzTtUnDWYBp3OWsJLTjc9gZESilFrfOrrIS6aA6WLZo1E0Bdjm/6BIuluh1TNGrlj2f/AyzU0mQdsjVd/fbLCrPxMWVLo0zOSvj3Y4VY9896yO3Tfa13expttmP3eECxYohCNdImO2M81RilzNz0mo1OZ6QddlheEt2dLxHitkUH19Fv2293Jmo8rA7G7WeaHOSb1MSpZPUn03XIwHUFG2X+P5ITEfOJkvNYV7amuM3O2ZzKOJqjE+Yy2ytncVWupin/RlAwNmJIqV5pjGjeIj7rgrgtU94KqfsGpbDhnURRrIvXMpzs8MNRgsMsG/9SqDC1RWopmR539Pkg5yXS+ccjMbrY2NaS4UuzoI1IcIzMi0RzF9QOnmOlO31gJdxyjm5wl9GCqp1Db6tK7NZnVCL4JXdwTUoE+GVRijUZGQcyXpdMQFhY1mV2AeFlReXkLBtolnJZZe07Ry7LC/FhY2nzUhit/4IHO7AJ3fdVrwQwXFNrJVyihKKQQ0rK4i8oZrq4oreq/pR2CJkiAT+SrXwocpw9ia7tm1MUmKGs8T2Qq8FQZ/x0nCezIaspV9mq83FJmqZ8aPZspZ4R5uiMjaaocNmyEsCEwQjnEAyD+hPDs7UOKOmPJ77M4Jz2tkEua63zHJnM74jzDZCnavYYdrEu5WAC2ph6IU7Wx3RMEGotjLnSj5EZo6I0/llmHLx1EqolV5J167NNWmzo1yRPsX5Oqe0dUex10gSThdpf1m0CA7+IsKC0oaGn0yq5SXScdq4cJG4ESu9zJExiyGBXIGMF9apskQpnedFxggo070sdv540sQbcCSPLeOK6KFdnrbSqnLKlOFGkYIOY6OmoolmO04YVHQloSQ9Z7eoiqkFH7gdNQLWPZ2VOkqKaK5Y5z3KcEZKRVVSIiTL8bmakvSUNqxhEHfT3fVQqeiKN0EMO6a2D/DTwsiZhYiTpFNUx2xapmvLIf05gB1kjos6FfBdbZnxxSwJg1OZEndmJttG52NwpeXN/GBsFnEkXa9zcmhuquF6GAQBs912Add1JLvohqIxpScryb82Yu2Igu5NcCfDmaG/7Gb0cHm4aAqIqyszOlz4ICsQ8xQo3X6G7GjumLTqqZomzbjDhB060gHSxkhiH1tlEo0R7CQGMcKGoGDJl9z1ZM/4hDaWKcozRMaJi8zD5qKfY1G1ZfDDomVH7dk5YOwm1aWtZtCr5SpiUs6kUu40WpB7a5E7bcGSbcEg1nZ+Wk242K5zE1OcTMvHeVlbFzs+TdsWlL5Y6qnWvonljTvdqX6SqbmC4ex2e9bqRZw1srwfYvsNVwF4w63A99Z5Iy2cccflmxwkCbpwGWnabtz5dnNe83pHn9vUS7NyfVHYLV+TAacFQFK6BEWVZdrLRhzu9vMZr89Mn3N473K+BHHExKJ5WeAGMfcmTdg4sxEnzpwkU0xyvxHXjVxESUxu+EiigqMQTXhBDUXaphqQG+XdniTHprlBCXOzarqDMpOtS90cZ2emC4O9NyodmrC95dSso6lDTtrYm4zjCUPuaeQ0XCurcyDy2iqSa15fyufNHE8TepWzvt8cw6Mqk7mrghyiRmFHX3bpqlOzaG5GnX5G7KDF3OhyDvluiK69a7SNDUyhSlB/qHJE4t7Msv1MlJpgxl7dzQlZYFZ83dq6q1DryylEkx1ZWWFGGUI73dGF1Xn4LCbGu9UEQ0NabDH8dNKiK4PsVWU6wZZNvDIVnd0cZWsyHlP40i4QEUAGaleYW1DCmb7RzZhxjpLxivHy+qoamibXk8lFQCZNm1Z8ShnTlSnZdbDkRY4pLS0zVNfIVpMj6uKLdGYFpSA7jbfHBFAgrSrVQA9XZNgts6XB7VY8P1nnYX1QdF3cjiMiqC8cjalqxOrbXbTySk8UyO2Z2u+2gVZEvAsCEyWAvLSoyflms7YKRZ2cSCmYN3t8t1ypXUtxq10tEbNsu3FzvvQX0WjnxfaJP9mH5YhXLWM3KrbjC1IQ47PCmbIDyk3CXKPZcRVb6hhHyxANfAlU9vF8yO2G00gQY4pCZWGanlJJoux1pi2jtUFamiVpVLdeTee7brMQ97v83Ojd2ZkGxSiKmbPvaBdtMwuRGjd5QRjW8aGRihFEiuUM2wbbGtcT2RGky2XU0qQSbWdptJlywnXrTJWjLaY8exKsQj+Oluku45M2TrHDpq5PoXMg1aRoPCxrUGzm2BTCY+zUNDLRW81Yb1nP4qM/ZDk5d69Bsw0nzubIToJwRqyHa/sgjGcbFaA0S3ao1bDN1+a+jIZrBkQHrz1UJdFgSnAZWzuKPhAVvw8I7jjaVvUu8XysjrQNb01zY076qFexLebNhHbHO5GiAeVwOidqBp47ow2rtRP11Cw5ueIOV7tdgDOCjdPTusPG7VrYaUQnMWdmJIU1LXeySO/PtnAtM4Y+7pU1U++patUgEYLMRuPSPHV8vRpty4BfE90ZmbMgsrNTlfXPyCT0g4CjV2m2toeoF27x7SrthDSXHb3wHUmuXHy+wgEoCQiZOI4acsfxMj+sL7PNKefAlnTM3XfeZl7U03w+3jAx5jrdhNwGy1L2hkeAUaQIsSkVk0KSRSy/bsZuSSQHUGvTNN4EHGkM01WT4paITA5DutMPIo5XVGub04poLwuGs9jpeetEsX+xd+b5mjKL0yheSM4i8q/IVVtE127P0doQu9JptacabU8PV/yEsScT4YBx8jidjbDRuc0bZX09dbo5GldupR0Zv8h4TkaRCzhUhbDKJvoxczfSekrMg4SZO8skWE/0aDTt3LXLlRp6mEr8qdW3pLIMWW13SJKCXdvrqzBMcMxkFrmNanSVtSMWQZptoxqbJbrpdJ7D/ZWFKCvc0DrxQLCmuqm2M1m5Htm5p103hNmKfoEdF8qqOsoYm8ySVTSijmHHxUSmxVNNHItndKzVRIxPzzPymqPpObmmuGzhabuzd3Yoq91GEHEgdexs+IbEQ4dep+mZ5w1QNyDe2Rrbo8Uq1EMTaDcAmGWP40gy1No9u5eS8NDOZXPETgg8ak+mwcsSuS2ybLjXlg6v6+gmDqtSVzSD3djePMcjZmspIlono0k4O5x8my0OBrXnl6SnjCtc2UR7V99MT7pTKV4R002K6qMCPZRcx6y05DgmW+WY0W6OoryMr8uSUqmuMKWAMIoUvSw7JDuLQeDPZA4waJKU3/MH9+KhErvYc12u1nqUVBbGXk8pq4wPV/aYWUN5dNyPz0tw2mKNi52mpe1zJRyHeK1JS9dophzOtcIk3paJuFvNo1bEbGsEapVky+GInU5HShLa5RqT0UxHRBkdYs7xOvHq80g6jVvMdLyFNvRMit5yzRCvUGzSRZehvxKOoJTrzu6GO+BdONu7xOh03YlzxE8iZHZM1MzCx/tEvqrz9XA6NQqRVEWbJyQUuTK5TZ14p+SJqbhI7KWwzku93jPD6blpG32/UPQKWfrMyK1HCiMD957ZdFob6bw96fYImTHXxdCOY9Slq9zHFpJNbujpapaNEYQ5nJppo6G450vVdUx4wVwohmuO9BFip9iVfloNURun9tl465jHI1p4J13dYnltXCeVFjvL+RTxmzUd+Eo1PeOelwzdpJSuq2VZevmp6YwtHTXgKMiXmaZcUpPlg7VxILXtfnLR3HBiFMsG32+xdBF50ganjz7VeFk5UqwunIRbg6nI2WxLDwM+mbn8sDXsPNxye93hAWqpJwdi143H+M6akwq3d7OMt4qrNwKFPn3GNDyIrZnnlPGUFNksSMcJtj1JVTlhNSWxo/NpHUeOBSDJCo/sGD81KoXXaxrok9XEGcgeVUvJDrZP2WgjdvImOi3xqCq7iUZW22AdWAcbl1AFS3KAV5m2CxjhHC5jIr2sktOasFcA8xZnS2HPrZ0zPI0SUSeGG8G7JKQWmPbaWg6t8opOynQnXwJvmHWIoYxJO1E6fJG0BCF52nl02hJ+mC8Dix6Wpr+9UA7KJu5653W8VQZoUfOUEBEEdpY2MrEmTmPKY84su8yVPY50WJJF9owlR+Omq8ULvAlCELukDGOMsyvT7yJ2S5M00sokRhw1s+AQRLUz4NcIv4wM0jF2tjNShFCRA8otlsNkumfactPw/sgg0XGbbZiiGx02s6OpILh5Dvj5cjPJA2+Dpq511DxkIksCiuvH2ZSiqM93H+76N+PuPo3xMTH9cPftJYs/7Rgeuqj4+rByQs5Q+CrIv6oFdutT5WcgR+b6sItY+rb3qef+6W2hfv1wV7oREODWU7w1tft2XlXnpf/x1sH7+EoHr2pvb+nlGfzX7489tVt7+G93395tu4NvDsB/llGXt47ah7tn1CChb//XkY/whZNnr8ac/bK6NT+BeEDAP/4XPrcbYIxGAAA= -->
