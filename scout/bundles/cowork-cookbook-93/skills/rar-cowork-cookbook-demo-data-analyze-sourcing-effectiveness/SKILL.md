---
name: "rar-cowork-cookbook-demo-data-analyze-sourcing-effectiveness"
description: "Generates 25 realistic demo records for analyze sourcing effectiveness in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_sourcing_effectiveness", "rar_sha256": "4642fa737c1eefdf66540e2ced034d62c5f6d1f9579e49f56ca3046eb5e5905b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
