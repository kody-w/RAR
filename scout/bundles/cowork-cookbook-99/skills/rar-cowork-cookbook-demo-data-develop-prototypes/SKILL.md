---
name: "rar-cowork-cookbook-demo-data-develop-prototypes"
description: "Generates 25 realistic demo records for develop prototypes in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_prototypes", "rar_sha256": "032f42efdef4a6cbe3b4f941a55b174ce103e72645b946a8d3c7a15389137be4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_prototypes`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_prototypes_agent.py` and in the RCI capsule.

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

Develop prototypes Demo Data Generator — Generates 25 realistic demo records for develop prototypes in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-prototypes
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
      "description": "Sandbox D365 legal entity to write into (default USMF); must not be production.",
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
    "record_scope": {
      "description": "What the demo records represent \u2014 the 'develop prototypes' scenario or entity type.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-develop-prototypes-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_prototypes_agent.py` and embedded as the fenced Python below (sha256 032f42efdef4a6cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_prototypes_agent.py` first:

```bash
python3 demo_data_develop_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_prototypes_agent.py   # or on stdin
python3 demo_data_develop_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop prototypes Demo Data Generator — Generates 25 realistic demo records for develop prototypes in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_prototypes',
    "version": '3.0.3',
    "display_name": 'Develop prototypes Demo Data Generator',
    "description": "Generates 25 realistic demo records for develop prototypes in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '88711b54c237de0f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/develop-prototypes'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-develop-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'record_scope': "What the demo records represent — the 'develop prototypes' scenario or entity type.", 'workbook_name': 'Excel staging file name, e.g. demo-data-develop-prototypes-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop prototypes data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop prototypes. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-prototypes-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop prototypes records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for develop prototypes in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo records for develop prototypes in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': "What the demo records represent — the 'develop prototypes' scenario or entity type.", 'name': 'record_scope'}, {'description': 'Excel staging file name, e.g. demo-data-develop-prototypes-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded demo/training/pilot data in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopPrototypes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopPrototypes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'record_scope': {'description': "What the demo records represent — the 'develop prototypes' scenario or entity type.", 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-develop-prototypes-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
