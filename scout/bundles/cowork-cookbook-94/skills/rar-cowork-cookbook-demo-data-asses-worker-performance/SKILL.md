---
name: "rar-cowork-cookbook-demo-data-asses-worker-performance"
description: "Generates 25 realistic worker-performance demo records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_asses_worker_performance", "rar_sha256": "ff71af2840674da5782f44f41db4be91134fb6392eb7b3ac2b6f9147c0aa744b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_asses_worker_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_asses_worker_performance_agent.py` and in the RCI capsule.

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

Asses worker performance Demo Data Generator — Generates 25 realistic worker-performance demo records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-asses-worker-performance
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
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-asses-worker-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_asses_worker_performance_agent.py` and embedded as the fenced Python below (sha256 ff71af2840674da5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_asses_worker_performance_agent.py` first:

```bash
python3 demo_data_asses_worker_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_asses_worker_performance_agent.py   # or on stdin
python3 demo_data_asses_worker_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Asses worker performance Demo Data Generator — Generates 25 realistic worker-performance demo records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-asses-worker-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_asses_worker_performance',
    "version": '3.0.3',
    "display_name": 'Asses worker performance Demo Data Generator',
    "description": "Generates 25 realistic worker-performance demo records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-asses-worker-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-asses-worker-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '38e3a3bf32b78c74',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/asses-worker-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-asses-worker-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-asses-worker-performance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic asses worker performance data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for asses worker performance. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-asses-worker-performance-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic asses worker performance records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic worker-performance demo records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.", 'example_request': 'Generate 25 demo worker performance records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-asses-worker-performance-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need synthetic worker performance assessment data in a D365 F&SCM sandbox for training or pilot demos. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAssesWorkerPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAssesWorkerPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-asses-worker-performance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAssesWorkerPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
