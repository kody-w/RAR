---
name: "rar-cowork-cookbook-bulk-update-prepare-to-go-live"
description: "Applies a bulk field update across prepare to go live records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_prepare_to_go_live", "rar_sha256": "57bcd271f599dbd0e5d431dea947e0df0f64946e28bdaa00bf891b505aca554e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_prepare_to_go_live_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-prepare-to-go-live:cbb0abd22c13b7c4317c43b0cb65f39d81b446e50a93bd295249fd6f97278fd2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_prepare_to_go_live`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_prepare_to_go_live_agent.py` is
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

Prepare to go live Bulk Field Update — Applies a bulk field update across prepare to go live records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-prepare-to-go-live
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_prepare_to_go_live_agent.py` and embedded as the fenced Python below (sha256 57bcd271f599dbd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_prepare_to_go_live_agent.py` first:

```bash
python3 bulk_update_prepare_to_go_live_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_prepare_to_go_live_agent.py   # or on stdin
python3 bulk_update_prepare_to_go_live_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare to go live Bulk Field Update — Applies a bulk field update across prepare to go live records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-prepare-to-go-live
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_prepare_to_go_live',
    "version": '2.0.0',
    "display_name": 'Prepare to go live Bulk Field Update',
    "description": 'Applies a bulk field update across prepare to go live records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-prepare-to-go-live',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-prepare-to-go-live',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a53fa905475fb98',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/prepare-to-go-live'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-prepare-to-go-live', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePrepareToGoLive(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePrepareToGoLive'
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
    print(BulkUpdatePrepareToGoLive().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
