---
name: "rar-cowork-cookbook-adaptive-card-develop-merchandise-and-assortment-plans"
description: "Generates a read-only Adaptive Card JSON file summarizing merchandise and assortment planning status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans", "rar_sha256": "e474373f7da6c648c5ca8a79bdef8040aeb6f42fbbbe12eeed03d27f85466486", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` and in the RCI capsule.

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

Develop merchandise and assortment plans Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing merchandise and assortment planning status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-merchandise-and-assortment-plans
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
    "as_of_date": {
      "description": "Snapshot date used in the card header timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` and embedded as the fenced Python below (sha256 e474373f7da6c648…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_merchandise_and_assortment_plans_agent.py` first:

```bash
python3 adaptive_card_develop_merchandise_and_assortment_plans_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_merchandise_and_assortment_plans_agent.py   # or on stdin
python3 adaptive_card_develop_merchandise_and_assortment_plans_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop merchandise and assortment plans Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing merchandise and assortment planning status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-merchandise-and-assortment-plans
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_merchandise_and_assortment_plans',
    "version": '3.0.2',
    "display_name": 'Develop merchandise and assortment plans Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing merchandise and assortment planning status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-develop-merchandise-and-assortment-plans',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-merchandise-and-assortment-plans',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9a3294d6ce4580c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-merchandise-and-assortment-plans'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-develop-merchandise-and-assortment-plans', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card header timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop merchandise and assortment plans status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-merchandise-and-assortment-plans-2026-05-24-card.json' that visualizes the current state of develop merchandise and assortment plans. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop merchandise and assortment plans KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing merchandise and assortment planning status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card showing merchandise and assortment plan status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card header timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of merchandise/assortment plan status for Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopMerchandiseAndAssortmentPlans(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopMerchandiseAndAssortmentPlans'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card header timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce in Documents/Cowork/output/.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopMerchandiseAndAssortmentPlans().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
