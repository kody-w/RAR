---
name: "rar-cowork-cookbook-teams-update-close-a-case"
description: "Drafts a Teams channel post on close a case status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_close_a_case", "rar_sha256": "77f6a608e05a34aec266574213eda4c13e1799dc8e181e9382dfa05f526cb757", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_close_a_case_agent.py` and embedded as the fenced Python below (sha256 77f6a608e05a34ae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_close_a_case_agent.py` first:

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
    "version": '2.0.0',
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
