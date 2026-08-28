---
name: "rar-cowork-cookbook-configure-manage-service-accounts-and-certificates"
description: "Applies a bulk configuration change to manage service accounts and certificates from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_service_accounts_and_certificates", "rar_sha256": "ca087ca83d343da1fab0f43cdc5ab92e91c36fdddb7c01e1b8fbbc49bb37beaa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_service_accounts_and_certificates_agent.py` and embedded as the fenced Python below (sha256 ca087ca83d343da1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_service_accounts_and_certificates_agent.py` first:

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
    "version": '2.0.0',
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
