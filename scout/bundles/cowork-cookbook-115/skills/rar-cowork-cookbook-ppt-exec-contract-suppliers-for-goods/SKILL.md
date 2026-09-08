---
name: "rar-cowork-cookbook-ppt-exec-contract-suppliers-for-goods"
description: "Builds a read-only executive PowerPoint deck on contract suppliers for goods from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_contract_suppliers_for_goods", "rar_sha256": "6f51e6345ccb376d2814e55c235e247d0548216a5b2b521d03dced2e748ea11c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
