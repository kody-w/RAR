---
name: "rar-cowork-cookbook-demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt"
description: "Generates 25 realistic demo records for an upsell/cross-sell/repeat-sale scenario in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each new primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt", "rar_sha256": "dc11447ad23ed34baa8cce232741fe2a2c9d0c6a68115e875b34197ce014bdfc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt`. The original RAPP
agent is preserved byte-for-byte in `demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` and in the RCI capsule.

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

Conduct upsell, cross sell or repeat sale prompt Demo Data Generator — Generates 25 realistic demo records for an upsell/cross-sell/repeat-sale scenario in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each new primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
    "record_count": {
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` and embedded as the fenced Python below (sha256 dc11447ad23ed34b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py` first:

```bash
python3 demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py   # or on stdin
python3 demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct upsell, cross sell or repeat sale prompt Demo Data Generator — Generates 25 realistic demo records for an upsell/cross-sell/repeat-sale scenario in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each new primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt',
    "version": '3.0.3',
    "display_name": 'Conduct upsell, cross sell or repeat sale prompt Demo Data Generator',
    "description": 'Generates 25 realistic demo records for an upsell/cross-sell/repeat-sale scenario in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each new primary key.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '66e66e0b816a0fbe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-upsell-cross-sell-or-repeat-sale-prompt'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic conduct upsell, cross sell or repeat sale prompt data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for conduct upsell, cross sell or repeat sale prompt. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic conduct upsell, cross sell or repeat sale prompt records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates 25 realistic demo records for an upsell/cross-sell/repeat-sale scenario in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each new primary key.', 'example_request': 'Generate 25 demo upsell/cross-sell records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded demo data for upsell/cross-sell/repeat-sale training or pilot scenarios in a D365 sandbox tenant. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataConductUpsellCrossSellOrRepeatSalePrompt(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConductUpsellCrossSellOrRepeatSalePrompt'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataConductUpsellCrossSellOrRepeatSalePrompt().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
