---
name: "rar-cowork-cookbook-dashboard-identify-notification-triggers"
description: "Pulls notification-trigger data from Dynamics 365 F&SCM for a given legal entity and fiscal period via the Cowork D365 ERP plugin, and saves a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_notification_triggers", "rar_sha256": "c8887670464a0f967703be44afdbb94421e531dc1e86fa14d2b110da5d90451a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
