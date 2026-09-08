---
name: "rar-cowork-cookbook-dashboard-define-security-approach"
description: "Pulls define-security-approach data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_security_approach", "rar_sha256": "a96ee358ba2b8e903a673912687f19af0c92f8050af5154b0d83bfb97fe23132", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_security_approach`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_security_approach_agent.py` and in the RCI capsule.

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

Define security approach Interactive HTML Dashboard — Pulls define-security-approach data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-security-approach
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
      "description": "Name of the generated HTML file, e.g. dashboard-define-security-approach-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_security_approach_agent.py` and embedded as the fenced Python below (sha256 a96ee358ba2b8e90…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_security_approach_agent.py` first:

```bash
python3 dashboard_define_security_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_security_approach_agent.py   # or on stdin
python3 dashboard_define_security_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define security approach Interactive HTML Dashboard — Pulls define-security-approach data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-security-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_security_approach',
    "version": '3.0.3',
    "display_name": 'Define security approach Interactive HTML Dashboard',
    "description": 'Pulls define-security-approach data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou',
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
        "upstream_slug": 'dashboard-define-security-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-security-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '864c934e68ff92c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-security-approach'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-define-security-approach', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-define-security-approach-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define security approach with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define security approach data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-security-approach-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define security approach.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls define-security-approach data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou', 'example_request': 'Build an interactive HTML dashboard of define security approach data for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-define-security-approach-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of define security approach D365 data for someone without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineSecurityApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineSecurityApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-define-security-approach-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDefineSecurityApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
