---
name: "rar-cowork-cookbook-scheduled-brief-monitor-service-assets"
description: "Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_service_assets", "rar_sha256": "bb3815b5db90efa669934689260c5ae71ed08777cdcc7d70637135e241008113", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_monitor_service_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-monitor-service-assets:e96a935ab0056cca0c93fe18801bf8e5fdc65d05b6a31f439ada7c0e8bfe3df6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_monitor_service_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_monitor_service_assets_agent.py` is
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

Monitor service assets Scheduled Email Brief — Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_service_assets_agent.py` and embedded as the fenced Python below (sha256 bb3815b5db90efa6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_service_assets_agent.py` first:

```bash
python3 scheduled_brief_monitor_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_service_assets_agent.py   # or on stdin
python3 scheduled_brief_monitor_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service assets Scheduled Email Brief — Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_service_assets',
    "version": '2.0.0',
    "display_name": 'Monitor service assets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing monitor service assets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-monitor-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b39251510a4eaee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/monitor-service-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-monitor-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefMonitorServiceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorServiceAssets'
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
    print(ScheduledBriefMonitorServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
