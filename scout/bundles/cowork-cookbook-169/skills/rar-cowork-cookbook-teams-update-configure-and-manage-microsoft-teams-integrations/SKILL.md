---
name: "rar-cowork-cookbook-teams-update-configure-and-manage-microsoft-teams-integrations"
description: "Drafts a Teams channel post on configure and manage Microsoft Teams integrations status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations", "rar_sha256": "759acb068dddbf36a9f95a9e44db6cbaf2718113705c50112f6e14084a073898", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_configure_and_manage_microsoft_teams_integrations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-configure-and-manage-microsoft-teams-integrations:e3fc6b965bb6cd5d4ffb867545ab7f7b35077b749caf3b3ece2746c9512b52ab", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_configure_and_manage_microsoft_teams_integrations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_configure_and_manage_microsoft_teams_integrations_agent.py` is
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
