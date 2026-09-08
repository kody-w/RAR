---
name: "rar-cowork-cookbook-report-reconcile-freight"
description: "Builds a read-only freight reconciliation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_reconcile_freight", "rar_sha256": "7e9e2d9822f204cd31b4fff85b06ee288befaec6b29dbe1eaea713dff7d31e07", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_reconcile_freight`. The original RAPP
agent is preserved byte-for-byte in `report_reconcile_freight_agent.py` and in the RCI capsule.

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

Reconcile freight Summary Report — Builds a read-only freight reconciliation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-reconcile-freight
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
    "breakdown_dimensions": {
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Excel workbook filename, e.g. report-reconcile-freight-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_reconcile_freight_agent.py` and embedded as the fenced Python below (sha256 7e9e2d9822f204cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_reconcile_freight_agent.py` first:

```bash
python3 report_reconcile_freight_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_reconcile_freight_agent.py   # or on stdin
python3 report_reconcile_freight_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile freight Summary Report — Builds a read-only freight reconciliation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-reconcile-freight
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_reconcile_freight',
    "version": '3.0.3',
    "display_name": 'Reconcile freight Summary Report',
    "description": 'Builds a read-only freight reconciliation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-reconcile-freight',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-reconcile-freight',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ced9a2fe84d08134',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/reconcile-freight'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-reconcile-freight', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-reconcile-freight-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where reconcile freight stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of reconcile freight for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-reconcile-freight-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads reconcile freight records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only freight reconciliation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a freight reconciliation summary for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook filename, e.g. report-reconcile-freight-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a freight reconciliation summary with totals, by-dimension breakdowns, and top 10 by value from D365 ERP data, without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportReconcileFreight(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReconcileFreight'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-reconcile-freight-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportReconcileFreight().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6abPbRpblX+G8jhjbTelhJRZ1VMSAIABiJYiFm1UhYweIlViIxV3/fRIkJdtVclVXxHwZ6umRBDJv3vWcmy/x65vTtXFZv316MwOnWAhOliVxUC+cwl+wZV/WKXgrUxf8X3hl0daJ27Vl3bx9ePODxquTqk3KAkxfd0nmNwtnUQeO/7EssnER1kESxS24AmZ6SZY489hF0+W5U4/gclXWLRhV5ovNWDh54jULjFgt+P9tsuoiLIEWiyi5B8UiCyInWwRFm7TjQ7WqbNoAvAV1UvofgKi2q4ukiMDNBTd4QbaYVX9o3SdtvDCfa35YbILWSbIPDyFWWSHwoomDoG3egUHB4ORVFjRvn37+64e3BHx++/Trm5c5Dbj0ZjzUNV62BPzTODAtc4oI3K9G4MgCfAdKAd1zcMkPwsXr249NkIUfFv/5n2nv1FHz06fPxeL1+vw2/zO6YtHGwaItnYdpnlM5LvBZO74vmKx3xuZl5ezjBsShiN6fM3+TVFaLv8z3fnwu8h4F7Y+f30qgwsPzn99+WgCnfn6ru/nz+yyl+vGn96zsg/rHn36T03TuNfDaWRjQ+v3L6/tLLBj429AkXHwxdY59rQVCnVQBEP47++bXU/WXuJdLvjwH/1hWHxbflzzb8xeg7zPTXCD3+2KBD8DMt/drmRQ/vtaoS5A4TuEFP/70Z2K9OPDSLGna/5Hcn5+CY5DewFsvl/z04RG+vy6WL9u+yfzzZSuQMP+OJWD41+W+OerPZD8i+3eis6QImm+x/K64701Y/mXx85/a9s8mfFiEn982QQYqt3bcLPi0+PWRIj//4P928Ye//g2I/pdizLKrvYeEL7lTJGHQtF++/PxD87j8w19//qGrQBYHTv6lq7PvyfyeXx/r/MGDr1E//nEuWN8u0qLsi8W3Glr8Wlb/q/7b++LgZIn/2/Xm0+L3lTi/lovZiK+LPl3wu2psgK6/8+NPb38DmFMAazrvcRvgx3/8x0JNvLpsyrBdmF7ZASztAAjmway8FSfNAvzMqFEHwK9NAhz7Ggfyf47wrHEZLn75P94Dyz96LyyHnuD75Ss0B19eYP3L+8IC8so6iZICYK7B6PrnwokA9s5rVXXQBPUd4JM7tsFHUMYf5w+LpFj88mcivzxmv1fjLw/UTZ44Z7DijHFNlwXvszXHGOD8U3cPgHgwBF4HBGelB7QIgbhmhvmmzO4AI2fLmzTJsoWfgPUAIT1pAXjn0yzsl19+cZ0m/lw8QRlbPJmqgcCAb+osPn4E5oTZrOPnIvDicvHDr3/7YfHfi3826yF8XkMHtPDyPdBQMnfaAtRSl4NhICwgkAAoHr7/9W8vpwIxBaBWEKkkTILnZJCLaeB/9bC5ZT6iK2LhBsCzwKv57NGZ1pL2fSGGi2/6vshz5oIYUOHCD6qg8IPCG4FUB5jzzZNF2S4akHBNCNiva4LHqr+4tfNQMQdF7bS/LFRWB8xTZuDXrOZjEJhcFglw/7f4P68DIfUPzWL9VcT7Qpuzb1E5tVPFtfNaI3SecZlp/DUdCHcWRdB/LmZyDWZXPUrh6R4wCHjGe4X04xxz0HIA3i785uvajzHOzI/Wgyfrz0XzSnOnDh6dBlBlXERd4s/g/1+vlGrissv8h/+AprOkVxT8V1QeOfiN3L+1Lq++YfEk/8XnDoURfPH/e68z28oIgsEJjMVtFpxmGednDOYWb47VsyucNZhVe9Tbbw3JV9D5ir2fiywBCVWP//Uc+Yjca8wTz7oaGGAwxkM+SBsQg1nuI6vnLK3ruR6cz8VXkAdKLx6IBnwIIACUyJyZXxec737VNAZ1Pn//jfAfMaj92WyQuYuqczOQVWEQ+K7jpUCrOWpfQwlSPJirtI8TL/6DVXMIQOSA/AVQIgG1Bojg/RvwPu9+Vf0PE599zTzl0fN1oDDrhwCgRzArOAdkDhVQr3121MDOTw8hwIy8amfbXZBBwNLnxaAObl3SJO0Mg0+/BhWA3o/z+9PS+WowVKAagLNAzlcd8O6jSuZcyUHXAnQAQAGKJk8KwOLAKS8nPAQ6+VzyAFJfbeZT4uPyy6DgUVoz/XydOBsyz5kZ/ZncTjH+Hhms76UJkJfPIx7r/n2mfVttlj2jYwMQDqz49e6T+t+f7P1sDxZf5X76hy3Lj//erubBx/YfE+DTIm7bqvkEQU8O/Uqh7wCboKeuzYtOP37jvo8vPPiDvKepnxb/nk5/EPGqiU8L5B1+h+dbyiunXi/gAvbj+vwRn+/OiPYbYoLlyxwk1RywEfD3N3r7OgRwXFQD9AGDn3TXzCzZA2J+4Dvw/ufi90k+FxmgjyKak7Ipf1f8D54HCf8M1jcaAreKFqztz11gFMx7rkdJNMHbp6LLsg9vABmDf7bXmjkmn1O4mbdmoFgAKrZJ8PjmAr1SHxTpFx+kaNE8m6hf/26fuvl275FS3yYBE4L36H1mUqduZ2r6APRug6icoRR0HhWY8miwwGDAF0CZdqxmZZ+bsbl9e2DS0P7jorvHByd7f2Fy8/tEf3HTzM2/q8enf4FfPWDjh4UPVGlmLgX+nc2fa9lp0ocR39XlQSNfnjTyHS/M3PMHppmJ/0lSZfFyhW2q/Hdlf+th/1HwEbQTsyy//DQz64cXoIF3sO8AHv26hQAWvTZ1j5130YH98s/z9mUO8mPK/AHMAW/fJn37o4MbvP31e3o9UO/LnILPRPp77f6OLr8OfNn7Z0X8EYVR4iO8+oji70PWDN/1yZOe/3FJ/ffsPXvm2RIkE+hN/CB0ugzUSVs+Yp7PrRxYfua1P7D+wrmDrJlR9jtrg8Uf7AA4dvbhb8H5zUXlY7v3UDNz2udfJ359A4XkgLxyXqX02i+A4QBMPzZz3wQBmAELgu9PQAD3/sc7ide8JnZARwsmkgEdoD5NoWiIwrjnY4iLh2FIrVyYCAKUokDT6wQe4aK07wZI4AQOiWB+GJJgaACTQN4TTr7MTWEy6zIrAlzwESBS8NttcMl/GfFUevbQt43LbOzLFgAZBA5GbvFGZJ4vFqIRFzqS7qicoBNMDZczV98uh1Ii7y5KNPBgOijXG6UfYS6KKjEbDfw1MTv5oihisCvjklsa0rK3MAlaUb06mPTFKlzLjxsu5axdsckmvSCLM+Xs8L7vLhKT7w1Dabwha/nyhNeK5+oDJY+rNOscfrkLQ2jkgyzjPLkTlJNexxqHJa5lExqkXu/41TTYaNr5gZVhOcE5oTtoNBcZUgjt8JoKKkhJoSDJj05El7cgoSzO6w5bsDTPCwN/ws0kGQ6xZ24nWYULcW3bwUXK5Km3q4FmhX3jtjp1qYRcW4qo3DpH/Jzi2dkOB0PNveqQWzjBH9P2Im+9PtC3BO2dLsTgg19hQkpdnSxp33OPR+bWn478Fb+4/M5DbqHA3o+pIa8LKFVc5q5T8p3BN5K1Dh1I8CxDbHxigixG8ordRhUYNWIxXCeTYX+0aELjVmmPytk0VNEm1kUqjTfFecnlcCaXTL+U6Wl9khSY2AhU38F5uQry++qktzfLXU66eEoh1twrOkVVLKxTyuANPBdlmSyw0xJn7GWq8pc4TS5mxbVDhxOsf1QhaVuVG2XPC2Ikh1qfc1p6IG0CaqYeq/JtJksqvPdcJTETy96dqa05iOcSs/dM6Sy5o2HgnbkRLEFTN5CUtCXcd+eN65RbqvKgLBbk5Jbmcbwa85FAObJKSV/cLI9bi7mkopBdLuyRC6oTcUs2JKpHMWVq7NGLKW60jW0UUMHo5i6xHnSc0AwnW9O+0RhnOa73602aeAY0WcGJXGO9pNAXtg1WGVMJWlVyaOWuj3HrMMwddQHLJnaytUPpaig1L98v7Vi2FLxm6VTyqMyPbx7JmXZ1vOK0nUNkaTdieCp3kMNga446odxGdPlidG4TX4ZtaC+5sUlGyWqI3TViPeFS4W4lNdfJiQi4xKn2iHcV5Q7E0oK1PEzwKbnZ0ybXB03HBPAjQMuLMImQqqMWcb7fV/QyuQRMLR05G8pSBokIzGMFk6Pdxo9kPjCMwy267ihrOhCNx4r6eineNHkK3T6690LZmQjjI8l4Cdn2smwS0ToIhTYcU/KiIY4xsarEpUoZMjfZXcMsOykHmvUZMCmQVojbAMHUyY82bnwTGA3H1nnfFLQiNeMODs+NpRtkL1hcvtye0Ja2ZIS9rmXKjPLA9pS9tbGSkszCvbgO0Z0fV4pyxrDbkWKFvl5eJMW+bKiVt4Owi4umq8oY6OJ2uixxh7IvGaWX4745W5prEfbQ01Uvlo5iR9s6C2XGjbglcUmF3f12FHpOsVQH3Z/cmnfS01hFqjFRBSKJscEWLYmcuiMkx5yjbtVTOU74ZeqRI0OZ3b7EsMMqMzwIuRK86lBiJVM+dsWqdOoHZhUhKppRuTUW9RmriT5K+zVy48OxrdD7eBx1viZkpkOUa1wQDgYiYhqn+0aPx6i5dvx22NzxTUjdpq02IOc+osi4IEVyUjitY/g0YI7FVfNhQuedi9XxUs/Qyr6TnZXI7jJ27eawK/VXLxgaXFqR563DJhXT67v6LpkWZjU0Vras4iQC3xMkTgxhex6LC2pehsnqGY9tLVIZqYPh1fk10GOrK04GXtt6hKUdur4CMLwf1ltdPmSlzRMViRms5hgFam7obDV6ZBcXZ5jhz7vocj7t8qujMNejtxWTU4HfGzE639xj6GAWuh9oaX3UWCVQz8SUBHE+CC5Ne51VYuqYa7TE7ZxTqmZ2pkod4gEw04eT4Yx2cOgL86j5/EasTpPgQeezbQR5u2fEEtO6ho46OD2bJMymvJ/Qy84+p1jsjm3hGWgUrW3N34wNcUp4xGt4Ajmv0ewsoOfVTqhL6NhYFV5ezZRQobuVrpZLd5xY0aLTnKG5zE5sNw7hxPK1XQwLGlkeINzAHGqJq2zXYidSZqVtMArqvYegZWZCd1Kh9CtmkSQOt8khDwz7qPaTPhjN/sx0o3ShttpIUbmasbZwXVmiPMZXUVveWXffI4fQrSKnuyyZ80qlV80YSdeMCzyEijNKRcU4O+11xoatPne0ULI4fTPyYukRt3XsbWmn4nfKEtIdmynvAewDmZk6buuSl8+AzkXIDqw1SL/tyQqCBqul4dq70tmZgqQfFbxtjXJ1ZJHggKD+svHdhOj4SscIJioVEeFgeyDNqkM5RnGOruh5J/Vs2Hw9nK5d7Gx4JwDdykZfsr1Byjy8gblU21jyWcnp43bAYIhjxn2Cd/ftcs1qOydSWwvmFJ7SsQyAbRoWUC33l3tb19FufxkOojM5t5o830LZBLhmcbcxPg2WydTHrIBInhvsLTLs93weIVAyKGIs7CfRik3vdt6IIRnWd5hdHqSYO+4PaSBsUqXi+U7vnaWZ4SUqQpYoIeU5UDYI76q3RGCK+nIQBNu87VxVmiQW35wBrBmHQKgqmT453hANFsX1zdkshzjbQHe57XiaaeWNEXD9begaNJSpvdLXxOWocfvuKN3Fk5orHHHDuD2iZb1dJJfLaTLFbHcPNv1+zV2m4ZShIpERVCaOiuNpyiqNCbpkvQ0baKy5Tdw4t5s7nCuHEeRmMum20/eSg4rY2bjE9i4+MbW+73NpvSVSFullOt4N+0ufREN9H1oREjrFZAWLpDWedkw/iXRUtgDANBafIJh5TnhUi4g6J1YNjHGr+xW5MkVMBASKknhp97bJcbvDXd7eJvdGRQiRuqrMcBkJKRS5sxzY2/lLSy1RS+4cfJMLUXLbo7gPyzEiVLeETxyJlRCJk62OgayqTAl70mSBNhVWY9Z1tttavNZFZ0nD1lTPZweQqnC4u6y2siGMuMwGrHANdQfhSSTzsSXDreszeThJdEFtNmllsNMobHtDpqVhe5Vkn8O7KToJV6H3T4qTqhfoNqhrXt5GhorepksaGMjJEVEqktecsEOLpSmisX66qlYb2GRyw10KlNMShzdeqQnuTepsjyCtmDDQJWQFRrXJyq4ffc+LM6NNyXF/lgTmuMQQiVWKgqIvvYXk7v7AmqkkHNhJjURTkuwEoKZzmFovMon0Gg1LMqdhni+YWKDZ4zo11+x432hF7IRHhUZsbQ+JOXY5KvczL+73gx4zKH/gmyQUREc7Rf0RZCvortNkN2InRiebYyebyOGOJ+utjPCjqK0Punnxp3GDseSmTvZR5Q6baE3Jm36sbta9uMVFkVbuFdcugtbCPIrcEpHx0TyXHS+9hyMWnNwDchuVraxr3O687w1n7Ur05eh2CR1aFeXr4eTRUF4TNHfH9kS/VLcHP1rrBoVVvBVPlXqFCAGRTox81DOuNs5LzErqhl2riWZmJE6OPKMmBEhlCznz8q1uOiSw9jePviwPhwCilztTg1Knig5WtsXF3CGuGzWBaTnXkzscb7cCRBZw6mJHiFuuvNbM0Oue4qjRTN1ohXKc5XhJwnl7ylCPSwli+INEAqSI5bV8ORhLXHPZKvIbt5tKYdBwIaOhdetP+8vh3G3XqVrujmw7HHUzZKVoK27lpYc5ttdSVV+kCXJIWq2hQ++0RAgAOVSsWfj93irxDsa0450P0yspbblRsh3NYmTVUfhS5jX5GgfiwBjc3qQONAXpJ3K8I5tTPpriuNokfsknjDi01WB7iLveXtcs4VPJ5qS27IZcoY0anOXUVD1uRV1Pdj0O4eY27S0LxyvOZ5aROLIN0p7y3dVyz7C2Xd7rnvJR2DMqM01vRoCUXXAIdmq+HRGxS7VcvDdIer7tcqXujazakLpjjOO1sBDzdsQUKp6OmKU2Xs7vc1sJO0+tCMFEOHPJkZC3CePdCsuWibxGh5A5gn5RNFLB0epdh4i12pVnSGRvhqwi0Tq3Lma82dpLRHPWXRDRonj2nMPdZtqVcjE7ZDJrmF6JVTzWBBefOVs/OBXeq826svtcZE9HpMvxUtFlzIgbtQYotKtlGRY7Z3v0iENWHzqlHOO21wSW6aPxGF9zTUVkLURuRwXOqeF+6+vrjWRISJ5u5FqBllLZZaCFyFu7CoQbgzdrP8kqzI/Sg0q5tw1H1EpBgK0hz8ZwdKhNAg95ym8pYQV68Ylrm+uSFAW8rSOJxjAFKgcpPqBt4dawErbTqjBQzCcp6kJSW5fJcQQ/ld0ZpoObQWhbkpsqdiU6iEWmoae1esfsl2cBJpIN7qmuKfEwimvUKt9fNManFBtu5US1UiOa+E1UVseRz0B/hFTIbVhyKo/3xhU79Vf3lk1UtNuUvQc4uLBRbLqttSO7PCtrwbABUrSwBrN+jNjFRSYwG3ZW0pmtoAHjejv0YimzeRcnpCEg9qVvK949oxol5G2hqRCtkXqM2MWlRpPnI2nc9XWRVEeJDTWEgKf+Xkur02lauT3dYLyMStU5oINgWNre1hfqoeFV+rK6hZsytcC2errtyaiS9rkREiehutthfGE8GxULq4hapDtMPnq4k55/3OsagZlUAkIl4fytvi2vUBXedG4T5RxRTjt9DFbp+mhrldDWYTBpB70ksiTMVtmOXG9hsGWq02ko3CBOSqeLIdOM7yq2CfGpzptNmDI0IsdHOKw9lMKWvAqWujZ+wyh7uLL2vbOBR5A0oA3c3JcJeVRVUnKgUD1RLiXAppPkLNlPDhrWyF67RZnkduYxaRLjTDmJtBXxHbG/d/dCxxCWW8NE7RHDBtruiN3kmgMPq1t8m+abKfC8c0dYqns17lZ5Owa7oCuPcnhYdmhEu4wR0K6332xJtZpAvauiWU6V1vfQFC/NgzZVU8HUiEreR3u976i6v8IrEnMOVwnb7gsf2ojY1QkvcMwQG1ISkdPOUWgP42hytVsSh7C+3LipIE+84e0CfQgO1/pmgk76WklmeJhoQhjJWyjlnAhHQsVFga5PgeD6WUWFp4Ez9ijYlV/JdUJUuVFr0SQjsKt4S3Lfnq41U6p3m293YIflAVmZTyfC2VMhztKLK0jcQzvcTybXqbvdkSu8i8+lq1KlYQqqxM2+8fqU1Y+786mw7sn1Lh97zDclaKdiNreB8aNBne2dAvOtmBbtHgE2D4MJGnUMc4hey614BGROleeNUxThiOrXFbX0D8gpHLfwKTXtqdUuRu5i0vUa+qebePCxdbgn87ZIzi2M8kuHIjMGPZLhZF4VGj1FBgx2qRjwzNpMEQxBxY6MxOuK2OTn4paqK+h0dWWC0SzpEqrMqj2oGwqli21xOjG+lvs9soqwemlG8dTFtIOzq0qUMHzl9GgEPKqQTl7HsFVcsAjKGge5VC4opHXgeEhtGWSZ5HnGkO0xH+9rXSNzcyXbR6H0y5Xc6Ibv6fvbCrBrjq8TuTx395S8LeEzn26WhE7sjSYvxasImlQcNzPfdlfSPryukfRAxpv7mQGo7JeqIuzonaMhhwIBu/Gt421XdFrfHCnbQtXKR2+uh4cdy53U+67y2F0o6PrR69i73sIKkgfeBPotJ7hRnS0WGw23tNWxXdf2kTBtUKJtlw+ETfhEl6zVE8EUq23OSHWvaXZ+uqxJqxpq5IBwjiYjaLUd14Lv6ECJlL75pO+2BIatsi0qNvV2jeVu5EfRxdqNRbI5sMt7mwjNtneucIvVdngcBOqyPPFDtCZWVVVgw7Svtvl4wk+xrtUGosZXbWnJrmUvL6oZJ9VUSfgpN1p/tbqs+HOXryFZ1IOt3vAJid7XUhOkceqjnU1OfnQ8drafew5fqasSyuXu3Hm5p5N7tiQncjeIPGOK8Gbc4TuIZ+p271+7JS9eJwkzxivV7Zw7yJwt7J6N5fGwwz1eROnYzws0JQM7uvirGxfgO6Xe2+SSrNvqkBdq48oo5uQygkBVeQZgpSJ1sj2fyWZEucnpxxsgQBxTvN4r2GIi9yuLxNIlIaV1FNpZ4iZKDQWF3yWqXEsXASKOVEvneHa/J2FFGkdFDJGKucXmiCGmx69kik0qCe59UTVRP68qG4t3WJyNThKafrAf5OEeOjGKtct7ta32q8ql6bIk6Y2yvK3MLUY3Ke3qwzQCDW+QI1rrXS35sj8yQghv5HJrpx52h8zlvvMP7SbMNL7try3YbOGeU5jo6bC8+e6EUltJWeFHQgXd/7al7ZG0dcJYeXa8bHRbHtxlQvjDYCkrq90w99OVGQyRLAMhC1zqTBMcuuru56u2gSfHD33ndFfzsVO5+3iQXIFxZG7I3a3ZLsdRb5V0GeCSS3pBZPR71Wuajqn4qDjByW1Nw/rYM7utcaWUQWlzHFtBFeVI1pAYQsjWJ1xoKPiCohjRn2Dg9e3dO+xpM1pusr1e62Af3d22ibn0YRrjywN2OLpQ4cNr6HpotBibVtPSQferE+30WoeVUwkA5A7aeUFVsdR2O9REcVMuiVtVH3GT1MKVv/ELCMbZItTxY6idZD+YjNua7M8kRWMy6TnIvROc8wGPwyunOaudnttWo5FQVQnbfKUo5f0Uqz7Nd5CDjuFoKAiB4TuR05UElpjbGl0dVNLymQPoP6zD3lx5p0qp+kBXuvoWaL7ITtmw1YM8ZB1Wi3VAiCURbIc9VmkcctMmhczo4CBsTwV9bcus76CVD6EifQwi0MFmBbYrjzSteFtkH5SKiQ3d3R+XbJzq6TmWGsiUudu5Kg1b8jc9lmN1kXmQjum97K27vbb1wlo5d4mixWlW5IE9FHS286spOW6bY8GWxAY6udcygDYQWmHKZWPPxyR/+cvbh7ffjtje/uVjX/PJzP+zQ6DnWc7XRz0eZ4aB4396rPXpX6vy1w9vtZcARZ4HW03WRa+jor871vr4Z4eB86zx+eTU19Pe59F160Tzk8NvCYCKpq3HL02ZPR7sADPcrpmfOWzmx1I98P77Q87nQm/zw3/AqvmRqS9t+eX1qOTj8vzERuAnThu8vkavA74Pb/7rWaIvGLH6EtTVbODrGQFgF/YOv2Nvf/u/oD8hd+UtAAA= -->
