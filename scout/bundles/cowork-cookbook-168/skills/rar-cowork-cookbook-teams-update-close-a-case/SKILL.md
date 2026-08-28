---
name: "rar-cowork-cookbook-teams-update-close-a-case"
description: "Drafts a Teams channel post on close a case status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_close_a_case", "rar_sha256": "601ed5eb2c7cf36d46f6b57434e421f1987ae6c592f3b0c54ed3d54edd73ee43", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_close_a_case`. The original RAPP
agent is preserved byte-for-byte in `teams_update_close_a_case_agent.py` and in the RCI capsule.

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

Close a case Teams Channel Update — Drafts a Teams channel post on close a case status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-close-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_close_a_case_agent.py` and embedded as the fenced Python below (sha256 601ed5eb2c7cf36d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_close_a_case_agent.py` first:

```bash
python3 teams_update_close_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_close_a_case_agent.py   # or on stdin
python3 teams_update_close_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Close a case Teams Channel Update — Drafts a Teams channel post on close a case status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-close-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_close_a_case',
    "version": '2.0.1',
    "display_name": 'Close a case Teams Channel Update',
    "description": 'Drafts a Teams channel post on close a case status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-close-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-close-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a26969739a0ec15f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/close-a-case'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-close-a-case', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateCloseACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCloseACase'
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
    print(TeamsUpdateCloseACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
