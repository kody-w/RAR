---
name: "rar-cowork-cookbook-ppt-exec-implement-the-disaster-recovery-plan"
description: "Generates an executive-ready PowerPoint deck on implement the disaster recovery plan status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan", "rar_sha256": "7fea9bab0aafb1e83b8016618c67d08e24a9108cb3c18dcd00a3426293a97923", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_implement_the_disaster_recovery_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-implement-the-disaster-recovery-plan:0ed0886cb478d52e72ada3754cb2a908c258c914ef3a7540fb34b2592350fc0d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_implement_the_disaster_recovery_plan_agent.py` is
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
