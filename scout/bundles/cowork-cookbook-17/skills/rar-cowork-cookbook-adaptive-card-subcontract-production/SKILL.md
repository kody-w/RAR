---
name: "rar-cowork-cookbook-adaptive-card-subcontract-production"
description: "Generates a read-only Adaptive Card JSON file summarizing subcontract production status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_subcontract_production", "rar_sha256": "2f711a77752563275c85da5a65f8b59daef5c298a30ddd28b15f651bc90d2b60", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_subcontract_production`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_subcontract_production_agent.py` and in the RCI capsule.

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

Subcontract production Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing subcontract production status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-subcontract-production
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
    "action_buttons": {
      "description": "Which 2-3 action buttons the card should offer.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date used for the snapshot timestamp and output filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_subcontract_production_agent.py` and embedded as the fenced Python below (sha256 2f711a7775256327…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_subcontract_production_agent.py` first:

```bash
python3 adaptive_card_subcontract_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_subcontract_production_agent.py   # or on stdin
python3 adaptive_card_subcontract_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Subcontract production Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing subcontract production status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-subcontract-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_subcontract_production',
    "version": '3.0.2',
    "display_name": 'Subcontract production Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing subcontract production status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-subcontract-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-subcontract-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fb38e54c7a413615',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/subcontract-production'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-subcontract-production', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'Which 2-3 action buttons the card should offer.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.', 'snapshot_date': 'Date used for the snapshot timestamp and output filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical subcontract production status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-subcontract-production-2026-05-24-card.json' that visualizes the current state of subcontract production. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current subcontract production KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing subcontract production status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of subcontract production status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the snapshot timestamp and output filename.', 'name': 'snapshot_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'Which 2-3 action buttons the card should offer.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of current subcontract production status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardSubcontractProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardSubcontractProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'Which 2-3 action buttons the card should offer.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used for the snapshot timestamp and output filename.', 'type': 'string'}},
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
    print(AdaptiveCardSubcontractProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
