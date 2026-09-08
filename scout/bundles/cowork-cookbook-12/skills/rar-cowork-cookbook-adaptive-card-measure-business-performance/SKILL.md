---
name: "rar-cowork-cookbook-adaptive-card-measure-business-performance"
description: "Generates a read-only Adaptive Card JSON file summarizing business performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_measure_business_performance", "rar_sha256": "cf11176991cf06ffb00832ed37ecf16bb8c03848902bbd07a916e7a76d2280aa", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_measure_business_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_measure_business_performance_agent.py` and in the RCI capsule.

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

Measure business performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing business performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-measure-business-performance
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
      "description": "Name of the Adaptive Card JSON file to produce.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date used for the card timestamp and output filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_measure_business_performance_agent.py` and embedded as the fenced Python below (sha256 cf11176991cf06ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_measure_business_performance_agent.py` first:

```bash
python3 adaptive_card_measure_business_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_measure_business_performance_agent.py   # or on stdin
python3 adaptive_card_measure_business_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure business performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing business performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-measure-business-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_measure_business_performance',
    "version": '3.0.2',
    "display_name": 'Measure business performance Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing business performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-measure-business-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-measure-business-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '99e5db50a2158cf0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-business-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-measure-business-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.', 'snapshot_date': 'Date used for the card timestamp and output filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical measure business performance status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-measure-business-performance-2026-05-24-card.json' that visualizes the current state of measure business performance. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current measure business performance KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing business performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of business performance status for USMF as of 2026-05-24.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the card timestamp and output filename.', 'name': 'snapshot_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of D365 ERP business performance status; requires the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardMeasureBusinessPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMeasureBusinessPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used for the card timestamp and output filename.', 'type': 'string'}},
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
    print(AdaptiveCardMeasureBusinessPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
