---
name: "rar-cowork-cookbook-build-a-project-board-from-work-context"
description: "Spin up a fully scoped project board without the manual setup tax - no copying from emails, chasing owners, or piecing together task lists from scattered threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_project_board_from_work_context", "rar_sha256": "70944c0fa56b37b5fd924cec6a80992cdc754fbb7faaaa0ac9f4eba285acaa6e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "build_a_project_board_from_work_context_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/build-a-project-board-from-work-context:9683e9a388dee1aebcb4de533f7ba71116474ca116d8f21fa8cf8f0f03b80374", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/build_a_project_board_from_work_context`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `build_a_project_board_from_work_context_agent.py` is
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

Build a project board from work context — Spin up a fully scoped project board without the manual setup tax - no copying from emails, chasing owners, or piecing together task lists from scattered threads.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-a-project-board-from-work-context
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_a_project_board_from_work_context_agent.py` and embedded as the fenced Python below (sha256 70944c0fa56b37b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_a_project_board_from_work_context_agent.py` first:

```bash
python3 build_a_project_board_from_work_context_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_a_project_board_from_work_context_agent.py   # or on stdin
python3 build_a_project_board_from_work_context_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a project board from work context — Spin up a fully scoped project board without the manual setup tax - no copying from emails, chasing owners, or piecing together task lists from scattered threads.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-a-project-board-from-work-context
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_a_project_board_from_work_context',
    "version": '2.0.0',
    "display_name": 'Build a project board from work context',
    "description": 'Spin up a fully scoped project board without the manual setup tax - no copying from emails, chasing owners, or piecing together task lists from scattered threads.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'intermediate', 'integration', 'monday_com'],
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
        "upstream_slug": 'build-a-project-board-from-work-context',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-a-project-board-from-work-context',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5d7875195d5c06fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['work-management'], 'process_tags': ['work-management/coordinate-team-work/set-up-project-boards'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/build-a-project-board-from-work-context', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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


class BuildAProjectBoardFromWorkContext(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildAProjectBoardFromWorkContext'
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
    print(BuildAProjectBoardFromWorkContext().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
