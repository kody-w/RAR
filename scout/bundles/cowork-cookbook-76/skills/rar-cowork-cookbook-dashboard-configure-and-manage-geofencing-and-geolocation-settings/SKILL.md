---
name: "rar-cowork-cookbook-dashboard-configure-and-manage-geofencing-and-geolocation-settings"
description: "Produces a self-contained interactive HTML dashboard for configure and manage geofencing and geolocation settings - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_and_manage_geofencing_and_geolocation_settings", "rar_sha256": "8c41ae153dba90e21c2650af4945bb61b50f0aed7279e6689230be2e32331c96", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-configure-and-manage-geofencing-and-geolocation-settings:6cd566c6f6161d073ca78ca3ebded67c8a25f85252285126719142aec4524c22", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_configure_and_manage_geofencing_and_geolocation_settings`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_configure_and_manage_geofencing_and_geolocation_settings_agent.py` is
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
