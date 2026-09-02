---
name: "rar-cowork-cookbook-configure-manage-signatures-and-signing-limits"
description: "Applies a bulk configuration change to manage signatures and signing limits from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_signatures_and_signing_limits", "rar_sha256": "fdb9fc77fdc2a924a3384e113549f5c3164c5088ee1480cffae15c7559c04710", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_signatures_and_signing_limits_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-signatures-and-signing-limits:72649e420c6ff1a10f837885d12df5a5015bdd17030efcea62c75a578ff57448", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_signatures_and_signing_limits`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_signatures_and_signing_limits_agent.py` is
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
