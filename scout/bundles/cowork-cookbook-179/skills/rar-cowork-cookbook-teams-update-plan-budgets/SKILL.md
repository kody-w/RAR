---
name: "rar-cowork-cookbook-teams-update-plan-budgets"
description: "Summarizes plan budgets from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs, status indicators, and quick-action buttons; does not p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_budgets", "rar_sha256": "0e9e1d0a40a2b8d8d69b2ec3fd73d8eeccca5afe546deb8dc73ac2f29634f58a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
