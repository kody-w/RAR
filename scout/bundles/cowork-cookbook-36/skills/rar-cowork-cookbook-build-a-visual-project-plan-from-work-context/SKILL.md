---
name: "rar-cowork-cookbook-build-a-visual-project-plan-from-work-context"
description: "Turn a scattered project picture - emails, meetings, files - into a single visual plan the team can rally around without rebuilding it from scratch."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_visual_project_plan_from_work_context", "rar_sha256": "1d9faafad3e0d547462d464ba521a4b1575fb8ab4c90938c6ee0ed35371c7796", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "integration", "miro"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_a_visual_project_plan_from_work_context_agent.py` and embedded as the fenced Python below (sha256 1d9faafad3e0d547…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_a_visual_project_plan_from_work_context_agent.py` first:

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
    "version": '2.0.1',
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
