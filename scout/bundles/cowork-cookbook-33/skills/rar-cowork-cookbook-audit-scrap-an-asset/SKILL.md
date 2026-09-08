---
name: "rar-cowork-cookbook-audit-scrap-an-asset"
description: "Audits scrap-an-asset records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy issues, returning an Excel workbook with a sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_scrap_an_asset", "rar_sha256": "124da2d0ce9c91be645b7f9c7d1653d6e998f9c9c4c29e70fec7678579c493d2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
