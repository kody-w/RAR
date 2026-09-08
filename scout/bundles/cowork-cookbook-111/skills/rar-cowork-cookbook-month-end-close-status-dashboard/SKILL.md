---
name: "rar-cowork-cookbook-month-end-close-status-dashboard"
description: "Builds a one-page month-end close status dashboard for the current period from Dynamics 365 F&SCM data, returning an Excel workbook plus a draft Adaptive Card summary; it does not post to Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/month_end_close_status_dashboard", "rar_sha256": "ea06b8159f6ca6993d4e24e786b0f7ea840cec31dd07dd6651fb71ff2a5e22d5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
