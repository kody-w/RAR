---
name: "rar-cowork-cookbook-teams-update-develop-budgeting-strategy"
description: "Summarizes budgeting strategy status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_budgeting_strategy", "rar_sha256": "ac96c7a2e444b375df6982dd6966a38d7fae639ae2101655139dd7807a460409", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_budgeting_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_budgeting_strategy_agent.py` and in the RCI capsule.

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

Develop budgeting strategy Teams Channel Update — Summarizes budgeting strategy status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-budgeting-strategy
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
    "as_of_date": {
      "description": "Date used in the update and card filename, e.g. 2026-05-24.",
      "type": "string"
    },
    "card_filename": {
      "description": "Output name for the Adaptive Card JSON artifact.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_budgeting_strategy_agent.py` and embedded as the fenced Python below (sha256 ac96c7a2e444b375…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_budgeting_strategy_agent.py` first:

```bash
python3 teams_update_develop_budgeting_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_budgeting_strategy_agent.py   # or on stdin
python3 teams_update_develop_budgeting_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop budgeting strategy Teams Channel Update — Summarizes budgeting strategy status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-budgeting-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_budgeting_strategy',
    "version": '3.0.3',
    "display_name": 'Develop budgeting strategy Teams Channel Update',
    "description": 'Summarizes budgeting strategy status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-develop-budgeting-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-budgeting-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1961a535a0dbd498',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-budgeting-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-develop-budgeting-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used in the update and card filename, e.g. 2026-05-24.', 'card_filename': 'Output name for the Adaptive Card JSON artifact.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of develop budgeting strategy. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-develop-budgeting-strategy-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads develop budgeting strategy, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes budgeting strategy status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post.', 'example_request': "Draft a Teams channel update on our budgeting strategy status in USMF with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the update and card filename, e.g. 2026-05-24.', 'name': 'as_of_date'}, {'description': 'Output name for the Adaptive Card JSON artifact.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update plus Adaptive Card on develop budgeting strategy status from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDevelopBudgetingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopBudgetingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used in the update and card filename, e.g. 2026-05-24.', 'type': 'string'}, 'card_filename': {'description': 'Output name for the Adaptive Card JSON artifact.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateDevelopBudgetingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
