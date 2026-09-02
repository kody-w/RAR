---
name: "rar-cowork-cookbook-bulk-update-adjust-notifications-and-alerts"
description: "Applies a bulk field update across adjust notifications and alerts records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_adjust_notifications_and_alerts", "rar_sha256": "58659a013ad349021e3b600f3e005f3284e87539f5680ec7e2084db296b36282", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_adjust_notifications_and_alerts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-adjust-notifications-and-alerts:ca9161d4f2cf2b2d3658644c1d63fb1b5d53b3a560bb3cc59b0c2c69578ad98b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_adjust_notifications_and_alerts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_adjust_notifications_and_alerts_agent.py` is
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

Adjust notifications and alerts Bulk Field Update — Applies a bulk field update across adjust notifications and alerts records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-adjust-notifications-and-alerts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_adjust_notifications_and_alerts_agent.py` and embedded as the fenced Python below (sha256 58659a013ad34902…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_adjust_notifications_and_alerts_agent.py` first:

```bash
python3 bulk_update_adjust_notifications_and_alerts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_adjust_notifications_and_alerts_agent.py   # or on stdin
python3 bulk_update_adjust_notifications_and_alerts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust notifications and alerts Bulk Field Update — Applies a bulk field update across adjust notifications and alerts records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-adjust-notifications-and-alerts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_adjust_notifications_and_alerts',
    "version": '2.0.0',
    "display_name": 'Adjust notifications and alerts Bulk Field Update',
    "description": 'Applies a bulk field update across adjust notifications and alerts records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-adjust-notifications-and-alerts',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-adjust-notifications-and-alerts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '968da44921a29dbe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/adjust-notifications-and-alerts'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-adjust-notifications-and-alerts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateAdjustNotificationsAndAlerts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAdjustNotificationsAndAlerts'
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
    print(BulkUpdateAdjustNotificationsAndAlerts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
