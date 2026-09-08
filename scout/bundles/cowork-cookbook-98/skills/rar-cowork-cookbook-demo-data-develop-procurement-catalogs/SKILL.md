---
name: "rar-cowork-cookbook-demo-data-develop-procurement-catalogs"
description: "Generates 25 realistic demo procurement catalog records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_procurement_catalogs", "rar_sha256": "37376544d418897fe25045745e20ecb46d4a0c3cecdb57e57da70b13b3efa7bd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
