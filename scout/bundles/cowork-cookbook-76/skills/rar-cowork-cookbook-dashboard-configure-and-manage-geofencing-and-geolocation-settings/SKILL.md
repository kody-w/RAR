---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-geofencing-and-geolocation-settings"
description: "Produces a self-contained interactive HTML dashboard for configure and manage geofencing and geolocation settings - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_geofencing_and_geolocation_settings", "rar_sha256": "8c41ae153dba90e21c2650af4945bb61b50f0aed7279e6689230be2e32331c96", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_and_manage_geofencing_and_geolocation_settings`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py` and in the RCI capsule.

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

Configure and manage geofencing and geolocation settings Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure and manage geofencing and geolocation settings - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-geofencing-and-geolocation-settings
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py` and embedded as the fenced Python below (sha256 8c41ae153dba90e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py` first:

```bash
python3 dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py   # or on stdin
python3 dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage geofencing and geolocation settings Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure and manage geofencing and geolocation settings - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-and-manage-geofencing-and-geolocation-settings
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_and_manage_geofencing_and_geolocation_settings',
    "version": '2.0.0',
    "display_name": 'Configure and manage geofencing and geolocation settings Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for configure and manage geofencing and geolocation settings - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-configure-and-manage-geofencing-and-geolocation-settings',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-and-manage-geofencing-and-geolocation-settings',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd62f6aaa373029a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-geofencing-and-geolocation-settings'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-and-manage-geofencing-and-geolocation-settings', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardConfigureAndManageGeofencingAndGeolocationSettings(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureAndManageGeofencingAndGeolocationSettings'
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
    print(DashboardConfigureAndManageGeofencingAndGeolocationSettings().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
