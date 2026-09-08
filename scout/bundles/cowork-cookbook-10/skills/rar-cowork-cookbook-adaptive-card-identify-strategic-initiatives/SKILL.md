---
name: "rar-cowork-cookbook-adaptive-card-identify-strategic-initiatives"
description: "Generates a read-only Adaptive Card JSON file summarizing strategic initiative status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_strategic_initiatives", "rar_sha256": "7eb14830ecd2618c3cf04b3b4fb80ce943031e3f19bb16b174e3d36b54c69275", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_identify_strategic_initiatives`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_identify_strategic_initiatives_agent.py` and in the RCI capsule.

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

Identify strategic initiatives Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing strategic initiative status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-strategic-initiatives-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_strategic_initiatives_agent.py` and embedded as the fenced Python below (sha256 7eb14830ecd2618c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_strategic_initiatives_agent.py` first:

```bash
python3 adaptive_card_identify_strategic_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_strategic_initiatives_agent.py   # or on stdin
python3 adaptive_card_identify_strategic_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify strategic initiatives Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing strategic initiative status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_strategic_initiatives',
    "version": '3.0.2',
    "display_name": 'Identify strategic initiatives Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing strategic initiative status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-identify-strategic-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-strategic-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f0958c5a35d96b6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/identify-strategic-initiatives'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-identify-strategic-initiatives', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card header timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-strategic-initiatives-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical identify strategic initiatives status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-identify-strategic-initiatives-2026-05-24-card.json' that visualizes the current state of identify strategic initiatives. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current identify strategic initiatives KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing strategic initiative status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing strategic initiative status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-strategic-initiatives-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Snapshot date used in the card header timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of strategic initiative status from D365 ERP for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardIdentifyStrategicInitiatives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyStrategicInitiatives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card header timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-strategic-initiatives-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardIdentifyStrategicInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
