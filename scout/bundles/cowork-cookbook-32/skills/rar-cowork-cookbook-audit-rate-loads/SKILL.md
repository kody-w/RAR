---
name: "rar-cowork-cookbook-audit-rate-loads"
description: "Runs a read-only completeness and policy audit of rate loads records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_rate_loads", "rar_sha256": "4a5d38107c4da1430f873b157ac098c218de095b1068f5a1b425c1f38feb9c25", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_rate_loads`. The original RAPP
agent is preserved byte-for-byte in `audit_rate_loads_agent.py` and in the RCI capsule.

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

Rate loads Completeness Audit — Runs a read-only completeness and policy audit of rate loads records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-rate-loads
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
      "description": "Dynamics 365 legal entity to audit, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-rate-loads-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_rate_loads_agent.py` and embedded as the fenced Python below (sha256 4a5d38107c4da143…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_rate_loads_agent.py` first:

```bash
python3 audit_rate_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_rate_loads_agent.py   # or on stdin
python3 audit_rate_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rate loads Completeness Audit — Runs a read-only completeness and policy audit of rate loads records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-rate-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_rate_loads',
    "version": '3.0.3',
    "display_name": 'Rate loads Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of rate loads records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-rate-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-rate-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7bf460be8de50448',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/rate-loads'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-rate-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-rate-loads-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit rate loads records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to rate loads. Output an Excel workbook 'audit-rate-loads-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no rate loads data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads rate loads records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of rate loads records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit rate loads in USMF for completeness and policy issues and give me the Excel workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-rate-loads-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants rate loads records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditRateLoads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRateLoads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-rate-loads-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditRateLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
