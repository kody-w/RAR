---
name: "rar-cowork-cookbook-ppt-exec-contract-suppliers-for-goods"
description: "Builds a read-only executive PowerPoint deck on contract suppliers for goods from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_contract_suppliers_for_goods", "rar_sha256": "6f51e6345ccb376d2814e55c235e247d0548216a5b2b521d03dced2e748ea11c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_contract_suppliers_for_goods`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_contract_suppliers_for_goods_agent.py` and in the RCI capsule.

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

Contract suppliers for goods Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on contract suppliers for goods from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-contract-suppliers-for-goods
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
      "description": "Dynamics 365 legal entity to pull data from (e.g. USMF).",
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
    "output_filename": {
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-contract-suppliers-for-goods-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_contract_suppliers_for_goods_agent.py` and embedded as the fenced Python below (sha256 6f51e6345ccb376d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_contract_suppliers_for_goods_agent.py` first:

```bash
python3 ppt_exec_contract_suppliers_for_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_contract_suppliers_for_goods_agent.py   # or on stdin
python3 ppt_exec_contract_suppliers_for_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract suppliers for goods Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on contract suppliers for goods from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-contract-suppliers-for-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_contract_suppliers_for_goods',
    "version": '3.0.3',
    "display_name": 'Contract suppliers for goods Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on contract suppliers for goods from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-contract-suppliers-for-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-contract-suppliers-for-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '03fa9b2127187141',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/contract-suppliers-for-goods'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-contract-suppliers-for-goods', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-contract-suppliers-for-goods-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for contract suppliers for goods reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on contract suppliers for goods for a 15-minute monthly review. Produce 'ppt-exec-contract-suppliers-for-goods-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads contract suppliers for goods data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on contract suppliers for goods from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive PowerPoint deck on contract suppliers for goods for USMF for this month's review.", 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-contract-suppliers-for-goods-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when preparing a 15-minute monthly executive review of contract supplier status and you need a ready-to-present deck from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecContractSuppliersForGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecContractSuppliersForGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-contract-suppliers-for-goods-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecContractSuppliersForGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
