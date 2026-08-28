---
name: "rar-cowork-cookbook-teams-update-monitor-compliance"
description: "Drafts a Teams channel post on monitor compliance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_monitor_compliance", "rar_sha256": "99f0b48b3fac208cb5b162cb329b1534b76cceffbbb1a24a417e2ab31f0c25b9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_monitor_compliance_agent.py` and embedded as the fenced Python below (sha256 99f0b48b3fac208c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_monitor_compliance_agent.py` first:

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
    "version": '2.0.1',
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
