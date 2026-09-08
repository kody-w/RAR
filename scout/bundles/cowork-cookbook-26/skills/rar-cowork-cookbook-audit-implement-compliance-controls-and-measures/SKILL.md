---
name: "rar-cowork-cookbook-audit-implement-compliance-controls-and-measures"
description: "Runs a read-only completeness audit of compliance control records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_compliance_controls_and_measures", "rar_sha256": "7acaff9aa65fb41c0f65f776fbd688323348df2c9f8ef1b2e12e5c81a05ec808", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
