---
name: "rar-cowork-cookbook-dashboard-analyze-accounts-receivable"
description: "Produces a self-contained interactive HTML dashboard for analyze accounts receivable - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_accounts_receivable", "rar_sha256": "f2884838154a21074b09f6ba2c172eb72666d7a9079ba04002d526190f2dace1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_analyze_accounts_receivable`. The original RAPP
agent is preserved byte-for-byte in `dashboard_analyze_accounts_receivable_agent.py` and in the RCI capsule.

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

Analyze accounts receivable Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for analyze accounts receivable - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-accounts-receivable
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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_accounts_receivable_agent.py` and embedded as the fenced Python below (sha256 f2884838154a2107…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_accounts_receivable_agent.py` first:

```bash
python3 dashboard_analyze_accounts_receivable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_analyze_accounts_receivable_agent.py   # or on stdin
python3 dashboard_analyze_accounts_receivable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze accounts receivable Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for analyze accounts receivable - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-accounts-receivable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_analyze_accounts_receivable',
    "version": '2.0.0',
    "display_name": 'Analyze accounts receivable Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for analyze accounts receivable - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-analyze-accounts-receivable',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-analyze-accounts-receivable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e96e46c708dc6c4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-accounts-receivable'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-analyze-accounts-receivable', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardAnalyzeAccountsReceivable(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAnalyzeAccountsReceivable'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(DashboardAnalyzeAccountsReceivable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
