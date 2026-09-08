---
name: "rar-cowork-cookbook-audit-define-extensions-approach"
description: "Read-only audit of 'define extensions approach' records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inac"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_extensions_approach", "rar_sha256": "23ee964442794ce21cb75ac0a7930a5435a14dee49bb57f2c270c3144860cbab", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_extensions_approach`. The original RAPP
agent is preserved byte-for-byte in `audit_define_extensions_approach_agent.py` and in the RCI capsule.

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

Define extensions approach Completeness Audit — Read-only audit of 'define extensions approach' records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inac

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-extensions-approach
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
      "description": "Date range used to judge stale dates; note USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-define-extensions-approach-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_extensions_approach_agent.py` and embedded as the fenced Python below (sha256 23ee964442794ce2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_extensions_approach_agent.py` first:

```bash
python3 audit_define_extensions_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_extensions_approach_agent.py   # or on stdin
python3 audit_define_extensions_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define extensions approach Completeness Audit — Read-only audit of 'define extensions approach' records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inac

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-extensions-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_extensions_approach',
    "version": '3.0.2',
    "display_name": 'Define extensions approach Completeness Audit',
    "description": "Read-only audit of 'define extensions approach' records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inac",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-extensions-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-extensions-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b1ed1be4daad592',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-extensions-approach'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-define-extensions-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; note USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-define-extensions-approach-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define extensions approach records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define extensions approach. Output an Excel workbook 'audit-define-extensions-approach-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define extensions approach data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-03', 'what_it_does': 'Reads define extensions approach records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Read-only audit of 'define extensions approach' records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inac", 'example_request': 'Audit define extensions approach records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; note USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-define-extensions-approach-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance check of define extensions approach records in D365 ERP, with findings exported to Excel and no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineExtensionsApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineExtensionsApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; note USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-define-extensions-approach-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineExtensionsApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
