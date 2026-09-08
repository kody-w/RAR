---
name: "rar-cowork-cookbook-dashboard-provide-ongoing-support"
description: "Pulls ongoing-support data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, and RAG in"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_provide_ongoing_support", "rar_sha256": "343c5294411bf0782891553b577348bcfdafdca99f153ed30bf51906b50a5ec9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_provide_ongoing_support`. The original RAPP
agent is preserved byte-for-byte in `dashboard_provide_ongoing_support_agent.py` and in the RCI capsule.

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

Provide ongoing support Interactive HTML Dashboard — Pulls ongoing-support data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, and RAG in

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-provide-ongoing-support
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
      "description": "Reporting period; defaults to the most recent fiscal period available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query; the recipe uses USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-provide-ongoing-support-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the file, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_provide_ongoing_support_agent.py` and embedded as the fenced Python below (sha256 343c5294411bf078…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_provide_ongoing_support_agent.py` first:

```bash
python3 dashboard_provide_ongoing_support_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_provide_ongoing_support_agent.py   # or on stdin
python3 dashboard_provide_ongoing_support_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Provide ongoing support Interactive HTML Dashboard — Pulls ongoing-support data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, and RAG in

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-provide-ongoing-support
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_provide_ongoing_support',
    "version": '3.0.3',
    "display_name": 'Provide ongoing support Interactive HTML Dashboard',
    "description": 'Pulls ongoing-support data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, and RAG in',
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
        "upstream_slug": 'dashboard-provide-ongoing-support',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-provide-ongoing-support',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2367ad8797b43292',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/provide-ongoing-support'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-provide-ongoing-support', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query; the recipe uses USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-provide-ongoing-support-2026-05-24.html.', 'output_folder': 'Destination folder for the file, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of provide ongoing support with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull provide ongoing support data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-provide-ongoing-support-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing provide ongoing support.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls ongoing-support data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, and RAG in', 'example_request': 'Build me an interactive HTML dashboard for ongoing support from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-provide-ongoing-support-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the file, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable ongoing-support dashboard from D365 ERP data that recipients can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardProvideOngoingSupport(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardProvideOngoingSupport'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-provide-ongoing-support-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the file, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardProvideOngoingSupport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
