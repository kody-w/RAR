---
name: "rar-cowork-cookbook-configure-manage-service-accounts-and-certificates"
description: "Applies a bulk configuration change to manage service accounts and certificates from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_service_accounts_and_certificates", "rar_sha256": "ca087ca83d343da1fab0f43cdc5ab92e91c36fdddb7c01e1b8fbbc49bb37beaa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_service_accounts_and_certificates_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-service-accounts-and-certificates:19920de55730c2a27a13e9a3f0ab101f5fdf3a47381c751edd4aa52ff1a47119", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_service_accounts_and_certificates`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_service_accounts_and_certificates_agent.py` is
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
