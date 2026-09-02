---
name: "rar-cowork-cookbook-ppt-exec-configure-monitoring-and-alert-systems"
description: "Generates an executive-ready PowerPoint deck on configure monitoring and alert systems status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_monitoring_and_alert_systems", "rar_sha256": "7be7776149cddac41e8e620e82664edb83fbce56d9f6ec930c19cb87e686f350", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_configure_monitoring_and_alert_systems_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-configure-monitoring-and-alert-systems:7b6048e13738b8646000acc1a7747fe2929b067fed2fc5e2597e5e729bb9c917", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_configure_monitoring_and_alert_systems`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_configure_monitoring_and_alert_systems_agent.py` is
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

Configure monitoring and alert systems Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure monitoring and alert systems status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-monitoring-and-alert-systems
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_monitoring_and_alert_systems_agent.py` and embedded as the fenced Python below (sha256 7be7776149cddac4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_monitoring_and_alert_systems_agent.py` first:

```bash
python3 ppt_exec_configure_monitoring_and_alert_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_configure_monitoring_and_alert_systems_agent.py   # or on stdin
python3 ppt_exec_configure_monitoring_and_alert_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure monitoring and alert systems Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on configure monitoring and alert systems status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-configure-monitoring-and-alert-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_configure_monitoring_and_alert_systems',
    "version": '2.0.0',
    "display_name": 'Configure monitoring and alert systems Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on configure monitoring and alert systems status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-configure-monitoring-and-alert-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-configure-monitoring-and-alert-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a09d49aa5eab3a2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/configure-monitoring-and-alert-systems'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-configure-monitoring-and-alert-systems', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecConfigureMonitoringAndAlertSystems(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConfigureMonitoringAndAlertSystems'
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
    print(PptExecConfigureMonitoringAndAlertSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
