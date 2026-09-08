---
name: "rar-cowork-cookbook-audit-develop-procurement-catalogs"
description: "Runs a read-only completeness and policy audit of procurement catalog records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_procurement_catalogs", "rar_sha256": "6dcdacda08e6a95a69ba921ff47b1a0151a3b21a1eda0b9ecb43cb2b2d7e939a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
