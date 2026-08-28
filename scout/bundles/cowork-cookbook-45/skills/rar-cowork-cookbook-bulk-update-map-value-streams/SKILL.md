---
name: "rar-cowork-cookbook-bulk-update-map-value-streams"
description: "Applies a bulk field update across map value streams records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_map_value_streams", "rar_sha256": "8eec2670a3a968b3100dd190aee04fdbbc3e25c6e7f43941efe686650e718ed0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_map_value_streams`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_map_value_streams_agent.py` and in the RCI capsule.

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

Map value streams Bulk Field Update — Applies a bulk field update across map value streams records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-map-value-streams
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_map_value_streams_agent.py` and embedded as the fenced Python below (sha256 8eec2670a3a968b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_map_value_streams_agent.py` first:

```bash
python3 bulk_update_map_value_streams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_map_value_streams_agent.py   # or on stdin
python3 bulk_update_map_value_streams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map value streams Bulk Field Update — Applies a bulk field update across map value streams records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-map-value-streams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_map_value_streams',
    "version": '2.0.1',
    "display_name": 'Map value streams Bulk Field Update',
    "description": 'Applies a bulk field update across map value streams records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-map-value-streams',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-map-value-streams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '104f195cb65884be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/map-value-streams'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-map-value-streams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateMapValueStreams(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMapValueStreams'
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
    print(BulkUpdateMapValueStreams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
