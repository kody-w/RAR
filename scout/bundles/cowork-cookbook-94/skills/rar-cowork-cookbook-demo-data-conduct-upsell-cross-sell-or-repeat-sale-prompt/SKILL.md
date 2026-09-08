---
name: "rar-cowork-cookbook-demo-data-conduct-upsell-cross-sell-or-repeat-sale-prompt"
description: "Generates 25 realistic demo records for an upsell/cross-sell/repeat-sale scenario in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each new primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_conduct_upsell_cross_sell_or_repeat_sale_prompt", "rar_sha256": "dc11447ad23ed34baa8cce232741fe2a2c9d0c6a68115e875b34197ce014bdfc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
