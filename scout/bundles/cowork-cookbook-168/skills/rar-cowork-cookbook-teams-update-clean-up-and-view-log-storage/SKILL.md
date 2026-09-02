---
name: "rar-cowork-cookbook-teams-update-clean-up-and-view-log-storage"
description: "Drafts a Teams channel post on clean up and view log storage status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_clean_up_and_view_log_storage", "rar_sha256": "fbd380c70f5d0b9f574af5433ca8326043179511492645036d670f1ebbfbbfff", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_clean_up_and_view_log_storage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-clean-up-and-view-log-storage:dc06742c42acacdbfc3af54811f990917455e529a524864244a013965e0fd312", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_clean_up_and_view_log_storage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_clean_up_and_view_log_storage_agent.py` is
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

Clean up and view log storage Teams Channel Update — Drafts a Teams channel post on clean up and view log storage status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-clean-up-and-view-log-storage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_clean_up_and_view_log_storage_agent.py` and embedded as the fenced Python below (sha256 fbd380c70f5d0b9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_clean_up_and_view_log_storage_agent.py` first:

```bash
python3 teams_update_clean_up_and_view_log_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_clean_up_and_view_log_storage_agent.py   # or on stdin
python3 teams_update_clean_up_and_view_log_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clean up and view log storage Teams Channel Update — Drafts a Teams channel post on clean up and view log storage status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-clean-up-and-view-log-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_clean_up_and_view_log_storage',
    "version": '2.0.0',
    "display_name": 'Clean up and view log storage Teams Channel Update',
    "description": 'Drafts a Teams channel post on clean up and view log storage status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-clean-up-and-view-log-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-clean-up-and-view-log-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '47c55292fdae5131',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/clean-up-and-view-log-storage'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-clean-up-and-view-log-storage', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateCleanUpAndViewLogStorage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCleanUpAndViewLogStorage'
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
    print(TeamsUpdateCleanUpAndViewLogStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
