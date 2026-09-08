---
name: "rar-cowork-cookbook-adaptive-card-define-depreciation-and-amortization-policies"
description: "Generates a read-only Adaptive Card JSON file summarizing depreciation and amortization policy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_depreciation_and_amortization_policies", "rar_sha256": "a0622b5b19db2e6abede68ca0a6eb284cdfc7a21be792c7de0ea5cb5362bf474", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_depreciation_and_amortization_policies`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_depreciation_and_amortization_policies_agent.py` and in the RCI capsule.

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

Define depreciation and amortization policies Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing depreciation and amortization policy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-depreciation-and-amortization-policies
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
      "description": "The 2-3 action buttons to place on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date used for the card timestamp and snapshot label.",
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
      "description": "D365 legal entity to report against (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-depreciation-and-amortization-policies-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_depreciation_and_amortization_policies_agent.py` and embedded as the fenced Python below (sha256 a0622b5b19db2e6a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_depreciation_and_amortization_policies_agent.py` first:

```bash
python3 adaptive_card_define_depreciation_and_amortization_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_depreciation_and_amortization_policies_agent.py   # or on stdin
python3 adaptive_card_define_depreciation_and_amortization_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define depreciation and amortization policies Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing depreciation and amortization policy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-depreciation-and-amortization-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_depreciation_and_amortization_policies',
    "version": '3.0.2',
    "display_name": 'Define depreciation and amortization policies Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing depreciation and amortization policy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-define-depreciation-and-amortization-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-depreciation-and-amortization-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5b92066d7f655225',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-depreciation-and-amortization-policies'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-define-depreciation-and-amortization-policies', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date used for the card timestamp and snapshot label.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report against (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-depreciation-and-amortization-policies-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define depreciation and amortization policies status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-depreciation-and-amortization-policies-2026-05-24-card.json' that visualizes the current state of define depreciation and amortization policies. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Generates an Adaptive Card JSON file with current define depreciation and amortization policies KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing depreciation and amortization policy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing depreciation and amortization policy status in USMF for Teams.', 'inputs': [{'description': 'D365 legal entity to report against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-depreciation-and-amortization-policies-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and snapshot label.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of D365 depreciation/amortization policy status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineDepreciationAndAmortizationPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineDepreciationAndAmortizationPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and snapshot label.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-depreciation-and-amortization-policies-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineDepreciationAndAmortizationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
