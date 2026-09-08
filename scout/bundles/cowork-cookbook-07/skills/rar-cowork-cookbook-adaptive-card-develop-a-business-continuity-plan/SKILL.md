---
name: "rar-cowork-cookbook-adaptive-card-develop-a-business-continuity-plan"
description: "Generates a read-only Adaptive Card JSON file summarizing business continuity plan status from Dynamics 365 ERP data for a legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan", "rar_sha256": "e91892196c2931b9ab47e083e98715257a06590e352e5603c228537363143349", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_a_business_continuity_plan_agent.py` and in the RCI capsule.

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

Develop a business continuity plan Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing business continuity plan status from Dynamics 365 ERP data for a legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-a-business-continuity-plan
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
      "description": "The 2-3 action buttons to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date used for the card timestamp and file naming.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-a-business-continuity-plan-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 e91892196c2931b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_a_business_continuity_plan_agent.py` first:

```bash
python3 adaptive_card_develop_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_a_business_continuity_plan_agent.py   # or on stdin
python3 adaptive_card_develop_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop a business continuity plan Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing business continuity plan status from Dynamics 365 ERP data for a legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan',
    "version": '3.0.2',
    "display_name": 'Develop a business continuity plan Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing business continuity plan status from Dynamics 365 ERP data for a legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-develop-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fe0bad3fa820d1db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/develop-a-business-continuity-plan'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-develop-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Date used for the card timestamp and file naming.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-a-business-continuity-plan-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop a business continuity plan status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-a-business-continuity-plan-2026-05-24-card.json' that visualizes the current state of develop a business continuity plan. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop a business continuity plan KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing business continuity plan status from Dynamics 365 ERP data for a legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON showing our business continuity plan status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-a-business-continuity-plan-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file naming.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of business continuity plan status from D365 F&SCM to embed in Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopABusinessContinuityPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopABusinessContinuityPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and file naming.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-a-business-continuity-plan-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
