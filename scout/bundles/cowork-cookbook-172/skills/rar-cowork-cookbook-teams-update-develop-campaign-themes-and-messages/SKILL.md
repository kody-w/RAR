---
name: "rar-cowork-cookbook-teams-update-develop-campaign-themes-and-messages"
description: "Summarizes campaign theme and message status from Dynamics 365 ERP for a given legal entity and returns a markdown Teams channel post plus a saved Adaptive Card JSON file with KPIs and quick-action buttons; does not post"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_campaign_themes_and_messages", "rar_sha256": "6902c9f34557c655a3ec64b702fca853a2c0b2740c7f79d4526c9943a15363c3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
