---
name: "rar-cowork-cookbook-bulk-update-manage-signatures-and-signing-limits"
description: "Applies a bulk field update across manage signatures and signing limits records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_signatures_and_signing_limits", "rar_sha256": "a06aa9f3b9e8afe737f432cbfd44637440438771aeabad2e392c361682a95da2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_signatures_and_signing_limits_agent.py` and embedded as the fenced Python below (sha256 a06aa9f3b9e8afe7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_signatures_and_signing_limits_agent.py` first:

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
    "version": '2.0.1',
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
