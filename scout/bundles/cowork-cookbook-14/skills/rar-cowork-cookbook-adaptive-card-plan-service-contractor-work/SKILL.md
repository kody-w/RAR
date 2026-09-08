---
name: "rar-cowork-cookbook-adaptive-card-plan-service-contractor-work"
description: "Generates a read-only Adaptive Card JSON file summarizing plan service contractor work status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_service_contractor_work", "rar_sha256": "5c326fb326afa2e0039a4e0042511cc215680c6e206d5352403c9cbdb0d78356", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_service_contractor_work`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_service_contractor_work_agent.py` and in the RCI capsule.

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

Plan service contractor work Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing plan service contractor work status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-service-contractor-work
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
    "action_buttons": {
      "description": "The 2-3 action buttons to place on the card.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-service-contractor-work-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date the status snapshot represents, used in the card timestamp and filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_service_contractor_work_agent.py` and embedded as the fenced Python below (sha256 5c326fb326afa2e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_service_contractor_work_agent.py` first:

```bash
python3 adaptive_card_plan_service_contractor_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_service_contractor_work_agent.py   # or on stdin
python3 adaptive_card_plan_service_contractor_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service contractor work Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing plan service contractor work status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-service-contractor-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_service_contractor_work',
    "version": '3.0.2',
    "display_name": 'Plan service contractor work Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing plan service contractor work status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-plan-service-contractor-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-service-contractor-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '168a6809b08c2b28',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-contractor-work'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-plan-service-contractor-work', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-service-contractor-work-2026-05-24-card.json.', 'snapshot_date': 'Date the status snapshot represents, used in the card timestamp and filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical plan service contractor work status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-plan-service-contractor-work-2026-05-24-card.json' that visualizes the current state of plan service contractor work. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current plan service contractor work KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing plan service contractor work status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing plan service contractor work status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-service-contractor-work-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date the status snapshot represents, used in the card timestamp and filename.', 'name': 'snapshot_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of plan service contractor work status for Teams, Outlook, or a dashboard, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardPlanServiceContractorWork(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanServiceContractorWork'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-plan-service-contractor-work-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date the status snapshot represents, used in the card timestamp and filename.', 'type': 'string'}},
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
    print(AdaptiveCardPlanServiceContractorWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
