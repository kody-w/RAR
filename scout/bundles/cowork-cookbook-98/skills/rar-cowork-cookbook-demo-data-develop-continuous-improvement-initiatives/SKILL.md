---
name: "rar-cowork-cookbook-demo-data-develop-continuous-improvement-initiatives"
description: "Generates 25 realistic demo records for continuous improvement initiatives in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_continuous_improvement_initiatives", "rar_sha256": "b7b58a0fadb39ff92ca5ceb5322e70f495948cdb8914e667c7cddb584e7cd565", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
