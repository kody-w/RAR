---
name: "rar-cowork-cookbook-audit-insure-assets"
description: "Runs a read-only completeness and policy audit of insure assets records in Dynamics 365 F&SCM for a legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_insure_assets", "rar_sha256": "b1b476f984754e51e6088562c003721346e95616cfb4b52b22770bfb239e11d8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
