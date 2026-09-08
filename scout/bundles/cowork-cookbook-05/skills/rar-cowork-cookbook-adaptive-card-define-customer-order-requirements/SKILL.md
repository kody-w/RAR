---
name: "rar-cowork-cookbook-adaptive-card-define-customer-order-requirements"
description: "Generates a read-only Adaptive Card JSON file visualizing define customer order requirements status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_customer_order_requirements", "rar_sha256": "a8462ca8d5d67394e2e251f5a7b7939c262ec29d83a5e23b62092205ce8bdac2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_customer_order_requirements`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_customer_order_requirements_agent.py` and in the RCI capsule.

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

Define customer order requirements Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define customer order requirements status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-order-requirements
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
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to read from, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-customer-order-requirements-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_customer_order_requirements_agent.py` and embedded as the fenced Python below (sha256 a8462ca8d5d67394…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_customer_order_requirements_agent.py` first:

```bash
python3 adaptive_card_define_customer_order_requirements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_customer_order_requirements_agent.py   # or on stdin
python3 adaptive_card_define_customer_order_requirements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer order requirements Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define customer order requirements status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-order-requirements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_customer_order_requirements',
    "version": '3.0.2',
    "display_name": 'Define customer order requirements Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing define customer order requirements status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-customer-order-requirements',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-customer-order-requirements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44e3d2cdf2b494b2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-customer-order-requirements'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-define-customer-order-requirements', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-customer-order-requirements-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define customer order requirements status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-customer-order-requirements-2026-05-24-card.json' that visualizes the current state of define customer order requirements. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current define customer order requirements KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing define customer order requirements status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing define customer order requirements status from USMF for Teams.', 'inputs': [{'description': 'D365 legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-customer-order-requirements-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of define customer order requirements status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineCustomerOrderRequirements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineCustomerOrderRequirements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-customer-order-requirements-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineCustomerOrderRequirements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
