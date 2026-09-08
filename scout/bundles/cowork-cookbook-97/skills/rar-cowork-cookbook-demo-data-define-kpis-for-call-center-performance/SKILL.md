---
name: "rar-cowork-cookbook-demo-data-define-kpis-for-call-center-performance"
description: "Generates 25 realistic call-center-KPI demo records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_kpis_for_call_center_performance", "rar_sha256": "60baf40072a42b9f51d8c23b408a727fa783eb705aa89695e4ae4640fae32d56", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
