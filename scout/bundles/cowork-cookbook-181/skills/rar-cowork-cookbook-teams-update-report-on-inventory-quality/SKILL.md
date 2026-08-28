---
name: "rar-cowork-cookbook-teams-update-report-on-inventory-quality"
description: "Drafts a Teams channel post on report on inventory quality status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_report_on_inventory_quality", "rar_sha256": "807788602993f25139de719a713d8e3243a9cc56c41845c0cba977d29b0a3a01", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_report_on_inventory_quality`. The original RAPP
agent is preserved byte-for-byte in `teams_update_report_on_inventory_quality_agent.py` and in the RCI capsule.

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

Report on inventory quality Teams Channel Update — Drafts a Teams channel post on report on inventory quality status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-on-inventory-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_report_on_inventory_quality_agent.py` and embedded as the fenced Python below (sha256 807788602993f251…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_report_on_inventory_quality_agent.py` first:

```bash
python3 teams_update_report_on_inventory_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_report_on_inventory_quality_agent.py   # or on stdin
python3 teams_update_report_on_inventory_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on inventory quality Teams Channel Update — Drafts a Teams channel post on report on inventory quality status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-on-inventory-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_report_on_inventory_quality',
    "version": '2.0.0',
    "display_name": 'Report on inventory quality Teams Channel Update',
    "description": 'Drafts a Teams channel post on report on inventory quality status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-report-on-inventory-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-report-on-inventory-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c606282a0b7caf6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/report-on-inventory-quality'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-report-on-inventory-quality', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateReportOnInventoryQuality(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReportOnInventoryQuality'
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
    print(TeamsUpdateReportOnInventoryQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
