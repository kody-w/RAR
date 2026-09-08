---
name: "rar-cowork-cookbook-adaptive-card-consolidate-requisitions"
description: "Generates a read-only Adaptive Card JSON file summarizing consolidate requisitions status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_consolidate_requisitions", "rar_sha256": "b2e67bc5da6949f89f2998b3b3feb486662d2390b005a801337601da7d3b353d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
