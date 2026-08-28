---
name: "rar-cowork-cookbook-teams-update-report-on-inventory-quality"
description: "Drafts a Teams channel post on report on inventory quality status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_report_on_inventory_quality", "rar_sha256": "bedfb39bfd0b1306017b0fab99b3ed14ed517c0162df146d7daff350b7351877", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_report_on_inventory_quality_agent.py` and embedded as the fenced Python below (sha256 bedfb39bfd0b1306…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_report_on_inventory_quality_agent.py` first:

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
    "version": '2.0.1',
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
