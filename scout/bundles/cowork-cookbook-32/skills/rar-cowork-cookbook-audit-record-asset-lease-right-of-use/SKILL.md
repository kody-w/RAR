---
name: "rar-cowork-cookbook-audit-record-asset-lease-right-of-use"
description: "Runs a read-only completeness and policy audit of asset lease right-of-use records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_asset_lease_right_of_use", "rar_sha256": "93006e933dffd33990037ee9db4f14a607e1d8267b7834c328f7305692e601bf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_record_asset_lease_right_of_use`. The original RAPP
agent is preserved byte-for-byte in `audit_record_asset_lease_right_of_use_agent.py` and in the RCI capsule.

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

Record asset lease right-of-use Completeness Audit — Runs a read-only completeness and policy audit of asset lease right-of-use records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-asset-lease-right-of-use
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
      "description": "Date range used to judge stale dates; adjust for demo data eras such as FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-record-asset-lease-right-of-use-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_asset_lease_right_of_use_agent.py` and embedded as the fenced Python below (sha256 93006e933dffd339…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_asset_lease_right_of_use_agent.py` first:

```bash
python3 audit_record_asset_lease_right_of_use_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_record_asset_lease_right_of_use_agent.py   # or on stdin
python3 audit_record_asset_lease_right_of_use_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record asset lease right-of-use Completeness Audit — Runs a read-only completeness and policy audit of asset lease right-of-use records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-asset-lease-right-of-use
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_record_asset_lease_right_of_use',
    "version": '3.0.3',
    "display_name": 'Record asset lease right-of-use Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of asset lease right-of-use records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.',
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
        "upstream_slug": 'audit-record-asset-lease-right-of-use',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-record-asset-lease-right-of-use',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'adafae92e0689695',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/record-asset-lease-right-of-use'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-record-asset-lease-right-of-use', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-record-asset-lease-right-of-use-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit record asset lease right-of-use records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to record asset lease right-of-use. Output an Excel workbook 'audit-record-asset-lease-right-of-use-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no record asset lease right-of-use data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads record asset lease right-of-use records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of asset lease right-of-use records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.', 'example_request': 'Audit asset lease right-of-use records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-record-asset-lease-right-of-use-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants asset lease right-of-use records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditRecordAssetLeaseRightOfUse(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRecordAssetLeaseRightOfUse'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data eras such as FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-record-asset-lease-right-of-use-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditRecordAssetLeaseRightOfUse().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
