---
name: "rar-cowork-cookbook-adaptive-card-conduct-exit-interviews"
description: "Produces a reusable Adaptive Card JSON snapshot of conduct exit interviews status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_conduct_exit_interviews", "rar_sha256": "b9aa77a1e731b02365dad5aa141743c98872a5c3ced6e9f0a9895e43caca79ce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_conduct_exit_interviews_agent.py` and embedded as the fenced Python below (sha256 b9aa77a1e731b023…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_conduct_exit_interviews_agent.py` first:

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
    "version": '2.0.0',
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
