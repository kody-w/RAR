---
name: "rar-cowork-cookbook-adaptive-card-track-employee-learning"
description: "Produces a reusable Adaptive Card JSON snapshot of track employee learning status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_employee_learning", "rar_sha256": "399dbefea93eb8b0451917daf10502d6d87bcc95e10ca0635d020484ef743b77", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_track_employee_learning`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_track_employee_learning_agent.py` and in the RCI capsule.

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

Track employee learning Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of track employee learning status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-employee-learning
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_employee_learning_agent.py` and embedded as the fenced Python below (sha256 399dbefea93eb8b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_employee_learning_agent.py` first:

```bash
python3 adaptive_card_track_employee_learning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_track_employee_learning_agent.py   # or on stdin
python3 adaptive_card_track_employee_learning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track employee learning Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of track employee learning status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-employee-learning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_track_employee_learning',
    "version": '2.0.0',
    "display_name": 'Track employee learning Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of track employee learning status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-track-employee-learning',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-track-employee-learning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4d65807175166c7f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/track-employee-learning'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-track-employee-learning', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardTrackEmployeeLearning(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardTrackEmployeeLearning'
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
    print(AdaptiveCardTrackEmployeeLearning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
