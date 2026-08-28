---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-store-devices"
description: "Produces a reusable Adaptive Card JSON snapshot of configure and manage store devices status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_store_devices", "rar_sha256": "e8af2a22d550629c8df424d3b3ab3c94868565293126a681a46f31c6012f2d79", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_manage_store_devices_agent.py` and embedded as the fenced Python below (sha256 e8af2a22d550629c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_manage_store_devices_agent.py` first:

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
    "version": '2.0.1',
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
