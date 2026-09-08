---
name: "rar-cowork-cookbook-audit-consume-resources"
description: "Runs a read-only completeness and policy audit of consume resources records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_consume_resources", "rar_sha256": "be9f7504c20e0e6851f26798c2abbf5f56bff4b07f7b537dcbb09e049149c5fc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_consume_resources`. The original RAPP
agent is preserved byte-for-byte in `audit_consume_resources_agent.py` and in the RCI capsule.

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

Consume resources Completeness Audit — Runs a read-only completeness and policy audit of consume resources records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-consume-resources
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
      "description": "Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-consume-resources-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_consume_resources_agent.py` and embedded as the fenced Python below (sha256 be9f7504c20e0e68…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_consume_resources_agent.py` first:

```bash
python3 audit_consume_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_consume_resources_agent.py   # or on stdin
python3 audit_consume_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consume resources Completeness Audit — Runs a read-only completeness and policy audit of consume resources records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-consume-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_consume_resources',
    "version": '3.0.2',
    "display_name": 'Consume resources Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of consume resources records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-consume-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-consume-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7120c1ca41afba8e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/consume-resources'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-consume-resources', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-consume-resources-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit consume resources records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to consume resources. Output an Excel workbook 'audit-consume-resources-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no consume resources data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads consume resources records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of consume resources records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit consume resources records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-consume-resources-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants consume resources records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditConsumeResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConsumeResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data vintage (USMF is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-consume-resources-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditConsumeResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
