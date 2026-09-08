---
name: "rar-cowork-cookbook-dashboard-confirm-purchase-details"
description: "Pulls confirm purchase details data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_confirm_purchase_details", "rar_sha256": "309b54ef6794ca0aae660f23cb8bfe794841ac548edbe6078369a72e4cb36f9c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_confirm_purchase_details`. The original RAPP
agent is preserved byte-for-byte in `dashboard_confirm_purchase_details_agent.py` and in the RCI capsule.

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

Confirm purchase details Interactive HTML Dashboard — Pulls confirm purchase details data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-confirm-purchase-details
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
      "description": "Name of the generated HTML file, e.g. dashboard-confirm-purchase-details-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the HTML file, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_confirm_purchase_details_agent.py` and embedded as the fenced Python below (sha256 309b54ef6794ca0a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_confirm_purchase_details_agent.py` first:

```bash
python3 dashboard_confirm_purchase_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_confirm_purchase_details_agent.py   # or on stdin
python3 dashboard_confirm_purchase_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Confirm purchase details Interactive HTML Dashboard — Pulls confirm purchase details data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-confirm-purchase-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_confirm_purchase_details',
    "version": '3.0.3',
    "display_name": 'Confirm purchase details Interactive HTML Dashboard',
    "description": 'Pulls confirm purchase details data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-confirm-purchase-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-confirm-purchase-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f994bcbe73e854f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/confirm-purchase-details'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-confirm-purchase-details', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-confirm-purchase-details-2026-05-24.html.', 'output_folder': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of confirm purchase details with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull confirm purchase details data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-confirm-purchase-details-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing confirm purchase details.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls confirm purchase details data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output f', 'example_request': 'Build an HTML dashboard of confirm purchase details from D365 for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-confirm-purchase-details-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants confirm purchase details from D365 packaged as a self-contained browser dashboard for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardConfirmPurchaseDetails(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfirmPurchaseDetails'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-confirm-purchase-details-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardConfirmPurchaseDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjVrLmX9G8N2JsX6peIRBbdXTEIIRAC0JiB1dHmX1fxCrw+L/PQVKV7e7q27cn5tOoypaAc3LPJzPr8Oub3bVRWb99epN9u1hwdpbFkV8v7MJbMOVQ1in4KlMH/Ldwy6KtY6dry7p5+/Dm+Y1bx1UblwXYfumyrJmXBHGdL6qudiO78Ree39oxeODZrb0I6jJfbMfCzmO3WaA4ttj9T5kRFkEJGC4yP7SzhV+0cTs++Odl0y5q3wW3FkHcuOBp5ddx6X14PB7quPUbsLFpwaWdlYW/iIvWr223jXt/wSvCCfBtIqe0a2/xo6xxCyBU3TYfFk1Zt7aT+YvH/z8sJJoDe73YtYFyPy3actFG/qLs2qoDvIGy/t3Oq8xv3j79/LcPbzH4/fbp1zc3sxtw6237lQvz1P/yUn/71B7sz+wiBAurEVi7ANdAEaB1Dm55frB4Xf3Y+FnwYfGf/5kOdh02P336XCxen89v8x+pKx6CtaXdtL63cO3KduIMGOx9QWeDPTbAXm1XF0+z1HERvj93/k6prBZ/nZ/9+GTyHvrtj5/fSiCCPbvy89tPC+COz291N/9+n6lUP/70npWDX//40+90ms5JfLediQGp37+8rl9kwcLfl8bB4ot8YZkXL+DSuPIB8T/oN3+eor/IvUzy5bn4x7L6sPg+5VmfvwJ5n+HoALrfJwtsAHa+vSdlXPz44lGXvV/Yhev/+NM/I+tGvptmcdP+t+j+/CQc+bYHrPUyyU8fHu772wJ66faN5j9nW4GA+Xc0Acu/svtmqH9G++HZvyOdxQXIpa++/C65722A/rr4+Z/q9l9t+LAIPr9t/Qwkaj2n4KfFr48Q+fkH7/ebP/ztN0D6X5KRS5BuDwpfcruIA79pv3z5+YfmcfuHv/38Q1eBKPbt/EtXZ9+j+T27Pvj8yYKvVT/+eS/grxZpUQ7F4lsOLX4tq/9R//a+0Ows9n6/33xa/DET5w+0mJX4yvRpgj9kYwNk/YMdf3r7DYBPAbTp3MdjgB//8R8LIXbrsimDdiG7ALMWwMFtnPuz8EoUNwvwd0aN2gd2beIZ9p7rQPzPHp4lLoPFL//LfQD+R/cF+Mtv4PnlhetfvuL6lxeu//K+UGagrOMwLgA+S/Tl8rmwwxmyAdeq9hu/7gFSOWPrfwQJ/XH+AaB28cu/Jv7lQee9Gn954H38xD6J2c+413SZ/z5rqEd+8dLHBRXMv/tuB1hk5Vwvghhg9gegeVNmoCS0szWaNM6yhRcDZAFg/yw1wGKfZmK//PKLA+T6XDyBGl08S1yzBAu+ibP4+BEoFmRxGLWfC9+NysUPv/72w+J/L/6rXQ/iM48LqBkvfwAJD7J4XoD86nKwDLgKOBeAx8Mfv/72Mi8gU4CaDLwXB7H/3AziM/W9r7aWefojguELxwc2BvbNK1DgAPov4vZ9sQ8W3+QFTOdHc32I5vLq+ZVfeH7hjoCqDdT5ZsmibBcNCMImGD8susZ/cP3Fqe2HiDlIdLv9ZSEwF1CNymwumfWrOoHNZQFKafYtEp73AZH6h2ax+UrifXGeI3JR2bVdRbX94hHYT7/MTcFrOyBuLwp/+FzMldefTfVIj6d5wCJgGffl0o+zz0EjkgMs8JqvvB9r7LlmKo/aWX8umlfo2/XsCheUAsA07GJvLgh/eYVUE5Vd5j3sBySdKb284L288ohB5p+1Pfu/70e+dQqLzx0Cr9aL/5/7ptk0NMdJLEcr7HbBnhXJfLpsbiVn8Z7d5yz4rMsjPX/vab7i1lf4/lxkMYi/evzLc+XD0a81T0jsauAXiZYe9EGUAZfNdB9JMAd1Xc/pY38uvtYJYJHFAxRBHADEABk16/CV4fz0q6TAK9F8/XvP8AgaYCBgRBDowHVOBoIw8H3Psd0USFXPifxyczFbGST1EMVu9CetZs+BwAP0F0CIGKQmqCXv37D7+fSr6H/a+GyN5i2PtrEDeVw/CAA5/FnAh7fjFsCZ3T47d6DnpwcRoEZetbPuDsgkoOnzpl/7ty5u5gD58LKrXwHM/jh/PzWd7/r3CiQPMNbT0+/PpJrxJgeND5Bhjl+/zuMCNALAKC8jPAja+YwQAIFfneqT4uP2SyH/kYlzBfu6cVZk3vMIvUc22MX4RyBRvhcmgF4+r3jw/ftI+8Ztpj2DaQMAEXD8+vTZPbw/G4Bnh7H4SvfTP4xGP/5709OjpKt/DoBPi6htq+bTcvksw1+r8DuAsuVT1ub3ivzxhRgfvyLGxxdi/InyU+lPi39Puj+ReGXHp8XqHX6H50enV3S9PsAYzMeN+XE9P/1cSP7vUAvYlzkIr9l1I2gBvtXFr0tAcQxrAF9g8bNONnN5HUBFfxQG4IfPxR/DfU43oG0R+g8s+gMMPBoEEPpPt32rX+BR0QLe3txShv77PInN4jf+26cCIO+HNwCq/n9rgpurVD5HdTNPfiB/AKa2sf+4eoDEvZ1//nkqFh8/7Ox98SL0x8h71Za5tv4hQZ5qAvVcwOHDXABA3oOgBGrOzOfkshsQrSBQZ3XasZrlfw57c3v4RPwvT8T/R4l2fywIj6r9aAgA9vwFJG1gdxmw4gvH/1hI7B6IP+ffd5k+atCXZw36R57buWT9qUwBBrcOZPmHhf8evi9UWdh9l+63Rvgfieqg/5jpeOWnuRR/eEEa+AbDy4fFtzkEmPA1Gc4c/KIDQ/fP8ww0+/SxZf4B9oCvb5u+/fOG47/97XtyPXDvyxx6zwD6e+nOM54BvP9z7/EorfOml97/Op0/IjCCf4Sxj8j6PWrz7PtWeklTZqACfMf8/ozNz8nkueYbyv29QNvSfTaiyydALJ+kl99hC/g+igUoubNBf/fU7/YqHwPkLCGwb/v8945f30AS2XNb80qj1wQClgNs/djMXdcSYA1gCK6fqACe/V/MJi8KTWSDzhiQQGHKwdZ+gBPU2rVh2/ZxHA4Q1HVIJ/DBTXK9sl1sTYIC7uMwQaI4ZROIv3YdFA8oF9B7osuXubmMZ6lmkYAxPgKA8n9/DG55L3We4s+2+jYKzWq/tPr1zcHXYCW/bvb088MsqZWDo3vnjhlQggdloV3bkL6ax8OpdY5bLYs1Gb7VxzTLVeIgn64mbAvDKpwEHrYZPG2Yu47J/BjxuRyIHjzd1W1YHROH22vOdT+htncpyBY9tSuY57yh7M5azmE79aZAUm4dN8zNMC35oKFcp4IOd22p8nLZd5QRxBpnO5VlVfsLgWQEdGzGE7O/LK8Eu83V213uJb3oVlF3nUglIQhMr6f1RLhFTWrHCj4e5eMqO+xkN1pm4rgNrzqGZvtMhfgy0/JLts7xEF4JHGusoMK016Mi3MfgoEtJpe47eOB2lpi0EwTtOPo2OeJh5GV7RPR0c6GW+wYP+kZx9xcpq1vxPp6M/Rmuy31KHustbF54FCP7CRvBsqKCjhiy9ItgOftqnVBofj8MDVmuxFhHbdlZH/bX2Bo51YSVM7lHDru006u0bTc7BlNyf+3na65md5O5l6IrxOfSLaSFQjljnGveLOcQEWVliFeQdmri8Pk944+YmqWCvU5vmW5HCasXS7a+bAIidXsZxSLWRKjt6kBZ+tHyh5q9QZzLbGnaWhvjmMB39VaZTEHJS5plUpsS1MyoSWV16K9oHSDXe7v3YMkK98J0x6cK2azPaLvtp7qTsfMVrqN1HjNyZSvqVdqMdYbrmw2rd8162gZbTvYriBvHE78RPYFeUk1awXBvSVgcQ3Yktzq/b6b9Mbb0Ir5Zp8JToGblVPvgZuInkmf3I1KqeetOo7DDT/V13PPEwcp0YisKUlKgweUuXnWu8qSNgEflFDoau2y16GoiYTpUfCiT6jJBXMKkOJ1kSUq+ba6CY8IHz4aZ9mTC4SFokExfsRUnDn04svfuvHJvaG46zhHgdnwKSNWSVAw6sAbUw2y9hDHptBwkRE0E7URuvG7PxzGyWTFWIzIrJEU2Dcj/6BbEMOIfqIw892cMNFtF5xD+FI4JYk9jj+e7KE8PW004bVUU7D1PpJ6TZzkzgXlOKNFcUNpbkxgCfNFcwiS2Ln1bQZHmbxtC0xuOAtGzzVrL0TfnymF8XcR4zLaSFLEHd90UKzHUWFOhoWsoWzk0hVs0PktqAYW41aYrLyqWO1vwBrg4IMgVtbqWVpVYF714GPt1dD9tSKbzaLgV020S+r7mdBi2LkGEenReCFMwsKPbGRs5lyXFyn2OVxqFvK/3t+UGgY6oNJ0kVbFhccLr7ZEyIt1QhdM1reXjaWSOB1Lbri9DPB4wYV1ny1jwd5ykpg7nVVngDteqRQah4B3Cli1/akByN5cmHjn9mG8acVwqrHxJXOYIAuyw7YRw3A7baj25lLCKDsX6YC/7Yb2/T7DbragjL3c4w/egE2HUsxOsiA0lT/jg9m7owVA2Gpuoc4/+SrsVIlUZJkzsKNNj1FiByWx7R0P2iownLkUBpKL+TUiXO42QKUlXo1g9uDG/Yrdo3QVsj1yy/ni6yGcW5AvOLVldMlTjwvtSMvSMuFtCRlPya9w8xPkaGaitezZ4QogGGW4bZlW60qaUxBsq0XErVMvNZnk/pohyO2D1fl+uGcY8MNyNGld1U/nbzj7j97K+HWh2oqAssmqVAE44DaNQ7upOpIZAI9poRCNciqxKoi/9IE55tdtDRmRqNlahvBAR1Z0KqACXwDy52aTrO7Z1eVe2JS4AEHxeTkUeszdic+FQK1NbaOA3iNIOG3yC4eZUCbUuJIfYSJCUpGOzum4O4aSOMB1r+I6VkqucO7vDFlXoqjfwldIbFT8g6mov65YtTVtmglw8zaHDVa+Ee6FiooponE/2tkoranmT+SFaY6kannJ0R1eHnUdNfCNe17GlmbQa901wEypX1EZtyq/4QFtyu6MRUuTa1jN7LR6z5EKj3i1G/TG1rvpk2bIhkBXIBIgSiwLCutVEV616kGpic6xIPtPj1O0uYus4l2tJaWkiWZoteuhSDPkY3SptuR5Sa7X168uSuN9wfanx1Lq6EDWOU8fo5CsFfQNju8MXDLx3acdKW2ib391xjOTIriM7MtYSfUUL6E67V6BwYNShHRP+np2iyXH2guxM8UXguqsCce1xYG54EYpNNYCMD66lYNxu0ciwuzTZXxVeoM7mLoSliCdta4nQ95E5sMNNLoRhGm0rOuVC0pd92OpHKtc1UN7XzqBk0EQEB/+aTHqsQcYQuwNKZTpfLpuQoaOM3VUIJ58s7nAAdT86OGvX9dzr1c2KMWoo0bhHh+xyJLtNJus35uwwO3gLsxnJjogpxZC+HFEWZfnYYtZQRHslwdKZzd03GLStaa+f9p0g4d6YWV4O3ZvuhDE3zI3PbZYFo2WdsEO2N0n9JAjoeLtSjkASUKnSkUnt7fAAZ+040ooQueb6mCjC6uwKyoVSnVw+oSOb8vpeSiGGM4yRG9yghFONGORUvscBcqkGb79aZ6osNRGEQtaO5cr7ERPD3Ehqmuzok+2ELW2MlGrx291pUMZ7eFQ4TlUO/o68nw7G+UgcbGBkIDjiHXc8OhTw6gRLNBYgYuLJaq/UBz+aJLVGT+KZbf2t2anL8yBuQuFaBGdXhThruDFSuY+GfNxoO2FZwtoZFzI6CEz9Su5KXrIVH7+Mu01LQ8rqrF7S6XA8Hn3hSA3HHV2vjbxUduw5YSdPoQta4u4RikjXNVo2S1uITuWKxlXQAmaQzk5cuNxHZ84XKtCEeCMW77t8w8SB0lZXDIGhxmKocBpW4uRoLrlTzNuG2RhaE/HIsNOwTd1K5DBsYqMnvGJKh57f8q6e4Hya9lyVZKAAex6tblajtD5wjiGFNqIDyDrAZcpc86i+VusuVqfdSafsE3O6Xla3sL/uLsc+9J1+24anW+hzcBkmTB2BbG06JiyiwcSneyX5FGb0bBw0Z4cFuUKwaGi6mb7X7evgH0/GIT9S2EEqL1tyyQ7mveG1UW8ciYDhmN7T3IHKSaS6t6D/9eiRLq/XtDniRzyF7EuTcPBmDVWeClcgX9HEK5YoRt16KpZLrzPF6VzdoYHqAxjSbm5ln1KhWE9sJnBKcGBC1WXq7F6N+0C5YOuRvmS7LFMPx2voqHVl0xuey0Y6vt4j9arh9xM3nrNj7SJRFYYK1WNF11qcU8Srjd0lzvpM3lzmcD2AeqXpQq/yZLIPeBYpx0aD9vS52Qq4qirU0apcazQN7JzrjUVWpt5vdg2OZ10ljIeBEZOIVIw0SoE0VpI4tWmkOyKNb8rBOln3XoiZm6OBuXkT5iJzFyP0pNZBkcyJJh3Y3tzD6vV+3qbn9XVNMq3dZKamUQI87fZrHmDS9k6SSw7MHGJfDfjSVRz8rHd9BWKzauCbJQsjvhOtylIV73CFrAjuN10g+eotruD1qmqZarUq7pq1Wh5uIu0FcBApo+Ak2JWlqTRX9teWvsoWMUlMmWamG+k3+346D4rJl+stfruMjB7ROV81amSPG7Q8FOG1JLAKz2BL5CjEbQpnL5PCJC4j0qvpMbsLRy+0FK/OeLM500t2tC+0KMZewarulkoPLBuDXqAVVKjrtMLxQnkMzlK8cSW4AoY8GMjAUMYAClawobVVb/VnUIIgYnVeesQqs8WDK0eImtFjtfK6G7IqU/iUmrIlp2ZzyUFONC51VZ0949b7k3zMDCu61VwgRJRTM7giW6D6S24a7WX6sAvscVAHdcei8nLLHlIGNSS33K+zTtqAdnZa2V5+y3UbMYvqJouHuOJZZ0sDevtSwuWjpzaw257bNj6jo9yqPorkkCDbV3IlIDLEUoaIrHcwRKz7m3ZEcqSDSGVnBdFKU0qpOaP6Nc0q9EYl0RUN4KQWJ+a4ZG7JFF6J4Z5nUgz3FTfd+6CInfKCHiJE34cmidEbsij0jmMIW+Aq1NLK02UQLEWM6EzYpBsvN4dDq5zGO18a6o6z9pftrWdCqTedc5K5ZC1dZFkLdQflJjxRIhOVOjZKrdvIGDZe6kPS2odisM/yCvS0Uogsl+OlF7trdPCPMU3vCXm9xka+O13Z1UrNFaVeB5q9PjqlnAc3lLiTuyA4jWYZoefdGJ9TjbWMehOMmIAdvUFV98PJFnPUDnceq6tWEeMEGGtO2LSTCd7ggwtoteD1RlcA2DjrIL2M1upoebUFWxSOolJ/lNISay6Uwo9bOLP81oRFj20hhQqVVKeMVPecvCb2Q5dRowdXQuE5cH44uptArS4kD9og+ULKdw2jYUbEisOo75TkOKykgCUMW+ZyPuKC82XvVLmw6ViGPa3g2HdUQoS8mJyatDW2DLS8lpE4dvqFEqUtOzm3Bld3FqoYQ5+ujqZd3M5NKeOsLQHUQiZEFQkBbzB9fxPxSt8Smz2RhPtTpafjzW8hXzPBFHM8KaJxwuzTEd17u/K6lZ0tKYACCvNgWJXPOOJLRj7qHue3OwpVgFgV7hqE5Z+IZtJNXSrM7ux5d8wIDSnac51Hakp/UzR6Q+i257cClXrX3Q1Ms5v7/az3h4uXrOFayxDXHILrErkjOAaZ6tBzQaakBs5AB2m75G5QByVLxjvmMNvAvIBzFugsR7IMRzvGw4guazMw2VvfnSPIiaEoIXWq628BRy4785g2vUOZhth1gdcn594RRHEzrdVbYARUM53GVrAdmjzzpiNzRmgJyLIc+LYxyJZYQhuFLBP8yPKCRy6dYG37DJzIEOIad+zknVerZlPDrZwhGRtd0FOjbyR+2/ksJXDubkkX2oWBYDBLupPAxjSSJdf7fQeY7bdpDvOc26g9rrBOsqqlwdIdkVpJDZHlVru+iMPKpIVMr1EryHqBde+rczyd7tGGVyCRcuJ7Iivieoe6asOlqVymS4LHbZxwm+rA7/dGu6SZonAcS4hiiNkd1iv9iFwo1mAmvOIoBz3aS5yZcsPgpYbxLtJRTwK3kKB8594YqAbDzFkbLVjWBXYE7floijw61UndTQK0t01mEzh610i7SDdPTI9MbA36i+4U2Jzt2urxdFptzKnNLb5ZWpURmFLOby8TOx3WBLNkCdfZjdEp2SRZdNAuB4st+03oZ4XHD/bumDKhtb4rDER6rnq2HE538lCkDim+D/Mt5MY2HftEuHXuEGlzjSRCImemrh4SELm10rXYFNvLkR+R6oCSHZ/c19B5szICcWN2rNzaJbZMk2N/LcSggn0z02rSYradBPu7bKWYAe5sM42bcly2XS8QWYoSMyURcTQnjnrUDd2d3fpQ5lwCFyQhnKVNnloWKl9sGYkUHnI0JURbyiJ2fZ2KSHLEbBd2zsVZulaTpOk+3Xs+40Gi2JzKY89DHVLlazclbjoJ5pat3Z93ZmCvWayazq12WN60jWBvplWb5b202geSI6fjdquLRpSLp+zGGTXaCIEgh8dYLZV+T5K2aF75NIGIi1je+Z3F331+y6qBtaPkUlyxnsMfUs3J6YsgojgfmUif+G2ge4iRrmqjYnB3hWEHzYIJQSBRbGlj3hjZsBoJ2LI1VLSok/UqV0JlveoqrEpgwfcax1kZHk6wpNMfqei2LhkzQfW8cCcbldfkycOqk4blO0Ms63skmTRG3KYdbjvZvSFq/Ra4cgnXBnczzvsIp6kNiSv3GB2nGu1DNFN9M8hg0FblJqde7VoY+RujMVDjjedOvEacBaQpIYwS1tWydyaaaUMA/kGa34/HliG3xP48+B1rHkvlvpmOuySplqp7uFomBl/Mk5DYuHIj5KPkCYnvyhuS8yznPHLQcTK9Q7CvE9d2kG5QaPiGrC9XtrpgGtpoPq5hzrD0aC7uZJLYpepm31/7PRE6pCr68Aa5oAPGWpYNOeoluhMAUqY9FDtyP94whQkxHWmVzguOp7aSNxl6L6XVzTWlskRbGHXgsCjI1joik6WvgMzJbSXroVWjrjBKSydrDvlqk2hnK5k6/R5i3flcINVY9B1oW3O5kyiZC3sy7+3wEmisedalUbisWuxEtPetS6UXBYkbXV4mw0Y7FtleTtfTXVpr52tUFebVzBq0le+KzxI+Z+ztO5WdsRNb69TyVpw1FIdSP9vmGTsGt5W7vNda6bsd6UPkhQMoJ4wtodEWa5nlivVjahwYX9hubjzrBmiPniBJdFXq7LUezd832bUDnZXlU213alVMIVqis4zpfOrgGxgRjJVz8tRlRmSTzB8D70oAFntrvduxRNbBAjMB2js26TeRrWH9lCFO4mg7nLWaIGcm46JHGHFtGup+IZNYvkd6HgqHfIINvRu8ScH6umF0bMXtLx2rbPenwJViWqn5zWFDkgnhhDxdat12t2zTHLUmK8VPUpgH/JK1VNPvSe8+rAqdMFJ6mfFXWB/uWgKdlOvF2DM11JQ17kBCidU66a00rSCROmQDZEUkrktCakA4CH/sG3TTjtCe4og1y7s9TYVIkydODhsGaan8TjvbKJekS2pfOk1gSVeOMi5rXekNW7MnIN7K5Dyppu6tcWhPzbXIMf8UVPmuJSfOiS8o0qJtlW8RaOL7/tied23ezaV1uYK0mkNldzj6xuGaMiVHZPAUnYWNeh20s7Y55VJ/cwDENYanIqSN67tiG4v+SoA4mHcYPU12EupexjCQmaMDO7mBHjnS3lM+mKmRxNislji2bKx1Q222Abq9dN6+JWxpLR4L7ypmSUL5WObugn1PL5mTj4N0Uu/ENSrHG0Cqeu7nl+TSC+hq4EBD5d2hps3xfYNwru1bmMEF+ICJhZ2Z/qgfd2xLCcoaR5PBg8YrjPKXa0jTb/OJ6NdTurd/46Wz+Tzn/9nR0fME6OubI48DSN/2Pj14ffp3hPrbh7fajYFIzyOyJuvC11HT3x2QffzXZ4vz/vH5LtfX8+vnmXhrh/OLzm9x4XVNW49fmjJ7vDsCdjhdM78Z2cwvz7rg+4+nqN9YPm8280siX9ryy60r2/l87PGWUe57sf3tMnwdGoLNr/ebvqA49sWvq1nV18sHswfe4Xf07bf/A3cE+sywLgAA -->
