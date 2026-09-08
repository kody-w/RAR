---
name: "rar-cowork-cookbook-ppt-exec-correct-ledger-vouchers"
description: "Builds a read-only executive PowerPoint deck on correct ledger vouchers from Dynamics 365 F&SCM data for a legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_correct_ledger_vouchers", "rar_sha256": "b9ae050cee2d576a7afa1423de2a8c00e1d55430e5f4e9e200c5d7a3e9306a2f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_correct_ledger_vouchers`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_correct_ledger_vouchers_agent.py` and in the RCI capsule.

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

Correct ledger vouchers Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on correct ledger vouchers from Dynamics 365 F&SCM data for a legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-ledger-vouchers
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
      "description": "Target .pptx filename, e.g. ppt-exec-correct-ledger-vouchers-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_correct_ledger_vouchers_agent.py` and embedded as the fenced Python below (sha256 b9ae050cee2d576a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_correct_ledger_vouchers_agent.py` first:

```bash
python3 ppt_exec_correct_ledger_vouchers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_correct_ledger_vouchers_agent.py   # or on stdin
python3 ppt_exec_correct_ledger_vouchers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct ledger vouchers Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on correct ledger vouchers from Dynamics 365 F&SCM data for a legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-ledger-vouchers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_correct_ledger_vouchers',
    "version": '3.0.3',
    "display_name": 'Correct ledger vouchers Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on correct ledger vouchers from Dynamics 365 F&SCM data for a legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-correct-ledger-vouchers',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-correct-ledger-vouchers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e8b2c51eb4938f30',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/correct-ledger-vouchers'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-correct-ledger-vouchers', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'briefing_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-correct-ledger-vouchers-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for correct ledger vouchers reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on correct ledger vouchers for a 15-minute monthly review. Produce 'ppt-exec-correct-ledger-vouchers-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads correct ledger vouchers data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on correct ledger vouchers from Dynamics 365 F&SCM data for a legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive PowerPoint deck on correct ledger vouchers for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-correct-ledger-vouchers-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'briefing_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a monthly executive review deck on correct ledger vouchers status from D365 ERP data, without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecCorrectLedgerVouchers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCorrectLedgerVouchers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'briefing_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-correct-ledger-vouchers-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).', 'type': 'string'}},
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
    print(PptExecCorrectLedgerVouchers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
