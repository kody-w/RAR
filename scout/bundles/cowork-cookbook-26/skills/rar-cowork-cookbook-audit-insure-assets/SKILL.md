---
name: "rar-cowork-cookbook-audit-insure-assets"
description: "Runs a read-only completeness and policy audit of insure assets records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_insure_assets", "rar_sha256": "b1b476f984754e51e6088562c003721346e95616cfb4b52b22770bfb239e11d8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_insure_assets`. The original RAPP
agent is preserved byte-for-byte in `audit_insure_assets_agent.py` and in the RCI capsule.

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

Insure assets Completeness Audit — Runs a read-only completeness and policy audit of insure assets records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-insure-assets
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
      "description": "Name of the Excel workbook to produce, e.g. audit-insure-assets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_insure_assets_agent.py` and embedded as the fenced Python below (sha256 b1b476f984754e51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_insure_assets_agent.py` first:

```bash
python3 audit_insure_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_insure_assets_agent.py   # or on stdin
python3 audit_insure_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Insure assets Completeness Audit — Runs a read-only completeness and policy audit of insure assets records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-insure-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_insure_assets',
    "version": '3.0.2',
    "display_name": 'Insure assets Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of insure assets records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
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
        "upstream_slug": 'audit-insure-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-insure-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4ef5eaf5547f9a59',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/insure-assets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-insure-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-insure-assets-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit insure assets records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to insure assets. Output an Excel workbook 'audit-insure-assets-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no insure assets data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads insure assets records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of insure assets records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit insure assets in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-insure-assets-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants insure assets records checked for missing fields, stale dates, blank descriptions, inactive entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditInsureAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditInsureAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-insure-assets-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditInsureAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
