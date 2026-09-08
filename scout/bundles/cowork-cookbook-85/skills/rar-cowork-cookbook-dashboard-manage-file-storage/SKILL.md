---
name: "rar-cowork-cookbook-dashboard-manage-file-storage"
description: "Pulls manage file storage data from Dynamics 365 F&SCM (via the Cowork D365 ERP plugin) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, sortable table, and RAG indicator;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_file_storage", "rar_sha256": "7889079a440a802ab487570344f459b2e644884df2aa29b9302a62858b44741c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
