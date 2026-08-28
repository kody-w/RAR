---
name: "rar-cowork-cookbook-ppt-exec-plan-training-delivery"
description: "Generates an executive-ready PowerPoint deck on plan training delivery status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_training_delivery", "rar_sha256": "87646da1a7bd814f44f3618ede6d60180bd4450404dab61609547b68f54cbfff", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_training_delivery`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_training_delivery_agent.py` and in the RCI capsule.

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
