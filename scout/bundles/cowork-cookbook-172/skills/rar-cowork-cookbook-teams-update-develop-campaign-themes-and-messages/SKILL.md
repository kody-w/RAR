---
name: "rar-cowork-cookbook-teams-update-develop-campaign-themes-and-messages"
description: "Drafts a Teams channel post on develop campaign themes and messages status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_campaign_themes_and_messages", "rar_sha256": "ee6ba4b3adf001419a26389eb9b01e869aa7769a9db3b9bd72e46af79959b0b6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_develop_campaign_themes_and_messages_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-develop-campaign-themes-and-messages:e0039860a46a68cc386541fb1f8f5c7eadd8ef5c8c9bbe1aeb3e95a1fc32611c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_develop_campaign_themes_and_messages`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_develop_campaign_themes_and_messages_agent.py` is
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

Develop campaign themes and messages Teams Channel Update — Drafts a Teams channel post on develop campaign themes and messages status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-campaign-themes-and-messages
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_campaign_themes_and_messages_agent.py` and embedded as the fenced Python below (sha256 ee6ba4b3adf00141…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_campaign_themes_and_messages_agent.py` first:

```bash
python3 teams_update_develop_campaign_themes_and_messages_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_campaign_themes_and_messages_agent.py   # or on stdin
python3 teams_update_develop_campaign_themes_and_messages_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop campaign themes and messages Teams Channel Update — Drafts a Teams channel post on develop campaign themes and messages status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-campaign-themes-and-messages
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_campaign_themes_and_messages',
    "version": '2.0.0',
    "display_name": 'Develop campaign themes and messages Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop campaign themes and messages status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-campaign-themes-and-messages',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-campaign-themes-and-messages',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6b548e3e34a9ad78',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-develop-campaign-themes-and-messages', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDevelopCampaignThemesAndMessages(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopCampaignThemesAndMessages'
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
    print(TeamsUpdateDevelopCampaignThemesAndMessages().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
