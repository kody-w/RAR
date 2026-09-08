---
name: "rar-cowork-cookbook-adaptive-card-define-performance-strategy"
description: "Generates a read-only Adaptive Card JSON file visualizing define performance strategy status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_performance_strategy", "rar_sha256": "d7687e0b5c20bc851748f95a92240034d04899eacc41d4aa0f6d9a2f272e025f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
