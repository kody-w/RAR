---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-geofencing-and-geolocation-settings"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and manage geofencing and geolocation settings status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_geofencing_and_geolocation_settings", "rar_sha256": "9471cbd5a76ef2659f453f30ea411253a4b12b152d6c4553397166b7bdb5192b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_configure_and_manage_geofencing_and_geolocation_settings`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py` and in the RCI capsule.

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
