---
name: "rar-cowork-cookbook-dashboard-mitigate-and-update-the-disaster-recovery-plan"
description: "Pulls disaster recovery plan data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals, inline SVG charts, sortable table, and RAG"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_mitigate_and_update_the_disaster_recovery_plan", "rar_sha256": "536a25daf5b3be184ee645188848232a96a1840b96f9231b27903526c6fa5fe7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_mitigate_and_update_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Mitigate and update the disaster recovery plan Interactive HTML Dashboard — Pulls disaster recovery plan data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals, inline SVG charts, sortable table, and RAG

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-mitigate-and-update-the-disaster-recovery-plan
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "fiscal_period": {
      "description": "Fiscal period to report on; defaults to the most recent available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-mitigate-and-update-the-disaster-recovery-plan-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 536a25daf5b3be18…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py` first:

```bash
python3 dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py   # or on stdin
python3 dashboard_mitigate_and_update_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Mitigate and update the disaster recovery plan Interactive HTML Dashboard — Pulls disaster recovery plan data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals, inline SVG charts, sortable table, and RAG

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-mitigate-and-update-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_mitigate_and_update_the_disaster_recovery_plan',
    "version": '3.0.3',
    "display_name": 'Mitigate and update the disaster recovery plan Interactive HTML Dashboard',
    "description": 'Pulls disaster recovery plan data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals, inline SVG charts, sortable table, and RAG',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-mitigate-and-update-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-mitigate-and-update-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'daafed20a47694a1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/mitigate-and-update-the-disaster-recovery-plan'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-mitigate-and-update-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-mitigate-and-update-the-disaster-recovery-plan-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of mitigate and update the disaster recovery plan with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull mitigate and update the disaster recovery plan data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-mitigate-and-update-the-disaster-recovery-plan-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing mitigate and update the disaster recovery plan.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls disaster recovery plan data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals, inline SVG charts, sortable table, and RAG', 'example_request': 'Build the disaster recovery plan dashboard from D365 USMF for the latest fiscal period as an HTML file.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-mitigate-and-update-the-disaster-recovery-plan-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable dashboard of D365 disaster recovery plan data that recipients can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMitigateAndUpdateTheDisasterRecoveryPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMitigateAndUpdateTheDisasterRecoveryPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-mitigate-and-update-the-disaster-recovery-plan-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardMitigateAndUpdateTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
