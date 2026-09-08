---
name: "rar-cowork-cookbook-gl-trial-balance-variance"
description: "Compares the most recent posted GL period to the prior period for a legal entity, flags accounts with variance >= $10,000 or >= 10%, and returns an Excel workbook plus a draft email to the controller."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/gl_trial_balance_variance", "rar_sha256": "8e1980e116808dd09d33dd994a9999b30945ed218831c5583baabc8c545dc818", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adejxpLmX9G8PTO2m6oSi0BQfe6cYdHKKrEK1z1ldhCrWAUe//dJJL1Vdl/7dvc582lk15GAzMiIyIjniXjJX9+cro3L+u3zmxo4xWLnZFkSB/XCKfwFWw5lnYKvMnXBv4VXFm2duF1b1s3bhzc/aLw6qdqkLMB0tswrpw6aRRsHi7xs2kUdeEHRLirwO/AXO2FRBXVS+ou2fIypwEX9fi8EP51FFkROtgCTknb8sAgzJ2oWjueVXdE2iyFp40Xv1IlTeMHif/1t8d8R+AMMwwswFVwh8P/48NC6DtquLsDEYrG5e0G2mI146F9lHbi98GsnbBdB7iTZuy4Py8osC+pPwLDg7uRVFjRvn3/++4e3BPx++/zrm5c5Dbj1tss0oEPGONmsiPFSCEwD1xF4Xo3AoQW4BqYBs3Jwyw/CxevqxybIwg+Lf/3XdHDqqPnp85di8fp8eZv/O3fFQ6W2dB5+85zKcZMMeOTTgs4GZ2y+W7howH4U0afnzO+Symrxt/nZj89FPkVB++OXtxKo4My79eXtp9lpX97qbv79aZZS/fjTp6wcgvrHn77LaTr3GnjtLAxo/enr6/olFgz8PjQJF19VZcO+1gJ7n1QBEP47++bPU/WXuJdLvj4H/1hWHxZ/Lnm2529A32fEuUDun4sFPgAz3z5dy6T48bVGXfZBMe/Qjz/9lVgvDrw0S5r2PyX356fgOHB84K2XS3768Ni+vy+gl23fZP71shUImP+KJWD4+3LfHPVXsh87++9EZ0kB0vN9L/9U3J9NgP62+PkvbftnE0AGf3njgizpQdy5WfB58esjRH7+wf9+84e//wZE/4di1LKrvYeEr7lTJGHQtF+//vxD87j9w99//qGrQBQHTv61q7M/k/lnfn2s8wcPvkb9+Me5YH29SItyKBbfcmjxa1n9t/q3TwvDyRL/+/3m8+L3mTh/oMVsxPuiTxf8LhsboOvv/PjT228AcwpgTec9HgP8+Jd/WYiJV5dNCYBLBXgIwBVgYpIHs/JanDSL5Am8dQD82iTAsa9xIP7nHZ41LsPFL//be2D6R++F6cso+9rOcPbVfeLZ13eE/eXTQgMCyzqJkgKg8plWlC+FE82QDharANQHdQ8Ayh3b4CPI44/zj0VSLH75S5lfH9M/VeMvD6ROnkh3Zg8zyjVdFnya7THjoHhp7wEQD+6B1wHJWekBNcIEAPMHYGdTZj1Aydn2Jk2ybOEnAEcANY1PFuiKz7OwX375xXWa+EvxhGVs8eSsZgkGfFNn8fEjsCfMkihuvxSBF5eLH3797YfF/1n8s1kP4fMaCiCGl/eBhkdVlhYgm7o8mGlr3koAFQ/v//rby6tATAFIFuxVEiYvzgTRmAb+u4vVPf0RxYmFGwDXArfmVVm3AOsXSftpcQgX3/QFi86PZjaIZ9b1gyoo/KDwRiDVAeZ882RRtosGhFwTAnLtmuCx6i9u7TxUzEFaO+0vC5FVAPeUD2qsX1wEJpdFAtz/LQCe94GQ+odmwbyL+LSQ5vhbgELAqeLaea0ROs99mTn+NR0IdxZFMHwpZnoNZlc9kuHpHjAIeMZ7benHec8BRecg8/3mfe3HGGdmSO3BlPWXonkFOihD5uIDAD9YNOoSf469f3uFVBOXXeY//Ac0nSW9dsF/7cojBkG18mD5xYvmF+88vzg/3L340qEwslr8/1L1zDbTu915s6O1DbfYSNr58tyLedBs0LNOBCo+tH7k3ffS5B1+3lH4S5ElILDq8d+eIx87+BrzRLauBt450+eHfBA+YC9muY/onqO1rue8cL4U73APzFw8sA1sMIACkCqzGe8Lzk/fNY1Bvs/X36n/EQ21PzsKRPCi6twMRFcYBL7reCnQqp4z9LWlINSDOVuHOPHiP1g17xGIKCB/AZRIwO4ASvj0DYKfT99V/8PEZ4UzT3lUfx1I0PohAOgRzArOWzhvNVCvfdbYwM7Pr4gBMdbOtrsgRYClz5tBHdy6pEnaGQ6ffg0qgMEf5++npfPd4F6BrADOArFfdcC7j2yZgSQH9QvQAQAGSJ48KQCfA6e8nPAQ6ORz6gNofQXXU+Lj9sug4JFiMxG9T5wNmefM3L4Igergzvh7hND+LEyAvHwe8Vj330fat9Vm2TNKNgDpwIrvT59FwKcnjz8LhcW73M//0MT8+F/rcx7MrP8xAD4v4ratms/L5ZNN38n0E8Co5VPXBhDrxwcJfnyR4Mf3JP6DwKetnxf/NaX+IOKVFJ8XyCf4Ezw/El5B9foAH7AfmcvH1fz0S3EOvkMnWL7MQVTNOzYCJv/Gc+9DANlFNcAnMPjJe81MlwNg6AfQA/d/KX4f5XOWAR4pojkqm/J32f8gfBDxz936xkfgUdGCtf25IIyCuf165EQTvH0uuiz78FaAePtnbddMNvkcw83cpYFsAeDaJsHj6gEJ93b++cduVX78cLJPCy4A8JM1v4+zF0XMFPm7dHhaB6zywAofFj7wSTOjMLBuXnxOJacBsQnCcraiHatZ7WeHNtd039H22fAkwPB/VOz8/miGoHnZJ243HWA/EHoP/P63B/EuAn/25zdZzXut0AD+n7vCP1Wiq2sw9uuTgP5xee3Paew7h3lPwvuwCD5FnxaiUwOMBC5a/+lqD2b7+mS2f1yLwwh8sf2fKiv+gQLnVW4dwJXXGroqbv9U+rcK+h9Fm6CUmeX45eeZ1T+8QBR8g+j5sPjWwIBtfLWUj76/6EC3/vPcPM1x9Zgy/wBzwNe3Sd/+9OEGb3//E70eFP9PPfyHIuC7U0F19IDJl+HbwK27edP/wr9gqQcHACadtf7uju9KlY/27qFU5rTPv0b8+gayxQHh67zy5dUfgOEAMj82c5W0BFgCFgTXz6wHz/7zncNrYhM7oIAFM8kAoUg4QBCChEnfhykfw3yfolYOBT4uBlMrPPBRhCQxxMNxEnMdx/VID1/hvkciJJD3BI2vcw2YzMrMmgAfAIQNgu+PwS3/ZcVT698eu/FqVGZrX8b8+uYSKzByv2oO9PPDLinEIzDBPVcuNBFheQ9Wze2cqmmHIRM7UFpqmrYdYGvxlPF4xvPqILPc+XhmWXrF8vaNiG9hB3OuCGt4WqAy5MMr2D6lhWLnVa7f4BOLOb5SkC0mtKi4mhIOQZdGcLaJ1Krjs7FunKWJxMQSXuljoRpOuV8uCQkzVXd76OF1ekOyqk3r+ykPbcTiI73AzOjEaoZpR5tbGq+0Q9nnForeN75ytm5bQ6MrQbCv7WUkDWdFYvCS78Sr4RtJg9iGD7lKQbRksL+gyrVc6VUnuCWhhNejbjFIgvKCeNmgEgK1eyt1K7lp2m2ajTeJre8mbdrtOOpYEcf2vrin6+shTa5qrjWXvUBBoeUSUH8lKV4nloFArpnWKuwmbhm0FyT7yESOjaMHH29qTM/J87k/NZmCWo6Bp2jbiGXBngO/QPPT3YurHXqa2IgSN9V5L6Gh6Ka9xpk7W5RYJABL0KsR5g8I0zY9F3tEPdHb1jSm/jAkhqlDx8C5m7lVrgNzWptWDWXrPDEsOXfsk7o9biv2xBRxINyEkwF3bbSyCmt1KHQ6vmTWRnVwvUFCnaCkoF3aTNck2NnI6SjeOipxjxKZCP1R6wUPbRwjwjXtLMEtM9ZihMP3VmGixDXV/S5dHbbWdpuveLptvF0tMgfbgPmLZcXbJFkeT/ayXovNxJ06/3qAIV+LXZcNsUzwj9xS2xtKloV6bFesswuOCB7EypZ33ZGGtjtGKFSUDcTTFcMC5axMUsuutrBl5pFr6GvR4C4Oykb3qkg1Esbinj7B/aDxgSuZAseW29O9uZcObkSSs2N6VrXc7mYkgqqf4xDPb/6Fs9ZSuuQnKTj1xiGEeHk0+HA4u0d8uSk25MYLJWGKpTASkDtN6sEgX05kNKi+HUasY611RMmsukyvExHs4ukuUSK5RFISjcVjGda34/GkRXfzFMsaP2JSVxyVW3iDkfimXzlUQUwFY8H/u2WwS8Rxie6XR1y0MHiC6JHc29gtWxl6sDvtTO16GQ6ZoBsJivJ9MIksRndMOlKIU3NMshnC5FAEfteVurvidPPobpQ8saWpU/sebIZURQV3hoq1zeAJfox21s7bsvX+tr7ScLo5eElTTsOO4Dp7Iihs6qxb50YOzKohhqxp2SZu3rTpNdaVpoSB1xcsDYf79e73Cc7vzol0OrTTNhU8Qt52vsXC4gCTN+WojRxzXNr4RrYrfIcVWX+kmu1Sgsfj/rSUw+OZu6wvBQM3K2gytXZJgwRdulvxMHKbxpmATcc7TWN7vo/LZmSgIoUYco1Dm15hFKHU0ctGs5cHTLa34g0KY20bZwPO7viJ6suDv6MEZluV4tKaIFzxFXyqhHhSuPSyvN9GzYWrleONN7kfSYrN3enQqqR7j8WOviMXiZyojcB5dySEPTzP1F26a6IAIpll0OGkdrPXncKNMOMvvWY6hYjV39ZcequhS87pyqmOVfIcrjb74RYh6KmrO4bZHVf36+rITcpGunHbi0OfL2vFId09a9NHjEwoZteUJqhYxit94C/DFjXW1x1BxfHg3lflOaaZU7UKK8IIsnGZLvdTul1JMr5aYQxSWE57lSb4Oo5jEllB5BaymnkkeSVLY/Ib4e6i0zpbNlZ57Su/pXeNe8MTVl4K2WEgj8i07HDJxX1UleB0Oh5NXVzvrmwdk5wornJfinNWsUfvxoQhz47JuU8dSNQgYtADL2p22cZNPJWLFbq4pBJByZaXnTXZvobOaXvJ6Lgujhrp+tlBU9PjVPl7/sRXim367mZDww0ZRxVqGroB9oxWeWkSauUCsm+zy2w6ZOsmbJFTvCtIwTG6dSRfRJZn0jKQKpUcujqLKtOlKd9k2ousITWvgKljwJ+aSuNalJK1ernydlXMhs0mVgb4lqpXklvlnivYpc9cQ4BnwcFHe6X1uSJZu37M7CbsUB6IE8KuQiisj7CxHxhoWe1XiJ/rmcx4J5JEFWYbaUOUT0eQuhI/LnlJ35bddtyFcWqg0BbeouT1xufjNOWrobruzytqqUwZIRcFGW/sZoyOV3Iq2nKzMUnTM8iCFeCzFFGH02B2bHhoNqRKcKeDrssnFzmm+iBCIukMYwJRhxUh0RBd9czJa8uEhASPHKzGvh+NywaZdnf2UCLuobTDrZSYlpOq2VhTWo1chUJc8z5Jb6ouOKn7lX2O9/dQU+Dyck9F6EyXpXuhDjw2TDv3XlFqdLy05jrzMfqe7cY7x+4DWTvZk3pONqt1vw251vRx+pB4+75ctuW04bbMJggPUORhWaC3fEPY7dpJNp5BK3xNx4V87KD6FpWKrG5Vrddvk3JMVo1M3gVoKSDbWt/p93Oe5ReKSBgmisfVcIysA5UFyT6k/LqGadYwrifzYKTEyOrWKNVeGCGbTEDOqRHswrY+DctdodIgRHYbTTE4/WTHZYS3USGXSsLhfEQXeiw7u94mClCjqxhzFHZ0KZr38yqbrJbu2619vguneGWGRj7hWgcF9LJArucNly1d73g/qpRcSsRW4s7MFF0MQxj4BNc8jF7t6Dvrk9lQDYl6dNFTxLf3YYQOW0W75cdBlE6wqAdHb2M76lI9VJbKyRwM/Jt5vH5m9ki8S7fKZRvc+tS7q+JI4Tu9jbX4jt44eHNCfYNVqpAqk01zTWVXKyjU8pPDDj0sLxmTKNypRTp01xDdYYd7U5HB+VAYQ9iUXCFeARi6/c08ZvTmwHqCKfS1n9SAIx3OPsbcpp44iFK0EaRPsBaLdH/M+u1xc1NMx4EYmavTKtpJZtWS/chq5y0jS6dYxYY94W83oBeS2HSL66kSR1e9wvIcMBQ6jeuSxUupqoidcaDYe5qrtCRAVqOh3Biq0kmjDGFFGY1+W0JLTznKYwlHfKMWZc4g43RluZVxYFsj4imx1O2oy5HkDrrXzQ3TmqXPD7SYHGRPcpTRSiM5YiNjDxknf02d8l4e1rejNpBL+lJUfC9Z6YSPXZsnei/d+4goIE1nz73KdwS/92wx2LEjzqheddh7V5Z3tFtCVtLlEBdUHg+ngg8dI/a8krytrGBPD5DEn867KEkaqwZobKZcOK5HKTmf1HpVtMK6CCj2aPX2CW6kdDyplX6og311u8nX8lRW2wiSmVsdATLcXoZyu+bOxbZirIKwU2xzxzAQrbsgOQTjBbmik0XGp8RlAVqo960Lypd7y5QZ4KPq5tODwez9MVYPAm0fU0APMZYGN2t7vfY1Xtdpm1tQcWtaoR1L1bv0+4qk5EjRDqRg38V94tcCehtdSbPOKydObvsJWflwbdxVzgShoTkNVN9TutsfMeCjVXX2bVU9nKycqJnDATnCJoxu2Pq6AzkBW0N2Dgz3qBfHQEWi09rckGi23JplTVh+e2PLlS+LhuOnFcrL+9BuKyQfRM/2UMJN+mqwUsbJgAyGXt1yV7yQqHzqBCZw7yKZJSG19JjBhfKkkgcxdAjkHKxZMRydBjtJaUPdtrrZUoYDWi+zpNxxRNukd25VjmMQq/TY1cZG9Yau1RKgg8vjKAfjzr3BzNrAr6Bgb9oTM7qkIaKEwJ+crYJk7iD1pma0NsExNsnx16lP6w7Q2Ro5yrShUAmoYM+ujkABoi51F1sNoVrRXF5uLhPDUVS/QpdJbSnRCcaPOqut9s7JyzzDcNElR55tw9SWa5gLCbff91geNvfxSspX2+k3qMzYGwndaeatv9BXAfJDs7aP1cDQ0yo5bfJcxRlQDFxbsyNBtDKXIcWPOHts9qG1KQ/4hcPaC06Z/YYOONDcVp2MrGKvNG7Bfbrw5YXEx2watSHeJ6p+NBRnwxJYzTL8uUoEWMuRgq6IGjLgSB84lErorYVvGQszqptGrMSbR1Ts9lC1OHXCmB0cGB6fo6qTd0lA8+MhWPJcizfafrupGglWUjHbllzr1jyKxkfhdEjtcWN6MmhGkCMZbZDQUUXQcqDANkx2adS6F/lSJcvmmJH5jrXkVaoi7JU17gjO7098E6us2w2hvuvonAmUbTYW8AW/5KPj6PLkytY9Ua+ZCGmCICUbWlU2uCW4ySnPzR1XXOVc34LS+oTupVPuyjQKkoDdmqJP2mftvkEgIb8kRiHtd6wObzo0TgWErfRdRAm6FZ82xT2Od5mabzdn+X4Tt6JX6/zmJtO23CfWeSxBg4YetJYJqTNknhMFNOYnZCvi/u2Ynku0vHZTVNC7BPTPRTjAenPVvfaG0lhWlrcO9QpQdTbxwVXMcpOupLvglybPcMbo77RjopGN5WRsssLlxtoF57QfZQtqVp3WWZrhraKVKAfiPUfdoCsFd0OtT97ZENZan5rdkMuZuDEuNa60bbYWp6y1Lrec9weZw9WD4R/dq2BQxFgvR6sTK5eqNH7Ad9e6zzfM6khf41KDUBcvBJiSKOOAmV1dxrRlirKn64aacqzlyZKNooJtruu1FHnwzuNNo2KXdy5HzYCA9XDtadtM3AtaoyCywNDtwF4MadDSyIijvEESpk3OZ4yRmzxzd4fxekRZpuwwQs8Ou/Ut5CX/2glB5E9boWWGvNiRHNIoFGkhN7LSYZViDS+277J50bXdXZF50eppHUnzEo8v+bRveqZYha0Hy8e2GjrAnSe96NXrBTQASlpr4hGG9kjQSZVCYwPpMEjIhkTD8mQGqmTYJrQuj7Y1GmTaLr/EUrvXLDGKm6SlqfGubP1Ur1db7kI0dod7nX5h+1qq9N7ahGaRJYp+5Ld47fK7APP84Qr1Ti0IPn+7h6eeqg582ehjPcqVizNeJ976FpTBcHs/Qak6VTfJR3he0G6qaF4QKJbvGw/XELugDqHYwMR+4i6xforze2RjZkvC2Xjb8DR/cfW9SudIOrZd7cNnttNitokDyZPOAUy4ZyIVN/bQLhUlVawch2hiS2jTuE0dBk6EymIPNttdeo4BKGCIN9fDrI29vOejBAXkYXmrO78qrUqmVxyrwY5BIAePkraIHqSF46Dj5HlB0WVXHwcdEUmsZb+Upat1XCOVb+zb/pLwuHClukI5llaBrW4C5bWOj7p1Dh+LSyAF/n0J111u6u2KMG7LUK/5c72PshqOi/5a0sxgb3jZMHq/2aKRrFjrsrbvtwq+tEVFXTU+zBGRgOQUhft17EibCed9v+2Va+FRKnKSEG5NAFgm9p7K2pu6wt0Iul5ALymZo+ab9yZBjPEsJF4vaeh6Qwl7x4lrqpzkofOp/rqHLpDaMJiWVLh/Ru9iKKNMJaoD7O3dqLMZDjRPe3EQed9Vluu2Xiag5Kz4UVdSYlpu+uEi52smnm6gA1ojTaaFQ34Q9pWPqwVT4nYy8UzpTfKyjM64RfJ6xmFQ7nnYxt1StFhd0E136OMDTpOH/fle0LJFHXOZy2ptuFliIROlyR2vgdaXym7Y5pzFivfTDZp4T8KvV3GTi+O528mdrwAc73FmrDcwVQB4jpzLmSc0ueigtdrY4qpp8O4SpuTadY8pva9DW9jdhnG7xiREDDqtv2Z+Ooqgm3DbpOx2igV1fIy1ark2OUhSl+uaSE10ZaWlNWycE7cBvLq/rgBxnjIbFd1VcvT4oG3PeKxantDkglLvz23LTe7WuYnNWA4U7Uhr73qgCjzNfCreXTxxuTnnGg7bbAMJlaPonOVu1E6Y6GRz30GjvazwzjmdsyrdRfYwaSxK+b4u4jdn4469HlcRkeKREqTaZqtlMOMG1flCKh7Jdg2u2K1991YBzktVKAdweuSIPsdwH7SAZNARZLk/dattuw5LnDORgFD2RXEkElmvyj4aKcUjcqmPL/4F2QbOkjBoVCxMTeUUaLgWKKGN4Th4OJVj5ToVJOSA9Lg8gES77+RasuExqeVVuWbNPh/WkyM7LC5fr67k+4w5XrDaKji7PR4TTiaIaBha6AoKY/pa8yt2jxO6n1y6wlYIaZi8cwW6p1urIOLOg/EUvUXQ5Tbkkgh56Lg2SqJoBldNR44zulCjPcs9ib1V2xfoYkZ8rJcGWWpMs44j86Ss6/AIKr9bGXl7euo8++zrLnqkl9h5y0HjEGEN7dg+ttxv7kWQt+ZS14i2mozu4pPEJEG+cZ/WKRSsdaHzZMs8iHmYkfjKq8Od7Jup5051VNG25+4acmWay7p36/gWrJfHi4KnpxgToNQSKI33hR7u6LHowjPHQHoLUFzuGJ036wJXdetqDxBl1Kaw25oEUl+HTctTCU6shU7ZufBA9ENt53BoQ5gc7rtzy+Q8l4nYISiPukDcsQOx8hleVjUSLSGKFVcd2YPoYrPomBWgsz5Ve1Rxzv4GPNnzW3YnkIUOJSWJehm3tXL14IUY2yO3TdJd2n1aXO+JtowmgbsAdEVTdK9aI7+2WH9tXo7pka+aes84GqRT620oCYkNUz4tR5ZIBLeiYQ+aXh2ExiU3kgTHhIidkL3Y1J7PK8MKr8IzjPVnvzVxybPjk3d1TQlTwxtgvoDJ9ml9AB36QVd5ae1LKFypU2dKmWu3k3QhMNLe8SrKSQE+/7Vo7bVX0Sxl51hIAyx4g1ewxbQ+4doSo7dUfbRk6mze+TqHxqSvIXa4RXG6xip3VDBXDSDUJtIW8Zq4PysbmDXMjtCiXmJ32RZeV5BB0bLu5lWlY7GMxdm4u/pT3sRX4+pAiJsFCI8WAcLlxxDZpVQt69hYZ2XodVNgXGR5WTX3xkUTZTycLwd8HyTnaWDtLbMitHjZw32hUdqIYJ3RsNgpMBPfAL0AhOV6hWhN3VnmVO8hxzjaIbdqslsXUDaK48eRVy703V1VuLzaYyody6TCcqrEIXTUx41rVP2YoebomiqVkIOs+S1KgdYVCnpvGEzquIm7CxPdNP7c+vgghDSKdhO+joy+uRP0homo+7hdbQ+NuII22llpA9KkmZGQrARV13YlQcusIpurbGgJu7z4oKPNh6yw1lbJhMZShc3hbnAorw2KESDuKjhbCOap1tT0xKk4+r5m97wPXXvK9YtlS0JmO5HEnl82Jo0ug30Qh16CNwqtD1Pgq+06EIT8cLve8rx1KwG2JgHUrWSPeMvYhhCvQgppV+6tCEfs3uLBUhhGGorIU6elJioOvhPzTdi3Lhaq4l4kzVCDQFVl3Kkd0pKg3bjb/DVWVr7EqweauxlXQoIHtYroJLglwuFqH2v5iqy87d66C61pNslxBW/7MfcSh2ti11GTaOXtQd1ztDmRoHDBze5hC8ttPwmXc92tQ0pdmunK6lZ4u75XSOepS2mp70EXXa2d9RT0p6ljq1Q5uVe7OKu3w+3i047u7RocJfDb/u5DSw4bnJRrhy0fLumTAJ9tsEPLwuMPyJLl1o6HKPEgWJEubZdCjhOiEi1daUuoNbKjafpvbx/e5vMFr1MC//HRw/l14f+zN5PPF4zvx4we744Dx//8WOvzf0KXv394q70EaPJ839pkXfR6gfnv3rZ+/MvjJPO08Xl+7/2ww/PcROtE8wn2t6Twu6atx69NmT2OFYEZbtfMZ1+b+Xi0B75//7r7eZ7w8WM+8PC1Lb9+u5UU81mhwE+cNnhdRq+Xzh/e/BFsQuI1XzEC/xrU1Wzd63AKMAr7BH/C3n77v6aPyBxxMAAA -->
