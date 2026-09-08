---
name: "rar-cowork-cookbook-adaptive-card-define-business-intelligence-reporting-and-analytics-strategy"
description: "Generates a read-only Adaptive Card JSON file summarizing BI, reporting, and analytics strategy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy", "rar_sha256": "1e5015dc3b2fe99ad9895df68537240e143705f6c63456b3a19f18271a5d9f77", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py` and in the RCI capsule.

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

Define business intelligence, reporting, and analytics strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing BI, reporting, and analytics strategy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy
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
    "action_button_count": {
      "description": "How many action buttons to include (2-3).",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date/timestamp shown in the card header.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-...-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py` and embedded as the fenced Python below (sha256 1e5015dc3b2fe99a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py` first:

```bash
python3 adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py   # or on stdin
python3 adaptive_card_define_business_intelligence_reporting_and_analytics_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business intelligence, reporting, and analytics strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing BI, reporting, and analytics strategy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy',
    "version": '3.0.2',
    "display_name": 'Define business intelligence, reporting, and analytics strategy Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing BI, reporting, and analytics strategy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-define-business-intelligence-reporting-and-analytics-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '85a5d958f06d593d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-business-intelligence-reporting-and-analytics-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-define-business-intelligence-reporting-and-analytics-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_button_count': 'How many action buttons to include (2-3).', 'as_of_date': 'Date/timestamp shown in the card header.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-...-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define business intelligence, reporting, and analytics strategy status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-business-intelligence-reporting-and-analytics-strategy-2026-05-24-card.json' that visualizes the current state of define business intelligence, reporting, and analytics strategy. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current define business intelligence, reporting, and analytics strategy KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing BI, reporting, and analytics strategy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing our BI and analytics strategy status from D365 USMF.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-...-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'How many action buttons to include (2-3).', 'name': 'action_button_count'}, {'description': 'Date/timestamp shown in the card header.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of BI/reporting/analytics strategy status from D365 ERP for Teams, Outlook, or dashboards.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineBusinessIntelligenceReportingAndAnalyticsStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineBusinessIntelligenceReportingAndAnalyticsStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_button_count': {'description': 'How many action buttons to include (2-3).', 'type': 'string'}, 'as_of_date': {'description': 'Date/timestamp shown in the card header.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-...-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineBusinessIntelligenceReportingAndAnalyticsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
