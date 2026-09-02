---
name: "rar-cowork-cookbook-adaptive-card-track-employee-learning"
description: "Produces a reusable Adaptive Card JSON snapshot of track employee learning status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_employee_learning", "rar_sha256": "399dbefea93eb8b0451917daf10502d6d87bcc95e10ca0635d020484ef743b77", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_track_employee_learning_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-track-employee-learning:71dd040dd12a32981fc4bbb554d6b8b94b5742433200e26cc7542963aaf7d128", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_track_employee_learning`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_track_employee_learning_agent.py` is
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
