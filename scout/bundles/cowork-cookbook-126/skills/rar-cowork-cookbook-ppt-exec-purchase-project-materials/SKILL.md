---
name: "rar-cowork-cookbook-ppt-exec-purchase-project-materials"
description: "Builds a read-only executive PowerPoint deck on purchase project materials from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_purchase_project_materials", "rar_sha256": "b4f335fd71e21650d42d3cac87e059f5e4f26c45bd24a8e72b8760475efd4da6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_purchase_project_materials`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_purchase_project_materials_agent.py` and in the RCI capsule.

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

Purchase project materials Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on purchase project materials from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-purchase-project-materials
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
      "description": "Prior period to compare against in the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull purchase project materials data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-purchase-project-materials-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_purchase_project_materials_agent.py` and embedded as the fenced Python below (sha256 b4f335fd71e21650…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_purchase_project_materials_agent.py` first:

```bash
python3 ppt_exec_purchase_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_purchase_project_materials_agent.py   # or on stdin
python3 ppt_exec_purchase_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purchase project materials Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on purchase project materials from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-purchase-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_purchase_project_materials',
    "version": '3.0.3',
    "display_name": 'Purchase project materials Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on purchase project materials from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-purchase-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-purchase-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '961ca8e0f4de6482',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/purchase-project-materials'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-purchase-project-materials', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull purchase project materials data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-purchase-project-materials-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for purchase project materials reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on purchase project materials for a 15-minute monthly review. Produce 'ppt-exec-purchase-project-materials-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads purchase project materials data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on purchase project materials from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint on purchase project materials for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull purchase project materials data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-purchase-project-materials-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing purchase project materials status from D365 ERP for a monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPurchaseProjectMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPurchaseProjectMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull purchase project materials data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-purchase-project-materials-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecPurchaseProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
