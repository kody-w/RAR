---
name: "rar-cowork-cookbook-audit-negotiate-and-finalize-quotations"
description: "Runs a read-only completeness and policy audit of quotation negotiation/finalization records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_negotiate_and_finalize_quotations", "rar_sha256": "9be0cd721776380c0e5ab7114fc7d85bbc97fa73894284674bf5c391bb42001b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_negotiate_and_finalize_quotations`. The original RAPP
agent is preserved byte-for-byte in `audit_negotiate_and_finalize_quotations_agent.py` and in the RCI capsule.

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

Negotiate and finalize quotations Completeness Audit — Runs a read-only completeness and policy audit of quotation negotiation/finalization records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-negotiate-and-finalize-quotations
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
      "description": "Date range to scope records; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-negotiate-and-finalize-quotations-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_negotiate_and_finalize_quotations_agent.py` and embedded as the fenced Python below (sha256 9be0cd721776380c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_negotiate_and_finalize_quotations_agent.py` first:

```bash
python3 audit_negotiate_and_finalize_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_negotiate_and_finalize_quotations_agent.py   # or on stdin
python3 audit_negotiate_and_finalize_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Negotiate and finalize quotations Completeness Audit — Runs a read-only completeness and policy audit of quotation negotiation/finalization records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-negotiate-and-finalize-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_negotiate_and_finalize_quotations',
    "version": '3.0.3',
    "display_name": 'Negotiate and finalize quotations Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of quotation negotiation/finalization records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-negotiate-and-finalize-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-negotiate-and-finalize-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44865480574a8ab1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/negotiate-and-finalize-quotations'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-negotiate-and-finalize-quotations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to scope records; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-negotiate-and-finalize-quotations-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit negotiate and finalize quotations records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to negotiate and finalize quotations. Output an Excel workbook 'audit-negotiate-and-finalize-quotations-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no negotiate and finalize quotations data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads negotiate and finalize quotations records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of quotation negotiation/finalization records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary', 'example_request': 'Audit negotiate and finalize quotations in USMF for completeness and give me the Excel audit workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range to scope records; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-negotiate-and-finalize-quotations-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to check D365 quotation negotiation records for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditNegotiateAndFinalizeQuotations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditNegotiateAndFinalizeQuotations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to scope records; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-negotiate-and-finalize-quotations-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditNegotiateAndFinalizeQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
