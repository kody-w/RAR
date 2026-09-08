---
name: "rar-cowork-cookbook-adaptive-card-report-an-injury-or-illness"
description: "Generates a read-only Adaptive Card JSON file summarizing injury/illness report status from Dynamics 365 F&SCM, with header, KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_report_an_injury_or_illness", "rar_sha256": "3cf97a9d7cdc6af254270533de03686691dc60ef5350f4c4b6b2be434e53f74a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
