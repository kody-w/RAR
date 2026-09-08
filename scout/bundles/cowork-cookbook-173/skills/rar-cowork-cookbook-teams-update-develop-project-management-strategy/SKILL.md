---
name: "rar-cowork-cookbook-teams-update-develop-project-management-strategy"
description: "Summarizes project management strategy status from Dynamics 365 ERP for a given legal entity and saves a Teams channel post (markdown) plus an Adaptive Card JSON file for review, without posting it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_project_management_strategy", "rar_sha256": "0cc190109ff8753c5f4a9ec23bf82be85bed94083b83784902def31fe360bee6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
