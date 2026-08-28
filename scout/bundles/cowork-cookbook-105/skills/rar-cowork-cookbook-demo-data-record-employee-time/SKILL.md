---
name: "rar-cowork-cookbook-demo-data-record-employee-time"
description: "Generates and creates realistic demo records for record employee time in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_employee_time", "rar_sha256": "725ad09ff59b48925a4366719543cceddf00a4db5b0e26106bb4e79eea66e351", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_record_employee_time`. The original RAPP
agent is preserved byte-for-byte in `demo_data_record_employee_time_agent.py` and in the RCI capsule.

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

Record employee time Demo Data Generator — Generates and creates realistic demo records for record employee time in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-employee-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_record_employee_time_agent.py` and embedded as the fenced Python below (sha256 725ad09ff59b4892…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_record_employee_time_agent.py` first:

```bash
python3 demo_data_record_employee_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_record_employee_time_agent.py   # or on stdin
python3 demo_data_record_employee_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record employee time Demo Data Generator — Generates and creates realistic demo records for record employee time in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-employee-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_record_employee_time',
    "version": '2.0.0',
    "display_name": 'Record employee time Demo Data Generator',
    "description": 'Generates and creates realistic demo records for record employee time in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'demo-data-record-employee-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-record-employee-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a5f456f5224ae16',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/record-employee-time'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-record-employee-time', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataRecordEmployeeTime(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRecordEmployeeTime'
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(DemoDataRecordEmployeeTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
