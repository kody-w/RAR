---
name: "rar-cowork-cookbook-adaptive-card-review-call-center-performance"
description: "Generates a read-only Adaptive Card JSON file summarizing call center performance from Dynamics 365 F&SCM (legal entity USMF), with a header, KPI tiles with trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_review_call_center_performance", "rar_sha256": "da80ba96ea7c8cbeb1234b8dcc82d97359c7ecc16f136b239c3413afcc22623f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_review_call_center_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_review_call_center_performance_agent.py` and in the RCI capsule.

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

Review call center performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing call center performance from Dynamics 365 F&SCM (legal entity USMF), with a header, KPI tiles with trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-review-call-center-performance
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
      "description": "The 2-3 action buttons to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date used for the card timestamp and reporting snapshot.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-review-call-center-performance-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_review_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 da80ba96ea7c8cbe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_review_call_center_performance_agent.py` first:

```bash
python3 adaptive_card_review_call_center_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_review_call_center_performance_agent.py   # or on stdin
python3 adaptive_card_review_call_center_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review call center performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing call center performance from Dynamics 365 F&SCM (legal entity USMF), with a header, KPI tiles with trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-review-call-center-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_review_call_center_performance',
    "version": '3.0.2',
    "display_name": 'Review call center performance Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing call center performance from Dynamics 365 F&SCM (legal entity USMF), with a header, KPI tiles with trend arrows, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-review-call-center-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-review-call-center-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a8ea1138aefe77b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/review-call-center-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-review-call-center-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Date used for the card timestamp and reporting snapshot.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-review-call-center-performance-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical review call center performance status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-review-call-center-performance-2026-05-24-card.json' that visualizes the current state of review call center performance. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current review call center performance KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing call center performance from Dynamics 365 F&SCM (legal entity USMF), with a header, KPI tiles with trend arrows, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of call center performance for USMF as of 2026-05-24 with KPI tiles and a RAG row.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-review-call-center-performance-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and reporting snapshot.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-renderable Adaptive Card snapshot of call center performance status from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardReviewCallCenterPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReviewCallCenterPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and reporting snapshot.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-review-call-center-performance-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardReviewCallCenterPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
