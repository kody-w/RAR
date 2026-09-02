---
name: "rar-cowork-cookbook-configure-prioritize-notifications"
description: "Applies a bulk configuration change to prioritize notifications from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_prioritize_notifications", "rar_sha256": "443f1af4bd6bae13af2b7e9d3abe34374857699deef7f4dbd6d9eed1757d91ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_prioritize_notifications_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-prioritize-notifications:0b8aeff63187b9a8589785a50f25b46520223a8fa468c12b7f993afbb1b59dbb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_prioritize_notifications`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_prioritize_notifications_agent.py` is
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

Prioritize notifications Configuration Bulk Setup — Applies a bulk configuration change to prioritize notifications from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-prioritize-notifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_prioritize_notifications_agent.py` and embedded as the fenced Python below (sha256 443f1af4bd6bae13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_prioritize_notifications_agent.py` first:

```bash
python3 configure_prioritize_notifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_prioritize_notifications_agent.py   # or on stdin
python3 configure_prioritize_notifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prioritize notifications Configuration Bulk Setup — Applies a bulk configuration change to prioritize notifications from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-prioritize-notifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_prioritize_notifications',
    "version": '2.0.0',
    "display_name": 'Prioritize notifications Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to prioritize notifications from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-prioritize-notifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-prioritize-notifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '526041cd3f860787',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/prioritize-notifications'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-prioritize-notifications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigurePrioritizeNotifications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePrioritizeNotifications'
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
    print(ConfigurePrioritizeNotifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
