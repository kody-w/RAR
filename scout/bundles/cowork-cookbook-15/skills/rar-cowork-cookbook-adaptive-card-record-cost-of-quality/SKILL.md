---
name: "rar-cowork-cookbook-adaptive-card-record-cost-of-quality"
description: "Produces a reusable Adaptive Card JSON snapshot of record cost of quality status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_record_cost_of_quality", "rar_sha256": "ad24f212e77e3e9305beb1ab2f9cc91ad7db1400aefb5ea81abe8c327bdbac54", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_record_cost_of_quality_agent.py` and embedded as the fenced Python below (sha256 ad24f212e77e3e93…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_record_cost_of_quality_agent.py` first:

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
    "version": '2.0.1',
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
