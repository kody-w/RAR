---
name: "rar-cowork-cookbook-adaptive-card-correct-production-processes"
description: "Generates a read-only Adaptive Card JSON file visualizing correct production processes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_correct_production_processes", "rar_sha256": "08a089136c4c40d7d9fd6b666ec18389b8084d0a243a9fd3fe79720813fcc478", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_correct_production_processes`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_correct_production_processes_agent.py` and in the RCI capsule.

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

Correct production processes Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing correct production processes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-correct-production-processes
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
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-correct-production-processes-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_correct_production_processes_agent.py` and embedded as the fenced Python below (sha256 08a089136c4c40d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_correct_production_processes_agent.py` first:

```bash
python3 adaptive_card_correct_production_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_correct_production_processes_agent.py   # or on stdin
python3 adaptive_card_correct_production_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct production processes Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing correct production processes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-correct-production-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_correct_production_processes',
    "version": '3.0.2',
    "display_name": 'Correct production processes Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing correct production processes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-correct-production-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-correct-production-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '68562b4e3054efef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/correct-production-processes'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-correct-production-processes', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-correct-production-processes-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical correct production processes status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-correct-production-processes-2026-05-24-card.json' that visualizes the current state of correct production processes. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current correct production processes KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing correct production processes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing correct production processes status in USMF for our Teams dashboard.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-correct-production-processes-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of production process status for Teams, Outlook, or a dashboard, without changing D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardCorrectProductionProcesses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCorrectProductionProcesses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-correct-production-processes-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardCorrectProductionProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
