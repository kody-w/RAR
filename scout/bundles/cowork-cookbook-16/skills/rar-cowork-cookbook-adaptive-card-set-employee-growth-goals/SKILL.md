---
name: "rar-cowork-cookbook-adaptive-card-set-employee-growth-goals"
description: "Generates a read-only Adaptive Card JSON file visualizing employee growth goal status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_set_employee_growth_goals", "rar_sha256": "e5b993ed175f802d414cb8bf0a256bf1441880d7aa22c6c2330874e49166a93c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
