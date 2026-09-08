---
name: "rar-cowork-cookbook-dashboard-establish-banking-relationships"
description: "Pulls establish-banking-relationships data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) and writes a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_establish_banking_relationships", "rar_sha256": "e458c38e55ac5441c7cd334b9311356a43a79b8cc298e4c72a7fb12863f32765", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_establish_banking_relationships`. The original RAPP
agent is preserved byte-for-byte in `dashboard_establish_banking_relationships_agent.py` and in the RCI capsule.

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

Establish banking relationships Interactive HTML Dashboard — Pulls establish-banking-relationships data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) and writes a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to t

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-banking-relationships
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-establish-banking-relationships-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_establish_banking_relationships_agent.py` and embedded as the fenced Python below (sha256 e458c38e55ac5441…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_establish_banking_relationships_agent.py` first:

```bash
python3 dashboard_establish_banking_relationships_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_establish_banking_relationships_agent.py   # or on stdin
python3 dashboard_establish_banking_relationships_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish banking relationships Interactive HTML Dashboard — Pulls establish-banking-relationships data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) and writes a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to t

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-banking-relationships
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_establish_banking_relationships',
    "version": '3.0.3',
    "display_name": 'Establish banking relationships Interactive HTML Dashboard',
    "description": 'Pulls establish-banking-relationships data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) and writes a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to t',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-establish-banking-relationships',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-establish-banking-relationships',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '03b50cfb910e1e35',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/establish-banking-relationships'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-establish-banking-relationships', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-establish-banking-relationships-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of establish banking relationships with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull establish banking relationships data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-establish-banking-relationships-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing establish banking relationships.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls establish-banking-relationships data from Dynamics 365 F&SCM (legal entity USMF, most recent fiscal period) and writes a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to t', 'example_request': 'Build the establish banking relationships HTML dashboard for USMF from the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-establish-banking-relationships-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when someone needs a shareable browser-viewable dashboard of establish banking relationships from D365, without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardEstablishBankingRelationships(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardEstablishBankingRelationships'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-establish-banking-relationships-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardEstablishBankingRelationships().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWJrmX9HcjpjMbNkXJDbhjooYiV0gsQtEusLJDmIVm0DZ+d/nIN1rO6tc3VUd82munXklOOfd3+d5j+H3F7fvkqp5+fSih2654Nw8T5OwWbhlsKCqW9Vk4FeVeeC/hV+VXZN6fVc17cuHlyBs/Satu7QqwXalz/N2Ebad6+Vpm3z03DJLy/hjE+buvKRN0rpdBG7nLqKmKhb0VLpF6rcLBMcW7P/WqcPi5zyM3XwRll3aTQtTP7AfFkXVdosm9MHFRZS2Prhfh01aBb88TLw1aRe2C3cB9JaBm1dluEjLLmxcv0uHcMEbBwkobROvchuwPO2ShZ+4Tdd+mDdVzWxuuHj8/8NDorvQthyQEaS+CxxddNWiA86Go1vUedi+fPr1rx9eUvD55dPvL37utuDSC/2ugXn3f/d0X/veeyAmd8sYrK8nEPQSfAe+RFVTgEtBGC3evv3chnn0YfHv/57d3CZuf/n0uVy8/Xx+mf9ofbnoEmB25bZdGCx8t3a9NAdRe11s85s7tSBkXd+Uz8g0wJDX585vkqp68Zf53s9PJa9x2P38+aUCJjwM/vzyywJ4//ml6efPr7OU+udfXvPqFjY///JNTtt7l9DvZmHA6tcvb9/fxIKF35am0eKLrjDUmy6Q1bQOgfDv/Jt/nqa/iXsLyZfn4p+r+sPix5Jnf/4C7H1WpQfk/lgsiAHY+fJ6qdLy5zcdTTWEpVv64c+//COxfhL6GUhs90/J/fUpOAndAETrLSS/fHik76+L5ZtvX2X+Y7U1KJh/xROw/F3d10D9I9mPzP6N6DwtQTu95/KH4n60YfmXxa//0Lf/asOHRfT5hQ5z0KvN3IOfFr8/SuTXn4JvF3/66x9A9H8rRq/6xn9I+FK4ZRoBLPry5def2sfln/766099Dao4dIsvfZP/SOaP4vrQ86cIvq36+c97gX6zzMrqVi6+9tDi96r+X80fr4uTm6fBt+vtp8X3nTj/LBezE+9KnyH4rhtbYOt3cfzl5Q+AQSXwpvcftwF+/Nu/LQ6p31RtFXUL3a96AJs9QNIinI03krRdgL8zajQhiGubzrj3XAfqf87wbHEVLX77P/4D9z/6b7gPfcXPL1/h/csbvH/5E7z/9rowgIKqSeO0BEitbRXlc+nGM3gD5XUTtmEzAMDypi78CPr64/wBgO3it39ax5eHuNd6+u0B1+kTCTVKmFGw7fPwdfbXSsLyzTsf0Fo4hn4PNOXVTCBRCoD8A4hDW+WAI7o5Nm2W5vkiSAHOANSfHrJB/D7Nwn777TcPmPe5fMI2snjyXguBBV/NWXz8CPyL8jROus9l6CfV4qff//hp8Z+L/2rXQ/isQwFE8pYdYOFel48L0G19AZaBxIFUAyh5ZOf3P96iDMSUgKhBLtMoDZ+bQbVmYfAecp3fflxj+MILQahBmIsa8B0I6CLtXhdCtPhqL1A635rZIpn5NgjrsAzC0p+AVBe48zWSZdUtWpCMNpo+LPo2fGj9zWvch4kFaHu3+21xoBTATVU+k2fzxlVgc1UCTs2/FsTzOhDS/NQudu8iXhfHuT4Xtdu4ddK4bzoi95kXwEnv24Fwd1GGt8/lTMfhHKpHmTzDAxaByPhvKf045xwMMAVAhqB91/1Y484MajyYtPlctm+N4DZzKnxADEBp3KfBTA//8VZSbVL1efCIH7B0lvSWheAtK48a/DoLLN4KefHnWUj42znl6xSx+Nyv4RW6+P95ppojtOU4jeG2BkMvmKOhnZ+Zm8fM2bTnZDqbHc175i79Nui8g9k7pn8u8xSUYTP9x3PlI99va5442TcgPdpWe8gHxQYyN8t99MJc200zd5H7uXwnj9mbB1KCcgDAARprNvxd4Xz33dIEBGP+/m2QeNQOCA7wHtT7ou5BAv1FFIaB5/oZsKqZ+/ktzeUcYdDbtyT1kz95NecN1B+QvwBGpKBDAcG8fgX059130/+08TkvzVses2QP2rl5CAB2hLOBj0yD1AHzuudUD/z89BAC3CjqbvbdA2UGPH1eDJvw2qftXBwf3uIa1gDBP86/n57OV8OxBj0EggU6pe5BdB+9NZd/AaYhYAOAF1BMRVqC6QAE5S0ID4FuMQMFAOK38fUp8XH5zaHw0ZAzrb1vnB2Z9zyK7tEGbjl9jyfGj8oEyCvmFQ+9f1tpX7XNsmdMbQEuAo3vd58jxetzKniOHYt3uZ/+7tj08792snrwvPnnAvi0SLqubj9B0JOb36n5FSAa9LS1/UbTH/8bxPiTgqfvnxb/mpF/EvHWJJ8Wq1f4FZ5vSW9F9vYDYkJ93J0/ovPdz6UWfgNeoL4qgGlzBicwF3xlyfclgCrjBmAYWPxkzXYm2xvg9wdNgHR8Lr+v+rnrABqV8VylbfUdGjzGBdABz+x9ZTNwq+yA7mAeN+PwdT6lzea34cunEgDwhxcAquG/csibqauYa7ydz4igmwC6dmn4+PaAjLGbP/75/Cw/Prj564IOATzl7fd1+EY4M+F+1y5Pb4GXPtDwYeYBgAKgRIG3s/K51dwW1C4o29mrbqpnN57nwXmCfGL/lyf2/71F7PfU8KDyx5QAkOg/QAtHbp+DYM5QDkz5nlLcAZg/d+MPlT746MuTj/5eJz0z158oCyi49uGM69/rnInsh+K/jsx/L9sCs8m8N6g+zTT94Q3nwG9wzPmw+HpiAZF8O0POGsKyB8fzX+fT0pzax5b5A9gDfn3d9PXfQ7zw5a8/susBhl/mQnyW099ad5xBDpDAHM0Hwz5qFpj7oOMPi/A1fl380y3+cQ2v8Y8w9nGNviZdkf84Vm82VTkghx/kIpxh+3mSea75CoDf+nc29c04uvKf8yr0RA7oKR/6gW6g/EEmgJLn2H5L2rfQVY9T52wmCHX3/EeS319AW7nzvPPWWG/HFrAcYO/Hdh7OIABCQCH4/oQLcO9/fqB5E9QmLpijgaQQxTY+sgkxzPUxFF35hB8gCOqRyGqFYLiLIi5BehvfX5ObEPWJtUtE3mq9wZEIWRM4BuQ90efLPIqms3GzZXP6AICF326DS8GbV08v5pB9PT/N3r859/uLh6NgJY+2wvb5Q0HkyoMswtMaD7LhzZiPwVn3Wj3XXW/n4lNvJemezLaGNZxdLWRP623lp/pYX+I2IfSLO17OCRmXCBViA3IsllQp+p10jC7azUULX7aVIlIIufD4iywcbXkIbd9VkXOflacVN7F1cYCMUU8DjLlqzpCtxiKqd/xqJW3waE14G71u7oGEWWGyVLoImjw5vVwstXaYuvaEjoEzkj9GDS2uWDckxiPJxZqjQMPOHBTiOPoZcTg3+bpasoYiVAhaDhKJk2WVdvAlO1PRTm0oIUB5+NrCKXteMiUop32Vj1dU7dsC1ZbNTqirFL+cfbsyHG3QJHpsV6Pi7iUxZeF6qWyMuk+lzRgMKiUfthfSLvz0NG1Dml1DYQkUbpYSeV0pI94NCHZf4uiw4tJsl4gGXbBQzjm+AaeF0wopTCmQZZvmXdlQCI9S0inUPZLQKTmvi4hwcCd2WwEn24Rjt0zo8HuGmfwDkkF6YXCOqPisRd6ZAz6l0nmzVup9J0hbV4/sQ3dQ2yo5+YLtnKXav3S4FXFoTCnX0Olrd1+iur4Tu7igbpsbF7LkLhBYR0+yFuq3e6XiaLPAdtnKbHxP3McwWSm4PniMBe92V8Ef1qge3HeoQbR3Ar6GFinf/FoTi5S+rEzV1PX4XsaotZd4blnZ1K7EQ4fkJoHq3cMNuQ3w6r4eVL2rzK6o/Cm7b+xMd6WCTbCp1HGEQerjeqnx7VW5quNEMdkpPNXbq7w8NYg8kTgcMZdNmtNU7DkaE+7uN6IuzgNqc5ARcxi506o4OplEe6LOznobj/syMzYwkq4PkoMpZLHPx9ykKnc9Vjp+ilnXGputjnjdNb/u9UOg+Veb1QputbmuLE1zhInFBQpCK/1a33133594l7WX9TWNIAZnJDy1Yxq6CscdszF7WBE89nITu+MFVqZlE3HYWtYwwFl3y98a2/ug0IG2dpLLqd00SJ0FlIrJy3UU+NHuKhlqY/FLLxWhUFvekmFoWM6JyB2fRkZ+J+UIXdoxImP5sJ1K9EbpeNv1lMQSvjbtEV3VrKJ3lqZ6Xy2Hw0at6YPD64xI4CrWx0Fwzo/qzd1XqKz5lNEIRUHqVzSSYd7YI9VdO+u1WNlcutFLoeX1/cax2gqG2ZYvkxAP1+Eew6X1je1uHb/bdV56FyxjaWW4YzvFWmLuh3ADhNgh3WzWVH21uOt1heYnd+OO1rB3rKR2Ae74WngT90paRAnGymcEKnO9I6NErEWmuvje4Db3osvZdo1lOAEZOi0toxLK6wvZmyq27c9ISxhi79xkZxJQT1InCiADmrpbmzAO43GLn47nabU5XLwV3p8FrT7GjBIeO29tnm+hJBEgPBJe8KcODTEZ2Us7uJdY5VznU+Mxkee2U10oOLahMiIssywM+1vLxafJr2R575Rm2U696x0lvQFte9I1TYirYHfH1v0EBaW+WrExfxRHFSK9kj1h98SMvJ0E3+J0WfDL7brnTMu57voIOexoZnPGQy5d1alF0ulw3AvrPAtkj6aCbQ3RIrZdV2SqIkdH41khNHiGKCW7T1eEso8RrxjbSqiuoYIuxaWeRUXEhSNHcqXjh14MNYPBXvoSvlDTVGy9kNm4XgY3WEhX/epiDDePI/NNM47GBksgvYdvSVBuJzcek6tLyd0hgeBBCUSUvNu0t6VEpzdlfeQFlJCEszT1Zmntoys1OJOf7n2ISm+pljTJLVV3CqTunEvKHfeUTJn6jupKFWlWJDHWB1fkTHLL0xeB4taxmOqaTzMhoRmiT4dpU3VS2BonUbDPuihSnK6jRdvutwxA+K5vyRgxs7NOHKgKZIy4hKKZNz0x1YifrJn0JMCmcr1Vkbo6pUur4aYjLIXrzCLX8EXk1sbemsZyV3UZ4sFkGNnDOMV6c+K4iKK5SMNOFaZgfO5eOr4ywzOumodp4Ps7WSfSkkiSNVzdWmclHsoJD5W4s6eIwPC9tNQNMA70hGiUVG1tNpMin1o1TrpMXzFbRLqvzxNcj4zbnDTV9D3Uuw/RxVdvq1Pk1bHeH8LoXm20ZXHBMJm/L3MmaNNxdelgFXUd9oj6vkFPY7zU1Cky4xvCnUU9cfxa5DVh8k/MCDCgvpwxaQcYc2uvLpXkMvVFPQpb5Y7iGLGRMuGYWifcVVD7BmkkT0T7UL/czckK7dvVIQf8aIYitlE1eCerawMXY2nD7ffXbZFI3hmcQnxVNfNyilpStsdulx/FzbCDdZ2mRGHPEjptbK3zbUkfBwQMIL3QowmjsbayiXiXGrej65mxEuVnP8DUU18flqug0MOa2XKHacXyHn+KfCciYnG/7fv9KpfzDdfS1eUYQbZIZwc95k1/qVvjWTBVCqF8M5dCv3CWUun0SinUDsaZjcXY2ZaSM++2W/P27cCnhJ+SVZut2QQ/8AV73DvcQaUn7YQzmSbemaQ8joy1rYRzfIZrw4KbyGONA6xe5TQ2272KFQkYReCyqiFnUpFaog7h4AEOEq8xvcHXWc2lgu1xN71ZGuwkd4HGKCexiHwr2l8tShMC2j/TzA6+l8ejZCXX5Ob0TMBZd1bf1Iw/4Id8G8W3zG8PBKu5I8R6eTOaKXFtWxXhmVy4pXhc3sWUYv3U3NB3swV8pl297Z690ZhQcJpxRpo20pWkieFtZ7JQUEOWSTCxIlyOhXWo4ZsVBMFF6EGL57a5WvlXhFkNTjrG99tduUtOsDGlM7mjKJvNJX4N+ycqb7v9Bq9uujkI/f00hfYlKXtpj+0m3b6YmBWP3HWIwxuOHVH2ElwrmPVOB6bI8FynBMmEKmZjB26e5Y3bsmDxVhy11jwaU4zuC+JGnCm8cnYDzoW7hPOCFq9c+1Cc4Vskt5lHlJFrHfgVBR/NAoRYrZXtTWULweLUKcQla29RG2yvXYd7u2QorTnLl6zbkcZAU/strHYyKd3dkltPJwlmt9tU3DdUWzC1UVwg/byOFT5XmqKmxmRoCwIUq5GfVO9Qql4kBlx0G5fwbhjgIXNVx5WyQO1l9SoUO2UTs3q1GW3pbmd4n0b3sWSXuW51alf21L7OV5SwYwoQBfVkroKR83pzfynRwluuXF/LQrKRg9U9WzZMY8RrweMddCuq4mlLCGpu0lOv3reSuuWZdYW1p6WwPbb0Ac+utpLjU3f0C25pnJCm8K4WW4Jhmtfr7eWEMaG9P6CVraQUh7WiaXhtnymrxmcC3fH2vhF0Gy03nI6t8mOW3OwiMWpf8qb9gSUcZikeBfViberNgSJdzuobr9wCXO9HKqD6orMVOiGNadhskA7J1tBlda2udGFzETNclwPTnh3MYnPTowEFgfklO1BYThzFSPetoqQjDgY4v9bcqz/c3cttCCE6NJmdtQ3TkfQZ1mOkM85whgqP8TkXJSnQtUFnmknfy+wNVTaiIFNFYhamNqBq4VDehsNVhgv942CI7DaROIBzbNaEnEtDsKSIyKFt7d2QFCfI26tLSRmUy57khd5NyXJthkcSnL8oYBFiFXI49MGmCetadU02RtF4AmckiRrGeI03SUUaK2o7XMt7SJyIk00bkHdBzwVveWa0KYWGrcjWPhMehXFKVp9bi/O6ZG/LVqUcs5DrXAqerkZo7i2HJvKRBjMpbuqHHDDMIT7KjFIcb5kwDozjQwrNkV12G8FQt2NPeiWj+UbbeaAzjmMLW6VYKobuy6D+d+uuA8OOjW23+8vJ0oxrw9NB2cpigEN5aaJtxmtsuymsfMeAqVUSqZ1LeClmEEMa1n7jAYuJlejkbHk+KZrgbyidBKk7n9KV3Ya6BYcZtIPPO/VurA55vLrHl93RnnRQrvzmZgdjtzyIF4e95alW4ZubpMh7P1SDarr3d7FL9xt1D0+cakg7Z1s6hTL55uR32ppd01qhaze0DHQksQy5xFZDO8ZwvO7o4JQRnpRle9zut/WVTe1xvazps0OuugQk2m+v/Pp4yhsZS1kDYHcvoPBRU6ALdi9Tuj/dtIplnST0Y4FOKYyST6e6cgMlIU8NlbO0iWk2H5ZJQ6AXI2QiCUi94GJ93NU56dEnXugs3vCEgMsJLdkzAuWZcFckLtSIB2bfUX0qj/TGOTv6rYpPp14kelMheEHcT73hxXg+DCW6u+uFi4siICl74+/kGhxSqE6+VUG6305Eaa7chjdC9XiTGgSys8EIgmgrFkbKCvQZjzOl0NLwqrVdO2XsIVEScd0RW1qd+Dgnik5FRanq/ftFS7b3MxKP5kFhKW09xKTY7HbuFmmWHETrZ19Aluz5tLEnbLPdgbGkJwEZWVtcI4U1d9oZHp/KVJW5/PVMmA5yO1khLaGr673uXS44Helj7/i7G58wU+Sw+xUn37D+elH0+5UU60jRkc4ThLWlEUpwsG/nZKPsKtsTPLdzzBrHT1l3WF83hIZ7x4xEJLLt2GDtNa6k3tuI62UUkgyiMSq2K43uROBZqQrePjWM3oA0jskKyyomGXESjmBX4jJgWY/MyMMNtch2NZTRlakQ4jjVo7HEzkXjoOvrkqSQ236zv6BHcKZ0YI2Waxrdq565YlYOtz1zMHTLNVT3eBJhMY5HO2IXrSFh4IPbKnE2COTsjkmOigSfhVMdtHG5wk7XfiS8gs9tDYOpGxxcutHWDWFXa7gx3niXgCAcGZYCvz+lfpb2TgNtNAWFt94gK4TFRkh0cayLT8lu2eg9XgXGbiLY2DxvCVqP6viSEmgGXy83uYQHL5PiMZbrM3zwtYjWpi1WX+hM5mSb3BfyeF3VsN8cSnlZr9mbfFhv+PIcdndOBZlshwkpaNnHkXGfYLc7ry0tOR1FpHYRX98sRZmm9KN5HsiGPAbB0jKze8KCkTemLveuaQv1El75vbCyOY/e+QgHhl55SXiud7qG94KPWM2XQ2UMT5fhnGvLjtd1Dmp44nDMb1BttZkAx1zNxKGi3GXODnJnc0ZGRk3a63oFRjIt96/TuV22AbdeDcfYvia5fW1pnbvr6zPsrsn10Vpqa8v3L1tjc29776AOo2yLcChYy0nITYOtUmvkdtM5ypyytzhN1+iK8xW4unQ2AiCvs9WLvym2V12u/YPqW6djfBDu6r7Brt4uJlCr67VE5LvmEMl8p4JzHyYgY60bCKRDfAWHCt/0vUtjmp9fk/5u5gerx44Hul6HVXK6+yNN9846ZBPYONuYd68BSekEfpTlAdHCHa8vxzEY7warqkhon1O2305DWcls6lz1u0Xrx7Zp6k4I4PZGFyvVlchY0s8d6e/WaweRvIJ2hiqnJBmXqvvtiK9uXjdqqyTYGag/2KDg68lYFtWq3NyPIoqc9msw2/X5gSNN3jhazFjnRrE8uUfFwkK2F3nh7NabrX9JMS/JcZKg+fsh3mkX82DXy/DI+wdq2oHT7Uo3L1SVohAfp6LSpsu6Y9qr0hXVJJJ3ii9olzTh0ePHwRr6lCAmd9VMRBAuN5tYBGeLlA89FOr8HlNXYSAUTkiQ6xJDDoybMyPTH4hO9hgyyeiO8MIr0sXoELMumDHs0/aSTUTKkCPcQzrayoF8qvW4Y5dXF0XrdnvenE6N1egYwRGDfR3OFy22bS6OYsZBeLIeSWOsbeTe2ysVSq/KPry7frnUxF3OFFeNU0ndrZCG9+/eJRO0wlwePaVXR54dxk3fboV1F6jJ0jqbWtAgzODSPu/VHFWZ6G0TJ2cUj0Y2vu63FyRQYx9XJOIuNn7Hw5SAopmCtim6ljhneSqWqLH2VxxqwYFEH4w8hPferjCWp4Bg7SEPi42CqFrVlLQ8OiyjH+HDJKMWxFJRp0cccfUvBzCeRCIPo2QFres4ugBwvVObux6T1rrz+pNy3Xd1uMv5VaOxaRRrcY106Moz+/wiW13uOV0jjiuo3p9rTz2smivvAJCY1szdva2uRTuiiOTfDtLFcMjrwZwgdA3wCx+5VRVeobtONOc1iEW8dnhBB+Pb3ds1hLMNaE8cHWk5HBiT4SV1tb/ZWXMTxYI29nCCSee+o26JIhwR+lIct5BWYBLTWCR0RbZEteoOpBm6JjcAQnSgi0WYG+yIk+5260GYAOqsO+9grUhpa0uyRBEzmzNnaLJ0JoZoaW8KE4VxBppwisgkN/G7FiXJxgtssb5zZQT56VAmHj6ZW1dp8CbviwAnJ2weGsLqmCIB15KXa76bEJdLtI5LrjfNVvHuukEwnVCILk3J9AArxt5r+EbfkO3aSW75UgOO3S6aWhzuDk43iDdilY8g653k47xwCDOaFqTIvzDb0pJ1ncKaEoNUcasSPieBifTYI8V9fysuJ2FpL4V7vcUilAAzidytB5UnGTmpuiS98q1V7gLzIkLTlA71EgX+dBJRntgwuIPJQ4MMu8+O430fQC3vN+KgDbSUkDR+RG7n47iZwAEURsPA6gmMuiboFVB/1Xl5hNm7DiHRQ6BZ9JIvCWs0GtntVHHY3Xsp7E89Sjb+HYZHaYygg7pq0o3fMsrQeVAQFzRi3/keDC3Kqdc6qN700CE8SzyigyIK3b2aieoREWuEc89UFVMZeWJCgwOnPpkeMX9F2xdbba1DufVJWFgWMO/FkrrTVF8xNhWvcupdhkJdRnWJ7C+r49rzGJfoEcgcVtWRoiH+qIRHuSNSG+u5zI+XeXw/hcQK5UjcPiSwjo4ebF5TsShV9igbmk8cgVpgJzQSo2vS/Y0tfChGveV1f9SqsrRceywxWebLS34OJ+vm7l0CzOtrgH/QjUePjshn2WG73f7lLy/zY9T3Z3ov//pbbPMjn/9nT5eeD4ne30F5PLUM3eDTQ9en/4Ftf/3w0vgpsOz5TK3N+/jtodTfPFH7+E8/mJzFTM9Xxd6fhD8fsnduPL9c/ZKWQd92zfSlrfLHOylgh9e382uY7fymrg9+f/8g9qvm+Vnd44H4l6768nxU/TK/JTm/axIGqduFb1/jt2eNYO/b+1JfEBz7Ejb17PDbywzAT+QVfkVe/vi/ekTJLCMvAAA= -->
