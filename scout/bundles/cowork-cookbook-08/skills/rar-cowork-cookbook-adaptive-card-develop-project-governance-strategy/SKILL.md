---
name: "rar-cowork-cookbook-adaptive-card-develop-project-governance-strategy"
description: "Generates a read-only Adaptive Card JSON file summarizing project governance strategy status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_project_governance_strategy", "rar_sha256": "f196a524ceb0dea02a1609cca20fce85f1ab47361957a96008ea4c8dae2ab27d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
