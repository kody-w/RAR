---
name: "rar-cowork-cookbook-bulk-update-allocate-or-assign-software-licenses"
description: "Applies a bulk field update across allocate or assign software licenses records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_allocate_or_assign_software_licenses", "rar_sha256": "5122f98a2d646493fceea75dac44aaab7611b7626e0b74d42e3bcf269bbfab4f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_allocate_or_assign_software_licenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-allocate-or-assign-software-licenses:0ba2ba54d2e45c1c2bd00838643ec840df8d96c564ff93bc166f75bc047ad0ae", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_allocate_or_assign_software_licenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_allocate_or_assign_software_licenses_agent.py` is
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

Allocate or assign software licenses Bulk Field Update — Applies a bulk field update across allocate or assign software licenses records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-allocate-or-assign-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_allocate_or_assign_software_licenses_agent.py` and embedded as the fenced Python below (sha256 5122f98a2d646493…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_allocate_or_assign_software_licenses_agent.py` first:

```bash
python3 bulk_update_allocate_or_assign_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_allocate_or_assign_software_licenses_agent.py   # or on stdin
python3 bulk_update_allocate_or_assign_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate or assign software licenses Bulk Field Update — Applies a bulk field update across allocate or assign software licenses records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-allocate-or-assign-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_allocate_or_assign_software_licenses',
    "version": '2.0.0',
    "display_name": 'Allocate or assign software licenses Bulk Field Update',
    "description": 'Applies a bulk field update across allocate or assign software licenses records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-allocate-or-assign-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-allocate-or-assign-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eb66051e559910a0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/allocate-or-assign-software-licenses'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-allocate-or-assign-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAllocateOrAssignSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAllocateOrAssignSoftwareLicenses'
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
    print(BulkUpdateAllocateOrAssignSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
