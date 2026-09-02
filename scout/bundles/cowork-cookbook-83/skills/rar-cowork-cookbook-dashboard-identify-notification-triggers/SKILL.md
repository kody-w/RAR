---
name: "rar-cowork-cookbook-dashboard-identify-notification-triggers"
description: "Produces a self-contained interactive HTML dashboard for identify notification triggers - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_notification_triggers", "rar_sha256": "c63619b7a0c3b26ac9a704154749e781a2a532b2147d53685e14435a9755b082", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_identify_notification_triggers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-identify-notification-triggers:6efd9e7d92f768149dca79597ccbaa5a826495c2b1b42163b646ab5a8ceb72c0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_identify_notification_triggers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_identify_notification_triggers_agent.py` is
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
