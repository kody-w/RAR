---
name: "rar-cowork-cookbook-demo-data-develop-continuous-improvement-initiatives"
description: "Generates 25 realistic demo records for continuous improvement initiatives in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives", "rar_sha256": "b7b58a0fadb39ff92ca5ceb5322e70f495948cdb8914e667c7cddb584e7cd565", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_continuous_improvement_initiatives_agent.py` and in the RCI capsule.

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

Develop continuous improvement initiatives Demo Data Generator — Generates 25 realistic demo records for continuous improvement initiatives in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-continuous-improvement-initiatives
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-develop-continuous-improvement-initiatives-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_continuous_improvement_initiatives_agent.py` and embedded as the fenced Python below (sha256 b7b58a0fadb39ff9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_continuous_improvement_initiatives_agent.py` first:

```bash
python3 demo_data_develop_continuous_improvement_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_continuous_improvement_initiatives_agent.py   # or on stdin
python3 demo_data_develop_continuous_improvement_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop continuous improvement initiatives Demo Data Generator — Generates 25 realistic demo records for continuous improvement initiatives in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-continuous-improvement-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives',
    "version": '3.0.3',
    "display_name": 'Develop continuous improvement initiatives Demo Data Generator',
    "description": "Generates 25 realistic demo records for continuous improvement initiatives in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-continuous-improvement-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-continuous-improvement-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a3154ba655bdfe3a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/develop-continuous-improvement-initiatives'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-develop-continuous-improvement-initiatives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-develop-continuous-improvement-initiatives-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop continuous improvement initiatives data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop continuous improvement initiatives. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-continuous-improvement-initiatives-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop continuous improvement initiatives records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for continuous improvement initiatives in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo continuous improvement initiative records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-develop-continuous-improvement-initiatives-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded demo data for continuous improvement initiatives in a D365 sandbox for training or pilot scenarios. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopContinuousImprovementInitiatives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopContinuousImprovementInitiatives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-develop-continuous-improvement-initiatives-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopContinuousImprovementInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
