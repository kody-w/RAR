---
name: "rar-cowork-cookbook-ppt-exec-configure-monitoring-and-alert-systems"
description: "Generates an executive-ready PowerPoint deck on configure monitoring and alert systems status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_configure_monitoring_and_alert_systems", "rar_sha256": "9075b05522301fd48612b9bad266fb614808a18dddbf1c160850ffd97a0a7401", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_configure_monitoring_and_alert_systems_agent.py` and embedded as the fenced Python below (sha256 9075b05522301fd4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_configure_monitoring_and_alert_systems_agent.py` first:

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
    "version": '2.0.1',
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
