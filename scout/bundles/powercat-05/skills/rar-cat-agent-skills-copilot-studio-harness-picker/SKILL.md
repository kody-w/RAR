---
name: "rar-cat-agent-skills-copilot-studio-harness-picker"
description: "Choose the right Copilot Studio harness and build shape; in Cowork, use GPT-5.6 with High effort for Detailed mode, Claude Opus 5 as fallback, or Auto for Quick mode."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_harness_picker", "rar_sha256": "1517c780cf92757e91fb379b2b85ddf7d16ea2c1dac2057dae9a320cd351af59", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "copilot_studio_harness_picker_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/copilot-studio-harness-picker:dddc680f2c77dd6a5b96ec3a7a0545176175820118004359a822910e5ffcb9af", "kind": "skill"}, "version": "2.1.0", "author": "Liam O'Grady", "tags": ["copilot_studio", "cowork", "architecture", "agent_design", "governance", "licensing"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/copilot_studio_harness_picker`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `copilot_studio_harness_picker_agent.py` is
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

Copilot Studio Harness Picker — Choose the right Copilot Studio harness and build shape; in Cowork, use GPT-5.6 with High effort for Detailed mode, Claude Opus 5 as fallback, or Auto for Quick mode.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-harness-picker
  Upstream author: Liam O'Grady
  Upstream version: 1.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
      "type": "string"
    },
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_harness_picker_agent.py` and embedded as the fenced Python below (sha256 1517c780cf92757e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_harness_picker_agent.py` first:

```bash
python3 copilot_studio_harness_picker_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_harness_picker_agent.py   # or on stdin
python3 copilot_studio_harness_picker_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Studio Harness Picker — Choose the right Copilot Studio harness and build shape; in Cowork, use GPT-5.6 with High effort for Detailed mode, Claude Opus 5 as fallback, or Auto for Quick mode.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-harness-picker
  Upstream author: Liam O'Grady
  Upstream version: 1.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_harness_picker',
    "version": '2.1.0',
    "display_name": 'Copilot Studio Harness Picker',
    "description": 'Choose the right Copilot Studio harness and build shape; in Cowork, use GPT-5.6 with High effort for Detailed mode, Claude Opus 5 as fallback, or Auto for Quick mode.',
    "author": "Liam O'Grady",
    "tags": ['copilot_studio', 'cowork', 'architecture', 'agent_design', 'governance', 'licensing'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'copilot-studio-harness-picker',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-harness-picker',
        "upstream_version": '1.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'eff1a28fe7b6e467',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.6, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:architecture', 'word:shape'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class CopilotStudioHarnessPicker(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioHarnessPicker'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(CopilotStudioHarnessPicker().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
