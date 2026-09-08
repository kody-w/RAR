---
name: "rar-cowork-cookbook-demo-data-scrap-defective-inventory"
description: "Generates 25 realistic demo scrap-defective-inventory records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_scrap_defective_inventory", "rar_sha256": "a4ab6cb7f77e380029ecbc1c847bbca09df61c85cd75f9d13af86a0a475d3c0d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_scrap_defective_inventory`. The original RAPP
agent is preserved byte-for-byte in `demo_data_scrap_defective_inventory_agent.py` and in the RCI capsule.

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

Scrap defective inventory Demo Data Generator — Generates 25 realistic demo scrap-defective-inventory records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-defective-inventory
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
      "description": "Sandbox D365 legal entity to generate records in (default USMF).",
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-scrap-defective-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_scrap_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 a4ab6cb7f77e3800…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_scrap_defective_inventory_agent.py` first:

```bash
python3 demo_data_scrap_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_scrap_defective_inventory_agent.py   # or on stdin
python3 demo_data_scrap_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap defective inventory Demo Data Generator — Generates 25 realistic demo scrap-defective-inventory records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_scrap_defective_inventory',
    "version": '3.0.3',
    "display_name": 'Scrap defective inventory Demo Data Generator',
    "description": "Generates 25 realistic demo scrap-defective-inventory records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-scrap-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-scrap-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd60e18c3a4bfd3a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/scrap-defective-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-scrap-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to generate records in (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-scrap-defective-inventory-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic scrap defective inventory data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for scrap defective inventory. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-scrap-defective-inventory-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic scrap defective inventory records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo scrap-defective-inventory records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo scrap defective inventory records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-scrap-defective-inventory-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or training data for scrap defective inventory in a sandbox D365 tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataScrapDefectiveInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataScrapDefectiveInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-scrap-defective-inventory-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataScrapDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
