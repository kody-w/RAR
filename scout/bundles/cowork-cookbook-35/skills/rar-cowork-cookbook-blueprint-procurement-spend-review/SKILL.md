---
name: "rar-cowork-cookbook-blueprint-procurement-spend-review"
description: "Runs a read-only procurement spend and supplier risk review against Dynamics 365 F&SCM for a given legal entity and fiscal year, returning a workbook with spend, concentration, payables, and risk sheets plus an email sum"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_procurement_spend_review", "rar_sha256": "f27afc4c8d493a0ad6324054bd80dacfde1846fdbdd2a317684a091a748c05ee", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "source_to_pay", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/blueprint_procurement_spend_review`. The original RAPP
agent is preserved byte-for-byte in `blueprint_procurement_spend_review_agent.py` and in the RCI capsule.

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

Procurement Spend & Supplier Risk Blueprint — Runs a read-only procurement spend and supplier risk review against Dynamics 365 F&SCM for a given legal entity and fiscal year, returning a workbook with spend, concentration, payables, and risk sheets plus an email sum

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
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-procurement-spend-review
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
    "concentrationthreshold": {
      "description": "Percent of spend with one vendor that flags concentration risk, e.g. 20.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "fiscalyear": {
      "description": "Fiscal year to analyze, e.g. 2017.",
      "type": "string"
    },
    "legalentity": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_procurement_spend_review_agent.py` and embedded as the fenced Python below (sha256 f27afc4c8d493a0a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_procurement_spend_review_agent.py` first:

```bash
python3 blueprint_procurement_spend_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blueprint_procurement_spend_review_agent.py   # or on stdin
python3 blueprint_procurement_spend_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Procurement Spend & Supplier Risk Blueprint — Runs a read-only procurement spend and supplier risk review against Dynamics 365 F&SCM for a given legal entity and fiscal year, returning a workbook with spend, concentration, payables, and risk sheets plus an email sum

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
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-procurement-spend-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/blueprint_procurement_spend_review',
    "version": '3.0.3',
    "display_name": 'Procurement Spend & Supplier Risk Blueprint',
    "description": 'Runs a read-only procurement spend and supplier risk review against Dynamics 365 F&SCM for a given legal entity and fiscal year, returning a workbook with spend, concentration, payables, and risk sheets plus an email sum',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_blueprint', 'blueprint', 'source_to_pay', 'advanced', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'blueprint-procurement-spend-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/blueprint-procurement-spend-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '880b7e127b408163',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing'], 'recipe_category': 'blueprint', 'recipe_type': 'prompt+blueprint', 'upstream_path': 'source-to-pay/blueprint-procurement-spend-review', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Procurement and Accounts payable roles', 'Prerequisite: Cowork D365 ERP plugin toggled on in the session', "Output matches: One workbook plus an email draft. This is the blueprint most likely to hit the halt node — USMF carries zero VendorInvoiceHeader records, so a clean 'no spend data' report is the correct outcome and is itself the deliverable."], 'confidence': 1.0, 'deliverable': "One workbook plus an email draft. This is the blueprint most likely to hit the halt node — USMF carries zero VendorInvoiceHeader records, so a clean 'no spend data' report is the correct outcome and is itself the deliverable.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'concentrationthreshold': 'Percent of spend with one vendor that flags concentration risk, e.g. 20.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscalyear': 'Fiscal year to analyze, e.g. 2017.', 'legalentity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Shows where spend is concentrated in a handful of suppliers before that concentration becomes a continuity problem, and does it without waiting on a BI request.', 'expected_output': "One workbook plus an email draft. This is the blueprint most likely to hit the halt node — USMF carries zero VendorInvoiceHeader records, so a clean 'no spend data' report is the correct outcome and is itself the deliverable.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Procurement and Accounts payable roles', 'Cowork D365 ERP plugin toggled on in the session'], 'prompt': 'The attached image is a workflow blueprint. Build and run it as an automated task using the Dynamics 365 ERP plugin. Follow the diagram exactly: execute each phase in the order shown, honour every decision diamond, and stop at a red halt node if its condition is met.\n\nDo not ask me clarifying questions — every input is bound below.\n\n## Input variables\n\n- legalEntity: USMF\n- fiscalYear: 2017\n- concentrationThreshold: 20\n\n## Trigger\n\nTrigger: quarterly, first business day\n\n## Outputs\n\n- procurement-spend-review.xlsx — Spend, Concentration, Payables, and Risk sheets\n\n## Notification\n\nEmail the spend summary to me\n\n## Guardrails\n\n- Read only. Do not create or modify vendors, purchase orders, or invoices.\n- Produce the workbook in this run — do not return a plan or a methodology document instead.\n- Report concentration and exposure; leave every sourcing decision to me.\n\nUSMF may have no vendor invoice records at all. If purchase or payable data is missing, say so explicitly, name the entity you queried, list what you could read from the vendor master, and stop. Do not infer spend from vendor records alone.', 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only procurement spend and supplier risk review against Dynamics 365 F&SCM for a given legal entity and fiscal year, returning a workbook with spend, concentration, payables, and risk sheets plus an email sum', 'example_request': 'Run the procurement spend and supplier risk review for USMF, FY2017, flag vendors over 20% of spend.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legalEntity'}, {'description': 'Fiscal year to analyze, e.g. 2017.', 'name': 'fiscalYear'}, {'description': 'Percent of spend with one vendor that flags concentration risk, e.g. 20.', 'name': 'concentrationThreshold'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a quarterly vendor spend profile, supplier concentration flags, and payables exposure from D365 ERP data for one legal entity and fiscal year.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BlueprintProcurementSpendReview(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlueprintProcurementSpendReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'concentrationthreshold': {'description': 'Percent of spend with one vendor that flags concentration risk, e.g. 20.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscalyear': {'description': 'Fiscal year to analyze, e.g. 2017.', 'type': 'string'}, 'legalentity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(BlueprintProcurementSpendReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
