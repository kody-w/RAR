---
name: "rar-cowork-cookbook-teams-update-monitor-service-quality"
description: "Drafts a Teams channel post on monitor service quality status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_service_quality", "rar_sha256": "7faf13f3eb52ea74afe1234fadeacea603e66b30758ab8145b94f2e7be15ae79", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_monitor_service_quality_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-monitor-service-quality:ee8b518d568a547383588a8ecbf4e1aa2a275db091d1f0b178c2cc91c4956786", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_monitor_service_quality`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_monitor_service_quality_agent.py` is
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

Monitor service quality Teams Channel Update — Drafts a Teams channel post on monitor service quality status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-service-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_service_quality_agent.py` and embedded as the fenced Python below (sha256 7faf13f3eb52ea74…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_service_quality_agent.py` first:

```bash
python3 teams_update_monitor_service_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_monitor_service_quality_agent.py   # or on stdin
python3 teams_update_monitor_service_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service quality Teams Channel Update — Drafts a Teams channel post on monitor service quality status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-service-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_monitor_service_quality',
    "version": '2.0.0',
    "display_name": 'Monitor service quality Teams Channel Update',
    "description": 'Drafts a Teams channel post on monitor service quality status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-monitor-service-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-monitor-service-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'db85b2ce9f36e546',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/monitor-service-quality'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-monitor-service-quality', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateMonitorServiceQuality(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMonitorServiceQuality'
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
    print(TeamsUpdateMonitorServiceQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
