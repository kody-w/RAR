---
name: "rar-cowork-cookbook-adaptive-card-define-recovery-objectives"
description: "Produces a reusable Adaptive Card JSON snapshot of define recovery objectives status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_recovery_objectives", "rar_sha256": "07e3fe10d5b15285af7921404e23657d31a8c759b8ad35c4cc381dfeafd36b89", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_recovery_objectives`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_recovery_objectives_agent.py` and in the RCI capsule.

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
