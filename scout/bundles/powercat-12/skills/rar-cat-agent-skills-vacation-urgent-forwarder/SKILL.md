---
name: "rar-cat-agent-skills-vacation-urgent-forwarder"
description: "A Scout automation installer that, only during a configured vacation window, scans work email and Teams and forwards genuinely urgent items to your personal email."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vacation_urgent_forwarder", "rar_sha256": "533f53f2a72c2b74cc2cd7496823a3c4d5ae60309c4774d192b6fd7b39c2bf84", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Giorgio Ughini", "tags": ["automation", "email", "teams", "out_of_office"]}
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
