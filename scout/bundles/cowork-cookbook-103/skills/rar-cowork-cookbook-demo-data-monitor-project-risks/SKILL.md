---
name: "rar-cowork-cookbook-demo-data-monitor-project-risks"
description: "Generates 25 realistic demo project-risk records for a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_project_risks", "rar_sha256": "eb7172be9dd44c047d299bd905fb63cf3babf2e151f6c9b95b9b8d3632c9b370", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
