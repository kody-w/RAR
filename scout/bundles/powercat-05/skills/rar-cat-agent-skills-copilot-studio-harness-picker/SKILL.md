---
name: "rar-cat-agent-skills-copilot-studio-harness-picker"
description: "Choose the right Copilot Studio harness and build shape; in Cowork, use GPT-5.6 with High effort for Detailed mode, Claude Opus 5 as fallback, or Auto for Quick mode."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_harness_picker", "rar_sha256": "8075c230d2a97c1096252928ca33d87849b787515ea071d1b27fbea0cd27af6d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.1.2", "author": "Liam O'Grady", "tags": ["copilot_studio", "cowork", "architecture", "agent_design", "governance", "licensing"]}
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
