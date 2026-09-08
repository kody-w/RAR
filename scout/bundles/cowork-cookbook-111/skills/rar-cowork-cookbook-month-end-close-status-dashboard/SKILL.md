---
name: "rar-cowork-cookbook-month-end-close-status-dashboard"
description: "Builds a one-page month-end close status dashboard for the current period from Dynamics 365 F&SCM data, returning an Excel workbook plus a draft Adaptive Card summary; it does not post to Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/month_end_close_status_dashboard", "rar_sha256": "ea06b8159f6ca6993d4e24e786b0f7ea840cec31dd07dd6651fb71ff2a5e22d5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/month_end_close_status_dashboard`. The original RAPP
agent is preserved byte-for-byte in `month_end_close_status_dashboard_agent.py` and in the RCI capsule.

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

Month-End Close Status Dashboard — Builds a one-page month-end close status dashboard for the current period from Dynamics 365 F&SCM data, returning an Excel workbook plus a draft Adaptive Card summary; it does not post to Teams.

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
  Upstream entry : https://coworkcookbook.com/recipes/month-end-close-status-dashboard
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `month_end_close_status_dashboard_agent.py` and embedded as the fenced Python below (sha256 ea06b8159f6ca699…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `month_end_close_status_dashboard_agent.py` first:

```bash
python3 month_end_close_status_dashboard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 month_end_close_status_dashboard_agent.py   # or on stdin
python3 month_end_close_status_dashboard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Month-End Close Status Dashboard — Builds a one-page month-end close status dashboard for the current period from Dynamics 365 F&SCM data, returning an Excel workbook plus a draft Adaptive Card summary; it does not post to Teams.

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
  Upstream entry : https://coworkcookbook.com/recipes/month-end-close-status-dashboard
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/month_end_close_status_dashboard',
    "version": '3.0.3',
    "display_name": 'Month-End Close Status Dashboard',
    "description": 'Builds a one-page month-end close status dashboard for the current period from Dynamics 365 F&SCM data, returning an Excel workbook plus a draft Adaptive Card summary; it does not post to Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'month-end-close-status-dashboard',
        "upstream_url": 'https://coworkcookbook.com/recipes/month-end-close-status-dashboard',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6d776651561c647e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/month-end-close-status-dashboard', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM read access', 'Output matches: One workbook and one Adaptive Card draft.'], 'confidence': 1.0, 'deliverable': 'One workbook and one Adaptive Card draft.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'where are we on close?' standup chatter with a glanceable RAG dashboard the finance lead can post to Teams.", 'expected_output': 'One workbook and one Adaptive Card draft.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM read access'], 'prompt': 'Build a one-page month-end close status dashboard for the current period. Include: AR sub-ledger reconciliation status, AP sub-ledger reconciliation status, journal posting completeness, FX revaluation completion, period-close switch state, and a RAG (Red/Amber/Green) overall indicator. Produce both an Excel workbook with the data and an Adaptive Card summary that can be posted to a Teams channel. Do not post the card on my behalf.', 'steps': ['Open Cowork and paste the prompt.', 'Review the Adaptive Card before sharing in Teams.'], 'tenant_caveat': 'Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF for December 2017. Cowork executed all 5 plan steps and produced two artifacts: CloseStatus-2017-12.xlsx (Dashboard + 5 supporting sheets) and CloseStatus-2017-12-card.json (Adaptive Card JSON ready to post to a Teams channel). Real RAG status: Overall AMBER. Findings: Period close switch Amber (Dec 2017 still Open, status=1); AR sub-ledger Amber (140 open invoices, $3.62M open, needs reconciliation to GL); AP sub-ledger Green (0 pending vendor invoices, no Dec 2017 AP activity); Journal posting Amber (Batch 00459 unposted, $0.00 MST); FX revaluation Red (not run, 0 transactions revalued). Concrete recommended steps included with specific batch/account references.', 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Builds an at-a-glance close status workbook and an Adaptive Card summary ready to be posted.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a one-page month-end close status dashboard for the current period from Dynamics 365 F&SCM data, returning an Excel workbook plus a draft Adaptive Card summary; it does not post to Teams.', 'example_request': 'Build me a month-end close status dashboard for the current period with a RAG indicator and a Teams card draft.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call during month-end close when you need a single-page status view of AR/AP reconciliation, journal posting, FX revaluation, period-close switch, and a RAG indicator.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and paste the prompt.', 'Review the Adaptive Card before sharing in Teams.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class MonthEndCloseStatusDashboard(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MonthEndCloseStatusDashboard'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(MonthEndCloseStatusDashboard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
