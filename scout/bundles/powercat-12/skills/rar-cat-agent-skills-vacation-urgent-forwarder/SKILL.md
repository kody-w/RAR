---
name: "rar-cat-agent-skills-vacation-urgent-forwarder"
description: "A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vacation_urgent_forwarder", "rar_sha256": "533f53f2a72c2b74cc2cd7496823a3c4d5ae60309c4774d192b6fd7b39c2bf84", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Giorgio Ughini", "tags": ["automation", "email", "teams", "out_of_office"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/vacation_urgent_forwarder`. The original RAPP
agent is preserved byte-for-byte in `vacation_urgent_forwarder_agent.py` and in the RCI capsule.

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

Vacation Urgent Forwarder — A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder
  Upstream author: Giorgio Ughini
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vacation_urgent_forwarder_agent.py` and embedded as the fenced Python below (sha256 533f53f2a72c2b74…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vacation_urgent_forwarder_agent.py` first:

```bash
python3 vacation_urgent_forwarder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vacation_urgent_forwarder_agent.py   # or on stdin
python3 vacation_urgent_forwarder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vacation Urgent Forwarder — A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder
  Upstream author: Giorgio Ughini
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/vacation_urgent_forwarder',
    "version": '3.0.2',
    "display_name": 'Vacation Urgent Forwarder',
    "description": 'A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email.',
    "author": 'Giorgio Ughini',
    "tags": ['automation', 'email', 'teams', 'out_of_office'],
    "category": 'productivity',
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
        "upstream_slug": 'vacation-urgent-forwarder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#vacation-urgent-forwarder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'e2fd9f42fce2d9e9',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.636, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class VacationUrgentForwarder(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VacationUrgentForwarder'
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
    print(VacationUrgentForwarder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
