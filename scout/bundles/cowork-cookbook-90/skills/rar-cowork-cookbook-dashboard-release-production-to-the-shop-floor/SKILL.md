---
name: "rar-cowork-cookbook-dashboard-release-production-to-the-shop-floor"
description: "Pulls release-to-shop-floor production data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_release_production_to_the_shop_floor", "rar_sha256": "11d79325302584cd5bf84f562f748ca4eb209441d6cb8e45f769ecc51cd567b0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_release_production_to_the_shop_floor`. The original RAPP
agent is preserved byte-for-byte in `dashboard_release_production_to_the_shop_floor_agent.py` and in the RCI capsule.

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

Release production to the shop floor Interactive HTML Dashboard — Pulls release-to-shop-floor production data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-release-production-to-the-shop-floor
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
      "description": "Name of the HTML file to write, e.g. dashboard-release-production-to-the-shop-floor-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_release_production_to_the_shop_floor_agent.py` and embedded as the fenced Python below (sha256 11d79325302584cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_release_production_to_the_shop_floor_agent.py` first:

```bash
python3 dashboard_release_production_to_the_shop_floor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_release_production_to_the_shop_floor_agent.py   # or on stdin
python3 dashboard_release_production_to_the_shop_floor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Release production to the shop floor Interactive HTML Dashboard — Pulls release-to-shop-floor production data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-release-production-to-the-shop-floor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_release_production_to_the_shop_floor',
    "version": '3.0.3',
    "display_name": 'Release production to the shop floor Interactive HTML Dashboard',
    "description": 'Pulls release-to-shop-floor production data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-release-production-to-the-shop-floor',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-release-production-to-the-shop-floor',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac735f9302a3b4a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/release-production-to-the-shop-floor'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-release-production-to-the-shop-floor', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-release-production-to-the-shop-floor-2026-05-24.html.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of release production to the shop floor with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull release production to the shop floor data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-release-production-to-the-shop-floor-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing release production to the shop floor.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls release-to-shop-floor production data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the', 'example_request': 'Build me an interactive HTML dashboard of production released to the shop floor in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-release-production-to-the-shop-floor-2026-05-24.html.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-viewable dashboard of production released to the shop floor without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardReleaseProductionToTheShopFloor(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReleaseProductionToTheShopFloor'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-release-production-to-the-shop-floor-2026-05-24.html.', 'type': 'string'}},
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
    print(DashboardReleaseProductionToTheShopFloor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
