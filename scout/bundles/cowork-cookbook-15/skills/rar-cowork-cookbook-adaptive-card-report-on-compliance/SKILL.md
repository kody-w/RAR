---
name: "rar-cowork-cookbook-adaptive-card-report-on-compliance"
description: "Generates a read-only Adaptive Card JSON file summarizing compliance status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_report_on_compliance", "rar_sha256": "cbfd0e109ddd8c4a6d730b01a29d7f3432d3a3178f36287e753420ce58882cd2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
