---
name: "rar-cowork-cookbook-adaptive-card-adjust-production-plan"
description: "Generates a read-only Adaptive Card JSON file visualizing adjust production plan status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_adjust_production_plan", "rar_sha256": "ce2e372a2cf9f3ed178096d6068b1d1690aaa1cfe3908643b05d6a08674468de", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
