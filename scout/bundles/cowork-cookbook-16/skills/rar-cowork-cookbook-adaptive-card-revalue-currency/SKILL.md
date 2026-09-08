---
name: "rar-cowork-cookbook-adaptive-card-revalue-currency"
description: "Generates a read-only Adaptive Card JSON file showing current revalue currency status for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons. Call when you need an embeddable status ca"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_revalue_currency", "rar_sha256": "509b644662fcadaaeba68e44e452cdcac0da58009ede87ad46ca9e109025126e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
