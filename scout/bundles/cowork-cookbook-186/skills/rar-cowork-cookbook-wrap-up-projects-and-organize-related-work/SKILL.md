---
name: "rar-cowork-cookbook-wrap-up-projects-and-organize-related-work"
description: "Close out a project with a clean, shareable archive - not a scattered trail of files."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/wrap_up_projects_and_organize_related_work", "rar_sha256": "8345d26f8d12ae87557dcd7a7c72cc10c9e5e2ce1e7efc5feaa712e2842ddd44", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "wrap_up_projects_and_organize_related_work_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/wrap-up-projects-and-organize-related-work:210c54ad3d83b5b653d4fc7162d528500e8e39658cb4618bb42cd87d16f90dce", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/wrap_up_projects_and_organize_related_work`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `wrap_up_projects_and_organize_related_work_agent.py` is
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

Wrap up projects and organize all related work — Close out a project with a clean, shareable archive - not a scattered trail of files.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/wrap-up-projects-and-organize-related-work
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wrap_up_projects_and_organize_related_work_agent.py` and embedded as the fenced Python below (sha256 8345d26f8d12ae87…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wrap_up_projects_and_organize_related_work_agent.py` first:

```bash
python3 wrap_up_projects_and_organize_related_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wrap_up_projects_and_organize_related_work_agent.py   # or on stdin
python3 wrap_up_projects_and_organize_related_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Wrap up projects and organize all related work — Close out a project with a clean, shareable archive - not a scattered trail of files.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/wrap-up-projects-and-organize-related-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/wrap_up_projects_and_organize_related_work',
    "version": '2.0.0',
    "display_name": 'Wrap up projects and organize all related work',
    "description": 'Close out a project with a clean, shareable archive - not a scattered trail of files.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'beginner', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'wrap-up-projects-and-organize-related-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/wrap-up-projects-and-organize-related-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f351da4abc366491',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/organize-information/archive-completed-work'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/wrap-up-projects-and-organize-related-work', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class WrapUpProjectsAndOrganizeRelatedWork(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WrapUpProjectsAndOrganizeRelatedWork'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(WrapUpProjectsAndOrganizeRelatedWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
