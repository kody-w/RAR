---
name: "rar-cowork-cookbook-bulk-update-maintain-quality-certifications"
description: "Applies a bulk field update across maintain quality certifications records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_maintain_quality_certifications", "rar_sha256": "6a42c919547b8084f266ef5b380172e0a1f766c0deec8bfbf10922b6ea70dda5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_maintain_quality_certifications_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-maintain-quality-certifications:8ec2343b5dac2187592084ec4592713bf9d93ec331610cc131e0f4d0a6fb1379", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_maintain_quality_certifications`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_maintain_quality_certifications_agent.py` is
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

Maintain quality certifications Bulk Field Update — Applies a bulk field update across maintain quality certifications records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-maintain-quality-certifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_maintain_quality_certifications_agent.py` and embedded as the fenced Python below (sha256 6a42c919547b8084…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_maintain_quality_certifications_agent.py` first:

```bash
python3 bulk_update_maintain_quality_certifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_maintain_quality_certifications_agent.py   # or on stdin
python3 bulk_update_maintain_quality_certifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain quality certifications Bulk Field Update — Applies a bulk field update across maintain quality certifications records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-maintain-quality-certifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_maintain_quality_certifications',
    "version": '2.0.0',
    "display_name": 'Maintain quality certifications Bulk Field Update',
    "description": 'Applies a bulk field update across maintain quality certifications records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-maintain-quality-certifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-maintain-quality-certifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1a3529012e63bc27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/maintain-quality-certifications'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-maintain-quality-certifications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateMaintainQualityCertifications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMaintainQualityCertifications'
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
    print(BulkUpdateMaintainQualityCertifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
