---
name: "rar-cowork-cookbook-audit-record-asset-lease-right-of-use"
description: "Runs a read-only completeness and policy audit of asset lease right-of-use records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_asset_lease_right_of_use", "rar_sha256": "93006e933dffd33990037ee9db4f14a607e1d8267b7834c328f7305692e601bf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
