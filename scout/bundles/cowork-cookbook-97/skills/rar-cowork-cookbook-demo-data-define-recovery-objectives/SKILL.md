---
name: "rar-cowork-cookbook-demo-data-define-recovery-objectives"
description: "Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_recovery_objectives", "rar_sha256": "e8f340486f30b7864fdf6fe69a95251002a3b298a42c0c1aa8380c33a2987327", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_recovery_objectives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-recovery-objectives:612cf3d3eed9f45e108e3a44adbaa7d270e8cb104e8fca0ef64a52736473b6d9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_recovery_objectives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_recovery_objectives_agent.py` is
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

Define recovery objectives Demo Data Generator — Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_recovery_objectives_agent.py` and embedded as the fenced Python below (sha256 e8f340486f30b786…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_recovery_objectives_agent.py` first:

```bash
python3 demo_data_define_recovery_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_recovery_objectives_agent.py   # or on stdin
python3 demo_data_define_recovery_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define recovery objectives Demo Data Generator — Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_recovery_objectives',
    "version": '2.0.0',
    "display_name": 'Define recovery objectives Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-recovery-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '425a1557d7a88d3e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-recovery-objectives'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-define-recovery-objectives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDefineRecoveryObjectives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineRecoveryObjectives'
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
    print(DemoDataDefineRecoveryObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
