---
name: "rar-cat-agent-skills-copilot-studio-harness-picker"
description: "Choose the right Copilot Studio harness and build shape; in Cowork, use GPT-5.6 with High effort for Detailed mode, Claude Opus 5 as fallback, or Auto for Quick mode."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_harness_picker", "rar_sha256": "1517c780cf92757e91fb379b2b85ddf7d16ea2c1dac2057dae9a320cd351af59", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.1.0", "author": "Liam O'Grady", "tags": ["copilot_studio", "cowork", "architecture", "agent_design", "governance", "licensing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_studio_harness_picker`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_harness_picker_agent.py` and in the RCI capsule.

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
