---
name: "rar-cat-agent-skills-ai-first-process-redesign"
description: "Redesign your existing processes with AI-first thinking"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_first_process_redesign", "rar_sha256": "e3d9ccd12cc26c79c1e294a7e0af59f2d7eb628d2366098ee45835223936c01b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "4.1.3", "author": "Tim Sparks", "tags": ["productivity", "process_improvement", "agentic_workflow"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/ai_first_process_redesign`. The original RAPP
agent is preserved byte-for-byte in `ai_first_process_redesign_agent.py` and in the RCI capsule.

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

AI-First Process Redesign — Redesign your existing processes with AI-first thinking

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign
  Upstream author: Tim Sparks
  Upstream version: 2.1.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to apply this capability to.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_first_process_redesign_agent.py` and embedded as the fenced Python below (sha256 e3d9ccd12cc26c79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_first_process_redesign_agent.py` first:

```bash
python3 ai_first_process_redesign_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_first_process_redesign_agent.py   # or on stdin
python3 ai_first_process_redesign_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/ai_first_process_redesign_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/ai_first_process_redesign_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/ai_first_process_redesign/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
AI-First Process Redesign — Redesign your existing processes with AI-first thinking

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign
  Upstream author: Tim Sparks
  Upstream version: 2.1.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/ai_first_process_redesign',
    "version": '4.1.3',
    "display_name": 'AI-First Process Redesign',
    "description": 'Redesign your existing processes with AI-first thinking',
    "author": 'Tim Sparks',
    "tags": ['productivity', 'process_improvement', 'agentic_workflow'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'ai-first-process-redesign',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#ai-first-process-redesign',
        "upstream_version": '2.1.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ae3bcfad1b711034',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class AiFirstProcessRedesign(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AiFirstProcessRedesign'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(AiFirstProcessRedesign().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
