---
name: "rar-cowork-cookbook-dashboard-revoke-users-access-to-systems"
description: "Pulls revoke-users-access-to-systems data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_revoke_users_access_to_systems", "rar_sha256": "2ae471e3c53a58e7cd4912f76822f6b2798685f108b09d0b3664c4b668fc8098", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_revoke_users_access_to_systems`. The original RAPP
agent is preserved byte-for-byte in `dashboard_revoke_users_access_to_systems_agent.py` and in the RCI capsule.

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

Revoke users access to systems Interactive HTML Dashboard — Pulls revoke-users-access-to-systems data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revoke-users-access-to-systems
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
      "description": "Name of the HTML file to write, e.g. dashboard-revoke-users-access-to-systems-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the HTML file, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_revoke_users_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 2ae471e3c53a58e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_revoke_users_access_to_systems_agent.py` first:

```bash
python3 dashboard_revoke_users_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_revoke_users_access_to_systems_agent.py   # or on stdin
python3 dashboard_revoke_users_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revoke users access to systems Interactive HTML Dashboard — Pulls revoke-users-access-to-systems data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revoke-users-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_revoke_users_access_to_systems',
    "version": '3.0.3',
    "display_name": 'Revoke users access to systems Interactive HTML Dashboard',
    "description": 'Pulls revoke-users-access-to-systems data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out',
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
        "upstream_slug": 'dashboard-revoke-users-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-revoke-users-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87addd9123830d52',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/revoke-users-access-to-systems'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-revoke-users-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-revoke-users-access-to-systems-2026-05-24.html.', 'output_folder': 'Destination folder for the HTML file, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of revoke users access to systems with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull revoke users access to systems data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-revoke-users-access-to-systems-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing revoke users access to systems.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls revoke-users-access-to-systems data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out', 'example_request': 'Build an interactive HTML dashboard of revoke users access to systems for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-revoke-users-access-to-systems-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the HTML file, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable dashboard of revoke users access to systems D365 data that viewers can open without D365 access. Read-only.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardRevokeUsersAccessToSystems(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRevokeUsersAccessToSystems'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-revoke-users-access-to-systems-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the HTML file, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardRevokeUsersAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
