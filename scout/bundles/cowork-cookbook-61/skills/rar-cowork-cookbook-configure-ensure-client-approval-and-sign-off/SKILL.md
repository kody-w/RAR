---
name: "rar-cowork-cookbook-configure-ensure-client-approval-and-sign-off"
description: "Applies a bulk configuration change to ensure client approval and sign-off from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_ensure_client_approval_and_sign_off", "rar_sha256": "4146c30a1bcd12f98d02cfeecfb34fe1f3eff157d12ebc76c4c99739f78aa72d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_ensure_client_approval_and_sign_off_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-ensure-client-approval-and-sign-off:40735f9e44d3a480c8e6c3cf2cd855cee46facbf95c213ecab87e83d40de8b21", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_ensure_client_approval_and_sign_off`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_ensure_client_approval_and_sign_off_agent.py` is
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
