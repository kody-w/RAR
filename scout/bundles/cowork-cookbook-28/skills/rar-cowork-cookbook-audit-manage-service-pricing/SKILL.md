---
name: "rar-cowork-cookbook-audit-manage-service-pricing"
description: "Runs a read-only completeness and policy audit of service pricing records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_service_pricing", "rar_sha256": "ad9381a3bdf8a37420e8484a940fe40d1e791550f64993dd05f79d18ee247c6d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_service_pricing`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_service_pricing_agent.py` and in the RCI capsule.

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

Manage service pricing Completeness Audit — Runs a read-only completeness and policy audit of service pricing records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-service-pricing
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
      "description": "D365 legal entity to audit; defaults to USMF.",
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
      "description": "Excel workbook name, e.g. audit-manage-service-pricing-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_service_pricing_agent.py` and embedded as the fenced Python below (sha256 ad9381a3bdf8a374…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_service_pricing_agent.py` first:

```bash
python3 audit_manage_service_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_service_pricing_agent.py   # or on stdin
python3 audit_manage_service_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service pricing Completeness Audit — Runs a read-only completeness and policy audit of service pricing records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-service-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_service_pricing',
    "version": '3.0.3',
    "display_name": 'Manage service pricing Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of service pricing records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-service-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-service-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b051040e708421fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/manage-service-pricing'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-manage-service-pricing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; defaults to USMF.', 'output_filename': 'Excel workbook name, e.g. audit-manage-service-pricing-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit manage service pricing records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to manage service pricing. Output an Excel workbook 'audit-manage-service-pricing-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no manage service pricing data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage service pricing records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of service pricing records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit service pricing records in USMF for completeness and export the findings to an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-manage-service-pricing-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants service pricing records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditManageServicePricing(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageServicePricing'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-manage-service-pricing-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditManageServicePricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
