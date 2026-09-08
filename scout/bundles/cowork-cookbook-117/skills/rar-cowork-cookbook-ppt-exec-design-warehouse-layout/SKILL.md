---
name: "rar-cowork-cookbook-ppt-exec-design-warehouse-layout"
description: "Builds a read-only executive PowerPoint deck on warehouse layout design from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, issues, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_design_warehouse_layout", "rar_sha256": "8dc38d6037626cf3b2d8044be244e6f87a868d9774dfce5c53e8991737a7e136", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
