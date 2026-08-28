---
name: "rar-cowork-cookbook-configure-manage-service-accounts-and-certificates"
description: "Applies a bulk configuration change to manage service accounts and certificates from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_service_accounts_and_certificates", "rar_sha256": "a98e3faae0ea9db7ae1f8ecf8608a55906bd7d5a3692cd5487f05c90e342abe8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_service_accounts_and_certificates`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_service_accounts_and_certificates_agent.py` and in the RCI capsule.

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

Manage service accounts and certificates Configuration Bulk Setup — Applies a bulk configuration change to manage service accounts and certificates from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-service-accounts-and-certificates
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_service_accounts_and_certificates_agent.py` and embedded as the fenced Python below (sha256 a98e3faae0ea9db7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_service_accounts_and_certificates_agent.py` first:

```bash
python3 configure_manage_service_accounts_and_certificates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_service_accounts_and_certificates_agent.py   # or on stdin
python3 configure_manage_service_accounts_and_certificates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service accounts and certificates Configuration Bulk Setup — Applies a bulk configuration change to manage service accounts and certificates from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-service-accounts-and-certificates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_service_accounts_and_certificates',
    "version": '2.0.1',
    "display_name": 'Manage service accounts and certificates Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage service accounts and certificates from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-manage-service-accounts-and-certificates',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-service-accounts-and-certificates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eba8546eb57b7775',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-service-accounts-and-certificates'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-service-accounts-and-certificates', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageServiceAccountsAndCertificates(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageServiceAccountsAndCertificates'
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
    print(ConfigureManageServiceAccountsAndCertificates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
