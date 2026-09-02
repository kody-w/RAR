---
name: "rar-cowork-cookbook-demo-data-record-employee-time"
description: "Generates and creates realistic demo records for record employee time in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_employee_time", "rar_sha256": "725ad09ff59b48925a4366719543cceddf00a4db5b0e26106bb4e79eea66e351", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_record_employee_time_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-record-employee-time:2bc82537fee0d8355cf0da0c4a33c555092885b79541c0ce7e46307f5627b957", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_record_employee_time`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_record_employee_time_agent.py` is
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
