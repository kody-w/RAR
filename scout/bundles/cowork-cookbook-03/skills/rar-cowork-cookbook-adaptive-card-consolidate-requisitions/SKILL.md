---
name: "rar-cowork-cookbook-adaptive-card-consolidate-requisitions"
description: "Generates a read-only Adaptive Card JSON file summarizing consolidate requisitions status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_consolidate_requisitions", "rar_sha256": "b2e67bc5da6949f89f2998b3b3feb486662d2390b005a801337601da7d3b353d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_consolidate_requisitions`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_consolidate_requisitions_agent.py` and in the RCI capsule.

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

Consolidate requisitions Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing consolidate requisitions status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions
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
      "description": "The 2-3 action buttons to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date used for the card timestamp and snapshot label.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-consolidate-requisitions-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_consolidate_requisitions_agent.py` and embedded as the fenced Python below (sha256 b2e67bc5da6949f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_consolidate_requisitions_agent.py` first:

```bash
python3 adaptive_card_consolidate_requisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_consolidate_requisitions_agent.py   # or on stdin
python3 adaptive_card_consolidate_requisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate requisitions Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing consolidate requisitions status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_consolidate_requisitions',
    "version": '3.0.2',
    "display_name": 'Consolidate requisitions Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing consolidate requisitions status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-consolidate-requisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1faa7838e5196bbf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/consolidate-requisitions'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-consolidate-requisitions', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Date used for the card timestamp and snapshot label.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-consolidate-requisitions-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical consolidate requisitions status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-consolidate-requisitions-2026-05-24-card.json' that visualizes the current state of consolidate requisitions. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current consolidate requisitions KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing consolidate requisitions status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of consolidate requisitions status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-consolidate-requisitions-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and snapshot label.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of consolidate requisitions status for Teams, Outlook, or a dashboard, without changing D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConsolidateRequisitions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConsolidateRequisitions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and snapshot label.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-consolidate-requisitions-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardConsolidateRequisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
