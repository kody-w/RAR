---
name: "rar-cowork-cookbook-period-close-checklist"
description: "Produces a period-close checklist for the active legal entity's current month covering AR/AP aging, FX revaluation, sub-ledger reconciliations, accrual reversals, journal posting, and the close switch, with owner roles a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/period_close_checklist", "rar_sha256": "b1b3b6bc760b21c75802e8e4d490d4d31bf45810655145c6b0a2081d9cc43f0f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/period_close_checklist`. The original RAPP
agent is preserved byte-for-byte in `period_close_checklist_agent.py` and in the RCI capsule.

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

Period Close Checklist Generator — Produces a period-close checklist for the active legal entity's current month covering AR/AP aging, FX revaluation, sub-ledger reconciliations, accrual reversals, journal posting, and the close switch, with owner roles a

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
  Upstream entry : https://coworkcookbook.com/recipes/period-close-checklist
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
      "description": "The active Dynamics 365 F&SCM legal entity the checklist is generated for.",
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
    "period": {
      "description": "The close period, defaulting to the current month.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `period_close_checklist_agent.py` and embedded as the fenced Python below (sha256 b1b3b6bc760b21c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `period_close_checklist_agent.py` first:

```bash
python3 period_close_checklist_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 period_close_checklist_agent.py   # or on stdin
python3 period_close_checklist_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Period Close Checklist Generator — Produces a period-close checklist for the active legal entity's current month covering AR/AP aging, FX revaluation, sub-ledger reconciliations, accrual reversals, journal posting, and the close switch, with owner roles a

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
  Upstream entry : https://coworkcookbook.com/recipes/period-close-checklist
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/period_close_checklist',
    "version": '3.0.3',
    "display_name": 'Period Close Checklist Generator',
    "description": "Produces a period-close checklist for the active legal entity's current month covering AR/AP aging, FX revaluation, sub-ledger reconciliations, accrual reversals, journal posting, and the close switch, with owner roles a",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'period-close-checklist',
        "upstream_url": 'https://coworkcookbook.com/recipes/period-close-checklist',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1da2baa5937af53e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/period-close-checklist', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM read access', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: One Word document and one Communications summary.'], 'confidence': 1.0, 'deliverable': 'One Word document and one Communications summary.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'The active Dynamics 365 F&SCM legal entity the checklist is generated for.', 'period': 'The close period, defaulting to the current month.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Standardizes the close calendar so nothing slips, and gives the controller a single-page view to chase owners across legal entities.', 'expected_output': 'One Word document and one Communications summary.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM read access', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Generate a period-close checklist for the active legal entity for the current month. Include: AR aging review, AP aging review, FX revaluation status, sub-ledger reconciliations (AR/AP/Inventory), accrual reversals, period-end journal posting, and the period-close switch. For each item include suggested owner role and an ETA in business days. Output as a Word document and as a chat-ready Communications draft summarizing the list.', 'steps': ['Open Cowork and paste the prompt.', 'Review the produced checklist and customize for your team.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF Dec 2017 (also USMF's fiscal year-end). Cowork ran all three plan steps and produced both 'USMF_Period_Close_Checklist_Dec_2017.docx' AND a chat-ready Communications draft. The 7-task table includes AR aging review (AR Accountant, 1bd), AP aging review (AP Accountant, 1bd), FX revaluation (Sr. GL Accountant, 1bd), Sub-ledger recs (GL Accountant, 2bd), Accrual reversals (GL Accountant, 1bd), Period-end journals (GL Accountant + Controller, 2bd), and Period-close switch (Controller, 1bd). Cowork added a sharp FY-end reminder: 'coordinate year-end close with Controller before flipping the period to Closed; variances on control accounts 130100 / 200100 / 140200 / 140400 must be cleared before item 7'.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Produces a tailored period-close checklist as both a Word document and a Communications-ready summary.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Produces a period-close checklist for the active legal entity's current month covering AR/AP aging, FX revaluation, sub-ledger reconciliations, accrual reversals, journal posting, and the close switch, with owner roles a", 'example_request': "Generate this month's period-close checklist for our active legal entity with owners and ETAs.", 'inputs': [{'description': 'The active Dynamics 365 F&SCM legal entity the checklist is generated for.', 'name': 'legal_entity'}, {'description': 'The close period, defaulting to the current month.', 'name': 'period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call at month-end when you need a tailored period-close task list with suggested owner roles and ETAs for the active legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and paste the prompt.', 'Review the produced checklist and customize for your team.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PeriodCloseChecklist(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PeriodCloseChecklist'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'The active Dynamics 365 F&SCM legal entity the checklist is generated for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'period': {'description': 'The close period, defaulting to the current month.', 'type': 'string'}},
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
    print(PeriodCloseChecklist().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
