---
name: "rar-cowork-cookbook-ppt-exec-implement-the-disaster-recovery-plan"
description: "Generates an executive-ready PowerPoint deck on implement the disaster recovery plan status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan", "rar_sha256": "7b38927d6bd29bff2e082f1243e82c5cbb20e0739505ba0be8c5e62a40f9ef68", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_implement_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Implement the disaster recovery plan Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement the disaster recovery plan status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-the-disaster-recovery-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 7b38927d6bd29bff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_the_disaster_recovery_plan_agent.py` first:

```bash
python3 ppt_exec_implement_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_the_disaster_recovery_plan_agent.py   # or on stdin
python3 ppt_exec_implement_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement the disaster recovery plan Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on implement the disaster recovery plan status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan',
    "version": '2.0.1',
    "display_name": 'Implement the disaster recovery plan Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on implement the disaster recovery plan status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-implement-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '35d240de5fa961bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/implement-the-disaster-recovery-plan'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecImplementTheDisasterRecoveryPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementTheDisasterRecoveryPlan'
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
    print(PptExecImplementTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
