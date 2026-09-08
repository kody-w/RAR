---
name: "rar-cowork-cookbook-audit-develop-contractor-network"
description: "Runs a read-only completeness and policy audit of develop contractor network records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet of c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_contractor_network", "rar_sha256": "8e50f1601ee0b3d3f5822966050a7f68e08d2a4b31dc28f8a3528517e2875984", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
