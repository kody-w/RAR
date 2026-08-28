---
name: "rar-cowork-cookbook-build-a-project-board-from-work-context"
description: "Spin up a fully scoped project board without the manual setup tax - no copying from emails, chasing owners, or piecing together task lists from scattered threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_project_board_from_work_context", "rar_sha256": "749a17142a8e152c60ba3d3b5e1e99313ce2e532d5e4abc099874e189eb7b44a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "integration", "monday_com"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_a_project_board_from_work_context_agent.py` and embedded as the fenced Python below (sha256 749a17142a8e152c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_a_project_board_from_work_context_agent.py` first:

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
    "version": '2.0.1',
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
