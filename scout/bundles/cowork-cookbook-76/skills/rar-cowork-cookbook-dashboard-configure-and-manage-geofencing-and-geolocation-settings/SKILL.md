---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-geofencing-and-geolocation-settings"
description: "Produces a self-contained interactive HTML dashboard for configure and manage geofencing and geolocation settings - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_geofencing_and_geolocation_settings", "rar_sha256": "1eba02c12fcc52a1384e2d4f77dffcf201641c68b6dc40b21eae60f6d187190e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py` and embedded as the fenced Python below (sha256 1eba02c12fcc52a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py` first:

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
    "version": '2.0.1',
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
