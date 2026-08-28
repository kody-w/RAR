---
name: "rar-cowork-cookbook-prepare-a-complete-out-of-office-handoff"
description: "Step away from your laptop knowing nothing in flight will stall while you are out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_a_complete_out_of_office_handoff", "rar_sha256": "3ee9b46982fb0bfa5bb9a6188107f9c8615a79a6e284271d6ddc29800209fbfa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prepare_a_complete_out_of_office_handoff`. The original RAPP
agent is preserved byte-for-byte in `prepare_a_complete_out_of_office_handoff_agent.py` and in the RCI capsule.

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

Prepare a complete out-of-office handoff — Step away from your laptop knowing nothing in flight will stall while you are out.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prepare_a_complete_out_of_office_handoff_agent.py` and embedded as the fenced Python below (sha256 3ee9b46982fb0bfa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prepare_a_complete_out_of_office_handoff_agent.py` first:

```bash
python3 prepare_a_complete_out_of_office_handoff_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prepare_a_complete_out_of_office_handoff_agent.py   # or on stdin
python3 prepare_a_complete_out_of_office_handoff_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare a complete out-of-office handoff — Step away from your laptop knowing nothing in flight will stall while you are out.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prepare_a_complete_out_of_office_handoff',
    "version": '2.0.1',
    "display_name": 'Prepare a complete out-of-office handoff',
    "description": 'Step away from your laptop knowing nothing in flight will stall while you are out.',
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
        "upstream_slug": 'prepare-a-complete-out-of-office-handoff',
        "upstream_url": 'https://coworkcookbook.com/recipes/prepare-a-complete-out-of-office-handoff',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f3c59d4f41c70cbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/coordinate-team-work/hand-off-work-during-absence'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/prepare-a-complete-out-of-office-handoff', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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


class PrepareACompleteOutOfOfficeHandoff(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepareACompleteOutOfOfficeHandoff'
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
    print(PrepareACompleteOutOfOfficeHandoff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
