---
name: "rar-cowork-cookbook-teams-update-estimate-the-cost-of-production"
description: "Summarizes production cost estimates from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rather tha"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_estimate_the_cost_of_production", "rar_sha256": "14c01f7e5d40fde75da2457d4a4a9abff5846e784211a2a48e72314143b7ab08", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_estimate_the_cost_of_production`. The original RAPP
agent is preserved byte-for-byte in `teams_update_estimate_the_cost_of_production_agent.py` and in the RCI capsule.

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

Estimate the cost of production Teams Channel Update — Summarizes production cost estimates from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rather tha

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production
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
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-estimate-the-cost-of-production-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_estimate_the_cost_of_production_agent.py` and embedded as the fenced Python below (sha256 14c01f7e5d40fde7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_estimate_the_cost_of_production_agent.py` first:

```bash
python3 teams_update_estimate_the_cost_of_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_estimate_the_cost_of_production_agent.py   # or on stdin
python3 teams_update_estimate_the_cost_of_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Estimate the cost of production Teams Channel Update — Summarizes production cost estimates from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rather tha

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_estimate_the_cost_of_production',
    "version": '3.0.3',
    "display_name": 'Estimate the cost of production Teams Channel Update',
    "description": 'Summarizes production cost estimates from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rather tha',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-estimate-the-cost-of-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '78ea31cea7f2bf23',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/estimate-the-cost-of-production'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-estimate-the-cost-of-production', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-estimate-the-cost-of-production-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of estimate the cost of production. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-estimate-the-cost-of-production-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads estimate the cost of production, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes production cost estimates from Dynamics 365 F&SCM for a given legal entity and returns a draft Teams channel post plus an Adaptive Card JSON file with KPIs and quick-action buttons, saved for review rather tha', 'example_request': "Draft a Teams update on production cost estimates for USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-estimate-the-cost-of-production-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a ready-to-review Teams update on production cost estimate status from D365 ERP, with an Adaptive Card artifact they will post themselves.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateEstimateTheCostOfProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEstimateTheCostOfProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-estimate-the-cost-of-production-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateEstimateTheCostOfProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
