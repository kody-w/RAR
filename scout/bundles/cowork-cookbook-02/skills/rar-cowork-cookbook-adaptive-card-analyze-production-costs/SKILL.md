---
name: "rar-cowork-cookbook-adaptive-card-analyze-production-costs"
description: "Generates a read-only Adaptive Card JSON file visualizing production cost status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_production_costs", "rar_sha256": "d8251b8accd903b304248baf61c8161429b4cf168ccd7f1df89505dc8156f311", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
