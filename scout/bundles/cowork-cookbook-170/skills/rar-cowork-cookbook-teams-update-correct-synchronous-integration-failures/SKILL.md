---
name: "rar-cowork-cookbook-teams-update-correct-synchronous-integration-failures"
description: "Drafts a Teams channel post on correct synchronous integration failures status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_synchronous_integration_failures", "rar_sha256": "88dac2188f35e74b852ca493bbaeeca76e3410bbd04006a45dfa7ce590bc569f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_correct_synchronous_integration_failures`. The original RAPP
agent is preserved byte-for-byte in `teams_update_correct_synchronous_integration_failures_agent.py` and in the RCI capsule.

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
