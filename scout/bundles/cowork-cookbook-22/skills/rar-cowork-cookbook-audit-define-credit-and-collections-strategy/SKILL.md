---
name: "rar-cowork-cookbook-audit-define-credit-and-collections-strategy"
description: "Audits Dynamics 365 credit and collections strategy records in a given legal entity for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning a read-only Excel audit workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_credit_and_collections_strategy", "rar_sha256": "d11555744a1575518a32e405ef01d2a46cda5c750505f6eb2cbf61c718218af8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_credit_and_collections_strategy`. The original RAPP
agent is preserved byte-for-byte in `audit_define_credit_and_collections_strategy_agent.py` and in the RCI capsule.

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

Define credit and collections strategy Completeness Audit — Audits Dynamics 365 credit and collections strategy records in a given legal entity for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning a read-only Excel audit workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-credit-and-collections-strategy
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
    "date_window": {
      "description": "Date range used to judge stale dates; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-define-credit-and-collections-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_credit_and_collections_strategy_agent.py` and embedded as the fenced Python below (sha256 d11555744a157551…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_credit_and_collections_strategy_agent.py` first:

```bash
python3 audit_define_credit_and_collections_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_credit_and_collections_strategy_agent.py   # or on stdin
python3 audit_define_credit_and_collections_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define credit and collections strategy Completeness Audit — Audits Dynamics 365 credit and collections strategy records in a given legal entity for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning a read-only Excel audit workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-credit-and-collections-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_credit_and_collections_strategy',
    "version": '3.0.2',
    "display_name": 'Define credit and collections strategy Completeness Audit',
    "description": 'Audits Dynamics 365 credit and collections strategy records in a given legal entity for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning a read-only Excel audit workbo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-define-credit-and-collections-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-credit-and-collections-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '92a5d0056af95147',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-credit-and-collections-strategy'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-define-credit-and-collections-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-define-credit-and-collections-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define credit and collections strategy records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define credit and collections strategy. Output an Excel workbook 'audit-define-credit-and-collections-strategy-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define credit and collections strategy data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads define credit and collections strategy records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits Dynamics 365 credit and collections strategy records in a given legal entity for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning a read-only Excel audit workbo', 'example_request': 'Audit credit and collections strategy records in USMF for completeness and give me the Excel audit workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-define-credit-and-collections-strategy-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy compliance audit of D365 credit and collections strategy records via the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineCreditAndCollectionsStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineCreditAndCollectionsStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-define-credit-and-collections-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineCreditAndCollectionsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
