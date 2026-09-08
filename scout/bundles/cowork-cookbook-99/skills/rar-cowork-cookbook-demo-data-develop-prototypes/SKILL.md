---
name: "rar-cowork-cookbook-demo-data-develop-prototypes"
description: "Generates 25 realistic demo records for develop prototypes in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_prototypes", "rar_sha256": "032f42efdef4a6cbe3b4f941a55b174ce103e72645b946a8d3c7a15389137be4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
