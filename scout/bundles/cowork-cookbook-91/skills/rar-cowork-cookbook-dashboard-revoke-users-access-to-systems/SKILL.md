---
name: "rar-cowork-cookbook-dashboard-revoke-users-access-to-systems"
description: "Pulls revoke-users-access-to-systems data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the out"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_revoke_users_access_to_systems", "rar_sha256": "2ae471e3c53a58e7cd4912f76822f6b2798685f108b09d0b3664c4b668fc8098", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
