---
name: "rar-cowork-cookbook-period-close-checklist"
description: "Produces a period-close checklist for the active legal entity's current month covering AR/AP aging, FX revaluation, sub-ledger reconciliations, accrual reversals, journal posting, and the close switch, with owner roles a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/period_close_checklist", "rar_sha256": "b1b3b6bc760b21c75802e8e4d490d4d31bf45810655145c6b0a2081d9cc43f0f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
