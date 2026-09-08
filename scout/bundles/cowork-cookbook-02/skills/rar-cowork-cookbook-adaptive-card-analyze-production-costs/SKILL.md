---
name: "rar-cowork-cookbook-adaptive-card-analyze-production-costs"
description: "Generates a read-only Adaptive Card JSON file visualizing production cost status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_production_costs", "rar_sha256": "d8251b8accd903b304248baf61c8161429b4cf168ccd7f1df89505dc8156f311", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_analyze_production_costs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_analyze_production_costs_agent.py` and in the RCI capsule.

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

Analyze production costs Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing production cost status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-production-costs
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
      "description": "The D365 F&SCM legal entity to analyze, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-production-costs-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_production_costs_agent.py` and embedded as the fenced Python below (sha256 d8251b8accd903b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_production_costs_agent.py` first:

```bash
python3 adaptive_card_analyze_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_production_costs_agent.py   # or on stdin
python3 adaptive_card_analyze_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze production costs Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing production cost status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_production_costs',
    "version": '3.0.2',
    "display_name": 'Analyze production costs Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing production cost status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-analyze-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b9e3bbd238ccafab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/analyze-production-costs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-analyze-production-costs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card header timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'The D365 F&SCM legal entity to analyze, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-production-costs-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical analyze production costs status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-analyze-production-costs-2026-05-24-card.json' that visualizes the current state of analyze production costs. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current analyze production costs KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing production cost status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON showing production cost status for USMF as of today.', 'inputs': [{'description': 'The D365 F&SCM legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-production-costs-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Snapshot date used in the card header timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of production cost status for Teams, Outlook, or a dashboard, without changing any D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardAnalyzeProductionCosts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeProductionCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card header timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'The D365 F&SCM legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-production-costs-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardAnalyzeProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
