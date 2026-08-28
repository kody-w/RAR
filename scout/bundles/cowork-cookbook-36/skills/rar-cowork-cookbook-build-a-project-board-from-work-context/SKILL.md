---
name: "rar-cowork-cookbook-build-a-project-board-from-work-context"
description: "Spin up a fully scoped project board without the manual setup tax - no copying from emails, chasing owners, or piecing together task lists from scattered threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_project_board_from_work_context", "rar_sha256": "70944c0fa56b37b5fd924cec6a80992cdc754fbb7faaaa0ac9f4eba285acaa6e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_a_project_board_from_work_context`. The original RAPP
agent is preserved byte-for-byte in `build_a_project_board_from_work_context_agent.py` and in the RCI capsule.

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
