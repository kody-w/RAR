---
name: "rar-cowork-cookbook-blueprint-procurement-spend-review"
description: "Runs a read-only procurement spend and supplier risk review against Dynamics 365 F&SCM for a given legal entity and fiscal year, returning a workbook with spend, concentration, payables, and risk sheets plus an email sum"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_procurement_spend_review", "rar_sha256": "f27afc4c8d493a0ad6324054bd80dacfde1846fdbdd2a317684a091a748c05ee", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "source_to_pay", "advanced", "integration", "dynamics_365_erp"]}
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
