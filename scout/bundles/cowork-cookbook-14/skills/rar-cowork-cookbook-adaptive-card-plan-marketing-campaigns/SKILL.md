---
name: "rar-cowork-cookbook-adaptive-card-plan-marketing-campaigns"
description: "Generates a read-only Adaptive Card JSON file summarizing marketing campaign planning status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_marketing_campaigns", "rar_sha256": "9650100e2c5c55dce073f7a8fe67aebef7c5422051829c1ebdeff15951375625", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
