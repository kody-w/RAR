---
name: "rar-cat-agent-skills-copilot-studio-harness-picker"
description: "Choose the right Copilot Studio harness and build shape; in Cowork, use GPT-5.6 with High effort for Detailed mode, Claude Opus 5 as fallback, or Auto for Quick mode."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_harness_picker", "rar_sha256": "1260a59deabc3fa4f801f715786f4e643a4ef09184950388aae09939855f7091", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.1.2", "author": "Liam O'Grady", "tags": ["copilot_studio", "cowork", "architecture", "agent_design", "governance", "licensing"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_harness_picker_agent.py` and embedded as the fenced Python below (sha256 1260a59deabc3fa4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_harness_picker_agent.py` first:

```bash
python3 copilot_studio_harness_picker_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_harness_picker_agent.py   # or on stdin
python3 copilot_studio_harness_picker_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/copilot_studio_harness_picker_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_harness_picker_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_studio_harness_picker/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
