---
name: "rar-cowork-cookbook-demo-data-monitor-product-performance"
description: "Generates 25 realistic demo records for monitor product performance in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_product_performance", "rar_sha256": "7dee6e1ae0ca5c5d77e97b6fe53634a4b1a4a5be0620842a97448a826273c04b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_product_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_product_performance_agent.py` and in the RCI capsule.

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

Monitor product performance Demo Data Generator — Generates 25 realistic demo records for monitor product performance in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-product-performance
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
      "description": "Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.",
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
      "description": "Number of demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-monitor-product-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_product_performance_agent.py` and embedded as the fenced Python below (sha256 7dee6e1ae0ca5c5d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_product_performance_agent.py` first:

```bash
python3 demo_data_monitor_product_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_product_performance_agent.py   # or on stdin
python3 demo_data_monitor_product_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor product performance Demo Data Generator — Generates 25 realistic demo records for monitor product performance in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-product-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_product_performance',
    "version": '3.0.3',
    "display_name": 'Monitor product performance Demo Data Generator',
    "description": "Generates 25 realistic demo records for monitor product performance in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-monitor-product-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-product-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '868429d400c8c136',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/monitor-product-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-monitor-product-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-monitor-product-performance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic monitor product performance data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for monitor product performance. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-monitor-product-performance-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic monitor product performance records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for monitor product performance in a Dynamics 365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo monitor product performance records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-monitor-product-performance-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for monitor product performance in a D365 sandbox tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMonitorProductPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorProductPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-monitor-product-performance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataMonitorProductPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
