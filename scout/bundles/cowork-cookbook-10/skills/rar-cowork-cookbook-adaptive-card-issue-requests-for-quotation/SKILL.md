---
name: "rar-cowork-cookbook-adaptive-card-issue-requests-for-quotation"
description: "Generates a read-only Adaptive Card JSON file summarizing issue requests for quotation status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_issue_requests_for_quotation", "rar_sha256": "42d3b0b1942859eebdda12f8158bf17468226d2998e04ecd7f855cddb4280e66", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
