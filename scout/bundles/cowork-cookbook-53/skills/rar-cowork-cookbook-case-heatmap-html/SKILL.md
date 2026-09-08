---
name: "rar-cowork-cookbook-case-heatmap-html"
description: "Reads open Dynamics 365 customer service cases and generates a standalone interactive HTML heatmap file of cases by product category vs priority and days-open bucket, with hover tooltips and totals."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/case_heatmap_html", "rar_sha256": "3be94a3d38f009dd86a7754fc27771c617179f9f12e038d6d3fe5005a0ea13de", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/case_heatmap_html`. The original RAPP
agent is preserved byte-for-byte in `case_heatmap_html_agent.py` and in the RCI capsule.

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

Customer Service Case Heatmap (HTML) — Reads open Dynamics 365 customer service cases and generates a standalone interactive HTML heatmap file of cases by product category vs priority and days-open bucket, with hover tooltips and totals.

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
  Upstream entry : https://coworkcookbook.com/recipes/case-heatmap-html
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
    "date_window": {
      "description": "Optional date range for which open cases to include; adjust for tenants with older data (e.g. USMF 2017 demo data).",
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
    "output_folder": {
      "description": "Folder where the generated Case-heatmap-<YYYY-MM-DD>.html file is saved.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `case_heatmap_html_agent.py` and embedded as the fenced Python below (sha256 3be94a3d38f009dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `case_heatmap_html_agent.py` first:

```bash
python3 case_heatmap_html_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 case_heatmap_html_agent.py   # or on stdin
python3 case_heatmap_html_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer Service Case Heatmap (HTML) — Reads open Dynamics 365 customer service cases and generates a standalone interactive HTML heatmap file of cases by product category vs priority and days-open bucket, with hover tooltips and totals.

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
  Upstream entry : https://coworkcookbook.com/recipes/case-heatmap-html
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/case_heatmap_html',
    "version": '3.0.3',
    "display_name": 'Customer Service Case Heatmap (HTML)',
    "description": 'Reads open Dynamics 365 customer service cases and generates a standalone interactive HTML heatmap file of cases by product category vs priority and days-open bucket, with hover tooltips and totals.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'case-heatmap-html',
        "upstream_url": 'https://coworkcookbook.com/recipes/case-heatmap-html',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9900f41d8d162237',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/case-heatmap-html', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 access with read on Customer Service cases', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: One standalone interactive HTML heatmap file.'], 'confidence': 1.0, 'deliverable': 'One standalone interactive HTML heatmap file.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Optional date range for which open cases to include; adjust for tenants with older data (e.g. USMF 2017 demo data).', 'output_folder': 'Folder where the generated Case-heatmap-<YYYY-MM-DD>.html file is saved.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives service-ops leadership a one-click view of where backlog is concentrated so staffing and SLA effort can be retargeted on the products that are actually causing pain.', 'expected_output': 'One standalone interactive HTML heatmap file.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 access with read on Customer Service cases', 'Cowork D365 ERP plugin enabled'], 'prompt': "Read open customer service cases. For each case capture: product category, priority, days-open bucket (0-3, 4-7, 8-14, 15-30, 30+), and current owner. Produce a standalone HTML file 'Case-heatmap-<YYYY-MM-DD>.html' that renders an interactive heatmap (use a vanilla SVG grid or a small d3 script embedded inline) with: product category on the Y axis, priority × age bucket on the X axis, cells colored by case count, and a tooltip on hover showing the top 5 case titles in that cell. Include a header with the total open case count and a 'data refreshed at' timestamp. Save the HTML to the output folder. (Tenant note: USMF demo data is largely 2017 — adjust the date window if your tenant has older cases.)", 'steps': ['Paste the prompt in Cowork.', 'Open the saved HTML in your browser and share via Teams or email.'], 'tenant_caveat': 'Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork pulled 20 open cases from USMF Case Management (the F&O module - not a dedicated CRM Customer Service module - which surfaces generic cases across Audit, Collections, FMLA, General, Product change, Production, Purchase, Sales). All cases were opened 2016-2018 so every one lands in the 30+ days age bucket. Real HTML produced: Case-heatmap-2026-05-23.html (9.9 KB) with an SVG heatmap (Priority × Age on X, Product Category on Y) and per-cell tooltips. Largest cell: Collections / Unset priority / 30+ days = 7 cases. Audit / Unset / 30+ = 3 cases. Product change / Normal / 30+ = 2 cases.', 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Builds a self-contained HTML heatmap of open cases — opens in any browser, no D365 access needed by the viewer.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads open Dynamics 365 customer service cases and generates a standalone interactive HTML heatmap file of cases by product category vs priority and days-open bucket, with hover tooltips and totals.', 'example_request': 'Build me an HTML heatmap of our open customer service cases by product category, priority, and age.', 'inputs': [{'description': 'Optional date range for which open cases to include; adjust for tenants with older data (e.g. USMF 2017 demo data).', 'name': 'date_window'}, {'description': 'Folder where the generated Case-heatmap-<YYYY-MM-DD>.html file is saved.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants a visual HTML heatmap of open customer service cases broken down by product category, priority, and case age.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt in Cowork.', 'Open the saved HTML in your browser and share via Teams or email.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CaseHeatmapHtml(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CaseHeatmapHtml'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Optional date range for which open cases to include; adjust for tenants with older data (e.g. USMF 2017 demo data).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_folder': {'description': 'Folder where the generated Case-heatmap-<YYYY-MM-DD>.html file is saved.', 'type': 'string'}},
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
    print(CaseHeatmapHtml().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
