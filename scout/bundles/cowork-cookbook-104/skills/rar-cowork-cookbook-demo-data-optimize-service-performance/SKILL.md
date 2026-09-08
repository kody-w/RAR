---
name: "rar-cowork-cookbook-demo-data-optimize-service-performance"
description: "Generates 25 realistic demo records for optimize service performance in a sandbox Dynamics 365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prima"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_optimize_service_performance", "rar_sha256": "bf8b3da18be08cb33edd36829488237e2417e24246b2dda4873b6a82d33cbea1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_optimize_service_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_optimize_service_performance_agent.py` and in the RCI capsule.

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

Optimize service performance Demo Data Generator — Generates 25 realistic demo records for optimize service performance in a sandbox Dynamics 365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prima

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-optimize-service-performance
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
    "scenario": {
      "description": "The scenario the records cover, here 'optimize service performance'.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-optimize-service-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_optimize_service_performance_agent.py` and embedded as the fenced Python below (sha256 bf8b3da18be08cb3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_optimize_service_performance_agent.py` first:

```bash
python3 demo_data_optimize_service_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_optimize_service_performance_agent.py   # or on stdin
python3 demo_data_optimize_service_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Optimize service performance Demo Data Generator — Generates 25 realistic demo records for optimize service performance in a sandbox Dynamics 365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prima

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-optimize-service-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_optimize_service_performance',
    "version": '3.0.3',
    "display_name": 'Optimize service performance Demo Data Generator',
    "description": "Generates 25 realistic demo records for optimize service performance in a sandbox Dynamics 365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prima",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-optimize-service-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-optimize-service-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '929b8285090150f9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/optimize-service-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-optimize-service-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'scenario': "The scenario the records cover, here 'optimize service performance'.", 'workbook_name': 'Excel staging file name, e.g. demo-data-optimize-service-performance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic optimize service performance data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for optimize service performance. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-optimize-service-performance-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic optimize service performance records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for optimize service performance in a sandbox Dynamics 365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prima", 'example_request': 'Generate 25 demo records for optimize service performance in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': "The scenario the records cover, here 'optimize service performance'.", 'name': 'scenario'}, {'description': 'Excel staging file name, e.g. demo-data-optimize-service-performance-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for optimize service performance in a D365 F&SCM sandbox. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataOptimizeServicePerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataOptimizeServicePerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'scenario': {'description': "The scenario the records cover, here 'optimize service performance'.", 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-optimize-service-performance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataOptimizeServicePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
