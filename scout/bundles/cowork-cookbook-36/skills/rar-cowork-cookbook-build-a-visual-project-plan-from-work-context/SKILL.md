---
name: "rar-cowork-cookbook-build-a-visual-project-plan-from-work-context"
description: "Turn a scattered project picture - emails, meetings, files - into a single visual plan the team can rally around without rebuilding it from scratch."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_visual_project_plan_from_work_context", "rar_sha256": "3c41b4be395f68f01460dfa7d06a013f2edc8ea6fc47c34f301ad07c2edaed88", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_a_visual_project_plan_from_work_context`. The original RAPP
agent is preserved byte-for-byte in `build_a_visual_project_plan_from_work_context_agent.py` and in the RCI capsule.

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

Build a visual project plan from work context — Turn a scattered project picture - emails, meetings, files - into a single visual plan the team can rally around without rebuilding it from scratch.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-a-visual-project-plan-from-work-context
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_a_visual_project_plan_from_work_context_agent.py` and embedded as the fenced Python below (sha256 3c41b4be395f68f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_a_visual_project_plan_from_work_context_agent.py` first:

```bash
python3 build_a_visual_project_plan_from_work_context_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_a_visual_project_plan_from_work_context_agent.py   # or on stdin
python3 build_a_visual_project_plan_from_work_context_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a visual project plan from work context — Turn a scattered project picture - emails, meetings, files - into a single visual plan the team can rally around without rebuilding it from scratch.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-a-visual-project-plan-from-work-context
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_a_visual_project_plan_from_work_context',
    "version": '2.0.0',
    "display_name": 'Build a visual project plan from work context',
    "description": 'Turn a scattered project picture - emails, meetings, files - into a single visual plan the team can rally around without rebuilding it from scratch.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'intermediate', 'integration', 'miro'],
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
        "upstream_slug": 'build-a-visual-project-plan-from-work-context',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-a-visual-project-plan-from-work-context',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '044eed996e164cab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['work-management'], 'process_tags': ['work-management/coordinate-team-work/build-project-plans'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/build-a-visual-project-plan-from-work-context', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BuildAVisualProjectPlanFromWorkContext(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildAVisualProjectPlanFromWorkContext'
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
    print(BuildAVisualProjectPlanFromWorkContext().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
