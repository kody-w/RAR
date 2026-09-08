---
name: "rar-cowork-cookbook-ppt-exec-manage-procurement-risks"
description: "Builds a read-only executive PowerPoint deck on procurement risk status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_procurement_risks", "rar_sha256": "0325f2022f139bdfc5d6f8e971d6d86baa1f9aa9ae56c279a68d2bbd12a05419", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_procurement_risks`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_procurement_risks_agent.py` and in the RCI capsule.

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

Manage procurement risks Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on procurement risk status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks
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
    "briefing_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull procurement data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-manage-procurement-risks-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_procurement_risks_agent.py` and embedded as the fenced Python below (sha256 0325f2022f139bdf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_procurement_risks_agent.py` first:

```bash
python3 ppt_exec_manage_procurement_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_procurement_risks_agent.py   # or on stdin
python3 ppt_exec_manage_procurement_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement risks Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on procurement risk status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_procurement_risks',
    "version": '3.0.3',
    "display_name": 'Manage procurement risks Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on procurement risk status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-procurement-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-procurement-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1883079969826972',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/manage-procurement-risks'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-manage-procurement-risks', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'briefing_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull procurement data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-procurement-risks-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for manage procurement risks reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on manage procurement risks for a 15-minute monthly review. Produce 'ppt-exec-manage-procurement-risks-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage procurement risks data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on procurement risk status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build an executive procurement risk deck from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull procurement data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-procurement-risks-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'briefing_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready procurement risk deck from D365 ERP data for a short monthly review, without modifying any source data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecManageProcurementRisks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageProcurementRisks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'briefing_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull procurement data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-procurement-risks-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review).', 'type': 'string'}},
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
    print(PptExecManageProcurementRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
