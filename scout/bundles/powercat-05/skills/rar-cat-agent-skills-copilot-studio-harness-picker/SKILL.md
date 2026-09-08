---
name: "rar-cat-agent-skills-copilot-studio-harness-picker"
description: "Choose the right Copilot Studio harness and build shape; in Cowork, use GPT-5.6 with High effort for Detailed mode, Claude Opus 5 as fallback, or Auto for Quick mode."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_harness_picker", "rar_sha256": "8075c230d2a97c1096252928ca33d87849b787515ea071d1b27fbea0cd27af6d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.1.2", "author": "Liam O'Grady", "tags": ["copilot_studio", "cowork", "architecture", "agent_design", "governance", "licensing"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_harness_picker_agent.py` and embedded as the fenced Python below (sha256 8075c230d2a97c10…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_harness_picker_agent.py` first:

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
    "version": '3.1.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
