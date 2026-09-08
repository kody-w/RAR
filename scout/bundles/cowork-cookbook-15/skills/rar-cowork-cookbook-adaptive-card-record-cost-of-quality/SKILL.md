---
name: "rar-cowork-cookbook-adaptive-card-record-cost-of-quality"
description: "Generates a read-only Adaptive Card JSON file summarizing cost of quality status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_record_cost_of_quality", "rar_sha256": "c81a0866774d097f5a9f9853e7b4c5299f45666f6cae3896de921de5afc800b3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_record_cost_of_quality`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_record_cost_of_quality_agent.py` and in the RCI capsule.

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

Record cost of quality Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing cost of quality status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-cost-of-quality
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
      "description": "Snapshot date used in the card timestamp and output filename.",
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
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_record_cost_of_quality_agent.py` and embedded as the fenced Python below (sha256 c81a0866774d097f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_record_cost_of_quality_agent.py` first:

```bash
python3 adaptive_card_record_cost_of_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_record_cost_of_quality_agent.py   # or on stdin
python3 adaptive_card_record_cost_of_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record cost of quality Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing cost of quality status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-cost-of-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_record_cost_of_quality',
    "version": '3.0.2',
    "display_name": 'Record cost of quality Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing cost of quality status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-record-cost-of-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-record-cost-of-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ccafdc7904fef4a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/record-cost-of-quality'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-record-cost-of-quality', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical record cost of quality status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-record-cost-of-quality-2026-05-24-card.json' that visualizes the current state of record cost of quality. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current record cost of quality KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing cost of quality status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of cost of quality status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of record cost of quality status from D365 ERP without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardRecordCostOfQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecordCostOfQuality'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardRecordCostOfQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
