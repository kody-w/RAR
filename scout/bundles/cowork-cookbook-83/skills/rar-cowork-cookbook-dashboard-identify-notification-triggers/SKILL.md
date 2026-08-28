---
name: "rar-cowork-cookbook-dashboard-identify-notification-triggers"
description: "Produces a self-contained interactive HTML dashboard for identify notification triggers - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_notification_triggers", "rar_sha256": "d32df23a838e5dbdc685672ebaa2419a1a46d60632c0ed620775c154bf0b5323", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_notification_triggers`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_notification_triggers_agent.py` and in the RCI capsule.

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

Identify notification triggers Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify notification triggers - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-notification-triggers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_notification_triggers_agent.py` and embedded as the fenced Python below (sha256 d32df23a838e5dbd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_notification_triggers_agent.py` first:

```bash
python3 dashboard_identify_notification_triggers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_notification_triggers_agent.py   # or on stdin
python3 dashboard_identify_notification_triggers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify notification triggers Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify notification triggers - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-notification-triggers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_notification_triggers',
    "version": '2.0.1',
    "display_name": 'Identify notification triggers Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for identify notification triggers - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-identify-notification-triggers',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-notification-triggers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0439ace214f4763f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/identify-notification-triggers'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-identify-notification-triggers', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardIdentifyNotificationTriggers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyNotificationTriggers'
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
    print(DashboardIdentifyNotificationTriggers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
