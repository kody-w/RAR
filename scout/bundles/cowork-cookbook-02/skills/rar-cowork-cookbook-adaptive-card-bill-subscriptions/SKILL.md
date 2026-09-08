---
name: "rar-cowork-cookbook-adaptive-card-bill-subscriptions"
description: "Generates a read-only Adaptive Card JSON file summarizing bill subscriptions status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_bill_subscriptions", "rar_sha256": "1981b86b41f4ca30f3d18870f51ffef4a011cb508e145d182cc178a33db6bea1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_bill_subscriptions`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_bill_subscriptions_agent.py` and in the RCI capsule.

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

Bill subscriptions Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing bill subscriptions status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-bill-subscriptions
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
      "description": "Name of the Adaptive Card JSON file to write into Documents/Cowork/output/.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date used in the card timestamp and output filename, e.g. 2026-05-24.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_bill_subscriptions_agent.py` and embedded as the fenced Python below (sha256 1981b86b41f4ca30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_bill_subscriptions_agent.py` first:

```bash
python3 adaptive_card_bill_subscriptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_bill_subscriptions_agent.py   # or on stdin
python3 adaptive_card_bill_subscriptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Bill subscriptions Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing bill subscriptions status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-bill-subscriptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_bill_subscriptions',
    "version": '3.0.2',
    "display_name": 'Bill subscriptions Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing bill subscriptions status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.',
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
        "upstream_slug": 'adaptive-card-bill-subscriptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-bill-subscriptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '65cee9d9e88cf78f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/bill-subscriptions'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-bill-subscriptions', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to write into Documents/Cowork/output/.', 'snapshot_date': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical bill subscriptions status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-bill-subscriptions-2026-05-24-card.json' that visualizes the current state of bill subscriptions. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current bill subscriptions KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing bill subscriptions status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.', 'example_request': 'Make me an Adaptive Card JSON of bill subscriptions status for USMF as of 2026-05-24 to post in Teams.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.', 'name': 'snapshot_date'}, {'description': 'Name of the Adaptive Card JSON file to write into Documents/Cowork/output/.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of bill subscriptions status for a dashboard, email, or Teams post, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardBillSubscriptions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardBillSubscriptions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to write into Documents/Cowork/output/.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.', 'type': 'string'}},
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
    print(AdaptiveCardBillSubscriptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
