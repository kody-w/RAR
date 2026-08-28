---
name: "rar-cowork-cookbook-dashboard-revalue-currency"
description: "Produces a self-contained interactive HTML dashboard for revalue currency - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_revalue_currency", "rar_sha256": "735a853235b26a5cc611fc5e48107f2abd35800f358d6cb2a51bae295b6a321b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_revalue_currency_agent.py` and embedded as the fenced Python below (sha256 735a853235b26a5c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_revalue_currency_agent.py` first:

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
    "version": '2.0.1',
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
