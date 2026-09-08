---
name: "rar-cowork-cookbook-adaptive-card-plan-service-contractor-work"
description: "Generates a read-only Adaptive Card JSON file summarizing plan service contractor work status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_service_contractor_work", "rar_sha256": "5c326fb326afa2e0039a4e0042511cc215680c6e206d5352403c9cbdb0d78356", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
