---
name: "rar-cowork-cookbook-adaptive-card-record-cost-of-quality"
description: "Produces a reusable Adaptive Card JSON snapshot of record cost of quality status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_record_cost_of_quality", "rar_sha256": "4b78b0b5055d3c401958155a44feb0aa04b17aee506a4c00e292015d7cbc03ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_record_cost_of_quality_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-record-cost-of-quality:efddebcf7e68e792b62cbcf779d7b36b199dbedf84186c6b6f00eedf72900bf7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_record_cost_of_quality`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_record_cost_of_quality_agent.py` is
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

Record cost of quality Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of record cost of quality status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-cost-of-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_record_cost_of_quality_agent.py` and embedded as the fenced Python below (sha256 4b78b0b5055d3c40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_record_cost_of_quality_agent.py` first:

```bash
python3 adaptive_card_record_cost_of_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_record_cost_of_quality_agent.py   # or on stdin
python3 adaptive_card_record_cost_of_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record cost of quality Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of record cost of quality status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-cost-of-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_record_cost_of_quality',
    "version": '2.0.0',
    "display_name": 'Record cost of quality Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of record cost of quality status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-record-cost-of-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-record-cost-of-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b8d255dec31a4de5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/record-cost-of-quality'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-record-cost-of-quality', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardRecordCostOfQuality(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecordCostOfQuality'
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
    print(AdaptiveCardRecordCostOfQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
