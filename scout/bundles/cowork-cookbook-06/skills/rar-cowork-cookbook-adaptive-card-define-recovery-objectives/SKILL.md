---
name: "rar-cowork-cookbook-adaptive-card-define-recovery-objectives"
description: "Produces a reusable Adaptive Card JSON snapshot of define recovery objectives status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_recovery_objectives", "rar_sha256": "42b4dd43b5eb3cce87818fbef992d35281ee1eb2dd064caa7a13c0ab94cf6b84", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_recovery_objectives_agent.py` and embedded as the fenced Python below (sha256 42b4dd43b5eb3cce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_recovery_objectives_agent.py` first:

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
    "version": '2.0.1',
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
