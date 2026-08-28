---
name: "rar-cowork-cookbook-bulk-update-discover-suppliers"
description: "Applies a bulk field update across discover suppliers records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_discover_suppliers", "rar_sha256": "dcffd64106606937b3fd26b8e123fd10ef4bd96024d65e8f367f84e1fad0909a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_discover_suppliers`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_discover_suppliers_agent.py` and in the RCI capsule.

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

Discover suppliers Bulk Field Update — Applies a bulk field update across discover suppliers records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-discover-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_discover_suppliers_agent.py` and embedded as the fenced Python below (sha256 dcffd64106606937…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_discover_suppliers_agent.py` first:

```bash
python3 bulk_update_discover_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_discover_suppliers_agent.py   # or on stdin
python3 bulk_update_discover_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Discover suppliers Bulk Field Update — Applies a bulk field update across discover suppliers records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-discover-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_discover_suppliers',
    "version": '2.0.1',
    "display_name": 'Discover suppliers Bulk Field Update',
    "description": 'Applies a bulk field update across discover suppliers records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-discover-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-discover-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '757d5d3848941378',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/discover-suppliers'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-discover-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDiscoverSuppliers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDiscoverSuppliers'
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
    print(BulkUpdateDiscoverSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
