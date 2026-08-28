---
name: "rar-cowork-cookbook-dashboard-revalue-currency"
description: "Produces a self-contained interactive HTML dashboard for revalue currency - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_revalue_currency", "rar_sha256": "70fc3bdf95b97ea482a1cd4deb5bfd945b1d6ae84f966aa217817476dd655b73", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_revalue_currency`. The original RAPP
agent is preserved byte-for-byte in `dashboard_revalue_currency_agent.py` and in the RCI capsule.

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

Revalue currency Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for revalue currency - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revalue-currency
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_revalue_currency_agent.py` and embedded as the fenced Python below (sha256 70fc3bdf95b97ea4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_revalue_currency_agent.py` first:

```bash
python3 dashboard_revalue_currency_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_revalue_currency_agent.py   # or on stdin
python3 dashboard_revalue_currency_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue currency Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for revalue currency - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-revalue-currency
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_revalue_currency',
    "version": '2.0.0',
    "display_name": 'Revalue currency Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for revalue currency - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-revalue-currency',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-revalue-currency',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a8e65201f2e2061',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/revalue-currency'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-revalue-currency', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardRevalueCurrency(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRevalueCurrency'
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
    print(DashboardRevalueCurrency().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
