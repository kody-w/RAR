---
name: "rar-cowork-cookbook-adaptive-card-monitor-customer-credit"
description: "Generates a read-only Adaptive Card JSON file snapshotting customer credit status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_customer_credit", "rar_sha256": "bbb02a2a0e1bd60700144c2689fc699838d66014e71de2a17973cbc08870a76d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
