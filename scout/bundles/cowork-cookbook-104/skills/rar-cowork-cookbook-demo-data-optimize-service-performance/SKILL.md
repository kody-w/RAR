---
name: "rar-cowork-cookbook-demo-data-optimize-service-performance"
description: "Generates 25 realistic demo records for optimize service performance in a sandbox Dynamics 365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's prima"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_optimize_service_performance", "rar_sha256": "bf8b3da18be08cb33edd36829488237e2417e24246b2dda4873b6a82d33cbea1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/91617LbSLblr3DOfaiqC0lwBEjqxo0YkgBoAcIbljpU8N571PS/T4LkkVTd1T3dE/M0RyEdEsjcfq+1U8Dvb2bbBHn19vlNcs1scTCTJAzcamFmzmKf93kVg195bIG/CzvPmiq02iav6rcPb45b21VYNGGege0HN3Mrs3HrBUYsKtdMwroJ7YXjpjn4aueVUy+8vFrkYEMaTu6idqsutN1F4Vbgempm4HOYLcxFDXRb+bCgxsxMQ7te4CSxSFzfTBZu1oTNuPjZcT2zTZqFIrHMLx8WdWP6QHETuOlThAMMcRb0YLvJYvZhNv/DwgZmNT+so4DgDw9PK7dpq6xeuKYdLDK3f1n8U70oqjA1gbPuYKZF4tZvn3/9y4e3EHx++/z7m52YNbj0RgEvKbMxby/npKdv/HfXgIjEzHywthhBwDPw/eU4uATceQ/Dz7WbeB8W//mfcW9Wfv3L5y/Z4vXz5W3+I7bZ7MCiyc16dtI2C9MKExCWT4tt0ptj/c0bEEqQr8z/9Nz5XVJeLP57vvfzU8kn321+/vKWF3MCQTa/vP2yAJn68la18+dPs5Ti518+JXnvVj//8l1O3VqRazezMGD1p6+v7y+xYOH3paG3+Crx9P6lC8Q3LFwg/Af/5p+n6S9xr5B8fS7+OS8+LP5c8uzPfwN7nxVpAbl/LhbEAOx8+xTlYfbzS0eVd242Z+jnX/6RWDtw7Xiu539J7q9PwYFrOiBar5CAIp1T8JcF9PLtm8x/rLYABfPveAKWv6v7Fqh/JPuR2b8RnYQZaI73XP6puD/bAP334td/6Ns/2/Bh4X0BnZOEHag7K3E/L35/lMivPznfL/70l78C0f9HMVLeVvZDwlfQbqHn1s3Xr7/+VD8u//SXX39qC1DFrpl+bavkz2T+WVwfev4Qwdeqn/+4F+hXsjjL+2zxrYcWv+fF/6j++mmhAiR0vl+vPy9+7MT5B1rMTrwrfYbgh26sga0/xPGXt78C/MmAN639uA3w4z/+Y8GGdpXXudcsJDtvmwVIMIAidzZeDsJ6ET5gDzgA4lqHILCvdaD+5wzPFufe4rf/aT8w/6P9wnx4xu+vAE7Nr+/A/fUF3F9/AO7fPi1kID2vQj/MAE6LW57/kgFQzppZc1G58yaAVtbYuB/Bro/zhxmDf/vXFHx9yPpUjL898Dp8YqC4P834V7eJ+2n2VAvc7OWXDcjMHVy7BWqS3AY2eSGA7w8gAnWedAA/56jUcZgkCycECANIbXxyQZt9noX99ttvllkHX7InYOOLJ9vVMFjwzZzFx4/AOS8J/aD5krl2kC9++v2vPy3+1+Kf7XoIn3XwgD5eeQEWnqUbtwB91qZgGUgZSDIAkUdefv/rK8RADODZBchi6IVPLpv7IXad93hLx+1HjCAXlguCB2KcFnnVABZYhM2nxclbfLMXKJ1vzTwR5HUDqLpwM8fN7BFINYE73yKZ5Q1g5SasvfHDoq3dh9bfrMp8mJiChjeb3xbsngeslCfgn9nMxyKwOc9CEP5v1fC8DoRUgF137yI+Lbi5MheFWZlFUJkvHZ75zAtgo/ftQLg5U/SXbCZhdw7Vo02e4fHnKWQeOx4p/TjnHIwtKaghp37X7b8mFWchPzi0+pLVrxYwK/dB/cCUceG3oTPX3n+9SqoO8jZxHvEDls6SXllwXll51ODtn80385ywmAeFxWtcmmm2xRB0ufj/eX6a47I9HET6sJVpakFzsmg88zWPlHNen1PobNvs46M3vw827+D1juFfsiQExVeN//Vc+cjya80TF9sKmC9uxYd8UGIgX7PcRwfMFV1Vc+8Au97JArixeCAjKAIAF6Cd5ip+Vzjffbc0AJgwf/8+OLycnQMBqnxRtFYCEue5rmOZdgysquYufqUZtIM7d3QfhCBUP3o1JwdUHZC/AEaEoC8BoXz6BuDPu++m/2Hjcz6atzxmxxY0cfUQAOxwZwPnFPVhA7DMbJ4TPPDz80MIcCMtmtl3C7QR8PR50a3csg3rsJkh8xlXtwCg/XH+/fR0vuoOBegcECzQH0ULovvoqBlsUjD9ABtA/YIGS8PsWc2vIDwEmukMDwB+X8XzlPi4/HLIfbThTGPvG2dH5j3zZLDwgOngyvgjish/ViZAXjqveOj920r7pm2WPSNpDdAQaHy/+xwhPj2ngOeYsXiX+/nvjkg//3unqAevK38sgM+LoGmK+jMMP7n4nYo/ARyDn7bWD1r+OLPmx3c8+PjCg48/4MEfpD8d/7z49yz8g4hXh3xeoJ+QT8h86/qqsNcPCMj+4874uJzvfslE9zvWAvV5CkpsTt8I5oBvxPi+BLCjXwGUAoufRFnP/NoDSn8wA8jFl+zHkp9bDhBP5s8lWuc/QMFjQgDl/0zdNwIDt7IG6Hbm2dJ3P81Hstn82n37nLVJ8uEN4KX7r57mZqZK5+Ku54MgaCMQ9yZ0H98eWDE088c/HpJvjw9m8gkwAcClpP6xAF/8MvPrD33y9BR4aAMNHx7IXM98CDydlc89Ztbxgxtmj5qxmF14HvzmUfEB/F+fwP/3BknvXPF3HAHgrwdtMh80/4Yv/muRtmBcmGNqPQDEeU6if6r+2xj797o1MDXM0p3880ygH15YBH6Dowdgm/dTBHD6da6bNbhZC47Mv84nmDkLjy3zB7AH/Pq26dv/T1ju21/+xK5nWL8CYs/+JE9cm1qg5gBO/4F/gbHv1fo9Jhjxy596XoPSMqsw/3vpM0i93/0hx4Dy5sHjwwL0pbv46Z8R/U9/qvGdqb8+6/hv1T7pfOb6GaAfnTIv/LBwP/mfFv8aonzEEIz8iBAfseWnIamHP7HjEVxAHoCC5zx9L4Dvacgfp8rZZJC25vmfIL+/gW4yZwNe/fQ6loDlAGs/1vMIBgPcAQrB9ydCgHv/lweWl5Q6MMGoDMRY3trCHRNdWy6yti0cdx0HJ9fYZrleY/jKxZbo/A+2JC3McczleoVbpLnGHBy3LddEgbwn2nydp81wtozYrDxks8G8JYohDqgWbOk4a3JN2sQKQ8yNZRIWsTGt71vjMHNe7j7dm2P57ew0h+Xl9e9vFrkEK4/L+rR9/uxhCLUgbGWNnA7ryHq4GwdeCQsR0wbZOSvdIJkY3Yv5tdpPuETYgnk8xbaAivqZqE3W3HW54NknSNLhbNr2RLGPLEl2N7lCbyVXZlOZz9ZRqx/k9sbi4ATp0BhUsUpg912O7C/yzaw4Dib31tIbMaSMOlxixk1yym6wfOSHZgWvUW+UAj1CtJssReQtjLYnEel29i6NXcY/0+Ixt9aSL3ZhtD4zY3pc68O1O+CKuj9VODxprDiubGd/TlVlVQt9sm/hMO4G3MkqhrwNF7qAI0O/Rk5f0iFt7G39PCDUYRlW3JW4F25Ea1vHLyv9eDxRvaZtETZJNJehr2SvGPE6LqbVzghH8tbwg7924Wzc3OSkhu1sgK7x5HXycZoGL+SYeG8k2u4MqdpKyqgwOt5Nq9ztdxmcXS+Xe0ab67ws+7y3dxhNe1ec3eDyRt6qonhle4Eq/b3t8558Jx0Wz9e+GhpWcieWqnHus9gzAgrajpeLeqWLWlCnS3eKJJEVC/t0vN/VvBOxNZcNLYxxVHel193dPknqUCcnYeo7pjogXHIZM6rYDZ6/F8W9mkLSObnEF/yAhtI2dCcoTo7DsdkqRkgXa32vuwa/d53Scw93wkJWuzGhU/N041WNEc+X482lAiOuFfPSGtVlsrfdOA2mGirY7cCayyNkJZZcFMKmOrTtkS1sWFVpUbCd6KpAd/lurvY6PjJtGsDn6OyzfVTZZe0nlFdMBMup6bUS1xK/ou5Ka1kXhtbka5MZ3VI7dF6EMdE1P5JlM153CE1uT3Yqh8e1uRqhYCmqxlDcHPdMUIW2y0tkzM1B8xtT2XUHWa/aUg2Pgn0WXQa7iMZk9Q0S5vz5IHTDLoEZwypl4C6xjZYSF1sDv2OhPFnuPTKkBJFnrg01HgZjfUhACVFTu7IOd+wsJ0k8pMiSyoIod1VSsEr3gmjnCxxBuxucy0vYl1eeL48w0yzTSmZhpoC5WGkonh0YzxWgdYB3g6sRMgSqxJbvK5jlY1T3iRuh5pGKBNcCbQzmkDRnwlgpgkgkZ51Bt8MdujUoFcp74zgyh23eYWs6W+/Ka+wvD02GyfdesXg0lQXRLAhvjxytM1rIB0O6X+JCivpLmA7OLtzhu9J0ttTRBxXQ8kV4upMXsmeaPoz3/TnqppMkQ2iMGbqZYld6Utv1LgvOHa5BqhPeD7w5SjsziQ1VGpF9cdf2xcCJcSNfrghny0Sjx64YKxq0ahnNvcs+cufEMQ/KSbNhyOiNSIqu55HepDFmxcKB8zuWz9zofBl8y2qY2DbYCCKMlm1Lge3z0FcFtt5mvHrbSs6mJByWz2FDijCR5WKHz5eyLy8N0UkTqCJpWZZhZZ0MPta39ztE2PWg+jBVcc5KGExkxW1iSJVhplcUU+J6yMAY45wV/o7iIOK6M8bWlDeTVsujJIXCcPKDZjcRaDtCt0y6kudtax6iACak7tJQ6WhD5DXE93s+b7x+iy7Zimi2zPFodweaEeVNqC7voYntTOR2Fg1bLrr19lTJe6vv2+2+4JFcjSRdFaUjs60oninVLLtrm4ztK2LQU+XAnfUI4ks4bo9pNoRQqGzTkrCpFo6iKNjhFSkCFJFprttqxEpJDnxeh1VjICuc6PG4C1eFAl81C7mml4AxbjBvRFMYgwy4O3jC25A2sZAvEZ+Vtmg8FA47lMurimxRMr1Me0v1S8U+GlnG9359yi1mqNcqybdBtB4ZJCiCQlaiRBrj070zSNTr+LuyJavxvFbEc7A60Nkxs2Xdz0cpNeTQo0rvFneaiirn64kh6L0ibOP7cCYKj+X7BNqsAt5wxOtBKZHteLYMWDITmrHIdlOK/NY+GYpARVarDY1jdGo5Fn7n40lF4Z2U34VMvt/7tiAEStZhmGyjeHLis68s23qQV7trsT4mWqh4uYeMsrNKjnmtCGNXxqATUWPLJ+2VavJln99RyuW7JIM2DdMdJ3hNtIweDVDbNQxWSDbBqdQ0ndaJNux8yjolcG/jV3hcxiepRbRc3QnB5Ya7GLVWBpSRLaI/25MtWOfbfVmT6GUf5xes0oNt5wVNcODKhFltG8mlD2VV0tudURwy5MJdt7a21IQMRnomsHws7o+cj3MiDx8jfUVmsrZBl1ObJwe0Nfa3qyndWGy1bhyxItLA4s21fINxbl8d61W7H11fjff7QVGUYSVz5uRukebSjCRzas+UFGcevzdoKTofO8jSq93QB6GuXypV0urbTtlOqxovSS6FY24XRtwu6DEG3oNDYrF0bmQnpbdtB0nj1kx06d7rnqkapMTh4iEv9VgkFGW5107oiBHrktkHSpQP4kTEfkOOW1aiEzbYVSfNLvHbEUZto4vlvbrzO42+x/1+p+oSY9hejtOq1Uu1uk4A5Mn+GktDendn9reIl9qKpSsGvQmoggPuP2tbuiwF9KR3qGRyB23lm2qwVbATkvvS6mJIOr2vsFNh0gXZF53mXfYC3+vIyJqnwK6549AQhk4gWHcaSrOKq9tewLowVi93bHnw+8NpysK2bAalTqHkuL+a9zRxw9ZDyF28OSiRsbOpjSMWWq2PchJuJOF2P2flzTSU4kLbGK0ZSC7RMmPkhws9ZJDC6RTDXY9G3p4EyEDM2pL4oQoRAbQ+LA3w5swOW2pi7o00pLzQtYkY0aq8uxxryDNCSnflcoyv7uVwILDKyjI/5a7k8XQAcZ26K0zlB8pzIp2Qtkh7rXE7E1vzdrjBbKZcz4F3PqXlKTPNcbtum6HImYPFcQLK0iDmsimf6Ijbt5EsjHSRmkpDIhptCpRWcmR2MU2vl6yOuvvXsmJsHnHSe787Dii5vFyc1d6XPc1jcDRcTno3eZjDVEvBpdOwKu0o9Xr7JnjKlT3l3o5eIRjtIonKHE7xhsOFkD40MXE7bK7LZizjHMmZ81qr8WJoQ0dytgdhu9ure3+kQNaMyNyuXQQKzbjJ96ui7WF8vZRzrpSWZptDjnIWKZmCZcySLry9AXTPZ35ctic7u0gUemoArJeFOraWtyKyHXO5b67K0RRigro2Wz84xZx0KW6FpCqqEuwJlWWrNc7B5fZC7Ruzq7BBGKaYHbSNde6qe3unT2qcrehoVTjFPr/cGX932xXTRUhWk5ZE9sXcQ/EA2faRufI8l5jxhRkmeIonok1cbJuQnV34V09L9ZqGaSY4XOsdupWME3/piUuWk4Gx9e/SWe+DhlCwUREYMKteSmKHHsIg91b52ggK5rhb88uNJGX+WbKHzlzbDLIryqNQx8b9qthWcHOmxOJOCspMRzq9lHgpBtmZ1EhpeQg2nOm2zBrJpoGEbj4eL13+vNxAKx1jwyXkuugNzMLDXTXY6oAl6lLr946AbkjbVgswV7PO/SJzSIfvBZW6rAVm2fIZ16sSRMJlRjSpzp+E1LxJO+ZaJyQm9cfVpVGudbpUXXJfcWrs5Bqk3QN9z2gYZBrbLRjCBmm1xWCrRKE1s+4lfGv1KqTZYXpm/LyDYx0q3fPAyvtKPxidY5Y2E6jZMh0diCo7mj6VfLnyY5EvmLLSPH7NeU5Pm9dbViGE162waOXhiVbAUDdqSehClymqfIyRbkTWKDEq65rn3MYjM+7C3kYSR9/klNbzF/6246j9OqKYaiWJQg6CpqkbfpCiiqu6WoMZFLfX+hQPTicjG6Xqp5A43PE8abKrJQMikw20L5cliKJplld1IjcarRNqFPN7BS6geC9TTgvFVMN7PFxvWKzixg16A6CEVXKrgaa7ZGLhOWxRUCIVKhpqDzXKoZSJRNKKaTzHOg8diw1iSpQlQWSDhmBnut0hnbFMmuVwylYtMqb0XtQOW2jAEn1E9cKYEB+uAstm+UurY5roJ75f8bdC02kPPzTsvYqUkaA9OhqE/CYvAzrdD9TBuyq7HnIlfB/qbip1J+Z2TWRB0fTbYXdpSMMjrPgSTpwwrdY0tSlDCcq2SVgV1/0Zt3ETvR4PpFfjFGeTecrEAdwTwgbXcLLn8i0aqFSsRGXNaUukRHtzO3KcdsGtcB3pZJpW4km+JPftCt8PxGHPTlfkclZH/xKaPO7lKJiHK6lLydDFIXRyh8u9WjLcSdtRhUR6+yTQD15Hw9K2YjwLt700kOHLWOS8oylBSOtld24lGJypiYE1mjMozW3sjg0sx0USXj2pHlYhj7bQXTRre5VCmT7ej+xgdnccxcWdm1OkbJsQOAO7LhWmgr7hVvtct8uto7DpchBQ7taeAkfsvBXkOEOMODkG8/Shv8PbCnRBv4tE8dAoIjij5Cw1mWPBTZLA7q/QFRVswKMg5b0IuXG4KTxzx8gBKmc46h/oNqPai5CvyOaWF37usOAUnUcpwzPsxdt4ubuJEF0XpkE/2ApqjMccr4rch8qdx5HKmHWuNaTa0KFrq0Qa3zl0Trtqpl3urjjHbHEDIVATvkabtruV5rCxs8n1oqybQBv2uJFqLUSuV4FZ+LUsug1S4gR/FQUSo9F7vyaWgFwScjp1qHtwdZ3vcueiVzXDtYiHBpsQv2E6kfRrjJcn5Wog0K4isyxw1NxNWfbQ2cctFNzom81hyM1i1vhN9++hPJWgH2JeGrDUr2EJk2vNtkoeHweICyfr6jBre31NUDS1smo9ECLkUaKLIZWumNidA4aDIQU6HuOGYW5LxDdDRKGA5TCGrmCfXwrgHCLuyNaBh+MaEC6oyzuOhWMN64OtOQkvCAJ6PthXAdG44CCswLAtMkeL6ptJum5LT85cLzxyW64QENUWYCoYt8SpE4fszByhejzkGxMxL2o6dXelYs7jRrcE1/EvYtAVAbrPscJL8cPl1o/1UDTLnqEqOCPlUMt074YzSy9mD+Cgn6P4KnM4x7lphiRCMkE5477Y4AZ1iHt+FIuOLUWF6lUCZiHSraetowmOa05VFeQYd8vyxhK7VsxhKSyIs6dGm/IQDMPp3NJC7NNF7Nt8hzMH3UmL9d009kfe0tpaVOO+ke4n1cXMxiTxBLIIAZXDaBujnXFAj5E2dSKJj5dxiuIT7ZVOPN1HAjrbhB4FlI6dmRIc7i/MKSOWLIU4uAiQ2CR2p4PLKn3XdkeaM/VDmpLxKjr1jiIUkU9QllDagsCb4GyuBRUtdxGWnY9MfoO7LXa/sdV5wBOaKJUYhlUKXUO3UCTwrNyvtepuSGx6bC6pk1rLs2ySEqNxKMvf7pG+1I4uJ+opjhs5TWirvWm7HrRc7yFfiePadtQgIV3CnlgVzW+Kre3JVIyqqdUwZaNqZecKGIXt3JU4iDi+N1dEV+V7TCY3xhpFiMtePxwSAtlBcc7jOUL2bV6ueeJsYl44RklZpd0EuYcaTYKJ8qM0Y0nE0FlWjaFeri3zSrmhqaw6DD3Hh+v1VgbpbUrag17BNauzlMDIGnLQ69RSI21LETnsRIdQp9I6yLlrRCnendlI+ZlQHOdyidUqpXn2hoMTZo51kdt4erIEuqbVEnBiDdv7wXAglOI3pIPddC8XE52eds7KgWXiyLI2MohrTnWdywQH6vXSbOCSTK1ohVQmRI1QHhGA969w33ZgAkF2E6mQ+Prs9TdCMU8r3itOGsRrK2d9I9Eyw+mSY1GS8KE84aMs4Mla15wuY3dwunXv5qrxjqXADelpr57SE1SflQrr8Rxb3oM9K2XYlEPEhl0WcLcatnvUV++gQ9LhdmkOG3514nqvXeaXXB5204WJogrODSmYgqkQzzwbuStlXI038c6u1rlPLRVoMhnEg8zJcM7dqYqMAo/ufio1Cup7h13BE/kKu3SNuWmWTrtlBFzUvDCKdydZmE6roForJxfbYTzeE7RZuHCm8NGw2UH76UbQGGrFKqoVSWVi7SSvRK67CkoJq9K5pmJMYS6bzuKaC7teJc1dwyx7Um7Z5tIwZ3NXdo4wccdNq/WppRwwyZgOndJEu8kmZa6ZEp6HjkaTurVjxrVs3zGPW3v25dTXqTiwHonbDYEvCR/QeUIOJnfxzsst2ch9vFM83C2zZord7C67KLeP12dozd4cY9flyNpN9UYjcGvvoGTrO0nUZjzi+qxxugOquQgu7IZbbFpL64rdsMotpHuxHq5FZ/u7DN2ONbtcrpoVPHapO0VwDiblfGgNtDyPuBxnWJMiHSqnUItjROLd6pbbF9SO8FC2Qame6XT15KAblKpNOHco6FZK8NXJTeYqcWD8j266i5YsTAQOdE2HvDNgdh9rnusTltJBzcCvqVYadmbq2+d4iC29lQhEBn1aj+4S1Wi2jb3t6erZ4riVqiN32vHWGYKQvU/f8F0N46NTYGtk6QgCMvGFHPqkfdPJ231ZTpVTYVtQAUXN1KxjwCGCUGgU6FBtVKTTnipiFRL3japk3t0Zow5BV0Vq3+0ORhivI0NwsNK3K7M2O6F2BxZfbS+my98mzakTRqhVEbcEDcUyLBxGElqynogdp+NxpU2ZXpuJce12WT2dW7VdopVj1Mt+NUgwaNPqqEBFcBt2PYwh0W6TMBmmt2Ra4o0OWja3cGspBEi2ptP0pNBb9IKuK46lVYEWeU5l4p2bqbgIPIXCqTZXalKdQveWc5Au05bkxExZkDcKErxkS6fJkUCJMYAvIa9Xm8iJsT7SNy28YtzqKgj4ME2rSL66ZOLKYY7T18I44XpLeDtLOk687+Mdoe51W0JO5LYMNhPhJejUwdFqtWT4LX46Ru0VITa4wGDIKAXGtZJlyN3oAa8tlxHVUwyvmjKhXyP/Du+m1C5PK0Pot9u3D2/z47TX4+N/8422+fnP/7PHUM8nRu9vpjyek7qm8/mh6/O/a9hfPrxVdgjMej52q5PWfz2e+puHbh//tYeHs4zx+cLY+wPy53P3xvTnF6vfwsxp66Yav9Z58nhHBeyw2np+DbOe39S1we8fH/p+c2iW/PKkAVeer4++ze9Jzm+fuE5oNu7rq/96Ggl2v96P+oqTxFe3KmZ/X284ADfxT8gn/O2v/xs23Cx9IS8AAA== -->
