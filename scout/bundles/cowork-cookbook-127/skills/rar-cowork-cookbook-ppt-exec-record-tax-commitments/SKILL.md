---
name: "rar-cowork-cookbook-ppt-exec-record-tax-commitments"
description: "Builds a read-only executive PowerPoint deck on record tax commitments from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_record_tax_commitments", "rar_sha256": "e31ab5c2b5049e96663442f5d72b92746f33560f3ac16656b9d8a0260fe35e34", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
