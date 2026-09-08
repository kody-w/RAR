---
name: "rar-cowork-cookbook-audit-pick-goods"
description: "Runs a read-only completeness and policy audit of pick goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_pick_goods", "rar_sha256": "410995b78d5cddcd39daee4cf0b2715232f309a03d93f8c09bdf2c8aef636894", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_pick_goods`. The original RAPP
agent is preserved byte-for-byte in `audit_pick_goods_agent.py` and in the RCI capsule.

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

Pick goods Completeness Audit — Runs a read-only completeness and policy audit of pick goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-pick-goods
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
      "description": "Date range to treat as current vs stale; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-pick-goods-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_pick_goods_agent.py` and embedded as the fenced Python below (sha256 410995b78d5cddcd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_pick_goods_agent.py` first:

```bash
python3 audit_pick_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_pick_goods_agent.py   # or on stdin
python3 audit_pick_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pick goods Completeness Audit — Runs a read-only completeness and policy audit of pick goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-pick-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_pick_goods',
    "version": '3.0.3',
    "display_name": 'Pick goods Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of pick goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-pick-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-pick-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '80e33ae3e1aae1fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pick-goods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-pick-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-pick-goods-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit pick goods records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to pick goods. Output an Excel workbook 'audit-pick-goods-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no pick goods data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads pick goods records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of pick goods records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit pick goods records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-pick-goods-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants pick goods records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditPickGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPickGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-pick-goods-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditPickGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
