---
name: "rar-cowork-cookbook-teams-update-establish-sales-commission-and-incentive-structures"
description: "Summarizes sales commission and incentive structure status from Dynamics 365 ERP (legal entity USMF) and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON with KPIs and quick actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_establish_sales_commission_and_incentive_structures", "rar_sha256": "16c7babb78f35872ba95e5ffdb807091cb01e117a40d2440ab02e0fc618e8499", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
