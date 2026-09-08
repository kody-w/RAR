---
name: "rar-cowork-cookbook-adaptive-card-audit-financial-results"
description: "Generates a read-only Adaptive Card JSON file summarizing audit financial results for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_audit_financial_results", "rar_sha256": "52968585e7d1c262a565b251528550ebdfed45f33dfb2296e66c7a08fb6d73c5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_audit_financial_results`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_audit_financial_results_agent.py` and in the RCI capsule.

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

Audit financial results Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing audit financial results for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-audit-financial-results
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-audit-financial-results-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_audit_financial_results_agent.py` and embedded as the fenced Python below (sha256 52968585e7d1c262…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_audit_financial_results_agent.py` first:

```bash
python3 adaptive_card_audit_financial_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_audit_financial_results_agent.py   # or on stdin
python3 adaptive_card_audit_financial_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial results Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing audit financial results for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-audit-financial-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_audit_financial_results',
    "version": '3.0.2',
    "display_name": 'Audit financial results Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing audit financial results for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.',
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
        "upstream_slug": 'adaptive-card-audit-financial-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-audit-financial-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c3e5940f543e4195',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-results'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-audit-financial-results', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-audit-financial-results-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical audit financial results status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-audit-financial-results-2026-05-24-card.json' that visualizes the current state of audit financial results. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current audit financial results KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing audit financial results for a Dynamics 365 F&SCM legal entity, with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.', 'example_request': 'Make an Adaptive Card JSON of audit financial results status for USMF I can drop into Teams.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-audit-financial-results-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of audit financial results status from D365 ERP to embed in a dashboard, email, or Teams message.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardAuditFinancialResults(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAuditFinancialResults'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-audit-financial-results-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardAuditFinancialResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
