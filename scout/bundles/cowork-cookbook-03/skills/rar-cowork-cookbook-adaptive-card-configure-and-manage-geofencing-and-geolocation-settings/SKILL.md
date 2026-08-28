---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-geofencing-and-geolocation-settings"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and manage geofencing and geolocation settings status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_geofencing_and_geolocation_settings", "rar_sha256": "862c37d20205f2fa14a27225aa2f5330c5e8637ee509297e7840658af22588bc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py` and embedded as the fenced Python below (sha256 862c37d20205f2fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py` first:

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
    "version": '2.0.1',
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
