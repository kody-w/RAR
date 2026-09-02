---
name: "rar-cowork-cookbook-teams-update-configure-and-manage-mobile-apps-and-devices"
description: "Drafts a Teams channel post on configure and manage mobile apps and devices status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_manage_mobile_apps_and_devices", "rar_sha256": "ad6dda744beb474b01f6fa5455158386787cd9c26a704bffcbc59d0f0909c462", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_configure_and_manage_mobile_apps_and_devices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-configure-and-manage-mobile-apps-and-devices:b30610ba803dd5c89e03b67697230473bd10a63fa509e7f8c1546061a4155abf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_configure_and_manage_mobile_apps_and_devices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_configure_and_manage_mobile_apps_and_devices_agent.py` is
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
