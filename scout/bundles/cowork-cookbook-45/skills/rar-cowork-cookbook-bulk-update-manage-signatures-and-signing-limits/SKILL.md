---
name: "rar-cowork-cookbook-bulk-update-manage-signatures-and-signing-limits"
description: "Applies a bulk field update across manage signatures and signing limits records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_signatures_and_signing_limits", "rar_sha256": "2ef211e9c1549936b89dbf9df9cd2e828fae3199591dd6855c29e9d45ecdafdc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_signatures_and_signing_limits`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_signatures_and_signing_limits_agent.py` and in the RCI capsule.

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
