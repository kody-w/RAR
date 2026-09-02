---
name: "rar-cowork-cookbook-teams-update-report-on-inventory-quality"
description: "Drafts a Teams channel post on report on inventory quality status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_report_on_inventory_quality", "rar_sha256": "807788602993f25139de719a713d8e3243a9cc56c41845c0cba977d29b0a3a01", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_report_on_inventory_quality_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-report-on-inventory-quality:fc05639d486d8e968afe30474d9dcb2763ab5251ba8489fbf97379b388404eae", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_report_on_inventory_quality`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_report_on_inventory_quality_agent.py` is
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
