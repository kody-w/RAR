---
name: "rar-cowork-cookbook-report-schedule-frontline-workers"
description: "Builds a structured summary report of schedule frontline workers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_schedule_frontline_workers", "rar_sha256": "7c24fece3f70fa43f2120664cfe3f634a46031c5be7c09528bc374f4199d2ca8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_schedule_frontline_workers`. The original RAPP
agent is preserved byte-for-byte in `report_schedule_frontline_workers_agent.py` and in the RCI capsule.

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

Schedule frontline workers Summary Report — Builds a structured summary report of schedule frontline workers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-frontline-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_schedule_frontline_workers_agent.py` and embedded as the fenced Python below (sha256 7c24fece3f70fa43…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_schedule_frontline_workers_agent.py` first:

```bash
python3 report_schedule_frontline_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_schedule_frontline_workers_agent.py   # or on stdin
python3 report_schedule_frontline_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule frontline workers Summary Report — Builds a structured summary report of schedule frontline workers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-frontline-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_schedule_frontline_workers',
    "version": '2.0.1',
    "display_name": 'Schedule frontline workers Summary Report',
    "description": 'Builds a structured summary report of schedule frontline workers activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-schedule-frontline-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-schedule-frontline-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '251e8099fda9fa54',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/schedule-frontline-workers'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-schedule-frontline-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.429, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ReportScheduleFrontlineWorkers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportScheduleFrontlineWorkers'
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
    print(ReportScheduleFrontlineWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
