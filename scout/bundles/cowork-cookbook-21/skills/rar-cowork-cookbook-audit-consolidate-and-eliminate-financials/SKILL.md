---
name: "rar-cowork-cookbook-audit-consolidate-and-eliminate-financials"
description: "Runs a read-only completeness and policy audit of consolidate-and-eliminate financials records in a Dynamics 365 F&SCM legal entity, returning an Excel workbook with one sheet per finding category plus a summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_consolidate_and_eliminate_financials", "rar_sha256": "bd668546bd833adcd13d7aff3ea177d4b2bd46ab9ee359ca5e5ab4e7dcca5e0f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_consolidate_and_eliminate_financials`. The original RAPP
agent is preserved byte-for-byte in `audit_consolidate_and_eliminate_financials_agent.py` and in the RCI capsule.

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

Consolidate and eliminate financials Completeness Audit — Runs a read-only completeness and policy audit of consolidate-and-eliminate financials records in a Dynamics 365 F&SCM legal entity, returning an Excel workbook with one sheet per finding category plus a summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-consolidate-and-eliminate-financials
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
      "description": "Name of the Excel workbook to produce, e.g. audit-consolidate-and-eliminate-financials-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_consolidate_and_eliminate_financials_agent.py` and embedded as the fenced Python below (sha256 bd668546bd833adc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_consolidate_and_eliminate_financials_agent.py` first:

```bash
python3 audit_consolidate_and_eliminate_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_consolidate_and_eliminate_financials_agent.py   # or on stdin
python3 audit_consolidate_and_eliminate_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate and eliminate financials Completeness Audit — Runs a read-only completeness and policy audit of consolidate-and-eliminate financials records in a Dynamics 365 F&SCM legal entity, returning an Excel workbook with one sheet per finding category plus a summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-consolidate-and-eliminate-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_consolidate_and_eliminate_financials',
    "version": '3.0.2',
    "display_name": 'Consolidate and eliminate financials Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of consolidate-and-eliminate financials records in a Dynamics 365 F&SCM legal entity, returning an Excel workbook with one sheet per finding category plus a summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-consolidate-and-eliminate-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-consolidate-and-eliminate-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55d9d31dbeec75e0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/consolidate-and-eliminate-financials'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-consolidate-and-eliminate-financials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-consolidate-and-eliminate-financials-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit consolidate and eliminate financials records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to consolidate and eliminate financials. Output an Excel workbook 'audit-consolidate-and-eliminate-financials-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no consolidate and eliminate financials data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads consolidate and eliminate financials records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of consolidate-and-eliminate financials records in a Dynamics 365 F&SCM legal entity, returning an Excel workbook with one sheet per finding category plus a summary.', 'example_request': 'Audit consolidate and eliminate financials in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-consolidate-and-eliminate-financials-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to check consolidate-and-eliminate financials records in D365 F&SCM for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditConsolidateAndEliminateFinancials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConsolidateAndEliminateFinancials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-consolidate-and-eliminate-financials-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditConsolidateAndEliminateFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
