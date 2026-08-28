---
name: "rar-cowork-cookbook-dashboard-analyze-accounts-receivable"
description: "Produces a self-contained interactive HTML dashboard for analyze accounts receivable - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_accounts_receivable", "rar_sha256": "c47cd5ca78e08e51360386c74949d458e4e4943e5c41bc118060592ba6509de1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_accounts_receivable_agent.py` and embedded as the fenced Python below (sha256 c47cd5ca78e08e51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_accounts_receivable_agent.py` first:

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
    "version": '2.0.1',
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
