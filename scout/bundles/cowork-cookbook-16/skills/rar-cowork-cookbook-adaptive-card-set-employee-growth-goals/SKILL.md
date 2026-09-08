---
name: "rar-cowork-cookbook-adaptive-card-set-employee-growth-goals"
description: "Generates a read-only Adaptive Card JSON file visualizing employee growth goal status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_set_employee_growth_goals", "rar_sha256": "e5b993ed175f802d414cb8bf0a256bf1441880d7aa22c6c2330874e49166a93c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_set_employee_growth_goals`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_set_employee_growth_goals_agent.py` and in the RCI capsule.

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

Set employee growth goals Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing employee growth goal status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-set-employee-growth-goals
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
      "description": "Snapshot date used in the card header timestamp and filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-set-employee-growth-goals-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_set_employee_growth_goals_agent.py` and embedded as the fenced Python below (sha256 e5b993ed175f802d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_set_employee_growth_goals_agent.py` first:

```bash
python3 adaptive_card_set_employee_growth_goals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_set_employee_growth_goals_agent.py   # or on stdin
python3 adaptive_card_set_employee_growth_goals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set employee growth goals Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing employee growth goal status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-set-employee-growth-goals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_set_employee_growth_goals',
    "version": '3.0.2',
    "display_name": 'Set employee growth goals Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing employee growth goal status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-set-employee-growth-goals',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-set-employee-growth-goals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8e7644f17d563a3c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/set-employee-growth-goals'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-set-employee-growth-goals', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card header timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-set-employee-growth-goals-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical set employee growth goals status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-set-employee-growth-goals-2026-05-24-card.json' that visualizes the current state of set employee growth goals. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current set employee growth goals KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing employee growth goal status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing employee growth goal status for USMF as of today.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-set-employee-growth-goals-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Snapshot date used in the card header timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of employee growth goal status for Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardSetEmployeeGrowthGoals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardSetEmployeeGrowthGoals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card header timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-set-employee-growth-goals-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardSetEmployeeGrowthGoals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
