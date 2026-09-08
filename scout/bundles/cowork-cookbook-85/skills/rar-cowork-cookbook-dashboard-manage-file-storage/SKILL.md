---
name: "rar-cowork-cookbook-dashboard-manage-file-storage"
description: "Pulls manage file storage data from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, sortable table, and RAG indicator;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_file_storage", "rar_sha256": "7889079a440a802ab487570344f459b2e644884df2aa29b9302a62858b44741c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_file_storage`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_file_storage_agent.py` and in the RCI capsule.

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

Manage file storage Interactive HTML Dashboard — Pulls manage file storage data from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, sortable table, and RAG indicator;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-file-storage
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-file-storage-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 7889079a440a802a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_file_storage_agent.py` first:

```bash
python3 dashboard_manage_file_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_file_storage_agent.py   # or on stdin
python3 dashboard_manage_file_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage file storage Interactive HTML Dashboard — Pulls manage file storage data from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, sortable table, and RAG indicator;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-file-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_file_storage',
    "version": '3.0.3',
    "display_name": 'Manage file storage Interactive HTML Dashboard',
    "description": 'Pulls manage file storage data from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, sortable table, and RAG indicator;',
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
        "upstream_slug": 'dashboard-manage-file-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-file-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07cf2c45d1981bf4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/manage-file-storage'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-manage-file-storage', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-file-storage-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage file storage with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage file storage data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-file-storage-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage file storage.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls manage file storage data from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, sortable table, and RAG indicator;', 'example_request': 'Build me an interactive HTML dashboard of manage file storage in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-file-storage-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 manage file storage data for the latest fiscal period, without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageFileStorage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageFileStorage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-file-storage-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardManageFileStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
