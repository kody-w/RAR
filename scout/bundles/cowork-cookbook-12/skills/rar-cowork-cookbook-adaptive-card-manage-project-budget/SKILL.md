---
name: "rar-cowork-cookbook-adaptive-card-manage-project-budget"
description: "Generates a read-only Adaptive Card JSON file visualizing project budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_project_budget", "rar_sha256": "03bbb498e61564bb1e40db39c562dfd28f0a862e8812ee81c45cad524afdc061", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_project_budget`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_project_budget_agent.py` and in the RCI capsule.

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

Manage project budget Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing project budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-project-budget
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
    "as_of_date": {
      "description": "Date used for the card timestamp and output filename, e.g. 2026-05-24.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
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
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_project_budget_agent.py` and embedded as the fenced Python below (sha256 03bbb498e61564bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_project_budget_agent.py` first:

```bash
python3 adaptive_card_manage_project_budget_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_project_budget_agent.py   # or on stdin
python3 adaptive_card_manage_project_budget_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project budget Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing project budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-project-budget
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_project_budget',
    "version": '3.0.2',
    "display_name": 'Manage project budget Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing project budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-project-budget',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-project-budget',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2ae4f5d2c241e86c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/manage-project-budget'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-manage-project-budget', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and output filename, e.g. 2026-05-24.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage project budget status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-project-budget-2026-05-24-card.json' that visualizes the current state of manage project budget. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage project budget KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing project budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing manage project budget status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the card timestamp and output filename, e.g. 2026-05-24.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of manage project budget status from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageProjectBudget(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageProjectBudget'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and output filename, e.g. 2026-05-24.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardManageProjectBudget().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
