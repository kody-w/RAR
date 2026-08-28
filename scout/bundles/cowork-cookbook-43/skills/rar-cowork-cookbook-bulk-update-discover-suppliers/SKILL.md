---
name: "rar-cowork-cookbook-bulk-update-discover-suppliers"
description: "Applies a bulk field update across discover suppliers records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_discover_suppliers", "rar_sha256": "e62abca6d07946b404132d793cfb907af58fdf71a1ffd440e195a3a507eabf6a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_discover_suppliers_agent.py` and embedded as the fenced Python below (sha256 e62abca6d07946b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_discover_suppliers_agent.py` first:

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
    "version": '2.0.0',
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
