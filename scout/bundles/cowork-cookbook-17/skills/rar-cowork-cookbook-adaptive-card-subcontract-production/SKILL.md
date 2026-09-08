---
name: "rar-cowork-cookbook-adaptive-card-subcontract-production"
description: "Generates a read-only Adaptive Card JSON file summarizing subcontract production status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_subcontract_production", "rar_sha256": "2f711a77752563275c85da5a65f8b59daef5c298a30ddd28b15f651bc90d2b60", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
