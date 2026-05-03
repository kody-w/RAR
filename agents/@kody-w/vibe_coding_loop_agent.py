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
