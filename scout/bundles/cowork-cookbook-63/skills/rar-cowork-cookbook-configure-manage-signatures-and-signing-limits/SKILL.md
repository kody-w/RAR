---
name: "rar-cowork-cookbook-configure-manage-signatures-and-signing-limits"
description: "Applies a bulk configuration change to manage signatures and signing limits from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_signatures_and_signing_limits", "rar_sha256": "ee6c41562ec4f9de3c9899558be2b935c575e2901b5e28021f8319aadf642535", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_signatures_and_signing_limits`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_signatures_and_signing_limits_agent.py` and in the RCI capsule.

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

Manage signatures and signing limits Configuration Bulk Setup — Applies a bulk configuration change to manage signatures and signing limits from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-signatures-and-signing-limits
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_signatures_and_signing_limits_agent.py` and embedded as the fenced Python below (sha256 ee6c41562ec4f9de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_signatures_and_signing_limits_agent.py` first:

```bash
python3 configure_manage_signatures_and_signing_limits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_signatures_and_signing_limits_agent.py   # or on stdin
python3 configure_manage_signatures_and_signing_limits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage signatures and signing limits Configuration Bulk Setup — Applies a bulk configuration change to manage signatures and signing limits from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-signatures-and-signing-limits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_signatures_and_signing_limits',
    "version": '2.0.1',
    "display_name": 'Manage signatures and signing limits Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage signatures and signing limits from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-manage-signatures-and-signing-limits',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-signatures-and-signing-limits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a68bfe034119dee6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-signatures-and-signing-limits'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-signatures-and-signing-limits', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageSignaturesAndSigningLimits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageSignaturesAndSigningLimits'
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
    print(ConfigureManageSignaturesAndSigningLimits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
