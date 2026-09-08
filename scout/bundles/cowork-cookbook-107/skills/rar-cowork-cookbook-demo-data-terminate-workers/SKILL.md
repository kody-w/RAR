---
name: "rar-cowork-cookbook-demo-data-terminate-workers"
description: "Generates 25 realistic demo worker-termination records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_terminate_workers", "rar_sha256": "71acd52bf7120968fd847362fe01e54caf681673a9afc408fada452f7c2d33f6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
