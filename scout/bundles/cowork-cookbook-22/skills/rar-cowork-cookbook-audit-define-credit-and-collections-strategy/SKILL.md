---
name: "rar-cowork-cookbook-audit-define-credit-and-collections-strategy"
description: "Audits Dynamics 365 credit and collections strategy records in a given legal entity for missing fields, stale dates, blank descriptions, inactive references and policy violations, returning a read-only Excel audit workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_credit_and_collections_strategy", "rar_sha256": "d11555744a1575518a32e405ef01d2a46cda5c750505f6eb2cbf61c718218af8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
