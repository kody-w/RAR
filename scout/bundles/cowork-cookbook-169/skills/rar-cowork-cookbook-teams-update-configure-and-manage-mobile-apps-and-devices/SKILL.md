---
name: "rar-cowork-cookbook-teams-update-configure-and-manage-mobile-apps-and-devices"
description: "Drafts a Teams channel post on configure and manage mobile apps and devices status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_manage_mobile_apps_and_devices", "rar_sha256": "136676b859c7a9aedc440b7ade974f1c9e27c73770ce2a7f9d1bb510bed8ceec", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_configure_and_manage_mobile_apps_and_devices`. The original RAPP
agent is preserved byte-for-byte in `teams_update_configure_and_manage_mobile_apps_and_devices_agent.py` and in the RCI capsule.

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

Configure and manage mobile apps and devices Teams Channel Update — Drafts a Teams channel post on configure and manage mobile apps and devices status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-manage-mobile-apps-and-devices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_manage_mobile_apps_and_devices_agent.py` and embedded as the fenced Python below (sha256 136676b859c7a9ae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_manage_mobile_apps_and_devices_agent.py` first:

```bash
python3 teams_update_configure_and_manage_mobile_apps_and_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_configure_and_manage_mobile_apps_and_devices_agent.py   # or on stdin
python3 teams_update_configure_and_manage_mobile_apps_and_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage mobile apps and devices Teams Channel Update — Drafts a Teams channel post on configure and manage mobile apps and devices status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-manage-mobile-apps-and-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_configure_and_manage_mobile_apps_and_devices',
    "version": '2.0.1',
    "display_name": 'Configure and manage mobile apps and devices Teams Channel Update',
    "description": 'Drafts a Teams channel post on configure and manage mobile apps and devices status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-configure-and-manage-mobile-apps-and-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-configure-and-manage-mobile-apps-and-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd27d9d6cc5324de',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-mobile-apps-and-devices'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-configure-and-manage-mobile-apps-and-devices', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateConfigureAndManageMobileAppsAndDevices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConfigureAndManageMobileAppsAndDevices'
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
    print(TeamsUpdateConfigureAndManageMobileAppsAndDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
