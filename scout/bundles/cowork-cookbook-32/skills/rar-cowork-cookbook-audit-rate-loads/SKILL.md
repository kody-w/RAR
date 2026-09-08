---
name: "rar-cowork-cookbook-audit-rate-loads"
description: "Runs a read-only completeness and policy audit of rate loads records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_rate_loads", "rar_sha256": "4a5d38107c4da1430f873b157ac098c218de095b1068f5a1b425c1f38feb9c25", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
