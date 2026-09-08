---
name: "rar-cat-agent-skills-ai-first-process-redesign"
description: "Redesign your existing processes with AI-first thinking"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_first_process_redesign", "rar_sha256": "fed0d3782855d0c5ce6e0aaa4c9ffb05a91f85f2a156b281c18d7fd7cf3afaa0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "4.1.3", "author": "Tim Sparks", "tags": ["productivity", "process_improvement", "agentic_workflow"]}
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
