---
name: "rar-cowork-cookbook-fx-revaluation-health-check"
description: "Audits FX revaluation setup for the active legal entity in Dynamics 365 F&SCM and returns an Excel workbook 'FX-health-<YYYY-MM-DD>.xlsx' listing misconfigured or skipped monetary accounts with recommendations; read-only"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/fx_revaluation_health_check", "rar_sha256": "d572f487d79724f67542765c231beda7874015002ee08109f02a4857ae7220b7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
