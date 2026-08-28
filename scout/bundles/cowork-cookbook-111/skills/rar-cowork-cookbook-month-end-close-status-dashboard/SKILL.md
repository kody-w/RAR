---
name: "rar-cowork-cookbook-month-end-close-status-dashboard"
description: "Builds a one-page status dashboard summarizing where each close task stands as of today."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/month_end_close_status_dashboard", "rar_sha256": "172221d868f3b44d13a2d20589369706391f05d020bfd670cbd8ab80364e12af", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `month_end_close_status_dashboard_agent.py` and embedded as the fenced Python below (sha256 172221d868f3b44d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `month_end_close_status_dashboard_agent.py` first:

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
    "version": '2.0.0',
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
