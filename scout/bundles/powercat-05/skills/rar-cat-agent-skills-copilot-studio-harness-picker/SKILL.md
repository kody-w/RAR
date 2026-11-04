---
name: "rar-cat-agent-skills-copilot-studio-harness-picker"
description: "Choose the right Copilot Studio harness and build shape; in Cowork, use GPT-5.6 with High effort for Detailed mode, Claude Opus 5 as fallback, or Auto for Quick mode."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_harness_picker", "rar_sha256": "1260a59deabc3fa4f801f715786f4e643a4ef09184950388aae09939855f7091", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.1.2", "author": "Liam O'Grady", "tags": ["copilot_studio", "cowork", "architecture", "agent_design", "governance", "licensing"]}
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
