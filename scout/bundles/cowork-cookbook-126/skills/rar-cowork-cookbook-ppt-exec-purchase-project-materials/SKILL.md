---
name: "rar-cowork-cookbook-ppt-exec-purchase-project-materials"
description: "Builds a read-only executive PowerPoint deck on purchase project materials from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_purchase_project_materials", "rar_sha256": "b4f335fd71e21650d42d3cac87e059f5e4f26c45bd24a8e72b8760475efd4da6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
