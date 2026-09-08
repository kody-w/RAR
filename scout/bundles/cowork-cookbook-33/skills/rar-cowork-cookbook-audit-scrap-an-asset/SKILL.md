---
name: "rar-cowork-cookbook-audit-scrap-an-asset"
description: "Audits scrap-an-asset records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy issues, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_scrap_an_asset", "rar_sha256": "124da2d0ce9c91be645b7f9c7d1653d6e998f9c9c4c29e70fec7678579c493d2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_scrap_an_asset`. The original RAPP
agent is preserved byte-for-byte in `audit_scrap_an_asset_agent.py` and in the RCI capsule.

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

Scrap an asset Completeness Audit — Audits scrap-an-asset records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy issues, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-scrap-an-asset
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
      "description": "Date range for stale-date checks; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-scrap-an-asset-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_scrap_an_asset_agent.py` and embedded as the fenced Python below (sha256 124da2d0ce9c91be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_scrap_an_asset_agent.py` first:

```bash
python3 audit_scrap_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_scrap_an_asset_agent.py   # or on stdin
python3 audit_scrap_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap an asset Completeness Audit — Audits scrap-an-asset records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy issues, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-scrap-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_scrap_an_asset',
    "version": '3.0.3',
    "display_name": 'Scrap an asset Completeness Audit',
    "description": 'Audits scrap-an-asset records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy issues, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-scrap-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-scrap-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'da9aca741265be85',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/scrap-an-asset'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-scrap-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit; defaults to USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-scrap-an-asset-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit scrap an asset records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to scrap an asset. Output an Excel workbook 'audit-scrap-an-asset-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no scrap an asset data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads scrap an asset records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits scrap-an-asset records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy issues, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit scrap an asset records in USMF for completeness and give me the Excel workbook with a summary sheet.', 'inputs': [{'description': 'D365 legal entity to audit; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-scrap-an-asset-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy compliance audit of scrap-an-asset records in D365 F&SCM, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditScrapAnAsset(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditScrapAnAsset'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-scrap-an-asset-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditScrapAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
