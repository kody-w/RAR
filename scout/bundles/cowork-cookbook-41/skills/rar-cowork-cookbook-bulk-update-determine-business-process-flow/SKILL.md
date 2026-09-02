---
name: "rar-cowork-cookbook-bulk-update-determine-business-process-flow"
description: "Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_determine_business_process_flow", "rar_sha256": "5eee37ddd22445e4614ccf34b4c462b702ed51f3fe43a22d7efc157167d17074", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_determine_business_process_flow_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-determine-business-process-flow:b24c02f4ce332903ef7d649df5073b9a82b0b2afc7d2f336cd95608570bde754", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_determine_business_process_flow`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_determine_business_process_flow_agent.py` is
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

Determine business process flow Bulk Field Update — Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_determine_business_process_flow_agent.py` and embedded as the fenced Python below (sha256 5eee37ddd22445e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_determine_business_process_flow_agent.py` first:

```bash
python3 bulk_update_determine_business_process_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_determine_business_process_flow_agent.py   # or on stdin
python3 bulk_update_determine_business_process_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine business process flow Bulk Field Update — Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_determine_business_process_flow',
    "version": '2.0.0',
    "display_name": 'Determine business process flow Bulk Field Update',
    "description": 'Applies a bulk field update across determine business process flow records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-determine-business-process-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-determine-business-process-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd43c76b21ba53c6b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/determine-business-process-flow'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-determine-business-process-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDetermineBusinessProcessFlow(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDetermineBusinessProcessFlow'
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
    print(BulkUpdateDetermineBusinessProcessFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
