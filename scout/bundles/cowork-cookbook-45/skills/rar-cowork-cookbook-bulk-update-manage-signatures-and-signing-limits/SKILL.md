---
name: "rar-cowork-cookbook-bulk-update-manage-signatures-and-signing-limits"
description: "Applies a bulk field update across manage signatures and signing limits records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_signatures_and_signing_limits", "rar_sha256": "2ef211e9c1549936b89dbf9df9cd2e828fae3199591dd6855c29e9d45ecdafdc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_manage_signatures_and_signing_limits_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-manage-signatures-and-signing-limits:98e003f5e45467ad66bca5dac965025f1991970ef575b8cb4062a98567bc6c74", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_manage_signatures_and_signing_limits`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_manage_signatures_and_signing_limits_agent.py` is
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

Manage signatures and signing limits Bulk Field Update — Applies a bulk field update across manage signatures and signing limits records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-signatures-and-signing-limits
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_signatures_and_signing_limits_agent.py` and embedded as the fenced Python below (sha256 2ef211e9c1549936…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_signatures_and_signing_limits_agent.py` first:

```bash
python3 bulk_update_manage_signatures_and_signing_limits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_signatures_and_signing_limits_agent.py   # or on stdin
python3 bulk_update_manage_signatures_and_signing_limits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage signatures and signing limits Bulk Field Update — Applies a bulk field update across manage signatures and signing limits records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-signatures-and-signing-limits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_signatures_and_signing_limits',
    "version": '2.0.0',
    "display_name": 'Manage signatures and signing limits Bulk Field Update',
    "description": 'Applies a bulk field update across manage signatures and signing limits records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-signatures-and-signing-limits',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-signatures-and-signing-limits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4973a21590ea08bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-signatures-and-signing-limits'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-manage-signatures-and-signing-limits', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateManageSignaturesAndSigningLimits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageSignaturesAndSigningLimits'
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
    print(BulkUpdateManageSignaturesAndSigningLimits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
