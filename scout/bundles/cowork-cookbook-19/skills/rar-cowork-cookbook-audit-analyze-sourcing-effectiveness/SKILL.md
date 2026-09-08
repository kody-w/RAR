---
name: "rar-cowork-cookbook-audit-analyze-sourcing-effectiveness"
description: "Runs a read-only completeness and policy audit of sourcing effectiveness records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_sourcing_effectiveness", "rar_sha256": "afb7b3954f8670dd00a67fd08837d7474d82d979b3de6e69b63ce2a1b8ecb45d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
