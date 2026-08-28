---
name: "rar-cowork-cookbook-dashboard-identify-notification-triggers"
description: "Produces a self-contained interactive HTML dashboard for identify notification triggers - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_notification_triggers", "rar_sha256": "c63619b7a0c3b26ac9a704154749e781a2a532b2147d53685e14435a9755b082", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_notification_triggers_agent.py` and embedded as the fenced Python below (sha256 c63619b7a0c3b26a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_notification_triggers_agent.py` first:

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
    "version": '2.0.0',
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
