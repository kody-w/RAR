---
name: "rar-cowork-cookbook-demo-data-monitor-project-risks"
description: "Generates 25 realistic demo project-risk records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_project_risks", "rar_sha256": "eb7172be9dd44c047d299bd905fb63cf3babf2e151f6c9b95b9b8d3632c9b370", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_project_risks`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_project_risks_agent.py` and in the RCI capsule.

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

Monitor project risks Demo Data Generator — Generates 25 realistic demo project-risk records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-project-risks
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
      "description": "Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.",
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
      "description": "Number of demo project risk records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. 'demo-data-monitor-project-risks-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_project_risks_agent.py` and embedded as the fenced Python below (sha256 eb7172be9dd44c04…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_project_risks_agent.py` first:

```bash
python3 demo_data_monitor_project_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_project_risks_agent.py   # or on stdin
python3 demo_data_monitor_project_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor project risks Demo Data Generator — Generates 25 realistic demo project-risk records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-project-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_project_risks',
    "version": '3.0.3',
    "display_name": 'Monitor project risks Demo Data Generator',
    "description": "Generates 25 realistic demo project-risk records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-monitor-project-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-project-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd695525083d33b80',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/monitor-project-risks'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-monitor-project-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'record_count': 'Number of demo project risk records to generate; defaults to 25.', 'workbook_name': "Excel staging file name, e.g. 'demo-data-monitor-project-risks-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic monitor project risks data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for monitor project risks. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-monitor-project-risks-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic monitor project risks records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo project-risk records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo project risk records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo project risk records to generate; defaults to 25.', 'name': 'record_count'}, {'description': "Excel staging file name, e.g. 'demo-data-monitor-project-risks-2026-05-24.xlsx'.", 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo project risk data in a D365 sandbox for training or pilot scenarios. Sandbox only - never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMonitorProjectRisks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorProjectRisks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo project risk records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': "Excel staging file name, e.g. 'demo-data-monitor-project-risks-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(DemoDataMonitorProjectRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
