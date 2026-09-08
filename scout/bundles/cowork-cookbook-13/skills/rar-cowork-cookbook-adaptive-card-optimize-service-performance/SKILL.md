---
name: "rar-cowork-cookbook-adaptive-card-optimize-service-performance"
description: "Generates a read-only Adaptive Card JSON file visualizing service performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_optimize_service_performance", "rar_sha256": "470b30303e930bbde10bf21b922094a0eb40b8794fd683bced4f2f1bc6ef9a30", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
