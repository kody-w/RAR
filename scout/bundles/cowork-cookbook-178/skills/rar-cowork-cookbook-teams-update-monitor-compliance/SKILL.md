---
name: "rar-cowork-cookbook-teams-update-monitor-compliance"
description: "Drafts a Teams channel post on monitor compliance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_compliance", "rar_sha256": "42c9c65bfcc00007a2b3c5254ffe9daff65d55aff46cf5a2e1fdcb87aafc3fa3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_monitor_compliance`. The original RAPP
agent is preserved byte-for-byte in `teams_update_monitor_compliance_agent.py` and in the RCI capsule.

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
