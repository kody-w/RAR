---
name: "rar-cowork-cookbook-dashboard-identify-notification-triggers"
description: "Pulls notification-trigger data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the Cowork D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_notification_triggers", "rar_sha256": "c8887670464a0f967703be44afdbb94421e531dc1e86fa14d2b110da5d90451a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_notification_triggers`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_notification_triggers_agent.py` and in the RCI capsule.

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

Identify notification triggers Interactive HTML Dashboard — Pulls notification-trigger data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the Cowork D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-notification-triggers
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
      "description": "Name of the HTML file to generate, e.g. dashboard-identify-notification-triggers-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the saved HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_notification_triggers_agent.py` and embedded as the fenced Python below (sha256 c8887670464a0f96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_notification_triggers_agent.py` first:

```bash
python3 dashboard_identify_notification_triggers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_notification_triggers_agent.py   # or on stdin
python3 dashboard_identify_notification_triggers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify notification triggers Interactive HTML Dashboard — Pulls notification-trigger data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the Cowork D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-notification-triggers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_notification_triggers',
    "version": '3.0.3',
    "display_name": 'Identify notification triggers Interactive HTML Dashboard',
    "description": 'Pulls notification-trigger data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the Cowork D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the output folder, read-only.',
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
        "upstream_slug": 'dashboard-identify-notification-triggers',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-notification-triggers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a13de68b3cd95d39',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/identify-notification-triggers'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-identify-notification-triggers', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to generate, e.g. dashboard-identify-notification-triggers-2026-05-24.html.', 'output_folder': 'Destination folder for the saved HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of identify notification triggers with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull identify notification triggers data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-identify-notification-triggers-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing identify notification triggers.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls notification-trigger data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the Cowork D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build an interactive HTML dashboard of notification triggers for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to generate, e.g. dashboard-identify-notification-triggers-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the saved HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a shareable browser-viewable dashboard of D365 notification trigger data for viewers who have no D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardIdentifyNotificationTriggers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyNotificationTriggers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to generate, e.g. dashboard-identify-notification-triggers-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the saved HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardIdentifyNotificationTriggers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
