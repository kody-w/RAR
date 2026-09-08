---
name: "rar-cowork-cookbook-adaptive-card-optimize-service-performance"
description: "Generates a read-only Adaptive Card JSON file visualizing service performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_optimize_service_performance", "rar_sha256": "470b30303e930bbde10bf21b922094a0eb40b8794fd683bced4f2f1bc6ef9a30", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_optimize_service_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_optimize_service_performance_agent.py` and in the RCI capsule.

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

Optimize service performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing service performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-optimize-service-performance
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
      "description": "Date used for the card timestamp and file name.",
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
      "description": "D365 F&SCM legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-optimize-service-performance-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_optimize_service_performance_agent.py` and embedded as the fenced Python below (sha256 470b30303e930bbd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_optimize_service_performance_agent.py` first:

```bash
python3 adaptive_card_optimize_service_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_optimize_service_performance_agent.py   # or on stdin
python3 adaptive_card_optimize_service_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Optimize service performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing service performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-optimize-service-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_optimize_service_performance',
    "version": '3.0.2',
    "display_name": 'Optimize service performance Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing service performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-optimize-service-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-optimize-service-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '73ce7472b2a88f0e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/optimize-service-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-optimize-service-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-optimize-service-performance-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical optimize service performance status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-optimize-service-performance-2026-05-24-card.json' that visualizes the current state of optimize service performance. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current optimize service performance KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing service performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of optimize service performance status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-optimize-service-performance-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of D365 ERP service performance status, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardOptimizeServicePerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardOptimizeServicePerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-optimize-service-performance-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardOptimizeServicePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
