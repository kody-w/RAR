---
name: "rar-cowork-cookbook-adaptive-card-define-preliminary-budgets"
description: "Generates a read-only Adaptive Card JSON file summarizing preliminary budget status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_preliminary_budgets", "rar_sha256": "c892de71c698aee84c4e3bf45a318cf07dc339c47574b2ae6048afc5aeb0b26c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
