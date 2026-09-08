---
name: "rar-cowork-cookbook-audit-develop-contractor-network"
description: "Runs a read-only completeness and policy audit of develop contractor network records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_contractor_network", "rar_sha256": "8e50f1601ee0b3d3f5822966050a7f68e08d2a4b31dc28f8a3528517e2875984", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_contractor_network`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_contractor_network_agent.py` and in the RCI capsule.

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

Develop contractor network Completeness Audit — Runs a read-only completeness and policy audit of develop contractor network records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of c

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-contractor-network
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
      "description": "Name of the Excel workbook to produce, e.g. audit-develop-contractor-network-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_contractor_network_agent.py` and embedded as the fenced Python below (sha256 8e50f1601ee0b3d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_contractor_network_agent.py` first:

```bash
python3 audit_develop_contractor_network_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_contractor_network_agent.py   # or on stdin
python3 audit_develop_contractor_network_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop contractor network Completeness Audit — Runs a read-only completeness and policy audit of develop contractor network records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of c

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-contractor-network
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_contractor_network',
    "version": '3.0.2',
    "display_name": 'Develop contractor network Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of develop contractor network records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of c',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-contractor-network',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-contractor-network',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f2d64f48aa6c095d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-contractor-network'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-develop-contractor-network', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-develop-contractor-network-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit develop contractor network records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to develop contractor network. Output an Excel workbook 'audit-develop-contractor-network-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no develop contractor network data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop contractor network records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of develop contractor network records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of c', 'example_request': 'Audit develop contractor network records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-contractor-network-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants develop contractor network records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDevelopContractorNetwork(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopContractorNetwork'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-develop-contractor-network-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDevelopContractorNetwork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
