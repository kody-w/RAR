---
name: "rar-cat-agent-skills-what-to-use-when"
description: "Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/what_to_use_when", "rar_sha256": "e80b02d38ecd766df8a02832be60359de48e852c670e6be8764e72cf25538337", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Gaurav Mahajan", "tags": ["productivity", "automation", "copilot", "routing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/what_to_use_when`. The original RAPP
agent is preserved byte-for-byte in `what_to_use_when_agent.py` and in the RCI capsule.

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

What to Use When — Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#what-to-use-when
  Upstream author: Gaurav Mahajan
  Upstream version: 1.0.0
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `what_to_use_when_agent.py` and embedded as the fenced Python below (sha256 e80b02d38ecd766d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `what_to_use_when_agent.py` first:

```bash
python3 what_to_use_when_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 what_to_use_when_agent.py   # or on stdin
python3 what_to_use_when_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
What to Use When — Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#what-to-use-when
  Upstream author: Gaurav Mahajan
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/what_to_use_when',
    "version": '3.0.2',
    "display_name": 'What to Use When',
    "description": 'Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.',
    "author": 'Gaurav Mahajan',
    "tags": ['productivity', 'automation', 'copilot', 'routing'],
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
        "upstream_slug": 'what-to-use-when',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#what-to-use-when',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd9b46fe1f7df7e9f',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class WhatToUseWhen(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WhatToUseWhen'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(WhatToUseWhen().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
