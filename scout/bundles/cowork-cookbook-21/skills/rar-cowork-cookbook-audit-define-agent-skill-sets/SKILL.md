---
name: "rar-cowork-cookbook-audit-define-agent-skill-sets"
description: "Runs a read-only completeness and policy audit of define agent skill sets records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_agent_skill_sets", "rar_sha256": "0e225cc817280bc3fa3da150de30bbd2fb29f8df78849fb5786c5c519bbe6a26", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_agent_skill_sets`. The original RAPP
agent is preserved byte-for-byte in `audit_define_agent_skill_sets_agent.py` and in the RCI capsule.

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

Define agent skill sets Completeness Audit — Runs a read-only completeness and policy audit of define agent skill sets records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-agent-skill-sets
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
      "description": "Date range used to judge stale dates; adjust for demo data that is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-define-agent-skill-sets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_agent_skill_sets_agent.py` and embedded as the fenced Python below (sha256 0e225cc817280bc3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_agent_skill_sets_agent.py` first:

```bash
python3 audit_define_agent_skill_sets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_agent_skill_sets_agent.py   # or on stdin
python3 audit_define_agent_skill_sets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define agent skill sets Completeness Audit — Runs a read-only completeness and policy audit of define agent skill sets records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-agent-skill-sets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_agent_skill_sets',
    "version": '3.0.2',
    "display_name": 'Define agent skill sets Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of define agent skill sets records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-agent-skill-sets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-agent-skill-sets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f1b75569312680d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-agent-skill-sets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-define-agent-skill-sets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data that is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-define-agent-skill-sets-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define agent skill sets records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define agent skill sets. Output an Excel workbook 'audit-define-agent-skill-sets-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define agent skill sets data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define agent skill sets records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of define agent skill sets records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit define agent skill sets in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data that is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-define-agent-skill-sets-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants define agent skill sets records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineAgentSkillSets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineAgentSkillSets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data that is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-define-agent-skill-sets-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineAgentSkillSets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
