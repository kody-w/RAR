---
name: "rar-cowork-cookbook-adaptive-card-define-business-intelligence-reporting-and-analytics-strategy"
description: "Generates a read-only Adaptive Card JSON file summarizing BI, reporting, and analytics strategy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_business_intelligence_reporting_and_analytics_strategy", "rar_sha256": "1e5015dc3b2fe99ad9895df68537240e143705f6c63456b3a19f18271a5d9f77", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
