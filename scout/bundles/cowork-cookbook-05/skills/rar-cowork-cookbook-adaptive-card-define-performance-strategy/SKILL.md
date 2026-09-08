---
name: "rar-cowork-cookbook-adaptive-card-define-performance-strategy"
description: "Generates a read-only Adaptive Card JSON file visualizing define performance strategy status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_performance_strategy", "rar_sha256": "d7687e0b5c20bc851748f95a92240034d04899eacc41d4aa0f6d9a2f272e025f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_performance_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_performance_strategy_agent.py` and in the RCI capsule.

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

Define performance strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define performance strategy status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-performance-strategy
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
      "description": "Snapshot date used in the card header timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-performance-strategy-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_performance_strategy_agent.py` and embedded as the fenced Python below (sha256 d7687e0b5c20bc85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_performance_strategy_agent.py` first:

```bash
python3 adaptive_card_define_performance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_performance_strategy_agent.py   # or on stdin
python3 adaptive_card_define_performance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define performance strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define performance strategy status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-performance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_performance_strategy',
    "version": '3.0.2',
    "display_name": 'Define performance strategy Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing define performance strategy status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-define-performance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-performance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a261e4230e401cd3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-performance-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-define-performance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Snapshot date used in the card header timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-performance-strategy-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define performance strategy status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-performance-strategy-2026-05-24-card.json' that visualizes the current state of define performance strategy. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current define performance strategy KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing define performance strategy status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card of define performance strategy status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card header timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-performance-strategy-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of define performance strategy status for Teams, Outlook, or a dashboard. Read-only; no data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefinePerformanceStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefinePerformanceStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Snapshot date used in the card header timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-performance-strategy-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefinePerformanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
