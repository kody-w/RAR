---
name: "rar-cowork-cookbook-dashboard-deploy-software-releases"
description: "Pulls deploy software releases data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_deploy_software_releases", "rar_sha256": "061418884cdec3b48a53f7247cc0c235d1c4d61144c358a674f982d7946ce523", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_deploy_software_releases`. The original RAPP
agent is preserved byte-for-byte in `dashboard_deploy_software_releases_agent.py` and in the RCI capsule.

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

Deploy software releases Interactive HTML Dashboard — Pulls deploy software releases data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-deploy-software-releases
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
      "description": "Name of the HTML file to write, e.g. dashboard-deploy-software-releases-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the generated HTML file is saved (Documents/Cowork/output).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_deploy_software_releases_agent.py` and embedded as the fenced Python below (sha256 061418884cdec3b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_deploy_software_releases_agent.py` first:

```bash
python3 dashboard_deploy_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_deploy_software_releases_agent.py   # or on stdin
python3 dashboard_deploy_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deploy software releases Interactive HTML Dashboard — Pulls deploy software releases data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-deploy-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_deploy_software_releases',
    "version": '3.0.3',
    "display_name": 'Deploy software releases Interactive HTML Dashboard',
    "description": 'Pulls deploy software releases data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.',
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
        "upstream_slug": 'dashboard-deploy-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-deploy-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '99dbcb0fc75bab2e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/deploy-software-releases'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-deploy-software-releases', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-deploy-software-releases-2026-05-24.html.', 'output_folder': 'Folder where the generated HTML file is saved (Documents/Cowork/output).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of deploy software releases with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull deploy software releases data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-deploy-software-releases-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing deploy software releases.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls deploy software releases data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build me an interactive HTML dashboard of deploy software releases from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-deploy-software-releases-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the generated HTML file is saved (Documents/Cowork/output).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of deploy software releases from D365 without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDeploySoftwareReleases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDeploySoftwareReleases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-deploy-software-releases-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the generated HTML file is saved (Documents/Cowork/output).', 'type': 'string'}},
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
    print(DashboardDeploySoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
