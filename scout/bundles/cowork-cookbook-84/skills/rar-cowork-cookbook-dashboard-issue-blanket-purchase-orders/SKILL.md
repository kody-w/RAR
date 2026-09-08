---
name: "rar-cowork-cookbook-dashboard-issue-blanket-purchase-orders"
description: "Pulls issue blanket purchase order data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_issue_blanket_purchase_orders", "rar_sha256": "2b36cb2f723b28e32f0007632f58cd69541c67cd550571a6665afed3bdb64888", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_issue_blanket_purchase_orders`. The original RAPP
agent is preserved byte-for-byte in `dashboard_issue_blanket_purchase_orders_agent.py` and in the RCI capsule.

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

Issue blanket purchase orders Interactive HTML Dashboard — Pulls issue blanket purchase order data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-blanket-purchase-orders
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
      "description": "Name of the HTML file to write, e.g. dashboard-issue-blanket-purchase-orders-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_issue_blanket_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 2b36cb2f723b28e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_issue_blanket_purchase_orders_agent.py` first:

```bash
python3 dashboard_issue_blanket_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_issue_blanket_purchase_orders_agent.py   # or on stdin
python3 dashboard_issue_blanket_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue blanket purchase orders Interactive HTML Dashboard — Pulls issue blanket purchase order data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-issue-blanket-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_issue_blanket_purchase_orders',
    "version": '3.0.3',
    "display_name": 'Issue blanket purchase orders Interactive HTML Dashboard',
    "description": 'Pulls issue blanket purchase order data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o',
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
        "upstream_slug": 'dashboard-issue-blanket-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-issue-blanket-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '656d6a78baf74e87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-blanket-purchase-orders'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-issue-blanket-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-issue-blanket-purchase-orders-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of issue blanket purchase orders with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull issue blanket purchase orders data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-issue-blanket-purchase-orders-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing issue blanket purchase orders.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls issue blanket purchase order data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the o', 'example_request': 'Build an interactive HTML dashboard of issue blanket purchase orders for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-issue-blanket-purchase-orders-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants blanket purchase order data from D365 packaged as a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardIssueBlanketPurchaseOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIssueBlanketPurchaseOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-issue-blanket-purchase-orders-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardIssueBlanketPurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWLblX1HfF9HpfLKNmCW/qIgWAkmAADGIQekKJ/M8gxDky//eB0m2M6tc1VUd/amv41oSnLPnvdY+F/32ZvddVDZvn95U3y4WBzvL4shvFnbhLXblUDYpeClTB/wu3LLomtjpu7Jp396/eX7rNnHVxWUBtp/7LGsXcdv2/sLJ7CL1u0XVN25kt/6ibDwg07M7exE0Zb6gx8LOY7ddoAS+2P9PdScsghIoXWR+aGcLv+jibnzYEMStC65UfhOX3vtFF/nForVvfgsWtx1YYWdl4S/iovMb2+3im784asIJ6Gojp7Qbb/GuKzsbmBb5NjDi/ULVDwtgVdO17xdt2XS2k/mLx//vF8r2AER5sWsDH39edOWscFECZ/27nVeZ3759+uWv799i8P7t029vbma34NIb/VUbO/tPPd0/v7yXZufngIHLIVhcjSDiBfgMnAJe5+CS5weL16d3rZ8F7xf/+Z/pYDdh+/Onz8Xi9fP5bf6n9MXDqq602873Fq5d2U6cgYB9XGyzwR7bReN3fVM8Q9TERfjxufO7pLJa/GW+9+6p5GPod+8+v5XABHtO5+e3n0HKgL6mn99/nKVU737+mJWD37z7+buctncS3+1mYcDqj19en19iwcLvS+Ng8UU9M7uXrsZ348oHwv/g3/zzNP0l7hWSL8/F78rq/eLHkmd//gLsfZakA+T+WCyIAdj59jEp4+LdS0dT3vzCLlz/3c//SKwb+W6axW33L8n95Sn4WW/vXiH5+f0jfX9dLF++fZP5j9VWoGD+HU/A8q/qvgXqH8l+ZPZvRGdxAfrqay5/KO5HG5Z/WfzyD337ZxveL4LPb7SfgaZt5v77tPjtUSK//OR9v/jTX38Hov+PYtQSdNtDwpfcLuLAb7svX375qX1c/umvv/zUV6CKfTv/0jfZj2T+KK4PPX+K4GvVuz/vBfovRVqUQ7H41kOL38rqfzS/f1zodhZ736+3nxZ/7MT5Z7mYnfiq9BmCP3RjC2z9Qxx/fvsdAFABvOndx22AH//xHwshdpuyLYNuobpl3y1Agrs492fjtSiekfmBGo0P4trGM+Y914H6nzM8W1wGi1//l/sA/Q/uC/Shb0D65YHtX17Y/uUrtn95YHv768eFNkNlE4dxAQBb2Z7Pnws7BFA+q64av/WbG4ArZ+z8D6CrP8xvANgufv0XNXx5CPtYjb8+iCF+oqCyY2cEbPvM/zj7aswE8fTMBXzm3323B3qycmaRIAYI/h7EoC0zQBTdHJc2jbNs4cUAYwDmP0kHxO7TLOzXX391gHGfiydko4sn4bUQWPDNnMWHD8C7IIvDqPtc+G5ULn767fefFv+9+Ge7HsJnHWfAIK/MAAs5VRIXoNP6HCwDSQNpBjDyyMxvv79iDMQUgE1BHuMg9p+bQaWmvvc14Opx+wHBiYXjg0CDIOcV4DnAA4u4+7hgg8U3e4HS+dbMFFHZdgvPr/zC8wt3BFJt4M63SBZlB3i3i9tgfL/oW/+h9VensR8m5qDl7e7XhbA7A14qs5k5mxdPgc1lARg1+1YOz+tASPNTu6C+ivi4EOfaXFR2Y1dRY790BPYzL/N48NoOhNuLwh8+FzMP+3OoHo3yDA9YBCLjvlL6Yc45mFxygApe+1X3Y409s6f2YNHmc9G+msBu5lS4gBSA0rCPvZka/utVUm1U9pn3iB+wdJb0yoL3ysqjBtl/MgS1C/ZvR5Vvw8Pic4+sYGzx//MoNcdnezgozGGrMfSCETXFeuZtni7n/D4H0tno2Y9Hj34fcb7C2Fc0/1xkMSjCZvyv58pHtl9rngjZNyA5ylZ5yAelBoI3y310wlzZTTP3kP25+Eob70E4HhgJigHABmir2fivCue7Xy0F+Yjmz99HiEflgECBYIJqB0lzMlCJge97ju2mwKpm7uZXmos52qCzhyh2oz95NWcNVB+QvwBGxKA/AbV8/Ablz7tfTf/TxuekNG95TJF9MRfLLADY4c8GzoUwxB3ANLt7DvPAz08PIcCNvOpm3x3QTvn710W/8es+buNuhs5nXP0KoPeH+fXp6XzVv1egg0CwQJ9UPYjuo7Nm0MlBsQAbALiAwsrjAswFICivIDwE2vkMEwCGX4PrU+Lj8ssh/9GOM6F93Tg7Mu951NyjE+xi/COaaD8qEyAvn1c89P5tpX3TNsueERVUegk0fr37HCY+PueB58Cx+Cr309+dlt79eweqB8Nf/lwAnxZR11XtJwh6svJXUv4I8Ax62tp+J+gPD8T48EKMD18R48MTd/4k/un5p8W/Z+KfRLxa5NMC/rj6uJpvnV4l9voBEdl9oKwP2Hz3c6H430EXqC9zUGNz/kYwEXxjyK9LAE2GDcAvsPjJmO1MtANArAdFgGR8Lv5Y83PPAWeL0H8g0R+w4DEqgPp/5u4bk4FbRQd0e/OYGfof59PZbH7rv30qAPy+fwOo6v/LJ7uZs/K5vNv5VAgaCYBsF/uPTw+0uHfz2z+fmKXHGzv7uKB9gExZ+8cSfDHNzLR/6JSnq8BFF2h4P7MAAABQncDVWfncZXYLyhZU7OxSN1azD89D4Dw2Pingy5MC/t6i/R8Z4sHhj/EAgNB/ge4N7D4DkXwheT7PC8CeB2TfgPlzI/5Q6YOIvjyJ6O910jNv/YmrgIK6B+3+fuF/DD8uLqqw/6HcbwPy3ws1wDQyy/HKTzMxv39hG3gFCXy/+HY+ASF8nRhnDX7Rg8P4L/PZaM7pY8v8BuwBL982ffvTh+O//fVHdj0A8Mtcfs8i+lvrxBnYAPDPYXww7KNSgbkDACP/5fa/2NYfkBVCfFjhHxDsY9Tl2Y8j9bKozMCWH6T9cX1ur8b/G6PmAdmex/Z3dOk+h1LoCRHQUyj08w80ApUP0gDUO8fze6K+h6t8nCtn40B4u+efQX57Az1kz6PNq4teBxOwHGDsh3YewSAAN0Ah+PwEBnDv//bI8hLTRjaYlYEcxEEJ10ECEkEdZO2jSLBarUgCvOJr1yM2OAa7BOl6OL7CSdgmCAK3A99DHc8hsPV6DeQ9UebLPG7Gs2n4hgxWmw0SYDCy8kALIZjnrYk14eIksrI3jo07+MZ2vm9Nwcz08vfp3xzMb6enOS4vt397A1rByiPWstvnzw7awA6BnhylcpYTEZR3Xe5GJfPPDBlr4rFpvFglzb3u8G3LwUJFy+0hVG1ux8iJzWxHnTBq34rwochVyCUrJ9pu5UuFwI0wuWqq7Ew1OBerHiWz1QhJazTuO3VMDfVK+WPKpVeF6Lcjsh9j6WpDTH0yZD9i9DXnGgFKQkuzGg5+A8uyQnABNHXkkm81iu2wWEgVSr6EegLYWZQ6JB/ii9DdimaVmMm9WLpFs9ZVXGXlWB/28ZWqGMVzGFtVDMEi7pwo4M2BV2rOGmGtxJiqpkVrr4Qqp9YGi6zv+70p0XJ0oYz97bRlRuF+zs+nwcDGsN0wWZMpDsVWEg0la5Wsxg3Flw1d7mn8Qqn8PlJrGL0R694g8XEZ3IrNkq8IyA+gvsIyLLn70dBwFWvxo8H3rsFfvb3UWfFEs2FquCtaXLNjlVVl51JV5zMxNLLieimGkilcbVSediHNtmN2ZzDfDdJwivc4G7UmMzH1wDPraczJwEVkpbxVKn5ghIsuUmqj7+T6JiitIBFGSfqStoxizVtO5h7lRCaieZO9ykmaEhHhZ1ib0q2ujnmoRFwQ7hRV8DNJbbOaJ9CL20Q3kjXQzCDYbmAoFxM9WOoLGAVsN9G3o4sItl5ik6qIaRuNnBBftNLPQlnhmupMNv0+QcP6xGIr/WqxwlSFx6UIZ1QOY4ziDFfEcseMXF5aCzvVF88oEtY5kddk2cJOxQajNTr0NuXU6/WgM1JF7v0w1jIv3g4CRY28KvBXsRCu2PF86nM9HkLXprntsVjtD7W/0bX+fuGixtrRTO4r50nzaWsQb22IWlUh6TIfJc4hEitjq5fOoaVOXY/URpmxHLondnZnGAKygeVS4sY9ybokXqLU5brkGNO+rZkGuuDyCYrdA07vT3fmNu3tIfb5k31MxXzA9kYfETQuw+dEIJk+Tqdz1Ukyh10RNFYuOZFFOrNuzvdhEtmhA78e+BVB91Q5jJ7vvHs3eC+8GUwOJREuHPOtuNk4KXmCWBbR1o4U3DMoufpLz2QKzGC2eWibOhVf93bX83fdKQV2OckA+xh6YzUmF+63TsIu1ZDbpIZWHk2DUy8rvnWkU2p0Vd5zrChOvlhJiNYquTGkk6JHHoVlytWSQl7G1b5chUK/Qadg6TS3eAziKvWd9VHFohrGhOUxk6+2mF9XldeP4nTsto2gOVDhHc6GVBQ4LAWizTmoGUs4iimxt1HXHp+uog1lZkv8ih9bl1AtqSc9DUODvbaquANi+j163NNuViLVCsGgyUs8aMdZtjsuiYMkMrmNbhydP+wSkt3sg4xqFBlpA58qYnFaTSsmD8oKXSve0ir1dXkeemTD0ugN3yv0XkRROBi2TEu0txPCGpsAzzLISYqd0us8rt/sCwJL94C5XS8UtVI3wO32oOcTv2cgdys4g3mogirzV52ZZcdrxsSgzyiKI8gCPurJxqPoUkrUjvD65Hbfpzo6OnE4wMsg0ugd1p6F7Q6zcDLDDhjEtof+2AjkMKVdK8Olq40V5Xfr6J5ZljYeOMw2WQplYvuA85KQlkVo4cFhzPfx8aoeaN8/b+8hW5+F47RB00ohO1SPs/t1q+mudFpCSVJEI0oTSnTFw1Q8b0/B5pJJ5waXxsgU+9HPvQ2P+cvsnFCjV2/kMF6J20DZFftNxQJop5Kbx7AweTDNigrSHc+lJoIacdgtBzrultettBpPXcKPVoZtqvOWzfkwVNjDshRKecvRiIWUV82j00kqYxZtN/YNZUCFIzeFo9J4kxwTAgGAXqKOL5O5dE3qTuE9PoNso7MZrmSMK8PqlBv7SjZZYngJtX6JJ8bRsjmPb7en0UDOsH1Rt02Yo5kaCeeDtGe2uInaYxVYgT4OdmNsT4h+d6ZKdYULwGHmZNuXXYpAAWqOkIDiLsZ75sHil4O6DChcLzOGOcJGLRbtRUpHBWtvl+QKrRt2v+mmC2nv2NPBUxPnju8TjLtBpMxm3WZ5CqBV41waaZ03F64qgniywpBq090q2p4iPHS38U6HElxjpXFQMUlsj9ig1HU/aRTsTmv5Su2QNXK1mDsSB5K9lEf/gAvD2ITHUMLug+Zy8VX2z9REXUyEvw5WQYWmnU6Rtccc+b4vgnV8MWuxP9jLS3yTrS45GkKz3G39pHIBhgDI5brjYEq3etKL3UhiXafEuLFDDvoN8ajWvpqa7fSJugurHbMKlDTB/Vi7pKdSNVDieNwwR5S7rnnnrGVry9Yi3OymFX/JZKWx5L6EBuaW5ui0dY/3ACIvocsqjKaT69TbHKxw1QQIc2Yxzz6KdzvDuz3e7kYXCQjJHvDUkY2xxNC+7iV+e0yLVdbc2RaHBRmP7LVzDcZMQa9xS+VUMaowz1LCiFy1UBX66+56xnodO1JX/jbER5aPHZoa95skmA7YxmP99tKkspIdaqw76zEh9xqPhdp1fcwUpWHUC+7ymqvju91Ad1VYw3tHhJFeF5iEOpOHbeXKltIW+HzGG/ldKB7ArCBMfAcODzrNMBDatApzTofGEBHcWEuiThw9Ue7UAYNRdX2IrIp2mm5jlqHUS3jVD1N0YTtdOd65VMp5jlRKIlhVOxeKIjbCHIMfU3V5cS8nyqY2Re+XERerF1fph3ralZewj/xlYjI6LNAA4fjLjiX3VLHj6UNPHlbJ2hZqRuF3ZglD+Em8MzTKeO0Yxef4fiCp1mPJbQnKfQpMuyolkvDbktoI04CCuZit1twhAkOEKWbrK7YM42ykISu8VgSdFvh6cyaLYTpSN2As75XjWbcqom7SQ5jXAXKXV3a9io0VTXPUIRKGfAdL+fYcu6UcG1N3OGxiJt5bLGJTmrYXL2cL37kbvDzVLYptQ46RGmRiorIb8zwJ18RgdIbn4ZdWZjrCnjk73A5+VA+6FVk4zZGlaGXWaUqzQwsFhZzTBzEkJHVFE3qvgZDsKNUj9ByVNplUi+FppEpWNfbXHWhl8bgMo27rnxE/t9OcETcr9ApNS5cNuXYUqW7iELs7nInQI5aar1d0VmpRusRwms9NjkzDQRW3Hd7XGmHK0GY9hUkpLIt6r7OqUFP5JMupuuv2XLldNaWBORnMMvd8dxYT63Dgd+cDWpx0H5Y1VqnGK9rQ3pTSS52nLDmsKz8lMibl/D12iBhPJZHtPQut4aKvUCbaFkilqqTQjVkd6OfLqmRvRHbpsytykeT9oJ9ra73jttd674lOpfT1Vu+vIk75OFunoxEjrjOxYZ3DdlKGFpeEbcKq81+3kwg6X04sSGPLLHmWjaPRWLOuT5ndTjHh/V0IXQqmbxJMSdi1bd3zcbqvxSOgNbAXxkW4vaS2TZSMDIcsxBZ8r49IVprHCwimdSNkVx6KPdd7a5xdas6+P/Gi0jTnuEZOJJ9GPHqj0f15dUlvB+YwgH4ygp0e7nbN0XdZYZ3yp5zHNZ3jEtKWD0yaUpvM2HPa0Cpg+LWxbkm5pYhL/TWrPN7Ybrk6w4iSQpfTDdocOZMOs32JHS6ovTGKI53eNkJ9Guij5JLiylU2mJDvFL665zXsuwe+JyPxOtKNMsGGnE5H3SgIPXNcL/AakffqKQ29xI7Toog3CnmZcAgvlikaKCfEleIWz3U1IUm98a/78oqwcsnsYEddN44ncOz9FsKUccma4gJiFsUTgQ7t8cZFPTfI3KTqOEutlHvjUPK2WFaiux7AME55atmBsVp12bhjbfvQHSbd0M76fJZibf2UemonqKG9TvfHMKxCjdJXsDRu2OuJRlG3xOjqzsWsPW23BL+uOt5LjuOIoASSmaYAj6a7Mpa0rdVyj1QZfhSZM+8Ld5/f63oNX+JezZi6W+4uhuLkt/JCUtci24UwxO3H+wDlIyJrgUZzrkqpJXOhlpJ3JUc1oVao09uOlxnpCtqOgsAyjCBLGmcoyVBQ1Nlhd57n6lcm8REe4ncH/NZiOYnj6n25Cu/s2pCQ4+ZwVPE+bzmTSbJcQu6w2mUHr6zB0LDGTR3a51FNQStx6XWKedzWCRdy592A0yprnnY728vMZq05G0LzE0286zB8SXpoaTmjpbXrE8UsQzA/x7GQeQDWN07tDZaLJB5llPplZ1+i03Vn55I1TAziuE2YQee+oHf42d7JnkkRqHomA5y+9r3h1PDJ9PerjXvc3bqKz6Y1uR6rZWZNvXLqMJnd0sTVO5XWxtUqfwuYrFlBpSnKZCUcs1O8Ky3aJkyf3OMZvS9Vs966yVCftxUjH6ajCDdmjrXwQdJCZbiy0OWU7ZgbOPlbBpsvqd5anRledRwR1bJ7voRHD2sjkG1I1mgT97mCO4bLkzjWK04OGltMdtDxMvU1JKMZjcqNZtSJhEEhOCUVCs5lOr7vERTMspBBkbuKBFNqU7nsWKPldkNSNgmYz8iQYnfHa2+yOrslTn4tJUFIwksS3poY4SgYui3Ku7m5BCJMILspuFXEyhxwZ71pj4cDwnWO3/neHZQaShda4vERoRErRuojvTmIt45e7oSMuO6X16HZ4yQJuD8j8L3p3egNU1inzS0jFH+3YQnduJttM0Tno6s2TsqYQInssXurOlxXaXKyCy/YeowfEzG1LZsrZAn1qhPva6cHB+y1sZFuY3DcEFIr6Tw41Ch415zQ4oolGtwmt2jb61yBTHAD6All9mK8PGwx29qZ8lXIoe2d7OLzJiEhiNYgdlPxAiRc15ATYPXlANOahEzoHT/6cmNaYrtLbNNNWxha7yYLZjb+dYhWoTfdhF1wkcajCZhyclfalrYvYkIz3D1cboU0siyyoFU/nZBhcJjxlCFO7jDQHq8Jw/e65mxMDMtJDILC1ym/Ca4eZvd2cKiUvt1gNnPS6dYrOoSTXsru850M8n8LbEJdb0QsDdc37EKvT5ojpYIxhBvuUG/Gakud74KxVqEaYRHSTj18DUeWSZu3UdnLBFK5bqMsiyoYx2VydPKtfEV9zJJpNlSCU4g5gd/uVqRAYjlXnvZVZxERc9F5oefPzlntPHMM9svyWt01cP41awQ9JoepvxPTSI1TklqHIBfTyRnJJbsjjCLaogjFNLFb7VTk5EsTvUkY3C0n3mTF7T3qi313F+/yOm8BIzprdJknKb07+Bo4YJ+KG7tF1m5gRw2j3Qov5477UoJuW+R62J1Oq0mNha5WPeikrNf+ORqEKrfouyLv4yicjIzDb1YuAWKWykg33Yimk2u11qhbPjSTCTB3PyWOb1tesGQ2tJ8KAHH2eS3ZeY/19/3kRntHslx0Dyag27kGg695oWx1WUwXydInYerO/g6/3XIkv/E4b90beHNW5OxOZX63DSybFjHRWHM1D9HL2qgarGNJxINXeCdNhm3cUTW18rNorwablAkKQDvs1kIxaolKtss+31P5wY59mGZck75IN7OwrV4WwJDglMeb1Ha5aG3PRYIfXL3CJH480la/FpVNasJ8iaYK3Aa5ovfWFupPpalhG2KFN6hjaEYX1EVN0He0hG2QcGGN4pCNd2NiAEwXCDBFN8G0lbdwSYc6tuo7PNNgQfV6zYFNndQYNPA9UtdHWYfZPvLOd5TXxATpUTLF97ZfYlRQxwmzh8tdoXb9CSbN0+oKG521tnSnMiRClQh3XGHondBPPYc2JRkku7NbeP45QVkwljOUmpupeWHqC245K88Vh+hw1Ui9XOIbAaugmzNtd11y0bAgze8SL0priWTFIeiZK19qd2ri91lSQbrLyVcLX+XYSUgMIhnJkVd8gVyXIY25y9E4teu1nt+Ja8I2ncs7qBfmSnfpQr+gqzOuo4LuDxvCGaBue4h6fU0yR+sgG5EvozKKlQpeUwCdolGYxg6XymA7teaGFpxWc5ReMZfW5ViPq8ZDKpISu9PgVsuNzbrHYGfZCubCPXq66vdTvuy6Q5Y0nYPbSK2vEsoi7oQhOewtWSOtYEe90IoRvD6xg7PqV0trvbnebxXH42jNIJlVO9CBQ8/ltKt3thYus9sp8DquIfHQVtHLOALwdMGZvuzoVUH5o0OVhHIQTINmxJtdgzkF0zL8uo6rwpzM1PV754g0nj0FTe2SF8m+aLVRehpEd0iFjyd4Iw9bBIr1DM8qE8xFeSxeVMJB2e11PQh17GneuIEIEzRRjZSnpVxCPS8S1LgCFIKIHRLYhWF4tzt+dfwLCleXe7q+1aNh45B11FH1yJOeTB5uBMPhabZFs34l7Da+QO+Z5NZHjo7f7hnanB2fWMfC6qydKpiGK3+9Pp0gWYW4S9ZaVFlqh2vr8YATIH/VqzgZZq13rymS2t7HEV0xbLsnopUiAwCFTuEW8w7nIeA2LWqQ0sQfFVYSE47GavvGwAVVSEhOmjs/PqYlTsTEsb6Yg12LxH2ol03NrjUTrYt+6PieqKegOg/0bQWfUtrF3RZCylbRg+uNPkV4bHPTYEmYr0DbjhOOpFf2t8tYSXxtwz13uAZLRUZdiEpTl7yS9ITXuNaAc5B8CujAyXvcdBKjm6LJoW/MaY1MautoeM6QxwBCsRvtCEXOmAVs2MQatTznZJIpvFwi6fG4M8ctcQnl7enSFJsKnLbz7Y4jajaP1frQEmcnQi96cOxXV3tki6Slz1l7P6zyK21cuqMPWecxVNXxWK3IUUH5GHJAbXh5PsQosdnAp42tRAoZ5+jt0Bj4nVujtOxf2MoSYLP3fL/1dnixkp2CuMiZyYg7KeStgFhDCIEX5H0Dr+kCbVI6mvaEvExKFbKv3ETcsosN4WaB0Rh6wCwtumu6lS7BkRknoaEl9rGFHxlhu93+5S9v81PXr08C3/7d77rND4b+nz2fej5K+vpdlceTTt/2Pj10ffq3Lfvr+7fGjYFdzydybdaHrwdXf/M87sO/+ChzFjI+v0z29ZH581F8Z4fz967f4sLr264Zv7Rl9vjeCtjh9O38Jc12/h6vC17/+OD2m97vj9e68ktlz1F9fMsp973Y7vzXx/D1kBJsfH2n6gtK4F/8ppp9fX3fAbiIflx9RN9+/9/JTq/SOy8AAA== -->
