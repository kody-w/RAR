---
name: "rar-cowork-cookbook-teams-update-develop-project-management-strategy"
description: "Summarizes project management strategy status from Dynamics 365 ERP for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON file for review, without posting it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_project_management_strategy", "rar_sha256": "0cc190109ff8753c5f4a9ec23bf82be85bed94083b83784902def31fe360bee6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_project_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_project_management_strategy_agent.py` and in the RCI capsule.

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

Develop project management strategy Teams Channel Update — Summarizes project management strategy status from Dynamics 365 ERP for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON file for review, without posting it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-project-management-strategy
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
      "description": "Output filename for the Adaptive Card JSON artifact.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize, e.g. USMF.",
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
    },
    "topic": {
      "description": "The initiative or subject to summarize, e.g. develop project management strategy.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_project_management_strategy_agent.py` and embedded as the fenced Python below (sha256 0cc190109ff8753c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_project_management_strategy_agent.py` first:

```bash
python3 teams_update_develop_project_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_project_management_strategy_agent.py   # or on stdin
python3 teams_update_develop_project_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project management strategy Teams Channel Update — Summarizes project management strategy status from Dynamics 365 ERP for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON file for review, without posting it.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-project-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_project_management_strategy',
    "version": '3.0.3',
    "display_name": 'Develop project management strategy Teams Channel Update',
    "description": 'Summarizes project management strategy status from Dynamics 365 ERP for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON file for review, without posting it.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-project-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-project-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa3eff12eb962a40',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-management-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-develop-project-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'topic': 'The initiative or subject to summarize, e.g. develop project management strategy.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of develop project management strategy. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-develop-project-management-strategy-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop project management strategy, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes project management strategy status from Dynamics 365 ERP for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON file for review, without posting it.', 'example_request': 'Draft a Teams update on our project management strategy status from D365 USMF, plus an Adaptive Card I can review.', 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The initiative or subject to summarize, e.g. develop project management strategy.', 'name': 'topic'}, {'description': 'Output filename for the Adaptive Card JSON artifact.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a draft Teams channel update with KPIs and quick-action buttons on develop project management strategy status from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDevelopProjectManagementStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopProjectManagementStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The initiative or subject to summarize, e.g. develop project management strategy.', 'type': 'string'}},
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
    print(TeamsUpdateDevelopProjectManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
