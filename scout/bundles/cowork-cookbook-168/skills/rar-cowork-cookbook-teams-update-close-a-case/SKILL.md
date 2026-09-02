---
name: "rar-cowork-cookbook-teams-update-close-a-case"
description: "Drafts a Teams channel post on close a case status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_close_a_case", "rar_sha256": "77f6a608e05a34aec266574213eda4c13e1799dc8e181e9382dfa05f526cb757", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_close_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-close-a-case:90611ee670699fc45e6c217b5c2f58754371ee838bc294e27a11bcd749c90249", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_close_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_close_a_case_agent.py` is
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
