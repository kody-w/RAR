---
name: "rar-cowork-cookbook-teams-update-develop-campaign-themes-and-messages"
description: "Summarizes campaign theme and message status from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file with KPIs and quick-action buttons; does not post"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_campaign_themes_and_messages", "rar_sha256": "6902c9f34557c655a3ec64b702fca853a2c0b2740c7f79d4526c9943a15363c3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

Develop campaign themes and messages Teams Channel Update — Summarizes campaign theme and message status from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file with KPIs and quick-action buttons; does not post

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-develop-campaign-themes-and-messages-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_campaign_themes_and_messages_agent.py` and embedded as the fenced Python below (sha256 6902c9f34557c655…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_campaign_themes_and_messages_agent.py` first:

```bash
python3 teams_update_develop_campaign_themes_and_messages_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_campaign_themes_and_messages_agent.py   # or on stdin
python3 teams_update_develop_campaign_themes_and_messages_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop campaign themes and messages Teams Channel Update — Summarizes campaign theme and message status from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file with KPIs and quick-action buttons; does not post

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "version": '3.0.3',
    "display_name": 'Develop campaign themes and messages Teams Channel Update',
    "description": 'Summarizes campaign theme and message status from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file with KPIs and quick-action buttons; does not post',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5c5e36c99eacf57',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-campaign-themes-and-messages-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of develop campaign themes and messages. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-develop-campaign-themes-and-messages-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop campaign themes and messages, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes campaign theme and message status from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file with KPIs and quick-action buttons; does not post', 'example_request': "Draft a Teams update on develop campaign themes and messages from D365 USMF with an Adaptive Card, don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-campaign-themes-and-messages-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on develop campaign themes and messages status, with an Adaptive Card artifact saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDevelopCampaignThemesAndMessages(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopCampaignThemesAndMessages'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-develop-campaign-themes-and-messages-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
