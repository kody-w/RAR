---
name: "rar-cowork-cookbook-demo-data-manage-supplier-risk"
description: "Generates 25 realistic demo supplier-risk records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_supplier_risk", "rar_sha256": "6d5446811ffe9f6554ba41678c28e20940746adf160a068f8d81c2ee9e08f9d2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_supplier_risk`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_supplier_risk_agent.py` and in the RCI capsule.

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

Manage supplier risk Demo Data Generator — Generates 25 realistic demo supplier-risk records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-supplier-risk
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
    "legal_entity": {
      "description": "Sandbox D365 legal entity to create records in (default USMF); production is not permitted.",
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
    "record_count": {
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-manage-supplier-risk-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_supplier_risk_agent.py` and embedded as the fenced Python below (sha256 6d5446811ffe9f65…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_supplier_risk_agent.py` first:

```bash
python3 demo_data_manage_supplier_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_supplier_risk_agent.py   # or on stdin
python3 demo_data_manage_supplier_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier risk Demo Data Generator — Generates 25 realistic demo supplier-risk records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-supplier-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_supplier_risk',
    "version": '3.0.3',
    "display_name": 'Manage supplier risk Demo Data Generator',
    "description": "Generates 25 realistic demo supplier-risk records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-supplier-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-supplier-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07be064bf07ba675',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-risk'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-manage-supplier-risk', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF); production is not permitted.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-supplier-risk-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage supplier risk data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage supplier risk. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-supplier-risk-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage supplier risk records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo supplier-risk records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.", 'example_request': 'Generate 25 demo supplier risk records in USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF); production is not permitted.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-supplier-risk-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo supplier risk data in a D365 sandbox legal entity for training or pilot scenarios. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageSupplierRisk(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageSupplierRisk'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF); production is not permitted.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-supplier-risk-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageSupplierRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
