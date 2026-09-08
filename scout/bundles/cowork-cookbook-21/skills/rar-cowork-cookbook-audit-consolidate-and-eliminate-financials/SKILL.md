---
name: "rar-cowork-cookbook-audit-consolidate-and-eliminate-financials"
description: "Runs a read-only completeness and policy audit of consolidate-and-eliminate financials records in a Dynamics 365 F&SCM legal entity, returning an Excel workbook with one sheet per finding category plus a summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_consolidate_and_eliminate_financials", "rar_sha256": "bd668546bd833adcd13d7aff3ea177d4b2bd46ab9ee359ca5e5ab4e7dcca5e0f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
