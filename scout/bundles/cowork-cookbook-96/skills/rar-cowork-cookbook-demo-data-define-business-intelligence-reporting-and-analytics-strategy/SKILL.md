---
name: "rar-cowork-cookbook-demo-data-define-business-intelligence-reporting-and-analytics-strategy"
description: "Generates 25 realistic demo records for business intelligence, reporting, and analytics strategy in a sandbox D365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and listing each primary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_business_intelligence_reporting_and_analytics_strategy", "rar_sha256": "37540336cec2c6b0428484a709d98e933294095052c8c87e25cc32febc03ff1e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
