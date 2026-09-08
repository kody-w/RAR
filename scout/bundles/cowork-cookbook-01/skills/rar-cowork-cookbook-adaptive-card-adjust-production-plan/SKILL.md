---
name: "rar-cowork-cookbook-adaptive-card-adjust-production-plan"
description: "Generates a read-only Adaptive Card JSON file visualizing adjust production plan status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_adjust_production_plan", "rar_sha256": "ce2e372a2cf9f3ed178096d6068b1d1690aaa1cfe3908643b05d6a08674468de", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_adjust_production_plan`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_adjust_production_plan_agent.py` and in the RCI capsule.

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

Adjust production plan Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing adjust production plan status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-production-plan
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-adjust-production-plan-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date used in the card timestamp and output filename, e.g. 2026-05-24.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_adjust_production_plan_agent.py` and embedded as the fenced Python below (sha256 ce2e372a2cf9f3ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_adjust_production_plan_agent.py` first:

```bash
python3 adaptive_card_adjust_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_adjust_production_plan_agent.py   # or on stdin
python3 adaptive_card_adjust_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust production plan Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing adjust production plan status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_adjust_production_plan',
    "version": '3.0.2',
    "display_name": 'Adjust production plan Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing adjust production plan status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-adjust-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-adjust-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf8934ccbe9d7e4e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/adjust-production-plan'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-adjust-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-adjust-production-plan-2026-05-24-card.json.', 'snapshot_date': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical adjust production plan status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-adjust-production-plan-2026-05-24-card.json' that visualizes the current state of adjust production plan. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current adjust production plan KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing adjust production plan status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of adjust production plan status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.', 'name': 'snapshot_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-adjust-production-plan-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of adjust production plan status from D365 ERP, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardAdjustProductionPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAdjustProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-adjust-production-plan-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used in the card timestamp and output filename, e.g. 2026-05-24.', 'type': 'string'}},
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
    print(AdaptiveCardAdjustProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
