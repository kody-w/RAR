---
name: "rar-cowork-cookbook-report-manage-service-accounts-and-certificates"
description: "Builds a read-only summary report of manage service accounts and certificates activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheet"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_service_accounts_and_certificates", "rar_sha256": "a59f909a07ffbfbcc2255cff10660456e2caadf9e2748bcedf742dd2a601e78e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_service_accounts_and_certificates`. The original RAPP
agent is preserved byte-for-byte in `report_manage_service_accounts_and_certificates_agent.py` and in the RCI capsule.

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

Manage service accounts and certificates Summary Report — Builds a read-only summary report of manage service accounts and certificates activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-service-accounts-and-certificates
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
    "breakdown_dimensions": {
      "description": "Dimensions for the by-dimension breakdowns, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-service-accounts-and-certificates-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_service_accounts_and_certificates_agent.py` and embedded as the fenced Python below (sha256 a59f909a07ffbfbc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_service_accounts_and_certificates_agent.py` first:

```bash
python3 report_manage_service_accounts_and_certificates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_service_accounts_and_certificates_agent.py   # or on stdin
python3 report_manage_service_accounts_and_certificates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service accounts and certificates Summary Report — Builds a read-only summary report of manage service accounts and certificates activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheet

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-service-accounts-and-certificates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_service_accounts_and_certificates',
    "version": '3.0.3',
    "display_name": 'Manage service accounts and certificates Summary Report',
    "description": 'Builds a read-only summary report of manage service accounts and certificates activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheet',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-service-accounts-and-certificates',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-service-accounts-and-certificates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '82d09cd56c56ece1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-service-accounts-and-certificates'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-manage-service-accounts-and-certificates', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for the by-dimension breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-service-accounts-and-certificates-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage service accounts and certificates stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage service accounts and certificates for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-service-accounts-and-certificates-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage service accounts and certificates records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of manage service accounts and certificates activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheet', 'example_request': 'Build a service accounts and certificates summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Dimensions for the by-dimension breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-service-accounts-and-certificates-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary report of service account and certificate activity with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageServiceAccountsAndCertificates(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageServiceAccountsAndCertificates'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for the by-dimension breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-service-accounts-and-certificates-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportManageServiceAccountsAndCertificates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
