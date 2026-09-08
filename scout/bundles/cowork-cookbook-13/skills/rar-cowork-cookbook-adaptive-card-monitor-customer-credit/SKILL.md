---
name: "rar-cowork-cookbook-adaptive-card-monitor-customer-credit"
description: "Generates a read-only Adaptive Card JSON file snapshotting customer credit status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_customer_credit", "rar_sha256": "bbb02a2a0e1bd60700144c2689fc699838d66014e71de2a17973cbc08870a76d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_monitor_customer_credit`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_monitor_customer_credit_agent.py` and in the RCI capsule.

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

Monitor customer credit Status Adaptive Card — Generates a read-only Adaptive Card JSON file snapshotting customer credit status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-customer-credit
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-customer-credit-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_customer_credit_agent.py` and embedded as the fenced Python below (sha256 bbb02a2a0e1bd607…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_customer_credit_agent.py` first:

```bash
python3 adaptive_card_monitor_customer_credit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_customer_credit_agent.py   # or on stdin
python3 adaptive_card_monitor_customer_credit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor customer credit Status Adaptive Card — Generates a read-only Adaptive Card JSON file snapshotting customer credit status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-customer-credit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_customer_credit',
    "version": '3.0.2',
    "display_name": 'Monitor customer credit Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file snapshotting customer credit status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-monitor-customer-credit',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-customer-credit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '425cd85da1bfd428',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/monitor-customer-credit'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-monitor-customer-credit', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_button_count': 'How many action buttons to include (2-3).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-customer-credit-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical monitor customer credit status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-monitor-customer-credit-2026-05-24-card.json' that visualizes the current state of monitor customer credit. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current monitor customer credit KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file snapshotting customer credit status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card of customer credit status for USMF with 4 KPI tiles and 2 action buttons.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-customer-credit-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'How many action buttons to include (2-3).', 'name': 'action_button_count'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card visualizing current customer credit status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardMonitorCustomerCredit(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorCustomerCredit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_button_count': {'description': 'How many action buttons to include (2-3).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-customer-credit-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardMonitorCustomerCredit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
