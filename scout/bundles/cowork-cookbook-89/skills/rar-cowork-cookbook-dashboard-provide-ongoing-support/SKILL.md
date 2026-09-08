---
name: "rar-cowork-cookbook-dashboard-provide-ongoing-support"
description: "Pulls ongoing-support data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with totals header, inline SVG charts, sortable table, and RAG in"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_provide_ongoing_support", "rar_sha256": "343c5294411bf0782891553b577348bcfdafdca99f153ed30bf51906b50a5ec9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
