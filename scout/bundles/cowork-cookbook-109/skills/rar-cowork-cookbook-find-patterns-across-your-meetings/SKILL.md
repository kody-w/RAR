---
name: "rar-cowork-cookbook-find-patterns-across-your-meetings"
description: "Surface the themes that are repeating across your meetings - without re-listening, re-reading transcripts, or relying on memory."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_patterns_across_your_meetings", "rar_sha256": "96763343ed4649f04c2a587872f170153f9059416d726ae3bc7d7aac1cd045f0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "find_patterns_across_your_meetings_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/find-patterns-across-your-meetings:3dc3f6a9c5dfbc72dab162160ebdc4518a72d4310d4dba25b15e8c0b76671b12", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/find_patterns_across_your_meetings`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `find_patterns_across_your_meetings_agent.py` is
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

Find patterns across your meetings — Surface the themes that are repeating across your meetings - without re-listening, re-reading transcripts, or relying on memory.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/find-patterns-across-your-meetings
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_patterns_across_your_meetings_agent.py` and embedded as the fenced Python below (sha256 96763343ed4649f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_patterns_across_your_meetings_agent.py` first:

```bash
python3 find_patterns_across_your_meetings_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 find_patterns_across_your_meetings_agent.py   # or on stdin
python3 find_patterns_across_your_meetings_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Find patterns across your meetings — Surface the themes that are repeating across your meetings - without re-listening, re-reading transcripts, or relying on memory.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/find-patterns-across-your-meetings
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/find_patterns_across_your_meetings',
    "version": '2.0.0',
    "display_name": 'Find patterns across your meetings',
    "description": 'Surface the themes that are repeating across your meetings - without re-listening, re-reading transcripts, or relying on memory.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'advanced', 'read_only'],
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
        "upstream_slug": 'find-patterns-across-your-meetings',
        "upstream_url": 'https://coworkcookbook.com/recipes/find-patterns-across-your-meetings',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c9119b37586c96b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/research-and-synthesize/analyze-collaboration-patterns'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/find-patterns-across-your-meetings', 'uses_skills': {'custom': [], 'ootb': ['Scheduling', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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


class FindPatternsAcrossYourMeetings(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FindPatternsAcrossYourMeetings'
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
    print(FindPatternsAcrossYourMeetings().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
