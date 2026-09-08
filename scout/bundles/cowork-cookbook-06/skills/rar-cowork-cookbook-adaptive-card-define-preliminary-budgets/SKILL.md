---
name: "rar-cowork-cookbook-adaptive-card-define-preliminary-budgets"
description: "Generates a read-only Adaptive Card JSON file summarizing preliminary budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_preliminary_budgets", "rar_sha256": "c892de71c698aee84c4e3bf45a318cf07dc339c47574b2ae6048afc5aeb0b26c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_preliminary_budgets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_preliminary_budgets_agent.py` and in the RCI capsule.

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

Define preliminary budgets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing preliminary budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-preliminary-budgets
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-preliminary-budgets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_preliminary_budgets_agent.py` and embedded as the fenced Python below (sha256 c892de71c698aee8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_preliminary_budgets_agent.py` first:

```bash
python3 adaptive_card_define_preliminary_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_preliminary_budgets_agent.py   # or on stdin
python3 adaptive_card_define_preliminary_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define preliminary budgets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing preliminary budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-preliminary-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_preliminary_budgets',
    "version": '3.0.2',
    "display_name": 'Define preliminary budgets Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing preliminary budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-preliminary-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-preliminary-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f67555dfc9097e3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/define-preliminary-budgets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-define-preliminary-budgets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card header timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-preliminary-budgets-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define preliminary budgets status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-preliminary-budgets-2026-05-24-card.json' that visualizes the current state of define preliminary budgets. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current define preliminary budgets KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing preliminary budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing preliminary budget status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-preliminary-budgets-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Snapshot date used in the card header timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of preliminary budget status for Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefinePreliminaryBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefinePreliminaryBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card header timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-preliminary-budgets-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefinePreliminaryBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
