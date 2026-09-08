---
name: "rar-cowork-cookbook-adaptive-card-measure-business-performance"
description: "Generates a read-only Adaptive Card JSON file summarizing business performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_measure_business_performance", "rar_sha256": "cf11176991cf06ffb00832ed37ecf16bb8c03848902bbd07a916e7a76d2280aa", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
