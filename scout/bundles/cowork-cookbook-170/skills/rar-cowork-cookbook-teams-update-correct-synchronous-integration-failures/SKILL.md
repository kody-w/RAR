---
name: "rar-cowork-cookbook-teams-update-correct-synchronous-integration-failures"
description: "Drafts a Teams channel post on correct synchronous integration failures status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_synchronous_integration_failures", "rar_sha256": "09f5479f1e7a247a46a7f24a62eb9f50f279dd7877b3da2fcf7d1979cf291ff1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_correct_synchronous_integration_failures_agent.py` and embedded as the fenced Python below (sha256 09f5479f1e7a247a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_correct_synchronous_integration_failures_agent.py` first:

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
    "version": '2.0.1',
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
