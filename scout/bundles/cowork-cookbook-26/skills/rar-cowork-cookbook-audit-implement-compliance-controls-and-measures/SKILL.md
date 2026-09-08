---
name: "rar-cowork-cookbook-audit-implement-compliance-controls-and-measures"
description: "Runs a read-only completeness audit of compliance control records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_compliance_controls_and_measures", "rar_sha256": "7acaff9aa65fb41c0f65f776fbd688323348df2c9f8ef1b2e12e5c81a05ec808", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_implement_compliance_controls_and_measures`. The original RAPP
agent is preserved byte-for-byte in `audit_implement_compliance_controls_and_measures_agent.py` and in the RCI capsule.

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

Implement compliance controls and measures Completeness Audit — Runs a read-only completeness audit of compliance control records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-compliance-controls-and-measures
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
      "description": "Name of the Excel workbook to produce, e.g. audit-implement-compliance-controls-and-measures-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_implement_compliance_controls_and_measures_agent.py` and embedded as the fenced Python below (sha256 7acaff9aa65fb41c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_implement_compliance_controls_and_measures_agent.py` first:

```bash
python3 audit_implement_compliance_controls_and_measures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_implement_compliance_controls_and_measures_agent.py   # or on stdin
python3 audit_implement_compliance_controls_and_measures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement compliance controls and measures Completeness Audit — Runs a read-only completeness audit of compliance control records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-compliance-controls-and-measures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_implement_compliance_controls_and_measures',
    "version": '3.0.2',
    "display_name": 'Implement compliance controls and measures Completeness Audit',
    "description": 'Runs a read-only completeness audit of compliance control records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
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
        "upstream_slug": 'audit-implement-compliance-controls-and-measures',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-implement-compliance-controls-and-measures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bff4ea542bfa7f91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/implement-compliance-controls-and-measures'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-implement-compliance-controls-and-measures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-implement-compliance-controls-and-measures-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit implement compliance controls and measures records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to implement compliance controls and measures. Output an Excel workbook 'audit-implement-compliance-controls-and-measures-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no implement compliance controls and measures data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-03', 'what_it_does': 'Reads implement compliance controls and measures records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness audit of compliance control records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit compliance control records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-implement-compliance-controls-and-measures-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants compliance control records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations, without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditImplementComplianceControlsAndMeasures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditImplementComplianceControlsAndMeasures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-implement-compliance-controls-and-measures-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditImplementComplianceControlsAndMeasures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
