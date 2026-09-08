---
name: "rar-cowork-cookbook-adaptive-card-report-an-injury-or-illness"
description: "Generates a read-only Adaptive Card JSON file summarizing injury/illness report status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_report_an_injury_or_illness", "rar_sha256": "3cf97a9d7cdc6af254270533de03686691dc60ef5350f4c4b6b2be434e53f74a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_report_an_injury_or_illness`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_report_an_injury_or_illness_agent.py` and in the RCI capsule.

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

Report an injury or illness Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing injury/illness report status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-report-an-injury-or-illness
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
      "description": "Date used for the card timestamp and file naming.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
    "output_file_name": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-report-an-injury-or-illness-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_report_an_injury_or_illness_agent.py` and embedded as the fenced Python below (sha256 3cf97a9d7cdc6af2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_report_an_injury_or_illness_agent.py` first:

```bash
python3 adaptive_card_report_an_injury_or_illness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_report_an_injury_or_illness_agent.py   # or on stdin
python3 adaptive_card_report_an_injury_or_illness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report an injury or illness Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing injury/illness report status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-report-an-injury-or-illness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_report_an_injury_or_illness',
    "version": '3.0.2',
    "display_name": 'Report an injury or illness Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing injury/illness report status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-report-an-injury-or-illness',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-report-an-injury-or-illness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5e926264b5f46888',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/report-an-injury-or-illness'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-report-an-injury-or-illness', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file naming.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'output_file_name': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-report-an-injury-or-illness-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical report an injury or illness status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-report-an-injury-or-illness-2026-05-24-card.json' that visualizes the current state of report an injury or illness. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current report an injury or illness KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing injury/illness report status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.', 'example_request': 'Make me an Adaptive Card showing injury and illness report status for USMF as of today.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-report-an-injury-or-illness-2026-05-24-card.json.', 'name': 'output_file_name'}, {'description': 'Date used for the card timestamp and file naming.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of injury or illness reporting status pulled from Dynamics 365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardReportAnInjuryOrIllness(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReportAnInjuryOrIllness'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file naming.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-report-an-injury-or-illness-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardReportAnInjuryOrIllness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
