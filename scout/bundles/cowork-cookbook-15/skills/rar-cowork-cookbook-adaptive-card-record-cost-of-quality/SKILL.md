---
name: "rar-cowork-cookbook-adaptive-card-record-cost-of-quality"
description: "Produces a reusable Adaptive Card JSON snapshot of record cost of quality status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_record_cost_of_quality", "rar_sha256": "4b78b0b5055d3c401958155a44feb0aa04b17aee506a4c00e292015d7cbc03ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_record_cost_of_quality`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_record_cost_of_quality_agent.py` and in the RCI capsule.

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
