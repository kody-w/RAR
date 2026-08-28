---
name: "rar-cowork-cookbook-find-patterns-across-your-meetings"
description: "Surface the themes that are repeating across your meetings - without re-listening, re-reading transcripts, or relying on memory."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_patterns_across_your_meetings", "rar_sha256": "96763343ed4649f04c2a587872f170153f9059416d726ae3bc7d7aac1cd045f0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/find_patterns_across_your_meetings`. The original RAPP
agent is preserved byte-for-byte in `find_patterns_across_your_meetings_agent.py` and in the RCI capsule.

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
