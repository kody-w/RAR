---
name: "rar-cowork-cookbook-dashboard-manage-product-compliance"
description: "Pulls product compliance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_product_compliance", "rar_sha256": "085d90ca9270deb96a62cb273cab077170222bd368da03c78cf9bf6195e28122", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_product_compliance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_product_compliance_agent.py` and in the RCI capsule.

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

Manage product compliance Interactive HTML Dashboard — Pulls product compliance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-product-compliance
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-product-compliance-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_product_compliance_agent.py` and embedded as the fenced Python below (sha256 085d90ca9270deb9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_product_compliance_agent.py` first:

```bash
python3 dashboard_manage_product_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_product_compliance_agent.py   # or on stdin
python3 dashboard_manage_product_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage product compliance Interactive HTML Dashboard — Pulls product compliance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-product-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_product_compliance',
    "version": '3.0.3',
    "display_name": 'Manage product compliance Interactive HTML Dashboard',
    "description": 'Pulls product compliance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder; read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-product-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-product-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37c40a13dc2a8fdf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-product-compliance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-manage-product-compliance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-product-compliance-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage product compliance with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage product compliance data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-product-compliance-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage product compliance.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls product compliance data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the Cowork output folder; read-only.', 'example_request': 'Build me an interactive HTML product compliance dashboard from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-product-compliance-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable product compliance dashboard from D365 ERP data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageProductCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageProductCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-product-compliance-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardManageProductCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPaWLLmX2HeGzFVdbFfhHa5oyMGtIAQQjsg2h0u7fsuoaVu//c5AmxXdbvvdE/Mp8F2gKRzcs8nM33025vVtWFRv3160zwrX+ysNI1Cr15Yubugi76oE/BVJDb4t3CKvK0ju2uLunn78OZ6jVNHZRsVOdgud2naLMq6cDunBUuzMo2s3PEWrtVaC78usgUz5lYWOc0CwbEF9z81Wlz8nHqBlS68vI3acWFoIvfLwi/qRRt6i6xo2kXtOeDhwo8aB6wrvToq3IdwfR21XrOwFk0LLq20yL1FlLdebTltdPcWe108At5NaBdW7QICqbdoiwfhl15F15YdIF2krlf/CXCy3I9Fno7vQDdvsIACXvP26S9//fAWgd9vn357c1KrAbfemK9kRSu3Ak9+Kk1/0xkQSK08ACvLEVg3B9dAcqBXBm65nr94Xf3ceKn/YfGf/5n0Vh00v3z6nC9en89v8x+1yx8St4XVtJ67cKzSsqMU2Op9sUl7a2yA2G1X509D1FEevD93fqdUlIs/z89+fjJ5D7z2589vBRDBml33+e2XBTD457e6m3+/z1TKn395T4veq3/+5TudprNjD7gWEANSv395Xb/IgoXfl0b+4osms/SLF/BhVHqA+O/0mz9P0V/kXib58lz8c1F+WPyY8qzPn4G8z/CzAd0fkwU2ADvf3uMiyn9+8aiLu5fPHvr5l39G1gk9J0mjpv2X6P7lSTgEsQOs9TLJLx8e7vvrYvnS7RvNf862BAHz72gCln9l981Q/4z2w7N/RzqNcpA9X335Q3I/2rD88+Iv/1S3/27Dh4X/+Y3xUpCatWWn3qfFb48Q+ctP7vebP/31b4D0/5GMVnS186DwJbPyyPea9suXv/zUPG7/9Ne//NSVIIo9K/vS1emPaP7Irg8+f7Dga9XPf9wL+Bt5khd9vviWQ4vfivJ/1H97X5ytNHK/328+LX6fifNnuZiV+Mr0aYLfZWMDZP2dHX95+xtAnxxoA/Blfgzw4z/+YyFGTl00hd8uNAeg2AI4uI0ybxZeD6NmAf7OqFF7wK5NBAz7Wgfif/bwLHHhL379X84DCD86L4BffYPL2a4A2L684PzLdzj/9X2hA9JFHQVRDhBZ3cjy53ktAOloxn+v8eo7gCp7bL2PIKM/zj8AMi9+/Reof3kQei/HXx8YHz3RT6X5GfmaLvXeZx0voZe/NHJAzfIGz+kAj7SYS8QM9M0HoHtTpKAMtLM9miRK04UbAWwBtWt80AY2+zQT+/XXX20g2Of8CdXI4lnUmhVY8E2cxcePQDM/jYKw/Zx7Tlgsfvrtbz8t/mvx3+16EJ95yKBsvDwCJDxo0mkBMqzLwDLgLOBeAB8Pj/z2t5d9AZkcVGHgv8iPvOdmEKGJ5341trbffIQxfGF7wMjAwFlZ1C3A/0XUvi94f/FNXsB0fjRXiHCuqK5Xernr5c4IqFpAnW+WzIt20YAwbPzxw6JrvAfXX+3aeoiYgVS32l8XIi2DelSkczWtX/UJbC7yCJj/Wyg87wMi9U/NYvuVxPviNMfkorRqqwxr68XDt55+AXXo63ZA3FrkXv85n4uvN5vqkSBP84BFwDLOy6UfH8UdRBGIK7f5yvuxxpqrpv6onvXnvHkFv1XPrnBAMQBMgy5y59j70yukmrDoUvdhP+/ZiLy84L688ojBZ+X/Ub/D/30T8q1bWHzuYGiNLv4/apVmU2x2O5XdbXSWWbAnXTWfLpqbxVmcZ385i/wUFqTj9y7mK1J9BezPeRqBeKvHPz1XPkR5rXmCYFcDP6gb9UEfRBVw0Uz3EfRzENf1nC7W5/xrZfgA9H7AIPA7QAiQQbNuXxnOT79KGgILzNffu4RHkNQPI4LAXpSdnYKg8z3PtS0nAVLNhvjq1Xw2K0jiPoyc8A9azT4DgQboL4AQEUhFUD3ev6H18+lX0f+w8dkMzVsejWIH8rZ+EAByeLOAD/dGLYAvq3325kDPTw8iQI2sbGfdbZA5QNPnTa/2qi5q5oj48LKrVwKQ/jh/PzWd73pDCZIFGOvp+vdnEs34koFWB8gAcAREUBbloPQDo7yM8CBoZTMiAMR99aZPio/bL4W8R+bNNevrxlmRec/cBjxTwMrH3wOH/qMwAfSyecWD799H2jduM+0ZPBsAgIDj16fPfuH9WfKfPcXiK91P/zD8/PzvzUePIm78MQA+LcK2LZtPq9Wz8H6tu+8AAlZPWZvvNfjjs0p+fOHEx+848QfST60/Lf498f5A4pUenxbrd+gdmh8dX+H1+gBr0B+35kd0fvo5V73v2ArYFxmIr9l3Iyj63wrh1yWgGgY1QC6w+FkYm7me9qCEPyoBcMTn/PfxPucbKDR5MMdnU/wOBx4dAYj9p9++FSzwKG8Bb3fuIgNvnt4e2dF4b59ygLQf3gCUev/a1DbXpWyO62Ye94DlAYq2kfe4esDE0M4//zj5So8fVvq+YDwASWnz+9h7VZO5mv4uRZ56Av0cwOHDjPsg80FYAj1n5nN6WQ2IVxCqsz7tWM4KPAe8uSV8YvyXJ8b/o0TcH0rAXKcfLQBAnz+BtPWtLgVmfCH870uHdQfizxn4Q6aP+vPlWX/+kSczV6o/lCjAoOpAnn9YeO/B+6Ni/ZDut+b3H4leQMcx03GLT3Px/fACNfANBpYPi2+zBzDhaxp8DO95Bwbtv8xzz+zTx5b5B9gDvr5t+vZfGLb39tcfyfVAvi9z7D0j6O+lO82IBhB/NuOjhn6tnI+C+1L7X8jnjzAE4x8h7COMvodtlv7YSi9pHiX4B+b3ZnR+TiPPNd9w7nuyzkIC0B/LV7oyhfNsQldPrFg9max+IACQ4FE4QPmdTfvdZ98tVzzGx1lWYOn2+b8dv72BdLLmvuaVUK/5AywHOPuxmTuuFYAdwBBcPwECPPu/mUxeJJrQAm0xoAGRmEtBjkXBBOR6NoVbOOzYMIE4lg0RxJqAYBi2XQQnXQtCHIJ0fMr28TWFeTC5hmFA74k0M48smsXCKMKHKAr20TUMuSCTYNR1SZzEHYyAIYuyLczGKMv+vjWJcvel61O32ZDfhqTZJi+Vf3uzcRSs3KMNv3l+6BW1tlcoYavlcXmFVurQnyWowljpao0exsghFUxtQ22IbeAd0DY4V1v7xrZRmPHTiuFi5EJvfDOk+hzWVlaFZyNfWpnd2HuBEB3TjLyxqyvcv66vCCCAePRa785mNCJnI7QMntJvR7PMdlo9CBp2PTZ8f0/92Kfw5Yq1vBGmx/VEywNFrJY6GPOSSi+ywT8YRXmuaz9yD75gq/0FbVn/PvD31V1usKNhHi5Fy+J7TYwwBK27aT2udmZ1nowLbsBSFXHHRCDPQoNGR7Zjp7QxcVanT0PqeKlQKIZqZnex3ZVsvrsOVpg5qpFrpWbRt1UhYGuf5uDzRblqUpEaqzCox0tUQbCeM/1NvhIYSa2mFFr5sk5ep9Ny5a88+khhwdVqN3uR4KvTVORhANeOxtGZk6b5aTP5womrqr5QrjyhSYf0eJddc5KUpb1lxA09Vjl/jq6ujEwctrOc6kYcBtxsr6ygiyQWw5IbAwp4WZRDMGFOdYQFN0q0PYdFJ9/OU1xAYgeVXRCJBXYW0noz8sbSafrNzjuTTcI0Z6G6BGXf33uVOQS2ZSZ6DWlnrEGRow4rRC24kGoH/A4dhGXN0QdCJ5qJGCa5vqSm5KCGfmYOViRUHHvM8ct2y166Zn2MHWan3rD7bhTq/VZyxc2K6pqShe43NY2jpRWO7Vk+n0dlZ4yNzBnw1cMz6tAh2mZ1HqCRO5hqst6sT1aaGY5dXC5DosrjQWsOZZuLN3QvH7vsFjtKJ46as8Hcg3IJVlWJmAWtTM02DFWZv2PlnRvoHp6Ab+HDbUoNurDgodDwc8BZl6HeaIjdVil+0Gh38NIdHzu3isjgsJoGIzlCym01qJJQTrelmF9SsiHPS3EqVXEw7j0Hk4EnHM29cch69Hj1dHY3eStrVy6P+jnNhmsP0whAEsnHSPlyM23NXCsoglz5IHOrjXiC9iF9S5ulhC0ZPctCoB45cdwKZVb93vN38mn0cebA4tmE4KZfZNcAcava2/pJ02+1ZdNOfGq0oXzMtZiWRUIwO2u33QvUFO5ccRv4vCnTE3Lr6eO0Kypto7gSOloIHRvT9cbDnJ0HhG06ImIFx1MpZF2ocNfKSNMCVWqfX6+lIFxtcLqXU4zlgxzNy022ogVnIxKkZ9MjfLnot8zdXe1GdwZi4C5cS0r3+FJleuwSvqLu9uj+rBLMdaAYoCCfiAUZjJDfeapyvWgHJDjfY2c6sLrR3AS3XfuJiPVLRLkwaku0pwZuoDtm1xtCPoU5a57rXXPlmDq8MJETSSDGyk0QFUdjJ/GIrMtqomOch+zjaKwjV60MKWHIKD9xExLdL8OVE3c14itru6WUWFg2mybAjDyArmmVKCjl4Ai1g3f5qSrzZXUQLsuC78/2AFsIZ5Z5HQDzptNZUaq7pbvHS0mMW0VT1AKk6nYi4G4kqFTjcq7IRXxSEDJH2ttt2jq+zRfHIoyX5xzfVN0W9W4W05ESuaFccuLR44nQ2bZiuIslqcn9RIG0EaAxJY91v7HUJA87a4xKiW9S3Bjwu9bixAEERBZbjcXjQbzF8NU0NmvYJicUFVGxOIBm6d47h2nqCqKl+LEhC2WHhEKSYZLj83xUuSZEDLjaIf4ScdqlkhHF1WLVjIn5U+8MHh2JITc6BJLKJ+lwRgRHvu0pTaTTHmfNWK6aMOggIkFQNy+EU34Y+dtE8kf6sBsMOzvU8VHbCB67N1XG68dTEW5UeHDq9ZKiekRollteUzY1j5Whqe2lkm8rWkwMXXAYEy5690g3uo4aHb+dhNNO3aEZ2UQbhk+QpiuoELpkhnAUab6WaSL2LCM1SpcwjksVi4JBPK2ZdVPtu9PaatKKSDd37m47jENYt3xrH/ICM8fN1I32efRlBOupEqH1ChriHA3qHPLO1kEfC4hYU8WWjodU08sMI31c3l6Onu6IEhzuuGZJ+31E+iNNeqrHMcvzsrZ213ZMiBEPmJM4LS82y/LWYdN6Oo562k5XUs6Jz14tCb02iDJmqlupEGxLDk79SXXvySHub2l33nEiO+wz5rqx5Bhg7t6mc/oU6nQbZPvzNqP3/ElV0DLBQlGkkfV6Z9HqRTSx290zdLkuaXMtpWR7a1wQZSx+cEThKvLmFLe30Ubv7pBgF/qErF3cG69HBiJqEqFbMuA220g1ruKN4RIGxHeS4tJSS3jUVMZSQJYrGwpvO4Zdgu7kRsNVsQ54n91ImiEwYtEzJ7JbYt2h48+szk1Ueho4s2crBRZF3vPNjYCZ5+AiT92lchmbkEY034iDoByoFjp7UaoKYHV4vvPxtMkEulBTeYWnNGoc0jFQ13nT8WNfhrSxWZfn0KiO+SH2IwxuQu0glBB6Ed2EujDGnuWukjxY8NYijSJpkpqJLWMvUi5/XmfORhq99GwY1sRN7C7IpoRnxUC5GDBjBfewKgZJMkAJO+42paNsYuIIAd+4QlrocRpq9MVN4QlVGGW19fXDuoi4EW2cDE9Dl6lPzsC4lzppdilKXXrtFOe3eGMGUuRgWCVMrbJlrn2EZnBGrnmygFwZd9KNr/SgPHP1ZedFSBePoWEZ/o3Ihb1mJume9RuBZBJBvRRJoNAGuCBHVz+mKzQ3+SRTFRNBzGXiMz5XbumCW+ZXFEoQdiM7ajYdQTE/svfcGUAHhdPbq7oeHBxO4PstmoJ+M8mTfaPIs26mW3qbCx1PjNMKJ5S1lIxXRymF3s1tbPTzPMy7o4oxo4kN27ZyT7etGlLjtuBYu98POi1ukuSGTlvzaAz8Zum7mjmWJl9uHRVX6cZQl5uyDpZbrCNleNNVcm+NYd9DvFFnOBEWRX/SvS0JQ/GNJDBcNU1gCTjCYn4VoM62So4iX/hbFrTdrNekJaTHS7tD+kQR7QPspJ1ctL3JFfyGO5AXEimHNnUVd1NsdnR06WteF/RDsRIaW9nHQ1bDLd1vrs4Jvq5WCF31cHkMMxS0PEMQt8neu7dtlWATJPOYL/LpeWK33oGXoW1y3d/PmjLijJ8jknDa5sBpZUnrmxyx2pCNlHVRiuzp0EymPrq7ZCrFKV13ppIsuVKiqJHUCv2K9RZ6ihuo35BnK1AS/lidSr6Ue0ZQ8g1UOPxlibJiw7CoAe2pwzp1OFq5Ym1j1CZbXrJ8y+FQxcW7s7kV6ThBfYMYlWB74YS1YK+tJbndO8lZs48H+3S6JdpZt9qziooshl4OhkxYGHG06AOf7g+bSBB1BWMcw/G215bWrpOAKdi9ttg63HcluvRlpo8pcX+FIN/v0vuYIdqlIGt7dzsbdie5l7wm2oqn8httC7QDwxc4R2TR2A8CROKyZl+ya+zuoKo2YcWugH21Q3i9r9RWCLdVILP7kunPHZpMppbQCm+QOsrCglB6QxfxoW0uYW0Kgoonq3oThpmrNtCmuG1riIN6Ye02datV4hgbW6URQNCptFn70GpZ1seq0elaz86yvVXRI2PI0ylCQjbmkPaujnvkarDagRPatVpP2AGoIQlBi2pWzQtmXN1VSqg7Il6dV0nkMtutChpjAyl3u3zJ4gomQ05XZdhOFWqbuNyrM8eX8DEx1EGIbw3oJoQuUde9ZvPj9mKc66Q6pcoqTU6dU8hXWzfVYrxmSTlutomKlTanbEJSvVHLVSljOXN3zM3NDNdSBinJ+RhEO3goAwuqea4IfWRkkfTojNeD0yvjdskUMeubmoaPlWvIrhyObNewICjVUjFuq4NGXCSZucLtEI50M94KjUiW1w5GWWNJoEl1seAKvu/IKbVLx4LL9YERg6G9N+GBrq4VqQ8mFBj3Roo3h4Zztdjcu6g2RSVmOuxeX5rHFQovM7pvVKXkE+2Ai0vQimXSToL7W+6mWdCv+NgyZV4wAicRmpi7dYK2vPBZhQ/8eKBJZ50a7Alf3drTetp0/ZbdWQms7PYTHtWDsVaXbBSV2cjkBlrAZOhBtlwkrry+nQeFXK5WE78XWJUaDNVPWTm8OYFJ0xUandwzCFYwLLbWXfB4UdfObotW+ztxvojK+S5xUrQpKm7soh2lbEwYOXvXKkXQ1TW67+/WyYN7JNvSF0GaTtQS8h3ONC+1F5fxPe4bZ7cLQhrHt9KorySF2R1df6ciSL2yjsVw3KuqcaZiedSBAWU8MGPkvOEVQdU1i/INT7LjYLfRupyi1XXpxCeHTbfc6uCUa0oQzaRvprtxRpK+5OUd460LPzRSeBgqYjg4HTHw7VG0Y31fIIq5s2RGGPjDOoSvvQxlCItuY2TXT7ZqX0lW3XTB4WwjtwQvEJm0UBGjLHhHrJm9wd1pastU5HSeDpnbq9dUs+AMsqejORX73NO24TKM9C44BTp+51btGEHQfVxexrGFrqrFJhA87JkOCWymQNdChdm2MiBtmug5ofouiubZ0suxJXyNloS4zrjkBh/j69XxOPQG3fBtkfu1QeCprbDeOquvNUCmPXsoz94lke63OsUMVlxa16Pu+jdRgBSqCbutXxy3vualesvhDcXrMcLi6G2zXxorFgl2jRHLOGism3gpK3oCsdeLvtkK66Mi6IN7qpZE3oY6emGgur1OHoY4glaRt1WoAaj2hGxA9413PbI30lrf6s6DyxBMziTMmZY85GgdHWbQxlgU3bfyakXZyIpjyCo90OJVTFer4xW1ePee7dr2fK8jbWmXRbgjNNi8WsYlWZHdYHJs4ynQFTc3qL7cAplapnYFAZPRo8lYlxMD2oEecgLJsnsUSeN8pYGp2Gotfy9Mh96vTqHTxYf7FoP39XlIqjQijmSLBVMu1Y5meo40QPL9fubbGoLz7iDtOUZN+JxVudXytAYfzA6FHCWN04rf5Yiu3Jp2T2bARELgSB59lDgE0drV+g4hE8Tdpa7bxWYyetG63YXYLqYkATGOeOM3/dq/5drW7PVDsAX/UN/3JKkjxAkNy6BQamu9jsRGiMPbuRtvrYW3aejtlfga55uiuRtcLMG3xJuoLNWpYGeS4krUxTxvjqTiDve7wHaiJV3YFHSFhRaROxW/rMobc6mcwKDli2Re8ymOQJ1vD7fO5gk808uRLvxTohvctkZ5Gwz0Q2ENLIGxt0gdbKbbB7a4j62RbFElPVpJ7uOJJ+9jFJJdikS5cZz4XSJdpsSZWl3faFRe8WsH2Zk9kblIaLoszC0vJJ6KXXi1h3LAKEKHRNzxJHzYTuJpryLH0I6kWh2ZsOluyQ2PoKsuSA2hBr55CqjwmsGKJayWxw1xcl36Ml7PNVLTBy3Ko5hGic1yPHFEb7uofj57DGVc2hxtCgI+UzesBk2uBQ+rW3LNZBGHIJvgMQpXOtGoRGS8xjpA/ArmmEQ8OVgqqaPb9iPlt2mMRejGOJ8ZDjvmsYowYFj2Vyq1znms4jt5QDfYXlL1czWp2h6G3RtnoWGMbFrZRdojMwRw3tKEPnlpPRGt1pLUtL6cdgOzkklnV10dlOz2IB38PdfrGEKsThprRvrutNZPO6+M1Yxq766HNI7ucpjf5tftVjc8HGXxvbPHr/vQHxDhIhiYPmgIchCV6yUQPLxhvGJHeI6HI5W4OxqOsB4OW0SnL7ls+VriWBfS6XNS4LGRW/dL2UmIrSRoKXtKZCOrTviAiDhqbwVxzLHyRhE4j6akzK2DbbY+Vtl+mKLo2Ga9sFf0YEX1/Tm6c/uEPexznTyKJ51PPExKjqnaWPIohe6JIDcqaBz8m80NZ0+YnPbU8vXdso6TuyXvjro7E6eujMQ7VdXw4S4Nq6a4NZvJuAqdHcTsmb9uCIHYxivDkOBDY/rlyI+ju2aLlR/D8bjPXMi2z93tKoEZR4DXtTvVhHq6HxWnWp60o7OHC1M4E/5ptz6C1jytbxfYdqazlFOH+nywttnd7afDnuouQ2Ybu5OxzmQJs3fb2MGnUztUae7LmTHJhtRae+hOEjJF+huB7y0xTgR/uJttvybJUQratdOkdz2nLXqXNl6CMmsd5TgVoI+lkGF7vcQlz4yM26NYrMjdrdMGYX338XLy3OW9zKNw0hJXWR8jH113lCzp3l0JNrsVmd48C7+wLnsrgnUgq1us2Mq7bQLpERgA7ithOYnupaX9rt23w65VpMvStdWh6YjUwIippbrzBWnlqE/4m3zEi3QJ8LuF8ZJJ0w51oyu1d0lNC4dosnfqrdtts1HN+2UroDA2rk5cO9GeurP3WAjhA76+y5ab3puDn3gaLPKQcYhF2AvwEyx31vVEUYGGSCHOECXbjzSYIIbNYR03WdCZ6lKC6ICVkG1EgjbBbrEKwiS1TP2DzWKQ4d6b29Sv8ytxLZhlvFegSz+sGVjQ+65y8aknx7qC0ex+P8mUbIHkdDPyhET7VVoje48YMW/VymZgrdSGsdvlDeeQ3jqNpE7SUAL5LhzhlCYkaFXeL2ha5iuMY1xqdTzwBDwtudy2Jr3eWW0ve6D1PC+xCxHD7WhOOn3nZBJmLt1xGHtluULuDEybIJcabyRHiLrAApHUyGnVkTEkSQkRBNCwD4KD0q4OJQgMky5i2lhD7NLMlkUrMd7grqdrfA0KQ9yLHpWIVAYxZmAbjNr7sE6GrAI7k3T3NAlUT8a7w2Bcs1h45d+XoV8r1n6/lCzPsVwbYe+TxwlY6B7VXUUhR1S2je5G8e0UnYNyzbqyFAims4tQCcdqAgNKx34A8Xs/OLLYClMGCtLs+LSJGugeyJLhIteMNJcjJq7phhIVlNjfe+Yc3MMQ3NlsNn9+mw9Svx7uvf07r6fNBzz/z86ZnkdCX985eRxcepb76cHr078l1V8/vNVOBGR6nqg1aRe8Dp/+7jzt479wKjkTGJ/vfX09+X4ep7dWML8X/Rblbte09filKdLHeydgh90183uUzSymA75/f/76jefz4DUK8i9t8aX22qiemT3eSMo8N7Lar5fB64wRrH+9D/UFwbEvXl3Oqr5eWwAaIu/QO/L2t/8N2OfjS80uAAA= -->
