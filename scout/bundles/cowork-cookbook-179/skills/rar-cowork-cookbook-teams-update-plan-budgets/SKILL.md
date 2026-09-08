---
name: "rar-cowork-cookbook-teams-update-plan-budgets"
description: "Summarizes plan budgets from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; does not p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_budgets", "rar_sha256": "0e9e1d0a40a2b8d8d69b2ec3fd73d8eeccca5afe546deb8dc73ac2f29634f58a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_plan_budgets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_plan_budgets_agent.py` and in the RCI capsule.

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

Plan budgets Teams Channel Update — Summarizes plan budgets from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; does not p

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-budgets
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
      "description": "Filename for the Adaptive Card JSON, e.g. teams-update-plan-budgets-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to summarize plan budgets for (e.g., USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_plan_budgets_agent.py` and embedded as the fenced Python below (sha256 0e9e1d0a40a2b8d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_plan_budgets_agent.py` first:

```bash
python3 teams_update_plan_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_plan_budgets_agent.py   # or on stdin
python3 teams_update_plan_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan budgets Teams Channel Update — Summarizes plan budgets from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; does not p

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_plan_budgets',
    "version": '3.0.3',
    "display_name": 'Plan budgets Teams Channel Update',
    "description": 'Summarizes plan budgets from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; does not p',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-plan-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-plan-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7557ce370dd1b1ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/plan-budgets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-plan-budgets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Filename for the Adaptive Card JSON, e.g. teams-update-plan-budgets-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize plan budgets for (e.g., USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of plan budgets. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-plan-budgets-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan budgets, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes plan budgets from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; does not p', 'example_request': "Draft a Teams post and Adaptive Card on plan budgets status for USMF — save them, don't post.", 'inputs': [{'description': 'D365 legal entity to summarize plan budgets for (e.g., USMF).', 'name': 'legal_entity'}, {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-plan-budgets-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on plan budgets status from D365 ERP, with an Adaptive Card for triage, saved rather than posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdatePlanBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePlanBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Filename for the Adaptive Card JSON, e.g. teams-update-plan-budgets-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize plan budgets for (e.g., USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdatePlanBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
