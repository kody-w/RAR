---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-store-devices"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and manage store devices status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_store_devices", "rar_sha256": "b9e89db6aa4c95df63cf4b4678dd3d70f460b7c9f4186d5f1a29f772cc365219", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_configure_and_manage_store_devices`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_configure_and_manage_store_devices_agent.py` and in the RCI capsule.

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
