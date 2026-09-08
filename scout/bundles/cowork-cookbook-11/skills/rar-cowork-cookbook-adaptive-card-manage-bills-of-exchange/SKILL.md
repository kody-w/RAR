---
name: "rar-cowork-cookbook-adaptive-card-manage-bills-of-exchange"
description: "Generates a read-only Adaptive Card JSON file summarizing bills of exchange status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_bills_of_exchange", "rar_sha256": "aa58eabf2837495a842db804710c0b7437266f8417e78a926b1c55718dc5df7b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
