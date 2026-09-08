---
name: "rar-cowork-cookbook-audit-perform-predictive-maintenance"
description: "Runs a read-only completeness and policy audit of predictive maintenance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_predictive_maintenance", "rar_sha256": "217eed92960be06c144b2d6b52dc2eadf948f875193695f04433e6a6389e3ed1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_perform_predictive_maintenance`. The original RAPP
agent is preserved byte-for-byte in `audit_perform_predictive_maintenance_agent.py` and in the RCI capsule.

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

Perform predictive maintenance Completeness Audit — Runs a read-only completeness and policy audit of predictive maintenance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-predictive-maintenance
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
      "description": "Name of the Excel workbook to produce, e.g. audit-perform-predictive-maintenance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_perform_predictive_maintenance_agent.py` and embedded as the fenced Python below (sha256 217eed92960be06c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_perform_predictive_maintenance_agent.py` first:

```bash
python3 audit_perform_predictive_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_perform_predictive_maintenance_agent.py   # or on stdin
python3 audit_perform_predictive_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform predictive maintenance Completeness Audit — Runs a read-only completeness and policy audit of predictive maintenance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-predictive-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_perform_predictive_maintenance',
    "version": '3.0.3',
    "display_name": 'Perform predictive maintenance Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of predictive maintenance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-perform-predictive-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-perform-predictive-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '715cfff7d08bee4a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-predictive-maintenance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-perform-predictive-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-perform-predictive-maintenance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit perform predictive maintenance records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to perform predictive maintenance. Output an Excel workbook 'audit-perform-predictive-maintenance-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no perform predictive maintenance data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads perform predictive maintenance records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of predictive maintenance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou', 'example_request': 'Audit predictive maintenance records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-perform-predictive-maintenance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants predictive maintenance records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPerformPredictiveMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPerformPredictiveMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-perform-predictive-maintenance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPerformPredictiveMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
