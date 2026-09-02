---
name: "rar-cowork-cookbook-ppt-exec-plan-training-delivery"
description: "Generates an executive-ready PowerPoint deck on plan training delivery status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_training_delivery", "rar_sha256": "87646da1a7bd814f44f3618ede6d60180bd4450404dab61609547b68f54cbfff", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_plan_training_delivery_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-plan-training-delivery:e727f5b6ee134182dacae7e516bfa4b76ce578a29f14e3af77af98b2e394eae2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_plan_training_delivery`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_plan_training_delivery_agent.py` is
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

Plan training delivery Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan training delivery status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-training-delivery
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_training_delivery_agent.py` and embedded as the fenced Python below (sha256 87646da1a7bd814f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_training_delivery_agent.py` first:

```bash
python3 ppt_exec_plan_training_delivery_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_training_delivery_agent.py   # or on stdin
python3 ppt_exec_plan_training_delivery_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan training delivery Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan training delivery status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-training-delivery
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_training_delivery',
    "version": '2.0.0',
    "display_name": 'Plan training delivery Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on plan training delivery status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-plan-training-delivery',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-training-delivery',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0cf9c5cb6ab48d83',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/plan-training-delivery'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-plan-training-delivery', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecPlanTrainingDelivery(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanTrainingDelivery'
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
    print(PptExecPlanTrainingDelivery().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
