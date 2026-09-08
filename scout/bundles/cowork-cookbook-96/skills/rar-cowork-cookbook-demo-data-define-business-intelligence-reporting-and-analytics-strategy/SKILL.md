---
name: "rar-cowork-cookbook-demo-data-define-business-intelligence-reporting-and-analytics-strategy"
description: "Generates 25 realistic demo records for business intelligence, reporting, and analytics strategy in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each primary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_business_intelligence_reporting_and_analytics_strategy", "rar_sha256": "37540336cec2c6b0428484a709d98e933294095052c8c87e25cc32febc03ff1e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_business_intelligence_reporting_and_analytics_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py` and in the RCI capsule.

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

Define business intelligence, reporting, and analytics strategy Demo Data Generator — Generates 25 realistic demo records for business intelligence, reporting, and analytics strategy in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each primary

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-business-intelligence-reporting-and-analytics-strategy
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
      "description": "Sandbox D365 legal entity to create records in (default USMF).",
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
      "description": "Excel staging workbook filename, e.g. demo-data-define-business-intelligence-reporting-and-analytics-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py` and embedded as the fenced Python below (sha256 37540336cec2c6b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py` first:

```bash
python3 demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py   # or on stdin
python3 demo_data_define_business_intelligence_reporting_and_analytics_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business intelligence, reporting, and analytics strategy Demo Data Generator — Generates 25 realistic demo records for business intelligence, reporting, and analytics strategy in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each primary

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-business-intelligence-reporting-and-analytics-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_business_intelligence_reporting_and_analytics_strategy',
    "version": '3.0.3',
    "display_name": 'Define business intelligence, reporting, and analytics strategy Demo Data Generator',
    "description": 'Generates 25 realistic demo records for business intelligence, reporting, and analytics strategy in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each primary',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-business-intelligence-reporting-and-analytics-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-business-intelligence-reporting-and-analytics-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b623647ffc3b2256',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-business-intelligence-reporting-and-analytics-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-define-business-intelligence-reporting-and-analytics-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging workbook filename, e.g. demo-data-define-business-intelligence-reporting-and-analytics-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define business intelligence, reporting, and analytics strategy data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define business intelligence, reporting, and analytics strategy. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-business-intelligence-reporting-and-analytics-strategy-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define business intelligence, reporting, and analytics strategy records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates 25 realistic demo records for business intelligence, reporting, and analytics strategy in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each primary', 'example_request': 'Generate 25 demo BI and reporting strategy records in the USMF sandbox, stage them in Excel, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging workbook filename, e.g. demo-data-define-business-intelligence-reporting-and-analytics-strategy-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need seeded demo/training/pilot data for BI, reporting and analytics strategy in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineBusinessIntelligenceReportingAndAnalyticsStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineBusinessIntelligenceReportingAndAnalyticsStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging workbook filename, e.g. demo-data-define-business-intelligence-reporting-and-analytics-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineBusinessIntelligenceReportingAndAnalyticsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
