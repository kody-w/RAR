---
name: "rar-cowork-cookbook-adaptive-card-conduct-exit-interviews"
description: "Produces a reusable Adaptive Card JSON snapshot of conduct exit interviews status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_conduct_exit_interviews", "rar_sha256": "7766c56a2042faf936c5f841e7d8b6b3daf1f250044837d552465307c4f26271", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_conduct_exit_interviews`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_conduct_exit_interviews_agent.py` and in the RCI capsule.

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

Conduct exit interviews Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of conduct exit interviews status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-conduct-exit-interviews
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_conduct_exit_interviews_agent.py` and embedded as the fenced Python below (sha256 7766c56a2042faf9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_conduct_exit_interviews_agent.py` first:

```bash
python3 adaptive_card_conduct_exit_interviews_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_conduct_exit_interviews_agent.py   # or on stdin
python3 adaptive_card_conduct_exit_interviews_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct exit interviews Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of conduct exit interviews status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-conduct-exit-interviews
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_conduct_exit_interviews',
    "version": '2.0.1',
    "display_name": 'Conduct exit interviews Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of conduct exit interviews status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-conduct-exit-interviews',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-conduct-exit-interviews',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '088ea9f4bc0f676d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/conduct-exit-interviews'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-conduct-exit-interviews', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardConductExitInterviews(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConductExitInterviews'
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
    print(AdaptiveCardConductExitInterviews().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
