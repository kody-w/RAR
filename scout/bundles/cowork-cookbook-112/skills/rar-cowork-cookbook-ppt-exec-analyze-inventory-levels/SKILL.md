---
name: "rar-cowork-cookbook-ppt-exec-analyze-inventory-levels"
description: "Builds a read-only executive PowerPoint deck on inventory levels from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_inventory_levels", "rar_sha256": "c037276e2b9d88c2d0bf1ce3a7c589b9f53ba4604e0276af67588aa0c61cd859", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
