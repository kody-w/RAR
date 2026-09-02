---
name: "rar-cowork-cookbook-bulk-update-create-a-case-manually"
description: "Applies a bulk field update across create a case manually records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_create_a_case_manually", "rar_sha256": "f6bd9640d0290ec2267136492b113c55c7621273149cb7aa218730f8a5e9e1ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_create_a_case_manually_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-create-a-case-manually:4e6df8acf65033bbbb82e1e67eb90c081e5f986c4eec743c1356707a30f972d5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_create_a_case_manually`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_create_a_case_manually_agent.py` is
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

Create a case manually Bulk Field Update — Applies a bulk field update across create a case manually records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-a-case-manually
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_create_a_case_manually_agent.py` and embedded as the fenced Python below (sha256 f6bd9640d0290ec2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_create_a_case_manually_agent.py` first:

```bash
python3 bulk_update_create_a_case_manually_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_create_a_case_manually_agent.py   # or on stdin
python3 bulk_update_create_a_case_manually_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create a case manually Bulk Field Update — Applies a bulk field update across create a case manually records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-a-case-manually
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_create_a_case_manually',
    "version": '2.0.0',
    "display_name": 'Create a case manually Bulk Field Update',
    "description": 'Applies a bulk field update across create a case manually records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-create-a-case-manually',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-create-a-case-manually',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a54d9cf903bdc2b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/create-a-case-manually'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-create-a-case-manually', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateCreateACaseManually(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCreateACaseManually'
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
    print(BulkUpdateCreateACaseManually().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
