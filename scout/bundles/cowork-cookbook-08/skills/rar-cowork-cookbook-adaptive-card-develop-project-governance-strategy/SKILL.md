---
name: "rar-cowork-cookbook-adaptive-card-develop-project-governance-strategy"
description: "Generates a read-only Adaptive Card JSON file summarizing project governance strategy status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_project_governance_strategy", "rar_sha256": "f196a524ceb0dea02a1609cca20fce85f1ab47361957a96008ea4c8dae2ab27d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_project_governance_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_project_governance_strategy_agent.py` and in the RCI capsule.

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

Develop project governance strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing project governance strategy status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-project-governance-strategy
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
      "description": "Dynamics 365 legal entity to read from; defaults to USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-project-governance-strategy-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_project_governance_strategy_agent.py` and embedded as the fenced Python below (sha256 f196a524ceb0dea0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_project_governance_strategy_agent.py` first:

```bash
python3 adaptive_card_develop_project_governance_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_project_governance_strategy_agent.py   # or on stdin
python3 adaptive_card_develop_project_governance_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project governance strategy Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing project governance strategy status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-project-governance-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_project_governance_strategy',
    "version": '3.0.2',
    "display_name": 'Develop project governance strategy Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing project governance strategy status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-develop-project-governance-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-project-governance-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4eae9b0421d78f48',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-governance-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-develop-project-governance-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card header timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to read from; defaults to USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-project-governance-strategy-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical develop project governance strategy status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-develop-project-governance-strategy-2026-05-24-card.json' that visualizes the current state of develop project governance strategy. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current develop project governance strategy KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing project governance strategy status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing our project governance strategy status from D365 USMF.', 'inputs': [{'description': 'Dynamics 365 legal entity to read from; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-project-governance-strategy-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Snapshot date used in the card header timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of develop project governance strategy status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDevelopProjectGovernanceStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopProjectGovernanceStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card header timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to read from; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-develop-project-governance-strategy-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDevelopProjectGovernanceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
