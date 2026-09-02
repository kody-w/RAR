---
name: "rar-cowork-cookbook-build-a-visual-project-plan-from-work-context"
description: "Turn a scattered project picture - emails, meetings, files - into a single visual plan the team can rally around without rebuilding it from scratch."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_visual_project_plan_from_work_context", "rar_sha256": "3c41b4be395f68f01460dfa7d06a013f2edc8ea6fc47c34f301ad07c2edaed88", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "build_a_visual_project_plan_from_work_context_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/build-a-visual-project-plan-from-work-context:1916e9f8f7894a544f2f13463380adbd557339f0afb588f262ff684df34b1deb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "integration", "miro"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/build_a_visual_project_plan_from_work_context`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `build_a_visual_project_plan_from_work_context_agent.py` is
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
