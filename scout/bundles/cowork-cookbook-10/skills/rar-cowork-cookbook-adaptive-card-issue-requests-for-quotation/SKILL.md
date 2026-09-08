---
name: "rar-cowork-cookbook-adaptive-card-issue-requests-for-quotation"
description: "Generates a read-only Adaptive Card JSON file summarizing issue requests for quotation status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_issue_requests_for_quotation", "rar_sha256": "42d3b0b1942859eebdda12f8158bf17468226d2998e04ecd7f855cddb4280e66", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_issue_requests_for_quotation`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_issue_requests_for_quotation_agent.py` and in the RCI capsule.

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

Issue requests for quotation Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing issue requests for quotation status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-issue-requests-for-quotation
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
      "description": "Date used for the card timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-issue-requests-for-quotation-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_issue_requests_for_quotation_agent.py` and embedded as the fenced Python below (sha256 42d3b0b1942859ee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_issue_requests_for_quotation_agent.py` first:

```bash
python3 adaptive_card_issue_requests_for_quotation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_issue_requests_for_quotation_agent.py   # or on stdin
python3 adaptive_card_issue_requests_for_quotation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for quotation Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing issue requests for quotation status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-issue-requests-for-quotation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_issue_requests_for_quotation',
    "version": '3.0.2',
    "display_name": 'Issue requests for quotation Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing issue requests for quotation status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-issue-requests-for-quotation',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-issue-requests-for-quotation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6cf265e2c33fa1eb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-quotation'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-issue-requests-for-quotation', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-issue-requests-for-quotation-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical issue requests for quotation status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-issue-requests-for-quotation-2026-05-24-card.json' that visualizes the current state of issue requests for quotation. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current issue requests for quotation KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing issue requests for quotation status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of issue requests for quotation status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-issue-requests-for-quotation-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of issue requests for quotation status to embed in Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardIssueRequestsForQuotation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIssueRequestsForQuotation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-issue-requests-for-quotation-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardIssueRequestsForQuotation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
