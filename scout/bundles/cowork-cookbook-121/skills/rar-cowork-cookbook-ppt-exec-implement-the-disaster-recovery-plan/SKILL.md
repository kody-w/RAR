---
name: "rar-cowork-cookbook-ppt-exec-implement-the-disaster-recovery-plan"
description: "Generates an executive-ready PowerPoint deck on implement the disaster recovery plan status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan", "rar_sha256": "7fea9bab0aafb1e83b8016618c67d08e24a9108cb3c18dcd00a3426293a97923", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 7fea9bab0aafb1e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_the_disaster_recovery_plan_agent.py` first:

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
    "version": '2.0.0',
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
