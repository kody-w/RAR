---
name: "rar-cowork-cookbook-audit-determine-sales-targets"
description: "Runs a read-only completeness and policy audit of determine sales targets records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_determine_sales_targets", "rar_sha256": "113a6056d12647525c83c62268ac341ecaeb4519d5c05a6de2b719180226c455", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_determine_sales_targets`. The original RAPP
agent is preserved byte-for-byte in `audit_determine_sales_targets_agent.py` and in the RCI capsule.

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

Determine sales targets Completeness Audit — Runs a read-only completeness and policy audit of determine sales targets records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-determine-sales-targets
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
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-determine-sales-targets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_determine_sales_targets_agent.py` and embedded as the fenced Python below (sha256 113a6056d1264752…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_determine_sales_targets_agent.py` first:

```bash
python3 audit_determine_sales_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_determine_sales_targets_agent.py   # or on stdin
python3 audit_determine_sales_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine sales targets Completeness Audit — Runs a read-only completeness and policy audit of determine sales targets records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-determine-sales-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_determine_sales_targets',
    "version": '3.0.2',
    "display_name": 'Determine sales targets Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of determine sales targets records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
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
        "upstream_slug": 'audit-determine-sales-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-determine-sales-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e0ef067f3e0d726b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/determine-sales-targets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-determine-sales-targets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-determine-sales-targets-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit determine sales targets records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to determine sales targets. Output an Excel workbook 'audit-determine-sales-targets-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no determine sales targets data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads determine sales targets records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of determine sales targets records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit determine sales targets records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-determine-sales-targets-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants determine sales targets records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDetermineSalesTargets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDetermineSalesTargets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-determine-sales-targets-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDetermineSalesTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
