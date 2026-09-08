---
name: "rar-cowork-cookbook-adaptive-card-develop-production-processes"
description: "Generates a read-only Adaptive Card JSON file summarizing develop-production-processes status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_production_processes", "rar_sha256": "a7045f67b67a0bb9ba37bfbc7a7fbd8e01413dea88b5938326c00e5bc5b50134", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
