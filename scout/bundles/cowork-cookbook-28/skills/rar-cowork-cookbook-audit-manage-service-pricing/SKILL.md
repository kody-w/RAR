---
name: "rar-cowork-cookbook-audit-manage-service-pricing"
description: "Runs a read-only completeness and policy audit of service pricing records in Dynamics 365 F&SCM (legal entity USMF) and returns an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_service_pricing", "rar_sha256": "ad9381a3bdf8a37420e8484a940fe40d1e791550f64993dd05f79d18ee247c6d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
