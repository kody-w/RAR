---
name: "rar-cowork-cookbook-adaptive-card-plan-marketing-campaigns"
description: "Generates a read-only Adaptive Card JSON file summarizing marketing campaign planning status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_marketing_campaigns", "rar_sha256": "9650100e2c5c55dce073f7a8fe67aebef7c5422051829c1ebdeff15951375625", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_marketing_campaigns`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_marketing_campaigns_agent.py` and in the RCI capsule.

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

Plan marketing campaigns Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing marketing campaign planning status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-marketing-campaigns
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-marketing-campaigns-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_marketing_campaigns_agent.py` and embedded as the fenced Python below (sha256 9650100e2c5c55dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_marketing_campaigns_agent.py` first:

```bash
python3 adaptive_card_plan_marketing_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_marketing_campaigns_agent.py   # or on stdin
python3 adaptive_card_plan_marketing_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan marketing campaigns Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing marketing campaign planning status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-marketing-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_marketing_campaigns',
    "version": '3.0.2',
    "display_name": 'Plan marketing campaigns Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing marketing campaign planning status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-plan-marketing-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-marketing-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eb2118391ec618f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-marketing-campaigns'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-plan-marketing-campaigns', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_button_count': 'How many action buttons to include (2-3).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-marketing-campaigns-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical plan marketing campaigns status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-plan-marketing-campaigns-2026-05-24-card.json' that visualizes the current state of plan marketing campaigns. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current plan marketing campaigns KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing marketing campaign planning status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing marketing campaign planning status from D365 USMF.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-marketing-campaigns-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'How many action buttons to include (2-3).', 'name': 'action_button_count'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of marketing campaign planning status to embed in Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardPlanMarketingCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanMarketingCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_button_count': {'description': 'How many action buttons to include (2-3).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-marketing-campaigns-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardPlanMarketingCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
