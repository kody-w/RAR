---
name: "rar-cowork-cookbook-gl-trial-balance-variance"
description: "Compares the most recent posted GL period to the prior period for a legal entity, flags accounts with variance >= $10,000 or >= 10%, and returns an Excel workbook plus a draft email to the controller."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/gl_trial_balance_variance", "rar_sha256": "8e1980e116808dd09d33dd994a9999b30945ed218831c5583baabc8c545dc818", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/gl_trial_balance_variance`. The original RAPP
agent is preserved byte-for-byte in `gl_trial_balance_variance_agent.py` and in the RCI capsule.

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

GL Trial Balance Variance Report — Compares the most recent posted GL period to the prior period for a legal entity, flags accounts with variance >= $10,000 or >= 10%, and returns an Excel workbook plus a draft email to the controller.

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
  Upstream entry : https://coworkcookbook.com/recipes/gl-trial-balance-variance
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
    "controller_recipient": {
      "description": "Recipient of the draft summary email; user edits recipients before sending.",
      "type": "string"
    },
    "current_period": {
      "description": "The most recent posted period to compare, e.g. March 2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
    "prior_period": {
      "description": "The prior period to compare against, e.g. February 2017.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `gl_trial_balance_variance_agent.py` and embedded as the fenced Python below (sha256 8e1980e116808dd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `gl_trial_balance_variance_agent.py` first:

```bash
python3 gl_trial_balance_variance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 gl_trial_balance_variance_agent.py   # or on stdin
python3 gl_trial_balance_variance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
GL Trial Balance Variance Report — Compares the most recent posted GL period to the prior period for a legal entity, flags accounts with variance >= $10,000 or >= 10%, and returns an Excel workbook plus a draft email to the controller.

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
  Upstream entry : https://coworkcookbook.com/recipes/gl-trial-balance-variance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/gl_trial_balance_variance',
    "version": '3.0.3',
    "display_name": 'GL Trial Balance Variance Report',
    "description": 'Compares the most recent posted GL period to the prior period for a legal entity, flags accounts with variance >= $10,000 or >= 10%, and returns an Excel workbook plus a draft email to the controller.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'gl-trial-balance-variance',
        "upstream_url": 'https://coworkcookbook.com/recipes/gl-trial-balance-variance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0eedf1ce300d7a58',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/gl-trial-balance-variance', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the General ledger user role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: An Excel workbook with Material/All sheets and a draft email summarizing the top variances.'], 'confidence': 1.0, 'deliverable': 'An Excel workbook with Material/All sheets and a draft email summarizing the top variances.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'controller_recipient': 'Recipient of the draft summary email; user edits recipients before sending.', 'current_period': 'The most recent posted period to compare, e.g. March 2017.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'prior_period': 'The prior period to compare against, e.g. February 2017.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts month-end review time by focusing the controller on the GL accounts with material variances instead of every line in the trial balance.', 'expected_output': 'An Excel workbook with Material/All sheets and a draft email summarizing the top variances.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the General ledger user role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin, query the trial balance for the most recent posted period AND the prior period for the same chart of accounts in legal entity USMF. For each posting account: compute the variance amount and the variance percent. Mark any account where |variance| >= $10,000 OR |variance %| >= 10% as 'material'.\n\nUse the Excel skill to produce a workbook 'TB-variance-<YYYY-MM>.xlsx' with two sheets: 'Material' (variances that crossed the threshold, sorted by absolute variance amount descending) and 'All' (every account).\n\nThen draft an email to the controller summarizing the count of material variances and the top 5 by amount. Do not modify any data.\n\n(Tenant note: the USMF demo tenant's posted GL activity is mostly FY2017 — if you want guaranteed data, ask Cowork to use March 2017 vs February 2017 explicitly. Cowork will derive the comparison from posted ledger journal lines if no trial-balance snapshot exists.)", 'steps': ['Open Cowork and paste the prompt.', 'Approve the read-only data access when prompted.', 'Review the produced workbook in the side panel.', 'Edit the email draft recipients before sending.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF demo data. Cowork executed the full 5-step plan (find trial balance entity → query March/February 2017 → compute variances → build workbook → draft email), produced 'TB-variance-2017-03.xlsx' with 8 material accounts and an 'All' sheet of 9 posting accounts, and saved a controller email draft summarizing the top 5 by absolute variance. Because USMF has no saved trial-balance snapshots for 2017, Cowork honestly derived the comparison from posted LedgerJournalLines activity rather than running balances — see the screenshot for the agent's note on this. For a tenant with running trial-balance snapshots you'll get period-end positions instead of period activity; both shapes are useful for variance review.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Pulls the trial balance for two consecutive periods, computes variance, flags material lines, and produces a workbook + email draft.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Compares the most recent posted GL period to the prior period for a legal entity, flags accounts with variance >= $10,000 or >= 10%, and returns an Excel workbook plus a draft email to the controller.', 'example_request': 'Run a GL trial balance variance report for USMF, March 2017 vs February 2017, and draft the controller email.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The most recent posted period to compare, e.g. March 2017.', 'name': 'current_period'}, {'description': 'The prior period to compare against, e.g. February 2017.', 'name': 'prior_period'}, {'description': 'Recipient of the draft summary email; user edits recipients before sending.', 'name': 'controller_recipient'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only period-over-period GL trial balance variance report with a material-variance workbook and a controller summary email.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and paste the prompt.', 'Approve the read-only data access when prompted.', 'Review the produced workbook in the side panel.', 'Edit the email draft recipients before sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class GlTrialBalanceVariance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GlTrialBalanceVariance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'controller_recipient': {'description': 'Recipient of the draft summary email; user edits recipients before sending.', 'type': 'string'}, 'current_period': {'description': 'The most recent posted period to compare, e.g. March 2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'prior_period': {'description': 'The prior period to compare against, e.g. February 2017.', 'type': 'string'}},
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
    print(GlTrialBalanceVariance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
