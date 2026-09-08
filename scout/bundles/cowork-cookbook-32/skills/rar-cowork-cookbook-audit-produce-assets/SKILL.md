---
name: "rar-cowork-cookbook-audit-produce-assets"
description: "Runs a read-only completeness and policy audit of produce assets records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_produce_assets", "rar_sha256": "78d726c8fb32b14191d3edbda0cb52e27dafa4780a454edc0b0b873c841cff44", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_produce_assets`. The original RAPP
agent is preserved byte-for-byte in `audit_produce_assets_agent.py` and in the RCI capsule.

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

Produce assets Completeness Audit — Runs a read-only completeness and policy audit of produce assets records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-produce-assets
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
      "description": "Name of the Excel workbook to produce, e.g. audit-produce-assets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_produce_assets_agent.py` and embedded as the fenced Python below (sha256 78d726c8fb32b141…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_produce_assets_agent.py` first:

```bash
python3 audit_produce_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_produce_assets_agent.py   # or on stdin
python3 audit_produce_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Produce assets Completeness Audit — Runs a read-only completeness and policy audit of produce assets records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-produce-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_produce_assets',
    "version": '3.0.3',
    "display_name": 'Produce assets Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of produce assets records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
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
        "upstream_slug": 'audit-produce-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-produce-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a4948b194beffd04',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/produce-assets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-produce-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-produce-assets-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit produce assets records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to produce assets. Output an Excel workbook 'audit-produce-assets-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no produce assets data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads produce assets records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of produce assets records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit produce assets in USMF for completeness and policy issues and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-produce-assets-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants produce assets records in a D365 legal entity checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditProduceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProduceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-produce-assets-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditProduceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
