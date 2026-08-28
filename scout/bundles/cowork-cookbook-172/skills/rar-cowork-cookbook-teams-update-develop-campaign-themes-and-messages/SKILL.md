---
name: "rar-cowork-cookbook-teams-update-develop-campaign-themes-and-messages"
description: "Drafts a Teams channel post on develop campaign themes and messages status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_campaign_themes_and_messages", "rar_sha256": "a4bbbc526ad7c03dc626b2ca2f93750171f15f81eb31533c1c99ffe12031d80f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_campaign_themes_and_messages_agent.py` and embedded as the fenced Python below (sha256 a4bbbc526ad7c03d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_campaign_themes_and_messages_agent.py` first:

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
    "version": '2.0.1',
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
