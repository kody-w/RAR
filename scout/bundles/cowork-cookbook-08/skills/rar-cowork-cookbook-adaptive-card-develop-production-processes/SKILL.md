---
name: "rar-cowork-cookbook-adaptive-card-develop-production-processes"
description: "Generates a read-only Adaptive Card JSON file summarizing develop-production-processes status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_production_processes", "rar_sha256": "a7045f67b67a0bb9ba37bfbc7a7fbd8e01413dea88b5938326c00e5bc5b50134", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_production_processes`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_production_processes_agent.py` and in the RCI capsule.

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

Develop production processes Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing develop-production-processes status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-production-processes
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-production-processes-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_production_processes_agent.py` and embedded as the fenced Python below (sha256 a7045f67b67a0bb9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_production_processes_agent.py` first:

```bash
python3 adaptive_card_develop_production_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_production_processes_agent.py   # or on stdin
python3 adaptive_card_develop_production_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop production processes Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing develop-production-processes status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-production-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_production_processes',
    "version": '3.0.2',
    "display_name": 'Develop production processes Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing develop-production-processes status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-develop-production-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-production-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2216e5a30f8b1cf3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/develop-production-processes'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-develop-production-processes', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-production-processes-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop production processes status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-production-processes-2026-05-24-card.json' that visualizes the current state of develop production processes. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop production processes KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing develop-production-processes status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of develop production processes status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-production-processes-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of develop production processes status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopProductionProcesses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopProductionProcesses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-production-processes-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopProductionProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
