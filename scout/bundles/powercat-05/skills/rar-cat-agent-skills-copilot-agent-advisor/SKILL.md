---
name: "rar-cat-agent-skills-copilot-agent-advisor"
description: "Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario \u2014 use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent \u2014 and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agent_advisor", "rar_sha256": "9de2c8ca78c8387755c34f06b7c478530cb3e84df8efe19abf60e1ad42e8932d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sandra Boucenna", "tags": ["copilot_studio", "agents", "decision_support", "architecture", "advisor"]}
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
