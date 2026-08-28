---
name: "rar-cowork-cookbook-bulk-update-map-value-streams"
description: "Applies a bulk field update across map value streams records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_map_value_streams", "rar_sha256": "2eb55f48a7fbf89322b76ff2c7bf0dccd24844ac2406b43a2a3b0520942ecc6a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
