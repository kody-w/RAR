---
name: "rar-cowork-cookbook-teams-update-develop-campaign-themes-and-messages"
description: "Drafts a Teams channel post on develop campaign themes and messages status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_campaign_themes_and_messages", "rar_sha256": "ee6ba4b3adf001419a26389eb9b01e869aa7769a9db3b9bd72e46af79959b0b6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_campaign_themes_and_messages`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_campaign_themes_and_messages_agent.py` and in the RCI capsule.

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
