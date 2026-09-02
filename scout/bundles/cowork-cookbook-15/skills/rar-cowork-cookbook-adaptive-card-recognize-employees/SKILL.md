---
name: "rar-cowork-cookbook-adaptive-card-recognize-employees"
description: "Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_recognize_employees", "rar_sha256": "854f79ff4bcf1cfaf3272123c171b55ca84e551f3e11b6858e2b41ba36bea4f2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_recognize_employees_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-recognize-employees:edeb6386876a2daf1421169efecdd8ddb9c2e87ee24e93b8d7166f0cd5124247", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_recognize_employees`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_recognize_employees_agent.py` is
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

Recognize employees Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recognize-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_recognize_employees_agent.py` and embedded as the fenced Python below (sha256 854f79ff4bcf1cfa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_recognize_employees_agent.py` first:

```bash
python3 adaptive_card_recognize_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_recognize_employees_agent.py   # or on stdin
python3 adaptive_card_recognize_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize employees Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-recognize-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_recognize_employees',
    "version": '2.0.0',
    "display_name": 'Recognize employees Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of recognize employees status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-recognize-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-recognize-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c48a376936c7297',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/recognize-employees'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-recognize-employees', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardRecognizeEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecognizeEmployees'
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
    print(AdaptiveCardRecognizeEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
