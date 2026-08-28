---
name: "rar-cowork-cookbook-demo-data-record-employee-time"
description: "Generates and creates realistic demo records for record employee time in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_employee_time", "rar_sha256": "ad7bf24744acc281870413ed39a827dd8d3de8e65a5ff65b58839c0cf21f3704", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_record_employee_time_agent.py` and embedded as the fenced Python below (sha256 ad7bf24744acc281…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_record_employee_time_agent.py` first:

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
    "version": '2.0.1',
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
