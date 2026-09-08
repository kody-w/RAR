---
name: "rar-cowork-cookbook-audit-develop-procurement-catalogs"
description: "Runs a read-only completeness and policy audit of procurement catalog records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_procurement_catalogs", "rar_sha256": "6dcdacda08e6a95a69ba921ff47b1a0151a3b21a1eda0b9ecb43cb2b2d7e939a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_procurement_catalogs`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_procurement_catalogs_agent.py` and in the RCI capsule.

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

Develop procurement catalogs Completeness Audit — Runs a read-only completeness and policy audit of procurement catalog records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-procurement-catalogs
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
      "description": "Name of the Excel workbook to produce, e.g. audit-develop-procurement-catalogs-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_procurement_catalogs_agent.py` and embedded as the fenced Python below (sha256 6dcdacda08e6a95a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_procurement_catalogs_agent.py` first:

```bash
python3 audit_develop_procurement_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_procurement_catalogs_agent.py   # or on stdin
python3 audit_develop_procurement_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement catalogs Completeness Audit — Runs a read-only completeness and policy audit of procurement catalog records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-procurement-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_procurement_catalogs',
    "version": '3.0.2',
    "display_name": 'Develop procurement catalogs Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of procurement catalog records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a summary.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-procurement-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-procurement-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'db19c85f5af74865',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-catalogs'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-develop-procurement-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-develop-procurement-catalogs-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop procurement catalogs records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop procurement catalogs. Output an Excel workbook 'audit-develop-procurement-catalogs-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop procurement catalogs data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads develop procurement catalogs records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of procurement catalog records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a summary.', 'example_request': 'Audit procurement catalogs in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-procurement-catalogs-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants procurement catalog records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopProcurementCatalogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopProcurementCatalogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-procurement-catalogs-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDevelopProcurementCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
