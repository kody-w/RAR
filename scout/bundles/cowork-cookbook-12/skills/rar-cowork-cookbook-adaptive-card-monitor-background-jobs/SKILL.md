---
name: "rar-cowork-cookbook-adaptive-card-monitor-background-jobs"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor background jobs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_background_jobs", "rar_sha256": "5f5978346dd372e146bce071abd8419abe6fbcf7021987675ae77fd158d4f511", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_monitor_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-monitor-background-jobs:d511700a0ea2edf8973aa8269e7b87f573c8ddf0b521209c8ac4f9880ab37caa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_monitor_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_monitor_background_jobs_agent.py` is
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

Monitor background jobs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor background jobs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_background_jobs_agent.py` and embedded as the fenced Python below (sha256 5f5978346dd372e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_background_jobs_agent.py` first:

```bash
python3 adaptive_card_monitor_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_background_jobs_agent.py   # or on stdin
python3 adaptive_card_monitor_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor background jobs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor background jobs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_background_jobs',
    "version": '2.0.0',
    "display_name": 'Monitor background jobs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of monitor background jobs status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-monitor-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51fce9282dbb24fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/monitor-background-jobs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-monitor-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardMonitorBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorBackgroundJobs'
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
    print(AdaptiveCardMonitorBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
