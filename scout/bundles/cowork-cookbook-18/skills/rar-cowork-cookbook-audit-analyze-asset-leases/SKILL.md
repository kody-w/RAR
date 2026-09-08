---
name: "rar-cowork-cookbook-audit-analyze-asset-leases"
description: "Runs a read-only completeness and policy audit of asset lease records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_asset_leases", "rar_sha256": "3257633079bcb9c23f7366b43add54188b282d2f6bf97e956a7d7fcd8f488b8a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_asset_leases_agent.py` and in the RCI capsule.

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

Analyze asset leases Completeness Audit — Runs a read-only completeness and policy audit of asset lease records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-asset-leases
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
      "description": "Name of the Excel workbook to produce, e.g. audit-analyze-asset-leases-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_asset_leases_agent.py` and embedded as the fenced Python below (sha256 3257633079bcb9c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_asset_leases_agent.py` first:

```bash
python3 audit_analyze_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_asset_leases_agent.py   # or on stdin
python3 audit_analyze_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset leases Completeness Audit — Runs a read-only completeness and policy audit of asset lease records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_asset_leases',
    "version": '3.0.2',
    "display_name": 'Analyze asset leases Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of asset lease records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
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
        "upstream_slug": 'audit-analyze-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9ae2947750c26625',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-leases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-analyze-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-analyze-asset-leases-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit analyze asset leases records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to analyze asset leases. Output an Excel workbook 'audit-analyze-asset-leases-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no analyze asset leases data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze asset leases records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of asset lease records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit asset leases in USMF for completeness and policy issues and give me the Excel workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-asset-leases-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants asset lease records checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAnalyzeAssetLeases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeAssetLeases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-analyze-asset-leases-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAnalyzeAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
