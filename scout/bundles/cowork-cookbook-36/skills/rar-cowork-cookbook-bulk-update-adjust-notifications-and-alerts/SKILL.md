---
name: "rar-cowork-cookbook-bulk-update-adjust-notifications-and-alerts"
description: "Applies a bulk field update across adjust notifications and alerts records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_adjust_notifications_and_alerts", "rar_sha256": "16e6fcd3e9259ba1c4e84daa9ce9655707d07fe6c78cfd6cbf7edbccc2675700", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_adjust_notifications_and_alerts_agent.py` and embedded as the fenced Python below (sha256 16e6fcd3e9259ba1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_adjust_notifications_and_alerts_agent.py` first:

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
    "version": '2.0.1',
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
