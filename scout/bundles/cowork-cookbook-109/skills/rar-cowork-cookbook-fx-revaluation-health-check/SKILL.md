---
name: "rar-cowork-cookbook-fx-revaluation-health-check"
description: "Audits FX revaluation setup for the active legal entity in Dynamics 365 F&SCM and returns an Excel workbook 'FX-health-<YYYY-MM-DD>.xlsx' listing misconfigured or skipped monetary accounts with recommendations; read-only"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/fx_revaluation_health_check", "rar_sha256": "d572f487d79724f67542765c231beda7874015002ee08109f02a4857ae7220b7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/fx_revaluation_health_check`. The original RAPP
agent is preserved byte-for-byte in `fx_revaluation_health_check_agent.py` and in the RCI capsule.

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

FX Revaluation Health Check — Audits FX revaluation setup for the active legal entity in Dynamics 365 F&SCM and returns an Excel workbook 'FX-health-<YYYY-MM-DD>.xlsx' listing misconfigured or skipped monetary accounts with recommendations; read-only

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
  Upstream entry : https://coworkcookbook.com/recipes/fx-revaluation-health-check
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `fx_revaluation_health_check_agent.py` and embedded as the fenced Python below (sha256 d572f487d79724f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `fx_revaluation_health_check_agent.py` first:

```bash
python3 fx_revaluation_health_check_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 fx_revaluation_health_check_agent.py   # or on stdin
python3 fx_revaluation_health_check_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
FX Revaluation Health Check — Audits FX revaluation setup for the active legal entity in Dynamics 365 F&SCM and returns an Excel workbook 'FX-health-<YYYY-MM-DD>.xlsx' listing misconfigured or skipped monetary accounts with recommendations; read-only

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
  Upstream entry : https://coworkcookbook.com/recipes/fx-revaluation-health-check
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/fx_revaluation_health_check',
    "version": '3.0.3',
    "display_name": 'FX Revaluation Health Check',
    "description": "Audits FX revaluation setup for the active legal entity in Dynamics 365 F&SCM and returns an Excel workbook 'FX-health-<YYYY-MM-DD>.xlsx' listing misconfigured or skipped monetary accounts with recommendations; read-only",
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
        "upstream_slug": 'fx-revaluation-health-check',
        "upstream_url": 'https://coworkcookbook.com/recipes/fx-revaluation-health-check',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eb81ff4446ba059c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/fx-revaluation-health-check', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the General ledger user role', 'Output matches: Workbook listing misconfigured accounts and missed runs.'], 'confidence': 1.0, 'deliverable': 'Workbook listing misconfigured accounts and missed runs.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Prevents misstated currency exposure by catching unflagged monetary accounts and skipped revaluations before they hit the financials.', 'expected_output': 'Workbook listing misconfigured accounts and missed runs.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the General ledger user role'], 'prompt': "Audit the FX revaluation setup for the active legal entity. For each monetary main account: confirm it is flagged for revaluation, the appropriate gain/loss accounts are configured, and there has been a revaluation run in the current period. Build an Excel report 'FX-health-<YYYY-MM-DD>.xlsx' listing any account that is misconfigured or appears to have been skipped, with the suggested fix in a 'Recommendation' column. Do not post or change anything.", 'steps': ['Open Cowork and paste the prompt.', 'Review the workbook with the GL team before changing any setup.'], 'tenant_caveat': "Validated against a live Cowork tenant on 2026-05-23 with USMF. Cowork engaged the D365 ERP plugin and researched the right entities (CurrencyGainLossAccountType enum, GeneralJournalAccountEntries, LedgerJournalLines + LedgerJournalHeaders, CurrencyRevaluationAccountsV2, MainAccounts filtered by Monetary=Yes + ForeignCurrencyRevaluation) and produced a detailed audit methodology / quick-reference for FX revaluation. Honesty note: on this run Cowork stopped after step 1 of 4 in the plan - it built the audit reference rather than executing the full Excel workbook. Re-running with a tighter 'produce the workbook now, do not pre-explain' prompt typically advances all 4 plan steps. The screenshot captures the research output, which is itself useful as a one-page handover document for the GL team.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Detects misconfigured monetary accounts and missed FX revaluation runs.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Audits FX revaluation setup for the active legal entity in Dynamics 365 F&SCM and returns an Excel workbook 'FX-health-<YYYY-MM-DD>.xlsx' listing misconfigured or skipped monetary accounts with recommendations; read-only", 'example_request': 'Run an FX revaluation health check for our active legal entity and give me the workbook.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants to check FX revaluation configuration and current-period run status before period close, without posting or changing anything.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and paste the prompt.', 'Review the workbook with the GL team before changing any setup.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class FxRevaluationHealthCheck(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FxRevaluationHealthCheck'
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
    print(FxRevaluationHealthCheck().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
