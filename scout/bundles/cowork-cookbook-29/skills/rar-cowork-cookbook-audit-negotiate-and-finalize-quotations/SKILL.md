---
name: "rar-cowork-cookbook-audit-negotiate-and-finalize-quotations"
description: "Runs a read-only completeness and policy audit of quotation negotiation/finalization records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_negotiate_and_finalize_quotations", "rar_sha256": "9be0cd721776380c0e5ab7114fc7d85bbc97fa73894284674bf5c391bb42001b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
