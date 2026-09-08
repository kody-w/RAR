---
name: "rar-cowork-cookbook-teams-update-develop-budgeting-strategy"
description: "Summarizes budgeting strategy status from Dynamics 365 ERP for a legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick-action buttons; does not post."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_budgeting_strategy", "rar_sha256": "ac96c7a2e444b375df6982dd6966a38d7fae639ae2101655139dd7807a460409", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
