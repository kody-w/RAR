---
name: "rar-cowork-cookbook-adaptive-card-identify-strategic-initiatives"
description: "Generates a read-only Adaptive Card JSON file summarizing strategic initiative status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_strategic_initiatives", "rar_sha256": "7eb14830ecd2618c3cf04b3b4fb80ce943031e3f19bb16b174e3d36b54c69275", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
