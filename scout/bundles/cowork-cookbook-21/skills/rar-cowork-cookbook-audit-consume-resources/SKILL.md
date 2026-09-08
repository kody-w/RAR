---
name: "rar-cowork-cookbook-audit-consume-resources"
description: "Runs a read-only completeness and policy audit of consume resources records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_consume_resources", "rar_sha256": "be9f7504c20e0e6851f26798c2abbf5f56bff4b07f7b537dcbb09e049149c5fc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
