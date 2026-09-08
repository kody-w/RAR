---
name: "rar-cowork-cookbook-demo-data-analyze-worker-performance"
description: "Generates 25 realistic demo worker-performance records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_worker_performance", "rar_sha256": "7246c4483da3cd5248b8ac9a16a8c04f0655b09486df4287e7e201b2c0837976", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_worker_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_worker_performance_agent.py` and in the RCI capsule.

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

Analyze worker performance Demo Data Generator — Generates 25 realistic demo worker-performance records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-worker-performance
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-analyze-worker-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_worker_performance_agent.py` and embedded as the fenced Python below (sha256 7246c4483da3cd52…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_worker_performance_agent.py` first:

```bash
python3 demo_data_analyze_worker_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_worker_performance_agent.py   # or on stdin
python3 demo_data_analyze_worker_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze worker performance Demo Data Generator — Generates 25 realistic demo worker-performance records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-worker-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_worker_performance',
    "version": '3.0.3',
    "display_name": 'Analyze worker performance Demo Data Generator',
    "description": "Generates 25 realistic demo worker-performance records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-analyze-worker-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-worker-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '63d989ff816f7ff4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-worker-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-analyze-worker-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-analyze-worker-performance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic analyze worker performance data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for analyze worker performance. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-analyze-worker-performance-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic analyze worker performance records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo worker-performance records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo worker performance records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-analyze-worker-performance-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo worker performance data seeded in a D365 sandbox (never production) for training or pilot scenarios.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAnalyzeWorkerPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeWorkerPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-analyze-worker-performance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAnalyzeWorkerPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
