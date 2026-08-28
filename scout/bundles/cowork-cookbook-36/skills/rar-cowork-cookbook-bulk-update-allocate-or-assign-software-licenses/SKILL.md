---
name: "rar-cowork-cookbook-bulk-update-allocate-or-assign-software-licenses"
description: "Applies a bulk field update across allocate or assign software licenses records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_allocate_or_assign_software_licenses", "rar_sha256": "0c7714dd4ef9f85d3e7c09e29cc90cfe8fff988e564ec3bd3106ea65503133c5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_allocate_or_assign_software_licenses_agent.py` and embedded as the fenced Python below (sha256 0c7714dd4ef9f85d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_allocate_or_assign_software_licenses_agent.py` first:

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
    "version": '2.0.1',
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
