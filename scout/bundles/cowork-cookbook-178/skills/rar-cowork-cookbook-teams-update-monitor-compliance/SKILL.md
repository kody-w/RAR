---
name: "rar-cowork-cookbook-teams-update-monitor-compliance"
description: "Drafts a Teams channel post on monitor compliance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_compliance", "rar_sha256": "42c9c65bfcc00007a2b3c5254ffe9daff65d55aff46cf5a2e1fdcb87aafc3fa3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_monitor_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-monitor-compliance:0b5b8da78700b3a35a4d83483f34022b7484a230ea69800ed32cd5df5b7fb1d9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_monitor_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_monitor_compliance_agent.py` is
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

Monitor compliance Teams Channel Update — Drafts a Teams channel post on monitor compliance status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_compliance_agent.py` and embedded as the fenced Python below (sha256 42c9c65bfcc00007…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_compliance_agent.py` first:

```bash
python3 teams_update_monitor_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_monitor_compliance_agent.py   # or on stdin
python3 teams_update_monitor_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor compliance Teams Channel Update — Drafts a Teams channel post on monitor compliance status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-monitor-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_monitor_compliance',
    "version": '2.0.0',
    "display_name": 'Monitor compliance Teams Channel Update',
    "description": 'Drafts a Teams channel post on monitor compliance status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-monitor-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-monitor-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f322f86c748566b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/monitor-compliance'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-monitor-compliance', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateMonitorCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateMonitorCompliance'
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
    print(TeamsUpdateMonitorCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
