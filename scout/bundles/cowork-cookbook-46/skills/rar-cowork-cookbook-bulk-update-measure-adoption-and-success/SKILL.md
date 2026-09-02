---
name: "rar-cowork-cookbook-bulk-update-measure-adoption-and-success"
description: "Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_measure_adoption_and_success", "rar_sha256": "5f4de8689040760a1a0a3e32f5febfc0bdec7bbdd3e71c520e52f385ad3deedf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_measure_adoption_and_success_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-measure-adoption-and-success:e4b3993bbc797b1d0312bb89e29b580720557d9df43ee1f95e555b85ffca45f7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_measure_adoption_and_success`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_measure_adoption_and_success_agent.py` is
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

Measure adoption and success Bulk Field Update — Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_measure_adoption_and_success_agent.py` and embedded as the fenced Python below (sha256 5f4de8689040760a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_measure_adoption_and_success_agent.py` first:

```bash
python3 bulk_update_measure_adoption_and_success_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_measure_adoption_and_success_agent.py   # or on stdin
python3 bulk_update_measure_adoption_and_success_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure adoption and success Bulk Field Update — Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_measure_adoption_and_success',
    "version": '2.0.0',
    "display_name": 'Measure adoption and success Bulk Field Update',
    "description": 'Applies a bulk field update across measure adoption and success records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-measure-adoption-and-success',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-measure-adoption-and-success',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eb7a04f62dee1a46',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/measure-adoption-and-success'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-measure-adoption-and-success', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateMeasureAdoptionAndSuccess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMeasureAdoptionAndSuccess'
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
    print(BulkUpdateMeasureAdoptionAndSuccess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
