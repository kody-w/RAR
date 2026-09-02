---
name: "rar-cowork-cookbook-bulk-update-respond-to-non-compliance"
description: "Applies a bulk field update across respond to non-compliance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_respond_to_non_compliance", "rar_sha256": "d957fb206b964afc3c48872245f1f08d95176abd5feb012c42e22809573a2b2d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_respond_to_non_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-respond-to-non-compliance:3f60f73dc223af1221e80398f3230f3e672b9b05e35e7c602562979d656d6cb7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_respond_to_non_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_respond_to_non_compliance_agent.py` is
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

Respond to non-compliance Bulk Field Update — Applies a bulk field update across respond to non-compliance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-respond-to-non-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_respond_to_non_compliance_agent.py` and embedded as the fenced Python below (sha256 d957fb206b964afc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_respond_to_non_compliance_agent.py` first:

```bash
python3 bulk_update_respond_to_non_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_respond_to_non_compliance_agent.py   # or on stdin
python3 bulk_update_respond_to_non_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Respond to non-compliance Bulk Field Update — Applies a bulk field update across respond to non-compliance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-respond-to-non-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_respond_to_non_compliance',
    "version": '2.0.0',
    "display_name": 'Respond to non-compliance Bulk Field Update',
    "description": 'Applies a bulk field update across respond to non-compliance records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-respond-to-non-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-respond-to-non-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b7085560e05fbca6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/respond-to-non-compliance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-respond-to-non-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateRespondToNonCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRespondToNonCompliance'
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
    print(BulkUpdateRespondToNonCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
