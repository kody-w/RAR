---
name: "rar-cowork-cookbook-dashboard-mitigate-and-update-the-disaster-recovery-plan"
description: "Pulls disaster recovery plan data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) read-only and saves a standalone interactive HTML dashboard with totals, inline SVG charts, sortable table, and RAG"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_mitigate_and_update_the_disaster_recovery_plan", "rar_sha256": "536a25daf5b3be184ee645188848232a96a1840b96f9231b27903526c6fa5fe7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
