---
name: "rar-cowork-cookbook-report-schedule-frontline-workers"
description: "Builds a structured summary report of schedule frontline workers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_schedule_frontline_workers", "rar_sha256": "792a6ed2d24f91e395f0a3f7cc85359400b5fbfccd0a7e7f7793b74c834ac300", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_schedule_frontline_workers_agent.py` and embedded as the fenced Python below (sha256 792a6ed2d24f91e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_schedule_frontline_workers_agent.py` first:

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
    "version": '2.0.0',
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
