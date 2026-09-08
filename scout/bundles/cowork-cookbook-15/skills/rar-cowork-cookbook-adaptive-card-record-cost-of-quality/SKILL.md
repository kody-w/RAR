---
name: "rar-cowork-cookbook-adaptive-card-record-cost-of-quality"
description: "Generates a read-only Adaptive Card JSON file summarizing cost of quality status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_record_cost_of_quality", "rar_sha256": "c81a0866774d097f5a9f9853e7b4c5299f45666f6cae3896de921de5afc800b3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
