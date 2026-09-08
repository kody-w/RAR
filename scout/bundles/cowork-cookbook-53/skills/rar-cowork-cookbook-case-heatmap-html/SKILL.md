---
name: "rar-cowork-cookbook-case-heatmap-html"
description: "Reads open Dynamics 365 customer service cases and generates a standalone interactive HTML heatmap file of cases by product category vs priority and days-open bucket, with hover tooltips and totals."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/case_heatmap_html", "rar_sha256": "3be94a3d38f009dd86a7754fc27771c617179f9f12e038d6d3fe5005a0ea13de", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
