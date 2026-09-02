---
name: "rar-cowork-cookbook-adaptive-card-identify-training-needs"
description: "Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_training_needs", "rar_sha256": "86548793362e6cd5a5dea31587aab1d7b6bdecfd2fb2824c0fcd5737ca428cb9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_identify_training_needs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-identify-training-needs:397908e03e7b88db9eb579b1d69c6ef8d264082064ad3445b68ee364273d189c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_identify_training_needs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_identify_training_needs_agent.py` is
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

Identify training needs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_training_needs_agent.py` and embedded as the fenced Python below (sha256 86548793362e6cd5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_training_needs_agent.py` first:

```bash
python3 adaptive_card_identify_training_needs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_training_needs_agent.py   # or on stdin
python3 adaptive_card_identify_training_needs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify training needs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_training_needs',
    "version": '2.0.0',
    "display_name": 'Identify training needs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-identify-training-needs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0d6a8de63b2a71f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/identify-training-needs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-identify-training-needs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardIdentifyTrainingNeeds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyTrainingNeeds'
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
    print(AdaptiveCardIdentifyTrainingNeeds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
