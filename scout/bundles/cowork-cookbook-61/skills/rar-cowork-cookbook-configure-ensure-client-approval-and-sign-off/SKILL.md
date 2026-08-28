---
name: "rar-cowork-cookbook-configure-ensure-client-approval-and-sign-off"
description: "Applies a bulk configuration change to ensure client approval and sign-off from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_ensure_client_approval_and_sign_off", "rar_sha256": "4146c30a1bcd12f98d02cfeecfb34fe1f3eff157d12ebc76c4c99739f78aa72d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_ensure_client_approval_and_sign_off`. The original RAPP
agent is preserved byte-for-byte in `configure_ensure_client_approval_and_sign_off_agent.py` and in the RCI capsule.

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

Ensure client approval and sign-off Configuration Bulk Setup — Applies a bulk configuration change to ensure client approval and sign-off from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-ensure-client-approval-and-sign-off
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_ensure_client_approval_and_sign_off_agent.py` and embedded as the fenced Python below (sha256 4146c30a1bcd12f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_ensure_client_approval_and_sign_off_agent.py` first:

```bash
python3 configure_ensure_client_approval_and_sign_off_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_ensure_client_approval_and_sign_off_agent.py   # or on stdin
python3 configure_ensure_client_approval_and_sign_off_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Ensure client approval and sign-off Configuration Bulk Setup — Applies a bulk configuration change to ensure client approval and sign-off from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-ensure-client-approval-and-sign-off
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_ensure_client_approval_and_sign_off',
    "version": '2.0.0',
    "display_name": 'Ensure client approval and sign-off Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to ensure client approval and sign-off from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-ensure-client-approval-and-sign-off',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-ensure-client-approval-and-sign-off',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8c59a3aaa163d652',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/ensure-client-approval-and-sign-off'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/configure-ensure-client-approval-and-sign-off', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureEnsureClientApprovalAndSignOff(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureEnsureClientApprovalAndSignOff'
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
    print(ConfigureEnsureClientApprovalAndSignOff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
