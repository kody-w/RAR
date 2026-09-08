---
name: "rar-cowork-cookbook-demo-data-develop-procurement-catalogs"
description: "Generates 25 realistic demo procurement catalog records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_procurement_catalogs", "rar_sha256": "37376544d418897fe25045745e20ecb46d4a0c3cecdb57e57da70b13b3efa7bd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_procurement_catalogs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_procurement_catalogs_agent.py` and in the RCI capsule.

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

Develop procurement catalogs Demo Data Generator — Generates 25 realistic demo procurement catalog records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-procurement-catalogs
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-develop-procurement-catalogs-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_procurement_catalogs_agent.py` and embedded as the fenced Python below (sha256 37376544d418897f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_procurement_catalogs_agent.py` first:

```bash
python3 demo_data_develop_procurement_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_procurement_catalogs_agent.py   # or on stdin
python3 demo_data_develop_procurement_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop procurement catalogs Demo Data Generator — Generates 25 realistic demo procurement catalog records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-procurement-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_procurement_catalogs',
    "version": '3.0.3',
    "display_name": 'Develop procurement catalogs Demo Data Generator',
    "description": "Generates 25 realistic demo procurement catalog records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-develop-procurement-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-procurement-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '30622b1b5d98d283',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-procurement-catalogs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-develop-procurement-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-develop-procurement-catalogs-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop procurement catalogs data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop procurement catalogs. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-procurement-catalogs-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop procurement catalogs records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo procurement catalog records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo procurement catalog records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-develop-procurement-catalogs-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training procurement catalog data created in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopProcurementCatalogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopProcurementCatalogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-develop-procurement-catalogs-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopProcurementCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
