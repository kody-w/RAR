---
name: "rar-cowork-cookbook-demo-data-analyze-worker-performance"
description: "Generates 25 realistic demo worker-performance records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_worker_performance", "rar_sha256": "7246c4483da3cd5248b8ac9a16a8c04f0655b09486df4287e7e201b2c0837976", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
