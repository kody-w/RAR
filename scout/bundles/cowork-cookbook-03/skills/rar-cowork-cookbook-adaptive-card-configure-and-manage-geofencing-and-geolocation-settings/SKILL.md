---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-geofencing-and-geolocation-settings"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and manage geofencing and geolocation settings status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_geofencing_and_geolocation_settings", "rar_sha256": "9471cbd5a76ef2659f453f30ea411253a4b12b152d6c4553397166b7bdb5192b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-configure-and-manage-geofencing-and-geolocation-settings:fefb7ee3c25ea54346abf2a84ea04e14e66d4ec1e2f38984dc49783cf51df253", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_configure_and_manage_geofencing_and_geolocation_settings`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py` is
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

Configure and manage geofencing and geolocation settings Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and manage geofencing and geolocation settings status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-geofencing-and-geolocation-settings
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py` and embedded as the fenced Python below (sha256 9471cbd5a76ef265…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py` first:

```bash
python3 adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py   # or on stdin
python3 adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage geofencing and geolocation settings Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and manage geofencing and geolocation settings status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-geofencing-and-geolocation-settings
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_and_manage_geofencing_and_geolocation_settings',
    "version": '2.0.0',
    "display_name": 'Configure and manage geofencing and geolocation settings Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of configure and manage geofencing and geolocation settings status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-configure-and-manage-geofencing-and-geolocation-settings',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-geofencing-and-geolocation-settings',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c48609a83346b31',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-geofencing-and-geolocation-settings'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-and-manage-geofencing-and-geolocation-settings', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardConfigureAndManageGeofencingAndGeolocationSettings(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureAndManageGeofencingAndGeolocationSettings'
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
    print(AdaptiveCardConfigureAndManageGeofencingAndGeolocationSettings().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
