---
name: "rar-cowork-cookbook-ppt-exec-configure-monitoring-and-alert-systems"
description: "Generates an executive-ready PowerPoint deck on configure monitoring and alert systems status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_monitoring_and_alert_systems", "rar_sha256": "7be7776149cddac41e8e620e82664edb83fbce56d9f6ec930c19cb87e686f350", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_configure_monitoring_and_alert_systems`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_configure_monitoring_and_alert_systems_agent.py` and in the RCI capsule.

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
