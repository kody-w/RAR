---
name: "rar-cowork-cookbook-bulk-update-hire-for-open-positions"
description: "Applies a bulk field update across hire for open positions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_hire_for_open_positions", "rar_sha256": "2df159badddbc45433daec8cd17a5df8b9a5774ebf7bb4b74e37d54b3315362e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_hire_for_open_positions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-hire-for-open-positions:cf0b4176e2fd79d5d106d0b9b266f196dc0ffe68b5ad092f7deddb87f80f9163", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_hire_for_open_positions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_hire_for_open_positions_agent.py` is
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

Hire for open positions Bulk Field Update — Applies a bulk field update across hire for open positions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-hire-for-open-positions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_hire_for_open_positions_agent.py` and embedded as the fenced Python below (sha256 2df159badddbc454…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_hire_for_open_positions_agent.py` first:

```bash
python3 bulk_update_hire_for_open_positions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_hire_for_open_positions_agent.py   # or on stdin
python3 bulk_update_hire_for_open_positions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Hire for open positions Bulk Field Update — Applies a bulk field update across hire for open positions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-hire-for-open-positions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_hire_for_open_positions',
    "version": '2.0.0',
    "display_name": 'Hire for open positions Bulk Field Update',
    "description": 'Applies a bulk field update across hire for open positions records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-hire-for-open-positions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-hire-for-open-positions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0567190f689d13f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/hire-for-open-positions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-hire-for-open-positions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateHireForOpenPositions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateHireForOpenPositions'
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
    print(BulkUpdateHireForOpenPositions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
