---
name: "rar-cowork-cookbook-month-end-close-status-dashboard"
description: "Builds a one-page status dashboard summarizing where each close task stands as of today."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/month_end_close_status_dashboard", "rar_sha256": "172221d868f3b44d13a2d20589369706391f05d020bfd670cbd8ab80364e12af", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "month_end_close_status_dashboard_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/month-end-close-status-dashboard:bfc52dabbae4aa0bae8f9a5b49aadf376b1b39968ab1b61dfae27e378dcd4009", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/month_end_close_status_dashboard`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `month_end_close_status_dashboard_agent.py` is
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
