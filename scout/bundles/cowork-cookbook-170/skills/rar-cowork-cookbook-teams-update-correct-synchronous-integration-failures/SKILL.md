---
name: "rar-cowork-cookbook-teams-update-correct-synchronous-integration-failures"
description: "Drafts a Teams channel post on correct synchronous integration failures status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_synchronous_integration_failures", "rar_sha256": "88dac2188f35e74b852ca493bbaeeca76e3410bbd04006a45dfa7ce590bc569f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_correct_synchronous_integration_failures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-correct-synchronous-integration-failures:2d41302c2a1e8d0117b35dffdf2cff27787a3b50c854cc4691c5e139b6ceeb4a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_correct_synchronous_integration_failures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_correct_synchronous_integration_failures_agent.py` is
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

Correct synchronous integration failures Teams Channel Update — Drafts a Teams channel post on correct synchronous integration failures status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-synchronous-integration-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_correct_synchronous_integration_failures_agent.py` and embedded as the fenced Python below (sha256 88dac2188f35e74b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_correct_synchronous_integration_failures_agent.py` first:

```bash
python3 teams_update_correct_synchronous_integration_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_correct_synchronous_integration_failures_agent.py   # or on stdin
python3 teams_update_correct_synchronous_integration_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct synchronous integration failures Teams Channel Update — Drafts a Teams channel post on correct synchronous integration failures status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-synchronous-integration-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_correct_synchronous_integration_failures',
    "version": '2.0.0',
    "display_name": 'Correct synchronous integration failures Teams Channel Update',
    "description": 'Drafts a Teams channel post on correct synchronous integration failures status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-correct-synchronous-integration-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-correct-synchronous-integration-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34a27326c31dd7ad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/correct-synchronous-integration-failures'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-correct-synchronous-integration-failures', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateCorrectSynchronousIntegrationFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCorrectSynchronousIntegrationFailures'
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
    print(TeamsUpdateCorrectSynchronousIntegrationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
