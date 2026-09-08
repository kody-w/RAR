---
name: "rar-cowork-cookbook-dashboard-define-security-approach"
description: "Pulls define-security-approach data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the ou"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_security_approach", "rar_sha256": "a96ee358ba2b8e903a673912687f19af0c92f8050af5154b0d83bfb97fe23132", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
