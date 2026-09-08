---
name: "rar-cowork-cookbook-audit-analyze-asset-leases"
description: "Runs a read-only completeness and policy audit of asset lease records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_asset_leases", "rar_sha256": "3257633079bcb9c23f7366b43add54188b282d2f6bf97e956a7d7fcd8f488b8a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
