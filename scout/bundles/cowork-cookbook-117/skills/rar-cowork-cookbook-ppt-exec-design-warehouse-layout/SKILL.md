---
name: "rar-cowork-cookbook-ppt-exec-design-warehouse-layout"
description: "Builds a read-only executive PowerPoint deck on warehouse layout design from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_design_warehouse_layout", "rar_sha256": "8dc38d6037626cf3b2d8044be244e6f87a868d9774dfce5c53e8991737a7e136", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_design_warehouse_layout`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_design_warehouse_layout_agent.py` and in the RCI capsule.

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

Design warehouse layout Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on warehouse layout design from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-design-warehouse-layout
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
    "comparison_period": {
      "description": "Prior period to chart the trend against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-design-warehouse-layout-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_design_warehouse_layout_agent.py` and embedded as the fenced Python below (sha256 8dc38d6037626cf3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_design_warehouse_layout_agent.py` first:

```bash
python3 ppt_exec_design_warehouse_layout_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_design_warehouse_layout_agent.py   # or on stdin
python3 ppt_exec_design_warehouse_layout_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design warehouse layout Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on warehouse layout design from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-design-warehouse-layout
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_design_warehouse_layout',
    "version": '3.0.3',
    "display_name": 'Design warehouse layout Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on warehouse layout design from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-design-warehouse-layout',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-design-warehouse-layout',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b5c6cbc149de7037',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/design-warehouse-layout'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-design-warehouse-layout', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-design-warehouse-layout-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for design warehouse layout reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on design warehouse layout for a 15-minute monthly review. Produce 'ppt-exec-design-warehouse-layout-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads design warehouse layout data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on warehouse layout design from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute exec deck on design warehouse layout from D365 USMF, with charts and speaker notes.', 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-design-warehouse-layout-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready warehouse layout design deck for a monthly review, sourced from D365 ERP without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDesignWarehouseLayout(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDesignWarehouseLayout'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-design-warehouse-layout-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDesignWarehouseLayout().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
