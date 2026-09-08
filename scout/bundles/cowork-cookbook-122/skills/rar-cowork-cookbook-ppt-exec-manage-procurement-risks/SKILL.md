---
name: "rar-cowork-cookbook-ppt-exec-manage-procurement-risks"
description: "Builds a read-only executive PowerPoint deck on procurement risk status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_procurement_risks", "rar_sha256": "0325f2022f139bdfc5d6f8e971d6d86baa1f9aa9ae56c279a68d2bbd12a05419", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
