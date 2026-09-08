---
name: "rar-cowork-cookbook-audit-develop-continuous-improvement-initiatives"
description: "Runs a read-only completeness and policy audit of continuous improvement initiative records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_continuous_improvement_initiatives", "rar_sha256": "a11ad47949311a6b9ab0e19cb8f46acae1b0f27cb41ed3f5a99f9735fe53d3e7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_continuous_improvement_initiatives`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_continuous_improvement_initiatives_agent.py` and in the RCI capsule.

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

Develop continuous improvement initiatives Completeness Audit — Runs a read-only completeness and policy audit of continuous improvement initiative records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives
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
      "description": "Name of the Excel workbook to produce, e.g. audit-develop-continuous-improvement-initiatives-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_continuous_improvement_initiatives_agent.py` and embedded as the fenced Python below (sha256 a11ad47949311a6b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_continuous_improvement_initiatives_agent.py` first:

```bash
python3 audit_develop_continuous_improvement_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_continuous_improvement_initiatives_agent.py   # or on stdin
python3 audit_develop_continuous_improvement_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop continuous improvement initiatives Completeness Audit — Runs a read-only completeness and policy audit of continuous improvement initiative records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_continuous_improvement_initiatives',
    "version": '3.0.2',
    "display_name": 'Develop continuous improvement initiatives Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of continuous improvement initiative records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-continuous-improvement-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f9e415524c5fbd71',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/develop-continuous-improvement-initiatives'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-develop-continuous-improvement-initiatives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-develop-continuous-improvement-initiatives-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop continuous improvement initiatives records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop continuous improvement initiatives. Output an Excel workbook 'audit-develop-continuous-improvement-initiatives-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop continuous improvement initiatives data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop continuous improvement initiatives records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of continuous improvement initiative records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary s', 'example_request': 'Audit continuous improvement initiative records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-continuous-improvement-initiatives-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants continuous improvement initiative records in D365 checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopContinuousImprovementInitiatives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopContinuousImprovementInitiatives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-continuous-improvement-initiatives-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDevelopContinuousImprovementInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
