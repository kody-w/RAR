---
name: "rar-cowork-cookbook-dashboard-manage-procurement-risks"
description: "Pulls procurement risk data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_procurement_risks", "rar_sha256": "d0e12e3bd273bba6c0e540db90ca9815d11251c0a1a8f3fa2f3c139ca47fc199", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_procurement_risks`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_procurement_risks_agent.py` and in the RCI capsule.

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

Manage procurement risks Interactive HTML Dashboard — Pulls procurement risk data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-procurement-risks
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-procurement-risks-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_procurement_risks_agent.py` and embedded as the fenced Python below (sha256 d0e12e3bd273bba6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_procurement_risks_agent.py` first:

```bash
python3 dashboard_manage_procurement_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_procurement_risks_agent.py   # or on stdin
python3 dashboard_manage_procurement_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement risks Interactive HTML Dashboard — Pulls procurement risk data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-procurement-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_procurement_risks',
    "version": '3.0.3',
    "display_name": 'Manage procurement risks Interactive HTML Dashboard',
    "description": 'Pulls procurement risk data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-procurement-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-procurement-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '965201866d8669a8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-procurement-risks'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-manage-procurement-risks', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-procurement-risks-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage procurement risks with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage procurement risks data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-procurement-risks-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage procurement risks.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls procurement risk data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; read-onl', 'example_request': 'Build me an interactive HTML procurement risk dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-procurement-risks-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of procurement risks from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageProcurementRisks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageProcurementRisks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-procurement-risks-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardManageProcurementRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZObWLbnV9Hki5hyPdkJAgHCHR0xSOybWIWkcoWLHQRiRwJq6rvPRUovVe1+/Xpi/hrZmZLg3rOf3zknL7+/uH2XlM3LxxczdIsF5+Z5moTNwi2Cxa68l00G3srMAz8Lvyy6JvX6rmzal/cvQdj6TVp1aVmA7Vqf5+2iakq/b8JrWHSLJm2zReB27iJqyuuCHgv3mvrtAsWxBfs/zZ2yiErAaBGnt7BY5GHs5guwL+3GB/cobX1wpQqbtAweV+5N2oUt2NF24Kubl0W4SIsubFy/AzQWvKXIgGGbeKXbBIt35oFb+InbdO37RVs2nevl4eLx+/3CoDiwN0h9F2jz86IrF10SLsq+q/oOyJUHYfO3RRO6wYeyyIGy4eBeqzxsXz7+8uv7lxR8fvn4+4ufuy249EJ/Yaq4hRuH2jcrGMAIs7Fyt4jBwmoE1i7Ad6AW0P4KLgVhtHj79q4N8+j94j//M7u7Tdz+/PFTsXh7fXqZ/xl98ZCzK922C4OF71aul+bAZK8LKr+7Ywtk7vqmeFqpSYv49bnzG6WyWvx9vvfuyeQ1Drt3n15KIII7u/LTy88L4JZPL00/f36dqVTvfn7Ny3vYvPv5G5229y6h383EgNSvn9++v5EFC78tTaPFZ1Njdm+8mtBPqxAQ/06/+fUU/Y3cm0k+Pxe/K6v3ix9TnvX5O5D3GY4eoPtjssAGYOfL66VMi3dvPJoShJ5b+OG7n/8ZWT8J/SxP2+6/RfeXJ+EEBA6w1ptJfn7/cN+vi+Wbbl9p/nO2FQiYf0cTsPwLu6+G+me0H579C+k8LUBqffHlD8n9aMPy74tf/qlu/9WG94vo0wsd5iBvmzkjPy5+f4TILz8F3y7+9OsfgPS/JGOWfeM/KHy+ukUahW33+fMvP7WPyz/9+stPfQWiOHSvn/sm/xHNH9n1wedPFnxb9e7PewF/u8iK8l4svubQ4vey+h/NH6+Lg5unwbfr7cfF95k4v5aLWYkvTJ8m+C4bWyDrd3b8+eUPAD4F0Kb3H7cBfvzHfyyU1G/Ktoy6hekDCFsAB3fpNZyFt5K0XYD/M2o0IbBrm84o+FwH4n/28CxxGS1++1/+A/A/+G+AD33F0tmuANc+fwfvn2d4b397XVgzbjZpnBYArQ1K0z7NSwH+p3M5CNuwuQGk8sYu/AAS+sP8ASDv4rd/Tfzzg85rNf72gP/0iX3GTphxr+3z8HXW0ElA9Xjq44MKFg6h3wMWeTlXjygFmP0eaN6WOagQ3WyNNkvzfBGkAFkA9j+LDbDYx5nYb7/95gG5PhVPoEYXzxLXQmDBV3EWHz4AxaI8jZPuUxH6Sbn46fc/flr878V/tetBfOahgZrx5g8goWju1QXIr37WG7gKOBeAx8Mfv//xZl5ApgA1GXgvjdLwuRnEZxYGX2xt8tQHBMMXXghsDOx7rUC9A+i/SLvXhRAtvsoLmM635vqQlG23CMIqLIKw8EdA1QXqfLVkUXaLFgRhG43vF30bPrj+5jXuQ8QrSHS3+22h7DRQjcp8rqDNW3UCm8sCVNb8ayQ8rwMizU/tYvuFxOtCnSNyUbmNWyWN+8Yjcp9+mZuDt+2AuLsowvunYq68jxB5pMfTPGARsIz/5tIPs89Br3IFYRW0X3g/1rhzzbQetbP5VLRvoe82syt8UAoA07hPg7kg/O0tpNqk7PPgYT8g6UzpzQvBm1ceMfgs+//Q/bQL4a/tyddOYfGpR+DVevH/c980m4biOIPhKIuhF4xqGaeny+ZWctb12X3Oos86PdLzW0/zBbe+wPenIk9B/DXj354rH45+W/OERGDCAIhoPOiDKAMum+k+kmAO6qaZ08f9VHypE++BVR6gCOIAIAbIqFmlLwznu18kTYB95u/feoZH0DQPE4NAX1S9l4MgjMIw8Fw/A1LNZvji5mI2Okjqe5L6yZ+0mn0HAg/QXwAhUpCaoJa8fsXu590vov9p47M1mrc82sYe5HHzIADkCGcBH85POwBnbvfs3IGeHx9EgBrXqpt190AmAU2fF8MmrPu0nePl/Ztdwwpg9of5/anpfDUcKpA8wFhPx78+k2rGmytofIAMAFdAfF3TAjQCwChvRngQdK8zQgAEfutUnxQfl98UCh+ZOFewLxtnReY9j0h8ZIVbjN8DifWjMAH0rvOKB9+/RtpXbjPtGUxbAIiA45e7z+7h9dkAPDuMxRe6H/9hNHr3701Pj5Ju/zkAPi6SrqvajxD0LMNfqvArgDLoKWv7rSJ/eBbND98Bx4cH5PyJ8lPpj4t/T7o/kXjLjo+L1Sv8Cs+35LfoensBY+w+bE8f1vPdT4URfoNawL68gvCaXTeCFuBrXfyyBBTHuAEABhY/62Q7l9c7qOiPwgD88Kn4PtzndAPIVMThA5q+g4FHgwBC/+m2r/UL3Co6wDuYW8o4fJ0nsVn8Nnz5WADkff8CwDX8b01wc5W6zlHdzpMfsDtA2C4NH98eIDF088c/T8X7xwc3f13QIQCkvP0+8t5qy1xbv0uQp5pAPR9weD8XApD3ICiBmjPzObncubSAQJ3V6cZqlv857M3t4RP/Pz/x/x8lYv9UHuaq/WgIAPb8DSRt5PY5sOIbrF/nDgHI80DqGxB/zr8fMn1Uoc/PKvSPPOm5dP2pUAEGdQ+y/P0ifI1fF7apsD+k+7UR/keiDug/ZjpB+XEuxe/fIA28g+Hl/eLrHAJM+DYZzhzCogdD9y/zDDT79LFl/gD2gLevm77+ecMLX379kVwP3Ps8h94zgP4qnTrjGcD72YyP+vqIUiDuoxi/qf2vs/kDAiP4Bxj7gKxfk+6a/9hIb8I8qu8PPP64PmdVE/5Fnrkbduf2/B0NGD86UOiJDNCTKPTzDzgClo8yAYrtbMpvPvpmqfIxOs7CAct2z790/P4C0sedG5u3BHqbPcBygKof2rnfggDKAIbg+xMPwL3/i6nkjUKbuKAnnv/EAocrJES9ACFQz3NxHw6xNRx4JOy75GaFBasVgq182F25mwiNXCRC/RVK+u6aiPwVSQJ6T1z5PLeV6SzVLBIwxgcATeG32+BS8KbOU/zZVl+HoFntN61+f/HwNVjJr1uBer52ELnyCIfwRvW4bPD+1GZU3hnSYTq69OF6lazwnnnrrboqdqMzDn7s8kLm6yvjKGDVFj0o6k7Gt0fE7IiiEIskHy/yaHkkstuJ4lG+TmIxLc/36bQJhm0NkQNLyll4qOz9eZQwdYeJHH7Yiwe7vfj0uinNsoFCKMI5lK/rDTySkapDmnaDhm1xNsbm5mQpSXVRo4mwBGNo6i1VKnWWkWYeQo3zujG8DWajJibklGIqOBJBOtw2POxHplgbKetmlDVJZwMpBAsnplqkJGVlbhsU98VcZI4usUvrm4EsySi90hds7bg78XhNvKVShTQkLuUNbt8U2tUomRQ3slDZ7Lat4EYWxljcDC6v8OvOX/YMbIXydr0v5BxId5wwkoQGW+Ohibjd+QMx0ZsdzeJdWh0H11N3EefaESvmQrqhVYjzjzCtLoWgulZUbKLxlLhYgS9D/M43qXA/n86xvs3sjN0IUIufb9tNrlzD0Q456XC3BQzNGTtJWsg0XPNwUASRaa5uWyaGZa230tQaCMHLyCri1jEHlXvZ5rMoEQWPZgV/8G6UAsln486e0kPeayZtQluGudIrMbXaYOf06oq7uyHCB6J3S+UTRa24LU+G4n5INyWJVgHmFauL2fKcY4ptslYNNqcqfgpkKk6tgxMejHZbYAamcqMs09t9oFAQ2bclA98gU96xtwN99ftozFIjs0dF42zkGOJXUtyjJgXlCXznticzy/WVWjXrurzqXVdgAiQk+r12EduQE9/fEWdEXrJJg66H1NfhUORyQ5sOp4xTS1HZGRhzY7U1WbQIddycd2GIHaiKU6uaWVbu1kk6V6duiOeAps9OedsXb7xknS5H4lAfcj67CMcyRSGWPdWFOmQ5XizNw7ISAxkSVNSkN4a8YaNO4OPUEdGdmKm7iVBXRgzfkK6JdmvEOHPV0rk7G8WiJn5PB/TNukjVGTsRlqyHjmuqO4u+3lWqaGgfYgeIdyqO8k8mvvS3yzUN0VcOUVUs3jC+JZJkq8EkGmN7MWh2UTSORn0P5JpVzzwXXCWMGRuhxAddmW7MhowanmGkGGIMYteiyIaJNttazkB8WkF7bWD5bgauWcIQjTgZcd4HrjPtDJHJ5DKiasnbwim7cxqcZbcku17zhTNZK03bMihF1ky5FtRJMc+7MUJbZJIIZbyfkDBFR800m3sQ1fBKIZy6Do6JezysafDTCHgiOAxjHsxlskuhToFok3OGG6S1TLXU5bEy7fZ2kjVVntItMpIN5Xp+dF6KSNRzN9Y5R7TMjjtH80KzVveWsBcRaS1vj2ZykNoDiKjzVDlwHd7zZnNye21KO0uGtjB5otn2bFy29z2KquEUZhSuEjQqoJWKqfn9dGm2ZG8TEx8ileJG6VKKzGqcSvYMcsdU1p7SMtbyTtFdjR1ETGmuSQOyAVfKqw9QR+A1y1+eqzbyPPhgGOUWtRSYXcrtWCd9KJHj8RxyCo+mN/9OTUlS9MfYu2zYuw1H7aDRoo4MspMM1DXPMGLcs2yS7MsjtD37MWGD8ajJ2nJKs+32coXd6n4592OmcJsg7zrqYNv3SEVDMytIq7/ku4sdX2uMKLZQwR+3l56HL7tpulJeyLhLL8OHjbZ1ji5WoZpwQa3LconfkMnYb3YX48KuvTWWshzIVmlgPKjQAk445FykxhRtykh2q5kAcOiSe0pgU6k5CMXupgxjfHLJsAlz2eppEhNT1Md0NewERod1hfR0gULPHYtDYR/UPRfo2c3ctrKRJW0VF3Z2RJNdZttjESN+fZBNtGFyesdRTLi75I1VCHl87nTJHJzIHwg6E094ftRF00E0+Fq5xmEp36T4cOczn5O2XRmqjUkOfZNnjdMy+8YRO1m18spR2BuHH0Uu5SJkcnsLQ6BQq4M427TtYK2Ng4WrUseUEEVW2ZVAJc04CY5zuhroDapjfeOsvaDbgdgz9Aid4JWv8EdoSmBX0SGIKKENf8rPRXaQufMZXZeIIOggnr1N0d03G0nLQdpx9cqxDzSXCt4EGRTAL+QQHZvYTYlQ4LRk8k6twpyxgb/SR+oMXZzkxLp4sVMDa9f5OLPamhtNsNNkMJmON06HOrPhcpduTqfxohE6AgpzcUE74kzcM+mqUVUSFJ4eGWF7aIRuQlwQ1KOVbSbiVIXGZbLHw/J4vx7IFmcdr4Y6hh62BiOm+IWixqQ2dYqupA7W9ntOEK7mgN2RsJAJPWt29xvonxg6F7rD/QJ0EUTtBE+qrKIphCFCv44Zgz1qmyPv7gbq7CadEFIMvmGsdCUPuDpEbHDOos0q35pbl3JG+HBEcqdn6ONdWqZJYIDpqKJm/LxhVqqLXDkAl2Zq75hCTXnMlRVqu9jfmFSGjhyxofBd1ZJswp81Pa4kfOtuhyUwZHMsi5OMqfFpedmOuZbV6SjFxyZir/apcsTr3SeVGwXrw7A9BhJb7XqtsYxqigXxdopZOg2VYxztcJvFpNu43XS4LkxKiYSjG3PCFlI9JxWO8na4WrWZr5Umx3iVNgL2dIdld+kaurDs1tqWYqxCY4Nj0JSxK1AW48CTwHjDZbsmK9Onlyanm1R4g4mdgp17UN2YdKQJzV/pG4vJgDnW9wYRdYmNdpvVzijj8oQf63N2IxlP5C6jRHPk4YLrsOpzJWfGR6K9EbqlgMIySC68CS4bW/PvYi30OUu50RE5J82tIk93ltgXSR/giIStpWxgd5m8P2wCBtFFZ2Xcbmclq6jx2BHkbcruHU8X/uEiqdloxVtitcro3fEoFDoYwnV+swJxZW3l8/6sxKYCK7iqsq15PVcgvY2TUVGqW/Lw1vLkJW0F60DZBnZyR0l+e9GTtLaakEtpaljh9NCc9wN2hPh0OxhNcCau/mVJJ3eu0Nt7moBYulknYz06hbHXsOW50Bld9UQ8yjmt7rYxV54VTrzmoaeMiFXnCjUxu2Qrng42sRI3cFDTe3R7QqqAgYaDry4ZKIJIyRfq7eGQb/qVoq+Jc4g2hGeKmk9ux/1x2okH3yiPIWgHqLPodXhtMkddI5dTetHPpOhIkp6VIonkJ0PIWFO6bHkThFRiFnYVON7dR8nGL5P9RjYDj7juSUc9FlzjI/vpSNH9QaKWelxXSFavyVjJdj5tJlISEbE+3hUrtcoLbluIDWOKuMER2YE3ditHaXoI4LRKxFpvt2K28W0ZHePd1WngK1Lv8tq4YofjWsCz8WpiLu2JFykdXc+u3TMd32jKgHOEWDc92qzIUvckRjsITGKkLiScUvo2SnlvmNe2LZj9DkcGal3USEEPm01EG+RGPcLrEAosj1OdTTecfJTAYNLul87YjpJ/iPJjK8qG4LWnHjOdJliaUnHImxJJD+d+muqbtGxrzSSJRsWstX2l79zOXrKyKypXjrqNNIg5l8oHg21SEbNs+cxfa7vVIJmehLLWw0QhGE5EdJ7cnpUdaR12R7/qTmdzKa/S++GyIZbXDtKDYBzPxqnn96xS7ldjUjj7NOJ2Oy1RDJYI7iVCYJbIMOnqUHeKT0Y+2iOEDkwKUNEsL1W5Pa+um0ro+/xWmJiNHVG7oxIZLxS0X3ErRt9AaM5x+1bLV3QkjuetO7kI3sD2rjj1xgUWbU9NNpfTZFGVzXBAtwO7dUGT0dXsqU266bytb563Ezlzc88lk1+lSwEfbGHgGcumLUXZHDWms/TK9hDzKKSd4p64jpsOVqAeuisO8HGdUzzl0VTDg5nAoJaJVh+EPQLByJkDrtqjSBTAqLGXbH93z8lrulov1wRxqptDjUdIiC8nx0gZvO9HjMMoCrq1ibSrwhzn7a5fnmknQCh7ZCpDW0vB+jRQtt/KOzNcrlaQ70VJSCFsJFKxtrUFEjj4yO+w0ukR/ZyHOOg3L0Kp7rk21q67e8Jhq3G3rCnWTG9NuqU3LZscLPE+YqWKTOsi2K+3VnmqehK6c5Fz62lFotdFnjPIHb5jOYdnB03voU6uQe0wV8sIv1orHtd8gzuK+vLERSA0XKG7T7mqrCQ1WtWOjFxNWw1U1g/WPXO7ZapSGtOetXtNqDW7v0okpahIcS4wXOSY8wmAiMM1uywbqNOwV3lxVQ5RK7FoGfQGGU3bmLEp2SroBBl5rIGZLmgyRNpXHoGqO6btWPZerIhbV5SVE2KWbvbp8WisTct3Sdp2eq+/jVRxs5aJsr71AdoxQ8nqKLHbWirNDgi9gXTXw09geDGZprxLfjdokdoMIyuslwEFmxfMXrq+7aQItTYZvFx2eikJq40sbdf6xGAXW1FRbkeR7U1h3ca/ZRdbbPlscsH4fWAwnD4aPF1bFKrZbq6vYRbduQ2t8ugyyN0GO4+wUtfETjqt1nS8l/YJN7h6vfGRoZMSTbQaVagCTQC1ghGQUCe0SKGnHVJs7/WWHWCkshBGU9Kbm0FeNTFqtpHkVXlbDfCZ8Pa81VocaE03xOVeEu22LpzMJpDCi3fB6LqtA6qutpbjenOXI1c+yFsIXbfHQk6DDoMldN/FUT8cr+d1E2hmh6bdLspOAZ6yPhsNUH5b0QLVMPciULejpIPGmCeVgT0wd8pUTZg6HpUci84Wcg9IeY8fwPTqaPyJNwjPhZIJa+Rb653AkKZoSUYtKQleIZqnDBvC3cupw102515CvEpXpT3omra4GUGbgYSGFWkbPMvJ9R6CMmjj2UaZrXIlhy4j0kLHOuEqySP9MUEPRKrxF8YmMZqSKgrCfYGCSifWCgYrrlEbpepBR7LYCiZ2sxXFy+4S7hX0LBZkXqJi6TSRpSzPuEQ6dg0dPT0MEkmbRYrasaDD0xoepMs+Q3mt97XRqXqVC9YwIR2D0YwdfTBrBdqTq9VhjQeDkqO+3vJr7opap7NC0uvM9SYpi5woFTq2gAxVW7Uog6HsbdeCic3LUjeBu90Gcy6kZN5yjHT36Doqz6h/OumWEBuRHK+9aN/vWkLz1olY1oLnoqud0NVmdTqEiJu7uJYPHqaTVtpQmXqD1XTPd0V4WRF5sLpwgq5AsKcVUyZvrHxs+R3btzvVYZIDmbRG6nMUThntWWjGna5sTlUSBX0vcRupT7jl1Qpxd88rUuw7hhI7TK9Xt3XZsAkhGLcEyUVebfZRT7e6sWmw9aiXI7/CJCiP777GE3VfT6Qu59fU6Q4Ffy6CK0L7OKTrNVGLyTApRLS742IpbUgSlsR26sHYe5HJexGf4bg9HQ/QYWvCKsoiQuLFwgXkXXIq6qxdxfDFk3BF1vlzpFBYZ3NJeAonRI6OVNBdgxHGYsSTRD2d+rRWNlv/pHCEbweno34MefyAiDXuZ1BZKxVJTmavrpzgdFKIytreDsZ0OSSKW1nVLXcu1mo8ql6ajBzXhy0vrHunPIe38D74Q0/VQpqkG28aSiyhQlMjSrLKhTvoHrVhLaQXQrjVB0OWaPzUwvOQuyVaWU+bgVhVxKkfNkjlbkbPLiKtvR0io9UhMuLJOkf3PBGT7CSDSQyF9pfjVEsTY6/xvlhmE6zoe7Tr8GZcHUHZO2Q+GXg2uzTkmrDKc+NVvp/vpzAuY4NdThK5ruKdu6Gtg3j14BPqjcTK6YzNIDUXZ89Je1wxJww1MLiJa7Qp/MjY8ojf1jwGZbIuDaZfpm21zkCj6/RDcaRL0cBtSG34LjI0PkruvRLzR9Akpsu97RhkW0BRQu/lYVATR95QrqXbYaRR8f3g1yboQow+4AIfy0EJSYgto0dmgXCDHx2TDJWtoykRaG2snXskH5kg96FzdZpkyJXIlEjRG+FyHqU55Chn6yxOK/fOn9ETFbmVhwzqhQwkg796bZ7zmL+B2/0G14yuOmJnm6ju9sVDWMSNXKvDzG2OXktjFftHpyzRDkY986Jxm/YsIdP56oIhWMxOlXxSVsSVOwlQNyLK4MZYeVUGApX1u0LczLPaa3aHjsdcmVYpGLANdcpYyMbke31Jsvv+3m048grTKHSn8D18SEeedHWpLPd2IlkXTeRTe7Xtr0ayHZ0hcJ34oq3FFW31CtMPOTYpDddNDb8hV3ifRlKhSmcGOpYYBKyrL7EAhvBTuI9sxEVc9ACa7upEwZfbWScAeJy364FOlxp2nHKojARxmZxWPUfi1JgdG45Tb8gGyfdZUAbjEvUr0K7f1XyjpaNTYwTDR0V2KynCwKXIPhzv4f7ENWx7XqXrk2MJXMezsHxxC3kDh8haxuFDG11psylu+qar0EO/LpbblXiKb5bOMeMZ1xqUH7Fqg64QQ/PxglL6LNoJcuRfYCpz9qG+E+sC5X2ZooiAa6aTSPbwdVJJ62JJy70pWGsfjwS0uDb7HoFsjmT2cUnmac2XNj8E9gWf7puxqfv19VaoGl7mbAAa7xtlEMZx2Un3iY2gDvMD96LfJi8mG0dAY1sbWhQE430KA7MjzrKcCPWlvmad18ntYcphkoAjA+FJniec4dKobncSbnNO72ug5qqJdAW5E8MOUjZwQ8GhAtNtR0BBjPDXtSyXt3OiBGTYQ2dkvGGazE5RuRd4TTZhcZfRwVgHw7WmGoGqtIPBZ0OfrQqD8Hs8aYamdWTOivd7HEy3Lt3FbEWtyz1RLW16TQvnwuvFoy+wS9TAEUjpUtVHPag54nc+MYj0it64wsEGeYPSZmjvzThobipO0ntMukah6AstIR0M1qJbGi/EsldBB7LEj6A6E+tuT6ECN+01FFduBntd381pUqU1CUn8FiEmeot4Z7NkizqFjvZmyS8zhWjCjpmPXf7+95f5vPTLGd7Lv/FI2nzm8//seOl5SvTluZLH8WToBh8fvD7+O0L9+v6l8VMg0vMYrc37+O046i+HaB/+9dHjvH98Pun15XT7eWLeufH8GPRLWgR92zXj57bMH0+WgB1e387PTbYPIcH792esX1l+Oy/rys+VO9vy8TjSNQxStwvfvsZvh4pg49sTUJ9RHPscNtWs5ttjCUA79BV+RV/++D+XiqXpyi4AAA== -->
