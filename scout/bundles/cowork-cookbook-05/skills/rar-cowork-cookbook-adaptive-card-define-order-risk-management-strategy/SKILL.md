---
name: "rar-cowork-cookbook-adaptive-card-define-order-risk-management-strategy"
description: "Generates a read-only Adaptive Card JSON file visualizing order risk management strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_order_risk_management_strategy", "rar_sha256": "38b61e18a2b76ff3c69d005d18ac786352ae032b8b393ff16400a92eb8e1df9a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_order_risk_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_order_risk_management_strategy_agent.py` and in the RCI capsule.

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

Define order risk management strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing order risk management strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-order-risk-management-strategy
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
    "as_of_date": {
      "description": "Date used for the card timestamp and status snapshot.",
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
      "description": "D365 F&SCM legal entity to read from (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-order-risk-management-strategy-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_order_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 38b61e18a2b76ff3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_order_risk_management_strategy_agent.py` first:

```bash
python3 adaptive_card_define_order_risk_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_order_risk_management_strategy_agent.py   # or on stdin
python3 adaptive_card_define_order_risk_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define order risk management strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing order risk management strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-order-risk-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_order_risk_management_strategy',
    "version": '3.0.2',
    "display_name": 'Define order risk management strategy Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing order risk management strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-order-risk-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-order-risk-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '964c975faab1e1c3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-order-risk-management-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-define-order-risk-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date used for the card timestamp and status snapshot.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 F&SCM legal entity to read from (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-order-risk-management-strategy-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define order risk management strategy status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-order-risk-management-strategy-2026-05-24-card.json' that visualizes the current state of define order risk management strategy. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current define order risk management strategy KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing order risk management strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON showing order risk management strategy status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to read from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-order-risk-management-strategy-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and status snapshot.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of order risk management strategy status from D365 ERP data, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineOrderRiskManagementStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineOrderRiskManagementStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and status snapshot.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to read from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-order-risk-management-strategy-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineOrderRiskManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
