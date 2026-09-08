---
name: "rar-cowork-cookbook-adaptive-card-bill-subscriptions"
description: "Generates a read-only Adaptive Card JSON file summarizing bill subscriptions status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_bill_subscriptions", "rar_sha256": "1981b86b41f4ca30f3d18870f51ffef4a011cb508e145d182cc178a33db6bea1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
