---
name: "rar-cowork-cookbook-teams-update-configure-and-manage-mobile-apps-and-devices"
description: "Drafts a Teams channel post on configure and manage mobile apps and devices status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_manage_mobile_apps_and_devices", "rar_sha256": "ad6dda744beb474b01f6fa5455158386787cd9c26a704bffcbc59d0f0909c462", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_manage_mobile_apps_and_devices_agent.py` and embedded as the fenced Python below (sha256 ad6dda744beb474b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_manage_mobile_apps_and_devices_agent.py` first:

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
    "version": '2.0.0',
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
