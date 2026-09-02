---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-store-devices"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and manage store devices status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_store_devices", "rar_sha256": "b9e89db6aa4c95df63cf4b4678dd3d70f460b7c9f4186d5f1a29f772cc365219", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_configure_and_manage_store_devices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-configure-and-manage-store-devices:365a6698140fe3235032a2a8f6e255b956e46d85394c0285387efed2ec3f6702", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_configure_and_manage_store_devices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_configure_and_manage_store_devices_agent.py` is
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

Configure and manage store devices Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and manage store devices status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-store-devices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_manage_store_devices_agent.py` and embedded as the fenced Python below (sha256 b9e89db6aa4c95df…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_manage_store_devices_agent.py` first:

```bash
python3 adaptive_card_configure_and_manage_store_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_and_manage_store_devices_agent.py   # or on stdin
python3 adaptive_card_configure_and_manage_store_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage store devices Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of configure and manage store devices status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-store-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_and_manage_store_devices',
    "version": '2.0.0',
    "display_name": 'Configure and manage store devices Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of configure and manage store devices status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-configure-and-manage-store-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-store-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bd260f225a5ed427',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-store-devices'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-and-manage-store-devices', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardConfigureAndManageStoreDevices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureAndManageStoreDevices'
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
    print(AdaptiveCardConfigureAndManageStoreDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
