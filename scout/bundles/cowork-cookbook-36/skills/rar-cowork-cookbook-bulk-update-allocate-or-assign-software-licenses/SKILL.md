---
name: "rar-cowork-cookbook-bulk-update-allocate-or-assign-software-licenses"
description: "Applies a bulk field update across allocate or assign software licenses records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_allocate_or_assign_software_licenses", "rar_sha256": "5122f98a2d646493fceea75dac44aaab7611b7626e0b74d42e3bcf269bbfab4f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_allocate_or_assign_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_allocate_or_assign_software_licenses_agent.py` and in the RCI capsule.

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
