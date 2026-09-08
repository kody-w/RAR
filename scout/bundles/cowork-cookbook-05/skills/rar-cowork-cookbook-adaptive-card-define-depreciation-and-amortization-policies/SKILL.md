---
name: "rar-cowork-cookbook-adaptive-card-define-depreciation-and-amortization-policies"
description: "Generates a read-only Adaptive Card JSON file summarizing depreciation and amortization policy status from Dynamics 365 F&SCM (legal entity USMF), with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_depreciation_and_amortization_policies", "rar_sha256": "a0622b5b19db2e6abede68ca0a6eb284cdfc7a21be792c7de0ea5cb5362bf474", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
