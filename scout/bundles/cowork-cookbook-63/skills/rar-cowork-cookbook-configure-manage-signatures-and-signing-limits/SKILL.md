---
name: "rar-cowork-cookbook-configure-manage-signatures-and-signing-limits"
description: "Applies a bulk configuration change to manage signatures and signing limits from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_signatures_and_signing_limits", "rar_sha256": "fdb9fc77fdc2a924a3384e113549f5c3164c5088ee1480cffae15c7559c04710", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_signatures_and_signing_limits_agent.py` and embedded as the fenced Python below (sha256 fdb9fc77fdc2a924…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_signatures_and_signing_limits_agent.py` first:

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
    "version": '2.0.0',
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
