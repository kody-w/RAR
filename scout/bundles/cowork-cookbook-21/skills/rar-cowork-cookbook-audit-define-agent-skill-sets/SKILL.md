---
name: "rar-cowork-cookbook-audit-define-agent-skill-sets"
description: "Runs a read-only completeness and policy audit of define agent skill sets records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_agent_skill_sets", "rar_sha256": "0e225cc817280bc3fa3da150de30bbd2fb29f8df78849fb5786c5c519bbe6a26", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
