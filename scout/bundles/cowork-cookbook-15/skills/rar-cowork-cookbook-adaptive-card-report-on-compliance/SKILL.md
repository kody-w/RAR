---
name: "rar-cowork-cookbook-adaptive-card-report-on-compliance"
description: "Generates a read-only Adaptive Card JSON file summarizing compliance status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_report_on_compliance", "rar_sha256": "cbfd0e109ddd8c4a6d730b01a29d7f3432d3a3178f36287e753420ce58882cd2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_report_on_compliance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_report_on_compliance_agent.py` and in the RCI capsule.

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

Report on compliance Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing compliance status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-report-on-compliance
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
      "description": "Snapshot date used in the card timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "Number of KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_report_on_compliance_agent.py` and embedded as the fenced Python below (sha256 cbfd0e109ddd8c4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_report_on_compliance_agent.py` first:

```bash
python3 adaptive_card_report_on_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_report_on_compliance_agent.py   # or on stdin
python3 adaptive_card_report_on_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on compliance Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing compliance status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-report-on-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_report_on_compliance',
    "version": '3.0.2',
    "display_name": 'Report on compliance Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing compliance status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-report-on-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-report-on-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7c76288f8405cffe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/report-on-compliance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-report-on-compliance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'Number of KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical report on compliance status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-report-on-compliance-2026-05-24-card.json' that visualizes the current state of report on compliance. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current report on compliance KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing compliance status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON of compliance status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'Number of KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a compliance-status Adaptive Card snapshot from D365 ERP to embed in Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardReportOnCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReportOnCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'Number of KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardReportOnCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
