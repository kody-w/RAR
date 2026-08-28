---
name: "rar-cowork-cookbook-ppt-exec-plan-training-delivery"
description: "Generates an executive-ready PowerPoint deck on plan training delivery status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_training_delivery", "rar_sha256": "64a9b20851440a27c9a971eda952f429b61b5712564c2faec61b8749fc9a8978", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_training_delivery_agent.py` and embedded as the fenced Python below (sha256 64a9b20851440a27…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_training_delivery_agent.py` first:

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
    "version": '2.0.1',
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
