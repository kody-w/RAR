---
name: "rar-cowork-cookbook-adaptive-card-correct-production-processes"
description: "Generates a read-only Adaptive Card JSON file visualizing correct production processes status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_correct_production_processes", "rar_sha256": "08a089136c4c40d7d9fd6b666ec18389b8084d0a243a9fd3fe79720813fcc478", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
