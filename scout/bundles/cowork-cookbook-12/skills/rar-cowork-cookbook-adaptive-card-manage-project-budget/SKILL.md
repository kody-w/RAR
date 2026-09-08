---
name: "rar-cowork-cookbook-adaptive-card-manage-project-budget"
description: "Generates a read-only Adaptive Card JSON file visualizing project budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_project_budget", "rar_sha256": "03bbb498e61564bb1e40db39c562dfd28f0a862e8812ee81c45cad524afdc061", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
