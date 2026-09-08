---
name: "rar-cowork-cookbook-adaptive-card-define-customer-order-requirements"
description: "Generates a read-only Adaptive Card JSON file visualizing define customer order requirements status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_customer_order_requirements", "rar_sha256": "a8462ca8d5d67394e2e251f5a7b7939c262ec29d83a5e23b62092205ce8bdac2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
