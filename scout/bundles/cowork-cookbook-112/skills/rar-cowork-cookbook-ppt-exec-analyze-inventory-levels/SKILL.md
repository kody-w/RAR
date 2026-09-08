---
name: "rar-cowork-cookbook-ppt-exec-analyze-inventory-levels"
description: "Builds a read-only executive PowerPoint deck on inventory levels from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_inventory_levels", "rar_sha256": "c037276e2b9d88c2d0bf1ce3a7c589b9f53ba4604e0276af67588aa0c61cd859", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_analyze_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_analyze_inventory_levels_agent.py` and in the RCI capsule.

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

Analyze inventory levels Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on inventory levels from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-inventory-levels
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
      "description": "Prior period to trend current inventory levels against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to analyze, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-analyze-inventory-levels-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 c037276e2b9d88c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_inventory_levels_agent.py` first:

```bash
python3 ppt_exec_analyze_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_analyze_inventory_levels_agent.py   # or on stdin
python3 ppt_exec_analyze_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze inventory levels Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on inventory levels from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_analyze_inventory_levels',
    "version": '3.0.3',
    "display_name": 'Analyze inventory levels Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on inventory levels from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-analyze-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-analyze-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '062ad2a2f965d736',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/analyze-inventory-levels'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/ppt-exec-analyze-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend current inventory levels against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-analyze-inventory-levels-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for analyze inventory levels reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on analyze inventory levels for a 15-minute monthly review. Produce 'ppt-exec-analyze-inventory-levels-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze inventory levels data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on inventory levels from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Make an exec PowerPoint on inventory levels for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-analyze-inventory-levels-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend current inventory levels against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready inventory-level deck for a short monthly review, sourced from D365 ERP without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecAnalyzeInventoryLevels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAnalyzeInventoryLevels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend current inventory levels against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-analyze-inventory-levels-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecAnalyzeInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
