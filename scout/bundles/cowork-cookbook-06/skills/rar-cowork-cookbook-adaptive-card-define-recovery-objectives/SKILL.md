---
name: "rar-cowork-cookbook-adaptive-card-define-recovery-objectives"
description: "Produces a reusable Adaptive Card JSON snapshot of define recovery objectives status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_recovery_objectives", "rar_sha256": "07e3fe10d5b15285af7921404e23657d31a8c759b8ad35c4cc381dfeafd36b89", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_recovery_objectives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-recovery-objectives:9ad262ed7ceef176daa74d876b243d3e01cecf0cd06787f367800cf4a1104c99", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_recovery_objectives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_recovery_objectives_agent.py` is
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

Define recovery objectives Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define recovery objectives status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-recovery-objectives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_recovery_objectives_agent.py` and embedded as the fenced Python below (sha256 07e3fe10d5b15285…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_recovery_objectives_agent.py` first:

```bash
python3 adaptive_card_define_recovery_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_recovery_objectives_agent.py   # or on stdin
python3 adaptive_card_define_recovery_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define recovery objectives Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define recovery objectives status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-recovery-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_recovery_objectives',
    "version": '2.0.0',
    "display_name": 'Define recovery objectives Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define recovery objectives status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-define-recovery-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-recovery-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ce91b1155c42f941',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-recovery-objectives'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-define-recovery-objectives', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDefineRecoveryObjectives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineRecoveryObjectives'
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
    print(AdaptiveCardDefineRecoveryObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
