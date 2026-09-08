---
name: "rar-cowork-cookbook-dashboard-deploy-software-releases"
description: "Pulls deploy software releases data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_deploy_software_releases", "rar_sha256": "061418884cdec3b48a53f7247cc0c235d1c4d61144c358a674f982d7946ce523", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
