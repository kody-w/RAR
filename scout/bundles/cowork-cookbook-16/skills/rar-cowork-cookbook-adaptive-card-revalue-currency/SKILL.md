---
name: "rar-cowork-cookbook-adaptive-card-revalue-currency"
description: "Generates a read-only Adaptive Card JSON file showing current revalue currency status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable status ca"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_revalue_currency", "rar_sha256": "509b644662fcadaaeba68e44e452cdcac0da58009ede87ad46ca9e109025126e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_revalue_currency`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_revalue_currency_agent.py` and in the RCI capsule.

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

Revalue currency Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing current revalue currency status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable status ca

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-currency
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
      "description": "Date the snapshot represents, used in the card timestamp and output filename.",
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-revalue-currency-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_revalue_currency_agent.py` and embedded as the fenced Python below (sha256 509b644662fcadaa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_revalue_currency_agent.py` first:

```bash
python3 adaptive_card_revalue_currency_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_revalue_currency_agent.py   # or on stdin
python3 adaptive_card_revalue_currency_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue currency Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing current revalue currency status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable status ca

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-currency
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_revalue_currency',
    "version": '3.0.2',
    "display_name": 'Revalue currency Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file showing current revalue currency status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable status ca',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-revalue-currency',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-revalue-currency',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9aa586907da6f1f1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/revalue-currency'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-revalue-currency', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date the snapshot represents, used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-revalue-currency-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical revalue currency status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-revalue-currency-2026-05-24-card.json' that visualizes the current state of revalue currency. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current revalue currency KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file showing current revalue currency status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable status ca', 'example_request': 'Make an Adaptive Card JSON of revalue currency status for USMF as of 2026-05-24, with KPI tiles and a RAG row.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents, used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-revalue-currency-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user wants a revalue currency status snapshot as Adaptive Card JSON to embed in Teams, Outlook, or a dashboard. Requires the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardRevalueCurrency(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRevalueCurrency'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date the snapshot represents, used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-revalue-currency-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardRevalueCurrency().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
