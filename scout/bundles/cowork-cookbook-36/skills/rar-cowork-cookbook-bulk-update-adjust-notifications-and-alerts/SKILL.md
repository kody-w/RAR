---
name: "rar-cowork-cookbook-bulk-update-adjust-notifications-and-alerts"
description: "Applies a bulk field update across adjust notifications and alerts records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_adjust_notifications_and_alerts", "rar_sha256": "58659a013ad349021e3b600f3e005f3284e87539f5680ec7e2084db296b36282", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_adjust_notifications_and_alerts`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_adjust_notifications_and_alerts_agent.py` and in the RCI capsule.

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
