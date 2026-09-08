---
name: "rar-cowork-cookbook-teams-update-establish-sales-commission-and-incentive-structures"
description: "Summarizes sales commission and incentive structure status from Dynamics 365 ERP (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_establish_sales_commission_and_incentive_structures", "rar_sha256": "16c7babb78f35872ba95e5ffdb807091cb01e117a40d2440ab02e0fc618e8499", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_establish_sales_commission_and_incentive_structures`. The original RAPP
agent is preserved byte-for-byte in `teams_update_establish_sales_commission_and_incentive_structures_agent.py` and in the RCI capsule.

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

Establish sales commission and incentive structures Teams Channel Update — Summarizes sales commission and incentive structure status from Dynamics 365 ERP (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-establish-sales-commission-and-incentive-structures
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
      "description": "Output name for the Adaptive Card JSON, typically dated (e.g. ...-2026-05-24-card.json).",
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
      "description": "The subject of the update, e.g. establish sales commission and incentive structures.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_establish_sales_commission_and_incentive_structures_agent.py` and embedded as the fenced Python below (sha256 16c7babb78f35872…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_establish_sales_commission_and_incentive_structures_agent.py` first:

```bash
python3 teams_update_establish_sales_commission_and_incentive_structures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_establish_sales_commission_and_incentive_structures_agent.py   # or on stdin
python3 teams_update_establish_sales_commission_and_incentive_structures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish sales commission and incentive structures Teams Channel Update — Summarizes sales commission and incentive structure status from Dynamics 365 ERP (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-establish-sales-commission-and-incentive-structures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_establish_sales_commission_and_incentive_structures',
    "version": '3.0.3',
    "display_name": 'Establish sales commission and incentive structures Teams Channel Update',
    "description": 'Summarizes sales commission and incentive structure status from Dynamics 365 ERP (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-establish-sales-commission-and-incentive-structures',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-establish-sales-commission-and-incentive-structures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c0db3bc2363cd453',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/establish-sales-commission-and-incentive-structures'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/teams-update-establish-sales-commission-and-incentive-structures', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output name for the Adaptive Card JSON, typically dated (e.g. ...-2026-05-24-card.json).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to summarize, e.g. USMF.', 'topic': 'The subject of the update, e.g. establish sales commission and incentive structures.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of establish sales commission and incentive structures. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-establish-sales-commission-and-incentive-structures-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads establish sales commission and incentive structures, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes sales commission and incentive structure status from Dynamics 365 ERP (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions.', 'example_request': "Draft a Teams update on our sales commission structures from D365 USMF with an Adaptive Card — don't post it.", 'inputs': [{'description': 'D365 legal entity to summarize, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The subject of the update, e.g. establish sales commission and incentive structures.', 'name': 'topic'}, {'description': 'Output name for the Adaptive Card JSON, typically dated (e.g. ...-2026-05-24-card.json).', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams update on sales commission/incentive structures from D365, with an Adaptive Card, without it being posted for them.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateEstablishSalesCommissionAndIncentiveStructures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEstablishSalesCommissionAndIncentiveStructures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output name for the Adaptive Card JSON, typically dated (e.g. ...-2026-05-24-card.json).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to summarize, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'The subject of the update, e.g. establish sales commission and incentive structures.', 'type': 'string'}},
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
    print(TeamsUpdateEstablishSalesCommissionAndIncentiveStructures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
