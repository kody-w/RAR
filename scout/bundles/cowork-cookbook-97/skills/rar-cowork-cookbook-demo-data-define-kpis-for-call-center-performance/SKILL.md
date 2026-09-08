---
name: "rar-cowork-cookbook-demo-data-define-kpis-for-call-center-performance"
description: "Generates 25 realistic call-center-KPI demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_kpis_for_call_center_performance", "rar_sha256": "60baf40072a42b9f51d8c23b408a727fa783eb705aa89695e4ae4640fae32d56", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_kpis_for_call_center_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_kpis_for_call_center_performance_agent.py` and in the RCI capsule.

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

Define KPIs for call center performance Demo Data Generator — Generates 25 realistic call-center-KPI demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-kpis-for-call-center-performance
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, defaults to demo-data-define-kpis-for-call-center-performance-<date>.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_kpis_for_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 60baf40072a42b9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_kpis_for_call_center_performance_agent.py` first:

```bash
python3 demo_data_define_kpis_for_call_center_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_kpis_for_call_center_performance_agent.py   # or on stdin
python3 demo_data_define_kpis_for_call_center_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define KPIs for call center performance Demo Data Generator — Generates 25 realistic call-center-KPI demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-kpis-for-call-center-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_kpis_for_call_center_performance',
    "version": '3.0.3',
    "display_name": 'Define KPIs for call center performance Demo Data Generator',
    "description": "Generates 25 realistic call-center-KPI demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-kpis-for-call-center-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-kpis-for-call-center-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7004ee4f57d994ca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-kpis-for-call-center-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-define-kpis-for-call-center-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, defaults to demo-data-define-kpis-for-call-center-performance-<date>.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define KPIs for call center performance data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define KPIs for call center performance. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-kpis-for-call-center-performance-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define KPIs for call center performance records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic call-center-KPI demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.", 'example_request': 'Generate 25 demo call center KPI records in USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, defaults to demo-data-define-kpis-for-call-center-performance-<date>.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need sample call center performance KPI data created in a D365 F&SCM sandbox legal entity for training or pilot demos. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineKpisForCallCenterPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineKpisForCallCenterPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, defaults to demo-data-define-kpis-for-call-center-performance-<date>.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineKpisForCallCenterPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
