---
name: "rar-cowork-cookbook-demo-data-analyze-sourcing-effectiveness"
description: "Generates 25 realistic demo records for analyze sourcing effectiveness in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_sourcing_effectiveness", "rar_sha256": "4642fa737c1eefdf66540e2ced034d62c5f6d1f9579e49f56ca3046eb5e5905b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_sourcing_effectiveness`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_sourcing_effectiveness_agent.py` and in the RCI capsule.

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

Analyze sourcing effectiveness Demo Data Generator — Generates 25 realistic demo records for analyze sourcing effectiveness in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sourcing-effectiveness
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
      "description": "Sandbox D365 legal entity to create records in (default USMF).",
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
      "description": "Excel staging file name, e.g. demo-data-analyze-sourcing-effectiveness-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_sourcing_effectiveness_agent.py` and embedded as the fenced Python below (sha256 4642fa737c1eefdf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_sourcing_effectiveness_agent.py` first:

```bash
python3 demo_data_analyze_sourcing_effectiveness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_sourcing_effectiveness_agent.py   # or on stdin
python3 demo_data_analyze_sourcing_effectiveness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing effectiveness Demo Data Generator — Generates 25 realistic demo records for analyze sourcing effectiveness in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-sourcing-effectiveness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_sourcing_effectiveness',
    "version": '3.0.3',
    "display_name": 'Analyze sourcing effectiveness Demo Data Generator',
    "description": "Generates 25 realistic demo records for analyze sourcing effectiveness in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-analyze-sourcing-effectiveness',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-sourcing-effectiveness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '481fb5cd4c206dc4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-sourcing-effectiveness'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-analyze-sourcing-effectiveness', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-analyze-sourcing-effectiveness-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic analyze sourcing effectiveness data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for analyze sourcing effectiveness. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-analyze-sourcing-effectiveness-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic analyze sourcing effectiveness records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for analyze sourcing effectiveness in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo records for analyze sourcing effectiveness in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-analyze-sourcing-effectiveness-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need sample sourcing-effectiveness data in a D365 sandbox for training or pilot demos. Sandbox only — never a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAnalyzeSourcingEffectiveness(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeSourcingEffectiveness'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-analyze-sourcing-effectiveness-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAnalyzeSourcingEffectiveness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
