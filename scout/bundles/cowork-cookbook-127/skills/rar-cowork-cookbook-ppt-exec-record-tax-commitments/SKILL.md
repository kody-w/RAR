---
name: "rar-cowork-cookbook-ppt-exec-record-tax-commitments"
description: "Builds a read-only executive PowerPoint deck on record tax commitments from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_record_tax_commitments", "rar_sha256": "e31ab5c2b5049e96663442f5d72b92746f33560f3ac16656b9d8a0260fe35e34", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_record_tax_commitments`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_record_tax_commitments_agent.py` and in the RCI capsule.

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

Record tax commitments Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on record tax commitments from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-record-tax-commitments
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
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-record-tax-commitments-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_record_tax_commitments_agent.py` and embedded as the fenced Python below (sha256 e31ab5c2b5049e96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_record_tax_commitments_agent.py` first:

```bash
python3 ppt_exec_record_tax_commitments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_record_tax_commitments_agent.py   # or on stdin
python3 ppt_exec_record_tax_commitments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record tax commitments Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on record tax commitments from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-record-tax-commitments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_record_tax_commitments',
    "version": '3.0.3',
    "display_name": 'Record tax commitments Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on record tax commitments from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-record-tax-commitments',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-record-tax-commitments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '439f5b16594c6a41',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-tax-commitments'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-record-tax-commitments', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-record-tax-commitments-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for record tax commitments reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on record tax commitments for a 15-minute monthly review. Produce 'ppt-exec-record-tax-commitments-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads record tax commitments data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on record tax commitments from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': "Build the exec PowerPoint on record tax commitments for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-record-tax-commitments-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (monthly review).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on record tax commitments sourced from Dynamics 365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecRecordTaxCommitments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRecordTaxCommitments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-record-tax-commitments-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (monthly review).', 'type': 'string'}},
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
    print(PptExecRecordTaxCommitments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
