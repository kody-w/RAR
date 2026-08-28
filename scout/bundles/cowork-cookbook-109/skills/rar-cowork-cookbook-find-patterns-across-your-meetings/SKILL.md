---
name: "rar-cowork-cookbook-find-patterns-across-your-meetings"
description: "Surface the themes that are repeating across your meetings - without re-listening, re-reading transcripts, or relying on memory."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_patterns_across_your_meetings", "rar_sha256": "b002c77a242c86f1f347676678c321f095571e9ed9a417d6d3d8eb102b2c2dc6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_patterns_across_your_meetings_agent.py` and embedded as the fenced Python below (sha256 b002c77a242c86f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_patterns_across_your_meetings_agent.py` first:

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
    "version": '2.0.1',
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
