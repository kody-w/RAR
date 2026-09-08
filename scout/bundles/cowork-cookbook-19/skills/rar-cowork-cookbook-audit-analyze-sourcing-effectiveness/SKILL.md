---
name: "rar-cowork-cookbook-audit-analyze-sourcing-effectiveness"
description: "Runs a read-only completeness and policy audit of sourcing effectiveness records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_sourcing_effectiveness", "rar_sha256": "afb7b3954f8670dd00a67fd08837d7474d82d979b3de6e69b63ce2a1b8ecb45d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_sourcing_effectiveness`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_sourcing_effectiveness_agent.py` and in the RCI capsule.

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

Analyze sourcing effectiveness Completeness Audit — Runs a read-only completeness and policy audit of sourcing effectiveness records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-sourcing-effectiveness
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
      "description": "Name of the Excel workbook to produce, e.g. audit-analyze-sourcing-effectiveness-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_sourcing_effectiveness_agent.py` and embedded as the fenced Python below (sha256 afb7b3954f8670dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_sourcing_effectiveness_agent.py` first:

```bash
python3 audit_analyze_sourcing_effectiveness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_sourcing_effectiveness_agent.py   # or on stdin
python3 audit_analyze_sourcing_effectiveness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing effectiveness Completeness Audit — Runs a read-only completeness and policy audit of sourcing effectiveness records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-sourcing-effectiveness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_sourcing_effectiveness',
    "version": '3.0.2',
    "display_name": 'Analyze sourcing effectiveness Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of sourcing effectiveness records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
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
        "upstream_slug": 'audit-analyze-sourcing-effectiveness',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-sourcing-effectiveness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd78b78d2a9422528',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-sourcing-effectiveness'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-analyze-sourcing-effectiveness', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-analyze-sourcing-effectiveness-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit analyze sourcing effectiveness records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to analyze sourcing effectiveness. Output an Excel workbook 'audit-analyze-sourcing-effectiveness-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no analyze sourcing effectiveness data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze sourcing effectiveness records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of sourcing effectiveness records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit sourcing effectiveness records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-sourcing-effectiveness-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants sourcing effectiveness records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAnalyzeSourcingEffectiveness(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeSourcingEffectiveness'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-sourcing-effectiveness-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAnalyzeSourcingEffectiveness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
