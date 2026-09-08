---
name: "rar-cat-agent-skills-ai-first-process-redesign"
description: "Redesign your existing processes with AI-first thinking"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_first_process_redesign", "rar_sha256": "fed0d3782855d0c5ce6e0aaa4c9ffb05a91f85f2a156b281c18d7fd7cf3afaa0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "4.1.3", "author": "Tim Sparks", "tags": ["productivity", "process_improvement", "agentic_workflow"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_first_process_redesign_agent.py` and embedded as the fenced Python below (sha256 fed0d3782855d0c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_first_process_redesign_agent.py` first:

```bash
python3 ai_first_process_redesign_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_first_process_redesign_agent.py   # or on stdin
python3 ai_first_process_redesign_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
