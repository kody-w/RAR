---
name: "rar-cowork-cookbook-adaptive-card-manage-bills-of-exchange"
description: "Generates a read-only Adaptive Card JSON file summarizing bills of exchange status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_bills_of_exchange", "rar_sha256": "aa58eabf2837495a842db804710c0b7437266f8417e78a926b1c55718dc5df7b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_bills_of_exchange`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_bills_of_exchange_agent.py` and in the RCI capsule.

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

Manage bills of exchange Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing bills of exchange status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-exchange
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
      "description": "Which 2-3 action buttons to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date/timestamp the card snapshot represents.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-bills-of-exchange-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_bills_of_exchange_agent.py` and embedded as the fenced Python below (sha256 aa58eabf2837495a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_bills_of_exchange_agent.py` first:

```bash
python3 adaptive_card_manage_bills_of_exchange_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_bills_of_exchange_agent.py   # or on stdin
python3 adaptive_card_manage_bills_of_exchange_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage bills of exchange Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing bills of exchange status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-exchange
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_bills_of_exchange',
    "version": '3.0.2',
    "display_name": 'Manage bills of exchange Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing bills of exchange status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-manage-bills-of-exchange',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-bills-of-exchange',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44e3e34b13a9d35d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/manage-bills-of-exchange'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-manage-bills-of-exchange', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'Which 2-3 action buttons to include on the card.', 'as_of_date': 'Date/timestamp the card snapshot represents.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-bills-of-exchange-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage bills of exchange status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-bills-of-exchange-2026-05-24-card.json' that visualizes the current state of manage bills of exchange. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage bills of exchange KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing bills of exchange status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of bills of exchange status in USMF as of 2026-05-24 for Teams.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-bills-of-exchange-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date/timestamp the card snapshot represents.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'Which 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of bills of exchange status for Teams, Outlook, or a dashboard, without changing any D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageBillsOfExchange(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageBillsOfExchange'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'Which 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date/timestamp the card snapshot represents.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-manage-bills-of-exchange-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardManageBillsOfExchange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
