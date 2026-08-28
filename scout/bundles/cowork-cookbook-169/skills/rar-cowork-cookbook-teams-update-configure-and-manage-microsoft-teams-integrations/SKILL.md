---
name: "rar-cowork-cookbook-teams-update-configure-and-manage-microsoft-teams-integrations"
description: "Drafts a Teams channel post on configure and manage Microsoft Teams integrations status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations", "rar_sha256": "b1aa0e40a1993d07fc48a0af5a1f08ff511f3b5cf04e45648c7bada886d5a9c8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations`. The original RAPP
agent is preserved byte-for-byte in `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` and in the RCI capsule.

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

Configure and manage Microsoft Teams integrations Teams Channel Update — Drafts a Teams channel post on configure and manage Microsoft Teams integrations status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-manage-microsoft-teams-integrations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` and embedded as the fenced Python below (sha256 b1aa0e40a1993d07…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` first:

```bash
python3 teams_update_configure_and_manage_microsoft_teams_integrations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_configure_and_manage_microsoft_teams_integrations_agent.py   # or on stdin
python3 teams_update_configure_and_manage_microsoft_teams_integrations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage Microsoft Teams integrations Teams Channel Update — Drafts a Teams channel post on configure and manage Microsoft Teams integrations status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-manage-microsoft-teams-integrations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations',
    "version": '2.0.1',
    "display_name": 'Configure and manage Microsoft Teams integrations Teams Channel Update',
    "description": 'Drafts a Teams channel post on configure and manage Microsoft Teams integrations status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-configure-and-manage-microsoft-teams-integrations',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-configure-and-manage-microsoft-teams-integrations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c05fe76870fe77ad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-microsoft-teams-integrations'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-configure-and-manage-microsoft-teams-integrations', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateConfigureAndManageMicrosoftTeamsIntegrations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConfigureAndManageMicrosoftTeamsIntegrations'
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
    print(TeamsUpdateConfigureAndManageMicrosoftTeamsIntegrations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
