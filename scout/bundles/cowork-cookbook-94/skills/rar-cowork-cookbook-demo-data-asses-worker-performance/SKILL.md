---
name: "rar-cowork-cookbook-demo-data-asses-worker-performance"
description: "Generates 25 realistic worker-performance demo records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_asses_worker_performance", "rar_sha256": "ff71af2840674da5782f44f41db4be91134fb6392eb7b3ac2b6f9147c0aa744b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbObWLbmX1Gf+5CZV/ZhEIPkiopohECAmAQCgdIVTmYQ8yyUN/97b6RzbGeV69atjn5qOXzEsPea17fWEvz+4vRdXDYvn170wCkWeyfLkjhoFk7hL+hyLJsUfJWpC/4vvLLomsTtu7JpXz68+EHrNUnVJWUBtu+DImicLmgXKL5oAidL2i7xFjOFoPlYBU1YNrlTeMHCD/ISrPDKxm8XSbFwFi3g5pa3xW5F4IssiJxsERRd0k2Ln/0gdPqsWxi6xP7yYdF2TgRYdHGQP7YWC+bmBdmDzUPGMGna7sPCAxJ0bws/zH8LwLHrm6JdBI4XL4pgfBPhp3ZRNUnuNNMiDaZXoFdwc/IqC9qXT7/+7cNLAo5fPv3+4mVOCy697ID0O6dzqLYN2vNDO/WbcmB75hQRWFdNwK4FOH9THVwCuizezn5ugyz8sPjP/0xHp4naXz59LhZvn88v8z+tL2axF13ptF3gLzynctwkAzZ5XVDZ6EztV4WA/YBbiuj1ufMbpbJa/HW+9/OTyWsUdD9/fimr2U/AaZ9fflmUDeDX9PPx60yl+vmX16wcg+bnX77RaXv3GnjdTAxI/frl7fyNLFj4bWkSLr7oKkO/8QImTqoAEP9Ov/nzFP2N3JtJvjwX/1xWHxY/pjzr81cg7zPwXED3x2SBDcDOl9drmRQ/v/FoyiEoZg/9/Ms/I+vFgZfOYfs/ovvrk3AcOD6w1ptJQITOLvjbYvmm21ea/5xtBQLm39EELH9n99VQ/4z2w7N/RzpLCpAY7778IbkfbVj+dfHrP9Xtv9vwYRF+BlmTJQOIOzcLPi1+f4TIrz/53y7+9Lc/AOl/SUYv+8Z7UPgC0i0Jg7b78uXXn9rH5Z/+9utPfQWiOHDyL32T/Yjmj+z64PMnC76t+vnPewF/o0iLciwWX3No8XtZ/a/mj9eFCQDP/3a9/bT4PhPnz3IxK/HO9GmC77KxBbJ+Z8dfXv4A2FMAbXrvcRvgx3/8x0JKvKZsy7Bb6F7Zdwvg4C7Jg1n4U5wAOH1AHlAA2LVNgGHf1oH4nz08S1yGi9/+t/eA9o/eG7RDMyZ/8QGsfXFmXPvyhO0v38H2b6+LE6BcNkmUFACgNUpVPxcAjYtu5lo1QRs0A0Aqd+qCj2DXx/lgBunf/jXxLw86r9X026PwJE/s02h+xr22z4LXWcPzDONPfTyA/MEt8HrAIis9IE+YAMj+ADRvy2wAuDlbo02TLFv4CUAWULOmB21gsU8zsd9++8112vhz8QTq1eJZzFoILPgqzuLjR6BYmCVR3H0uAi8uFz/9/sdPi/9a/He7HsRnHirQ980fQEJBV+QFyK8+B8vmygeA3fEf/vj9jzfzAjKgjC6A95IwedavOQ/SwH+3tc5RH1GcWLgBMB6wb16VTQfQf5F0rws+XHyVFzCdb831IS7bDpTdKij8oPAmQNUB6ny1ZFF2oAR3SRtOHxZ9Gzy4/uY2zkPEHCS60/22kGgVVKMyA39mMR+LwOaySID5v0bC8zog0oDCun0n8bqQ54hcVE7jVHHjvPEInadfQBV63w6IO3N1/lzMhTeYTfVIj6d5ornJAF3F06UfZ5+DriQHMfRsJbr3Nc5cM0+P2tl8Ltq30Hea4FH1gSjTIuoTf469v7yFVBuXfeY/7AcknSm9ecF/88ojBh9l/62rWXzf1cx9wWJuDBZvndBcWnsURrDF/yet0UP9/V5j9tSJ2S0Y+aTZT7fMjeHsvmcvOQsHNHqm4Le+5R2b3iH6c5ElIMaa6S/PlQ9nvq15wl7fANtrlPagDyIJWHym+wj0OXCbZk4R53PxXgs+AIM9gA/4GqACyJo5WN8ZznffJY1B6s/n3/qCN51njADBvKh6NwM+CoPAdx0vBVI1c7K+eRREfTAn7hgnwGLfazV7B9gL0F8AIRKQfqBevH7F5+fdd9H/tPHZ/sxbHq1hD3K1eRAAcgSzgDN6jUkHIMvpnn040PPTgwhQI6+6WXcXZMvTrXMkN0HdJ23Szcj4tGtQAVz+OH8/NZ2vBrcKJAgwFkiDqgfWfSTOjCk5aG6ADCAuQR7lSfEM3DcjPAg6+YwCAGXfYuhJ8XH5TaHgkW1zlXrfOCsy75kL/yIEooMr0/dgcfpRmAB6+bziwffvI+0rt5n2DJgtAD3A8f3us0N4fRb5ZxexeKf76R8GnZ//vVnoUbaNPwfAp0XcdVX7CYKepfa90r4CuIKesraPqvtxLowfH4Xx4z8iwp8oP5X+tPj3pPsTibfs+LRAXuFXeL4lvkXX2wcYg/64tT9i893PhRZ8g1PAvsxBeM2um0CZ/1r73peAAhg1AKLA4mctbOcSOgKEeYA/8MPn4vtwn9MN1JYimsOzLb+DgUcTAEL/6bavNQrcKjrA25/bxiiYh7VHcrTBy6eiz7IPLwUIvP/JkDYXonwO6nae7UD6AJt3SfA4e2DErZsP/zziKo8DJ3sFYA/wKGu/D7y38jGXz+/y46kl0M4DHD4s/AfygpgEWs7M59xyWhCsQLRZm26qZvGf89zcAT4Q/8sT8f9RIP2fFgcAeyNIj+BZUf9cKv6yyHvQD8wWdR/Q4T9bzB8K8LU//UfuZ9AWzIz88tNcIT+8oRD4BjMFqDPv4wFQ+21ge0zXRQ9m4V/n0WT2w2PLfAD2gK+vm77+vuAGL3/7gVxPw34Blbv4gafkPndBxAGE/lNFBcK+x+o3m6D4Lz/U/L1ufnnG1N+zeBbXuejOQPmI2nnhh0XwGr0u/nVmf0RhlPgI4x9R7PWWtbcfyPBQEwA4KIOzxb654ptBysfgNosLDNg9f2f4/QVEtjMzf4vtt84fLAd497Gdux0I5D9gCM6fmQru/V/MBG8U2tgBHSkgEYYk4oToGoMJEvMdnFyjIYaFGOK7mBtsEGSFhS6x2qCBS7orx0NdItwgGOnBjkNimAvoPTP+y9zUJbNUM1NgjI8ANIJvt8El/02dp/izrb6OILPab1r9/uISGFjJYS1PPT80tERc6Ey6k2hBFry+ZaN5OFysUpZzOLaEe2uT3ZZinBtJ31duN25tI9FuosVKRRbfVltJpjliq6J6QA6FkMbxTcsUNFu5SAtL+4NQ7LI7XtzX9zaQOM+7cFuHFSVNzjNIsPbHySJc/Jau6YNNZkJscWGfi939oPXmMu/Dq2tBeD3knN7evCRbYR57NgyHKk85LPAsx18qLrMTOtKG5LoW2Ckt1tZtvVluGJH1lu7+qGu5eb4zEu4fBiwT1j7ELe/nCLQBQmjb2SSevLWsMUUxSpf1/SDKIqxPUzRMDcOPzL7aYmQFjccmy84By4jEaJbpOnXu2NZOJkKRCxRiM/9GRGsuRsmwENC1quKYl+Dq6br0oEARr+eyjE5GMwrqVFsHD29tdxNxWyORdirEGAZMKrx500yz0iJ7p/AlbChTApnj3jD0u8RQREntpOxYbJeBtEqhKNIvLqsRWAYLIxiHbE1dUvxBzCoexcuuyTVfy8sI2znY2MP3Bg+SDrPUjkUHouitqjNuNpnXUMqm2KjKNWNIG30qdrG28SLdP9JsftIvFZ/qJHs/1XSl3Dcpa0fChjrbNFWvgzaPvGgJ96ShrOW7c6vO16sgMKi+5vi2ps+WAq/3tCC7VEomwjRYlLhu1+fsmMnXONv3WyjFzzBhm6GW1lZAx/elKZmsxsKq7E6ZnKXtZXV0N1iiXvRQuuUGwwpOZqZsaeFSaMZZG/OuOmlLm++z+87XynIy/RZiIAqGyTa4SZdqC5naoNmHuDlud2niadD9FFjwbqeTtCQgw00p/cPob/e5ubMO6bY5jjI2ObiP6K1GnOJDE9W3U7N3ArNPTQ3nJ5bgaQgrd/K5UphG4EKqMU/YbRC2YyaGkYhUuzWj3xTsJMXROcRbg5fFTeOsxhrJzxfWV3YRRhXbog5YQneptVl6xnapHvPtbquE416ZCKhEbdeK6zCaVvl4QON9jjVhYCzX1Wq4aWdcXW5hxjuZJCSp6V4cw8Krje2h1jN4RNvkpKOs3XcHnl9PbZOM1HRZEp25i6+0zU0MTZUDuubD9bYW02Hkuhw9maPZqEiuSZpT4cEEc65wr3TU1oVDWunX8ZDkN3+bbFdU5fg8jUVQ4fVqthYzQkBHthuTlD4K1+HEn09LJEVty1bavVw0Mla0TL323Y2ZV6mNuBSB17qiON216Y63bnOKnVhwUuaUKcYJX+1GtZwOIhSsPFFlMsnZ5/zFHFlrVawm7bAHRucn9xIK6WW/zKn7eLiLG7ik9dZGuEtQ7fbX4t6eyZqvme3hYEfYcafSbpGk64pZImFfiErbZANzL+ztMiQYEFeiKEgSr9xDz9QOmypGulI+1gfFPuLZqsjvV02kPGeAi5uYk2KO0HfIVFOD6C+ZwBXXI7+Vs4AW9t6OLyQ1unCCHOCDmVVbgeLWOr+7H72l70p9sovNDROF/KSN0CY7JU2J24Xa50c5Wl8PorXeKtYWXh1KCnQwDBpENR62dUiRp/O4O8dj1mxpT17RFKvbJ4XNxq0vLFm6d5KpPhyxarI1rNNhiOSb9pazwbI2piiOyjWEx5bXTWtjqRaGEzFIKKj+KvDWrqLgoS416sHedthuGuyUxzc4Y3pNPnijMfhKuLqaNyygV5HR8ntB6kb/VmdUudRim1xlqnwQMuTgyTeu0kWiUGVH2t42PCtWaGPv+0lArjx8YTHIVik+F2wQaJ7tpuEyjfcHVtLM2p6MgYF2fg6vGogkDrl3qn16R5sHKRqvuLS7uhG+C4xh6+8qQcdXBElPjY0hDF0mbdzzjnLh+AOO6Ix4r30TootKGrO8ZHlRZMjOqzTH1VcbW9my46k7J5Hrh/omqhtzHM5etG/PaF4q97g+e9yWTzFri5/OnHq/rXxOIDxDiAy4b28ncnuo1px5ToywDuHp5JPsrgQpPg2UdF8N/Y1SRP9sucdbrChBsTzeoVWRLK37BRtCaOIw6BQ6zXBMq/FSFEOOX6iWLpg9iqthhJdwyOLCUTbLvhxpzVE6xZ8YLK6qeolPu5pIMc0hZBnv64qhU4wdXbGhAjJutHpbdwK8a2hnjyTR0WCVC05fUYJljiXN3A/+4bAbpdHR+H1+GUc487a1KwXeyPB5fZ82B9/jAhxZ3dIym/DaDRTO6RUeJdddp8V4vnVIZ3VSIEuUavQ+brbXGxVbBwdL6oO9aexG6ygtKPa4TV0tKU7HcMjGw4axHQ0PgoGgPH9rV6kuCAZ33+VuJAXEZj0s3cLhKKNWqWPIKe5UNlQZFOEgwtXVbe7XQRtxk+l91poQc5lGVGouDzKu6ydKtBNO1IupMvaspl7Z/TE3abTmqZIPDJjZe3E11SUW+Dl5CfnEaK5Lp+d3W4dJ4j7lRwLSBrtalYXd4AIY04rtMVOZXJ8O6eUSZKxhV4FIXWiMwxKe2kbMyaTP5WETuKDS3HuJHlqezm9yvDtbwmnSschUbqxIRZuzKRN35ATgnIby7VVjxCxqHLkVdUi5yjgn7zQ/K0VdbZXGrvZ61gxbm6ITAycaPVmardkLsR2h50ttYVdjo9THghpzkhJ06LSW6qz2q6Vus0eBTBWj1Kv6aMDGZCNDsrVYVcKn6JI6tmoarBhZbSuX0XBhiOsluW/KiQmuxlY5kRvUwmthv6eWdqYeAmpCZRgFiRDVe//YrxAiw6zL5K0puqiHuPdrVBgJVhukI87cq2VO+1YaeNiZSJObcMyzpVdoN1/Ja0xatYKgDXsBzemxdjbb8hBPBEzvG1M5IitmTI7a+SQJUad10Q7bmLyin/16tFLd3ua0TBeOY8el7qpiEIl5dGwLxFtqwzaP4Yo/i152KGwFkpLmcvKcm5+nq/rurIdrh4nqRHvmbn8mIEbiSttjUP6sHKeAEM+CQ0Ox059SiBnLm7Q7T+dstx82261FG3lPp7nsuPAdlftK4wbaK6OzxZrbnQ7tmVs0gJC10f5gGYALJiyhZYHd9VLOT6WS2UHNnWJsq2ygy47HbhOsMvayB4zLdnJxXmWSsueCJLdq3A+Lq0wTxuQQ5cGIpSmzAp6iL6AGmse6bmru0NbsNd8syXwDU+xum7vuPQo6WYUux/xyQfR62e0B7sb+MVg7ar8hEoIKM4PiyT3f6wmzE6lbv5W2p/MBUg41L6bjCrmt62K39YJN4qLGIRBXgq1jB8fvECLtb0dvTHzKN9L+uktaRa8IqTgz4t7Qz+vKl+t2pPMxY534tOf3VxhGhOVmv2NkAwCTbbCMuTUl5LQnWdmk6aZOO0hkxhW7Wvf3qt1sQCNA2Ko67Je30Sruq1UTkXBDyeZu6rouqRIzu/h3hCQ9z6w2cOq5jsggyo4+meL2yMfd+uQKnIneMNYpnBIFPvWsi3SnNmyiFy7D0mZM1yZx5JyypC55P+0wXiAluL5tbUeR5dW4L4Wy6qLGqnJyOQxrZj1a160zmoFiwKgTVt45DKHyFlwCJm1X27ZD3aCtS9XcCKa9pHbEXSuhuKqhA3xttQNo566Waq32DctzKTbs4KV65iAShUZTdcNDLyIqL6UDtoytJukx8Q4awtQ/3y9cZxiIfzXV401PynG7k0NjSXNLVBOOfsRodhGdS+90OBECddZWqyLAK4XMQjI/9AG3mvBWxZOgMo/23dNhHCbWFS2ihJ6eqsiE+yircOri8L2gZqO9LbL90hiFnZ5hUEdagUiOkHryCX/w3UNl+Dp8z6KImUrCsVanspbSI58xvjG6m5M9Iht+7G8na9xPALiF1rj0dl2jl7XVyYksnnzxfBBcv9OF0O2kWrO1MwvCCGQG7ohpg2NJiNz8nilumrScJompdmq7JjPfOIWSs7qZiXxyo2at767KeJTyeJ1OGc2qYSim3fFYoOW5n45DaTM0u2XPzJXmtLwgbHfy0ikdN2scW9vGuq41/1x2OhF3O+HuowSlMIp8HCwVFLYQI1OZuV/GDZrjTinbrHHb8nm6S3KZXqLscS+nDYU2rl73PLKsKgdWmFt9PirdOPTUmFwmgu4N5sjeJKu5Ig7M4yZuGb4D2ZAV1qypjGs6c+7HzKpY0TyPA+hc7q64Oo2azufXdqXcYnQ0jFsD4Bg95uMaOdL7UXNqKEfEZR/yFnw/wEZt2lseFNqNbOcK3+GHVO1FaMmfuHOD+laHaiUhtKm1H2pTFvO4gfXdUKmeEZIZvytv0djs9PR2o+0B473Kw9nwYHSsu5d737swOWwViIVVK/hcgBnsQF8wydq2BHb3Ojs+T0KFSC2GqSiqe8FK3DFX6BiUG51FjOS21NgWv4KGWT6aRlaYsn/1IaMsRNUIzSMDywinROXVIPXl4d4FpMO0a/sYp8juWICZX/LwC7ZKYPfas310dWQwvxQnMGIRoaI6qETc0Rj4zVOg4r5dtQ5aeF1cBngzTcIV6YcluOVXRVmFXUaq/V2+CDYaJBsHI69wx/fR5dhROEoMoWES9HXCjwiB3VYaskVFVdaL83CJg0jhhtX8C2sVOUlOhx1cIe5GcEFhwHoC7jdXzOrqrckJGYwJRevKoKuoeUMLDAjZUWKD4qiRMlUykNoAt3JS9eo6jpyqyM+4BrUD09DYFQBZ7vJloFZTx/ouAmbu3ArUO2vbqoZgoi5oZAexkSzvNlgDbTY6hDHn9nJBTzzR99CNX7P5rel8LcSI1lVNzGAL7IRPFFWdo7Wvau6llJTLnkOOdwtaxky58Xa1b0+4GDnbI5pR2ua+XdMCf6UijttbeXpHR8xJUTHLm9xnQvaQs6Y7Bn5MIFgrXJY0f67Dc6GIgY31MXslIviaDmqo61VvngOMAf2qjx6js31LcGvpkU0l3uB7Eu0SMoKHsdv1Lm+j1XLSZfMOWl69uylBfxp63KpRJ5bwDr0Z1s4CIdvZOCoYYaPBaRYi5KbeI5jOsCkTYfH+QiVBuBsVNDSyC+y4WC5EhyVoQvH45usMj+S3y8YhkKwOyGNlXk9SDavHPVK4xqRelghdQ+OJV/ZhouVXBLn0/AorxIrm9iLn5GeayPj0EsmbdITKlSq1UpnRqi7ZVqMVut8fTqrp0zJSt6TB6KVdlqHD7pLt1tWFFVK6t5TEgsrRbyLZgYasOMHE6EtYmW+U1BpQPBgaGD2p6npz5Oi4FmkqrXzkOLX3cLsHHfSRuPV8gN+lA7QbiVtzaCeINKlc5i539bpaAqtLBK9L07hBwGRfkZko3fZohGs3W6wve6VRLu7lhFwuhA/teNVmyc5kVmF7Kbq87yPxorrI9W7dI1gAQ5ZVHDnCi4rgempoImnGtZtdL0tRV85NTw3qBWlO5zMn77eB490bLfZg7QSmHMX1y1YmhOpUua6RH+22xbU9CI0zdgmG5XjzRpky2eJ48pdVd5ZtSs2vG1RyBE9xpn0EB9JW81MLEaMiuyBoA5Kqt4/rkQzsid05S4lANtLKdE6kPBx8mLwj45rVVqQhbVbVysb9Zdyf1ieJvbfWKGakO2I53ZBk7WFra8UvV5sLGYasoHLj9cwCEM/0FT41lpYWYemFrCKhGb1WaWu9G0yOOGy42meHqm4Lc9PLQe3H++upC1p+qfOnq0aeSohDslV371f1YOVGbzQTbnDBhaZyXcilhvb5jScQ8vLgHE9UvfFypS8h+aCS+DriO1BTYvIiD6fkqqtdEW4Dbg2DIYJW1NWFKn0/xH3aUHzF5y9clbqWX58DDRWFCEoZa6AL1NX6rhlNl6vUivMbVlm7HjWZRNJe4UgWBmXYJA1hDJzCNeXWkJFLwZcclXAIk9DkGdruRJ8PrjIsa2htgGaYxrzwFKLGGGrb7gxKgemYDto1PdyPoquvuUOInBOXwuVsqw8ienf1QVaE0DK7GpVMtYF2habn6aXhbPWu3S/ZWs6RuErz9a1ERG/0Crq4k0f8RK6iAMfTJlqWorFiXIu8cAqRSKKQttdw01liCDLLJeGMCNbnRLeWPqU0hletDQ6kWuVjK+42nVf+Sa9U2ht2anqWwrM8iGXmmoPvkWkPmfBuXXrwZk0YurxMcghZV1tys4pCecDvUzvCFeTwp+3+zvS5P1H70Ngdxh2oIasB0pcXTOGDeJiUCMV0tLRERzkUDurqkKn4ZwI0V5mHxB5hHvdXAqpxtypsyOtrkLBczdn+Skc5LzS43CDH9eGc6mytCUHvN0YVknvS26lX7Xxb2vKh7TfhhGa+yyUhJhpZQm1kyj4JWbnsvJQDWBxaF2Zzq9XR3vA5fTwvsYShijOouvRyc8fDiKNKs99dyC513RY3Jp8asbsai9FlFbCNzJ4930d7drNbCRqCJgTXG9Z4qXfEOHYb0Jhs1FBJPZkMxLxuAAaHq0jFnWwcg3VvQITXcn7oDDsx3hgOuxpdFFtqVwoRFG7ll31v1CUYG1yk59F7iDXxklzikq+hu4krSPPOub2DHIVhe+3vl97sMaTxPQkem9sJkiKkAYarNOUupDgMn4R1njWwdV0WNFqikBhU5I7Ej7cxW+f7mGeoLXK4QY3MsOaR0lRf49JbkMqFhq37OrmvHQLAjJgoSiUvrSPj6kFqJiURcLfjqpIZtNvj2WZaDvuEs4rNtSuR8RSCjorcByJ3DFeb8U4WuhigRb+bmpUhVy4GWf3F2oYTN0pju+ork7KkAOZrqYx98uIi97GHQExhskKtwLQDUngjqRqbY5O+NMcGhHTiDVdqayvaBaYTqw9Mrws1TF1Tw/VEYnFMUxT115cPL/NjsLdHsP/GS1/zc53/Z4+Qnk+C3t/qeDxpDBz/04PXp39HqL99eGm8BIj0fFTWZn309sjp7x6UffzXD/vm/dPzXar3h8vP59WdE83vGb8khd+3XTN9acvs8V4H2OH27fxmYju/vOqB7+8fl35VBBzHSRN86covTdCBo5f5tcH5bY3AT5zu/TR6e3IIdk7AQYnXflkR+JegqWY9394KAOqtXuHX1csf/wdg7VpfFy4AAA== -->
