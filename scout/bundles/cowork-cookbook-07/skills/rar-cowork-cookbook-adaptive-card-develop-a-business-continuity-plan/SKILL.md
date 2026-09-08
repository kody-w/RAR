---
name: "rar-cowork-cookbook-adaptive-card-develop-a-business-continuity-plan"
description: "Generates a read-only Adaptive Card JSON file summarizing business continuity plan status from Dynamics 365 ERP data for a legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan", "rar_sha256": "e91892196c2931b9ab47e083e98715257a06590e352e5603c228537363143349", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
