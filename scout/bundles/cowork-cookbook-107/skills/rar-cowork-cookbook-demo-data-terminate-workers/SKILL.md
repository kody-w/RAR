---
name: "rar-cowork-cookbook-demo-data-terminate-workers"
description: "Generates 25 realistic demo worker-termination records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_terminate_workers", "rar_sha256": "71acd52bf7120968fd847362fe01e54caf681673a9afc408fada452f7c2d33f6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_terminate_workers`. The original RAPP
agent is preserved byte-for-byte in `demo_data_terminate_workers_agent.py` and in the RCI capsule.

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

Terminate workers Demo Data Generator — Generates 25 realistic demo worker-termination records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-terminate-workers
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
      "description": "Number of demo terminate-worker records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. 'demo-data-terminate-workers-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_terminate_workers_agent.py` and embedded as the fenced Python below (sha256 71acd52bf7120968…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_terminate_workers_agent.py` first:

```bash
python3 demo_data_terminate_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_terminate_workers_agent.py   # or on stdin
python3 demo_data_terminate_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Terminate workers Demo Data Generator — Generates 25 realistic demo worker-termination records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-terminate-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_terminate_workers',
    "version": '3.0.3',
    "display_name": 'Terminate workers Demo Data Generator',
    "description": "Generates 25 realistic demo worker-termination records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-terminate-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-terminate-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '130512d6f740c95f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/terminate-workers'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-terminate-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo terminate-worker records to generate (default 25).', 'workbook_name': "Excel staging file name, e.g. 'demo-data-terminate-workers-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic terminate workers data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for terminate workers. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-terminate-workers-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic terminate workers records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo worker-termination records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo terminate worker records in USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo terminate-worker records to generate (default 25).', 'name': 'record_count'}, {'description': "Excel staging file name, e.g. 'demo-data-terminate-workers-2026-05-24.xlsx'.", 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need synthetic terminate-worker demo data created in a D365 sandbox tenant for training or pilot scenarios. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataTerminateWorkers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTerminateWorkers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo terminate-worker records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': "Excel staging file name, e.g. 'demo-data-terminate-workers-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(DemoDataTerminateWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
