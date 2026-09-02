---
name: "rar-cowork-cookbook-bulk-update-map-value-streams"
description: "Applies a bulk field update across map value streams records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_map_value_streams", "rar_sha256": "2eb55f48a7fbf89322b76ff2c7bf0dccd24844ac2406b43a2a3b0520942ecc6a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_map_value_streams_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-map-value-streams:96b1c5e4ca61fe5ac375743af32a00000a38c6141868c12d8690c7f0f633b525", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_map_value_streams`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_map_value_streams_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_map_value_streams_agent.py` and embedded as the fenced Python below (sha256 2eb55f48a7fbf893…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_map_value_streams_agent.py` first:

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
    "version": '2.0.0',
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
