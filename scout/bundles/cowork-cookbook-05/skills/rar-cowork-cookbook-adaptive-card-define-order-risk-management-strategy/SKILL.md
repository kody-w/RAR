---
name: "rar-cowork-cookbook-adaptive-card-define-order-risk-management-strategy"
description: "Generates a read-only Adaptive Card JSON file visualizing order risk management strategy status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_order_risk_management_strategy", "rar_sha256": "38b61e18a2b76ff3c69d005d18ac786352ae032b8b393ff16400a92eb8e1df9a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
