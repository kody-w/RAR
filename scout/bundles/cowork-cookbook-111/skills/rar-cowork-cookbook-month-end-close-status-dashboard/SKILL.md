---
name: "rar-cowork-cookbook-month-end-close-status-dashboard"
description: "Builds a one-page status dashboard summarizing where each close task stands as of today."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/month_end_close_status_dashboard", "rar_sha256": "bf31bf92be9dab84b969edc9cfead49ac0ddad00fa5a1877339ce02d2df336ef", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

Month-End Close Status Dashboard — Builds a one-page status dashboard summarizing where each close task stands as of today.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `month_end_close_status_dashboard_agent.py` and embedded as the fenced Python below (sha256 bf31bf92be9dab84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `month_end_close_status_dashboard_agent.py` first:

```bash
python3 month_end_close_status_dashboard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 month_end_close_status_dashboard_agent.py   # or on stdin
python3 month_end_close_status_dashboard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Month-End Close Status Dashboard — Builds a one-page status dashboard summarizing where each close task stands as of today.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.1',
    "display_name": 'Month-End Close Status Dashboard',
    "description": 'Builds a one-page status dashboard summarizing where each close task stands as of today.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a6e6afcdebca360d',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class MonthEndCloseStatusDashboard(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MonthEndCloseStatusDashboard'
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
    print(MonthEndCloseStatusDashboard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
