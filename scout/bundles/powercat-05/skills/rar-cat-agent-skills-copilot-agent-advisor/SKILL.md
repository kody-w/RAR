---
name: "rar-cat-agent-skills-copilot-agent-advisor"
description: "Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario \u2014 use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent \u2014 and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agent_advisor", "rar_sha256": "9de2c8ca78c8387755c34f06b7c478530cb3e84df8efe19abf60e1ad42e8932d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sandra Boucenna", "tags": ["copilot_studio", "agents", "decision_support", "architecture", "advisor"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_agent_advisor`. The original RAPP
agent is preserved byte-for-byte in `copilot_agent_advisor_agent.py` and in the RCI capsule.

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

Copilot Agent Advisor — Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario — use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent — and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-agent-advisor
  Upstream author: Sandra Boucenna
  Upstream version: 1.0.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_agent_advisor_agent.py` and embedded as the fenced Python below (sha256 9de2c8ca78c83877…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_agent_advisor_agent.py` first:

```bash
python3 copilot_agent_advisor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_agent_advisor_agent.py   # or on stdin
python3 copilot_agent_advisor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Agent Advisor — Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario — use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent — and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-agent-advisor
  Upstream author: Sandra Boucenna
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_agent_advisor',
    "version": '3.0.2',
    "display_name": 'Copilot Agent Advisor',
    "description": 'Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario — use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent — and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on.',
    "author": 'Sandra Boucenna',
    "tags": ['copilot_studio', 'agents', 'decision_support', 'architecture', 'advisor'],
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
        "upstream_slug": 'copilot-agent-advisor',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-agent-advisor',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b04c9390fef8539e',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.5, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:architecture'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class CopilotAgentAdvisor(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotAgentAdvisor'
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
    print(CopilotAgentAdvisor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
