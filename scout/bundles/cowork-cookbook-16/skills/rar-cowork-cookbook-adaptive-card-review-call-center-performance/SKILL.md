---
name: "rar-cowork-cookbook-adaptive-card-review-call-center-performance"
description: "Generates a read-only Adaptive Card JSON file summarizing call center performance from Dynamics 365 F&SCM (legal entity USMF), with a header, KPI tiles with trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_review_call_center_performance", "rar_sha256": "da80ba96ea7c8cbeb1234b8dcc82d97359c7ecc16f136b239c3413afcc22623f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
