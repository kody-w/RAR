---
name: "rar-cowork-cookbook-audit-perform-predictive-maintenance"
description: "Runs a read-only completeness and policy audit of predictive maintenance records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of cou"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_predictive_maintenance", "rar_sha256": "217eed92960be06c144b2d6b52dc2eadf948f875193695f04433e6a6389e3ed1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
