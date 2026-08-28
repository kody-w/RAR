---
name: "rar-cowork-cookbook-wrap-up-projects-and-organize-related-work"
description: "Close out a project with a clean, shareable archive - not a scattered trail of files."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/wrap_up_projects_and_organize_related_work", "rar_sha256": "8345d26f8d12ae87557dcd7a7c72cc10c9e5e2ce1e7efc5feaa712e2842ddd44", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/wrap_up_projects_and_organize_related_work`. The original RAPP
agent is preserved byte-for-byte in `wrap_up_projects_and_organize_related_work_agent.py` and in the RCI capsule.

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
