---
name: "rar-cowork-cookbook-demo-data-monitor-background-jobs"
description: "Generates 25 realistic demo background-job records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_background_jobs", "rar_sha256": "59433331b729c0f632e95abe736b8f7dc10ff0ce42d774973bd989d1a3bbade0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_background_jobs_agent.py` and in the RCI capsule.

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

Monitor background jobs Demo Data Generator — Generates 25 realistic demo background-job records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-background-jobs
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
      "description": "Excel staging file name, e.g. demo-data-monitor-background-jobs-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_background_jobs_agent.py` and embedded as the fenced Python below (sha256 59433331b729c0f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_background_jobs_agent.py` first:

```bash
python3 demo_data_monitor_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_background_jobs_agent.py   # or on stdin
python3 demo_data_monitor_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor background jobs Demo Data Generator — Generates 25 realistic demo background-job records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_background_jobs',
    "version": '3.0.3',
    "display_name": 'Monitor background jobs Demo Data Generator',
    "description": "Generates 25 realistic demo background-job records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-monitor-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '756377500cfc55f6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/monitor-background-jobs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-monitor-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-monitor-background-jobs-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic monitor background jobs data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for monitor background jobs. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-monitor-background-jobs-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic monitor background jobs records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo background-job records for a sandbox D365 legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo monitor background job records in the USMF sandbox and create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-monitor-background-jobs-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for monitor background jobs in a D365 F&SCM sandbox — never against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMonitorBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-monitor-background-jobs-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataMonitorBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
