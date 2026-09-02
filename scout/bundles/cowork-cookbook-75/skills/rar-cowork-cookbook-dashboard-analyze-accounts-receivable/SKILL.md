---
name: "rar-cowork-cookbook-dashboard-analyze-accounts-receivable"
description: "Produces a self-contained interactive HTML dashboard for analyze accounts receivable - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_accounts_receivable", "rar_sha256": "f2884838154a21074b09f6ba2c172eb72666d7a9079ba04002d526190f2dace1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_analyze_accounts_receivable_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-analyze-accounts-receivable:accb43c9578d94a29c93b2c2042fc61feba4a216577ef862c9bbc28e14311993", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_analyze_accounts_receivable`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_analyze_accounts_receivable_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
