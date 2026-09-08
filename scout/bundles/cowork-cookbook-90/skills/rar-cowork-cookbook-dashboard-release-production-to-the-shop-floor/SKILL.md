---
name: "rar-cowork-cookbook-dashboard-release-production-to-the-shop-floor"
description: "Pulls release-to-shop-floor production data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_release_production_to_the_shop_floor", "rar_sha256": "11d79325302584cd5bf84f562f748ca4eb209441d6cb8e45f769ecc51cd567b0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
