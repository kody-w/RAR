---
name: "rar-cowork-cookbook-teams-update-configure-and-manage-microsoft-teams-integrations"
description: "Drafts a Teams channel post on configure and manage Microsoft Teams integrations status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations", "rar_sha256": "759acb068dddbf36a9f95a9e44db6cbaf2718113705c50112f6e14084a073898", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` and embedded as the fenced Python below (sha256 759acb068dddbf36…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` first:

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
    "version": '2.0.0',
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
