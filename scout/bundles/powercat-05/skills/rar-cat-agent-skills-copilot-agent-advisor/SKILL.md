---
name: "rar-cat-agent-skills-copilot-agent-advisor"
description: "Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario \u2014 use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent \u2014 and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agent_advisor", "rar_sha256": "cf82b12d57ab776f1e9e989e305df5f5cb1acbf749e45dc601841f6e62d83b2d", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Sandra Boucenna", "tags": ["copilot_studio", "agents", "decision_support", "architecture", "advisor"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_agent_advisor_agent.py` and embedded as the fenced Python below (sha256 cf82b12d57ab776f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_agent_advisor_agent.py` first:

```bash
python3 copilot_agent_advisor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_agent_advisor_agent.py   # or on stdin
python3 copilot_agent_advisor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/copilot_agent_advisor_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_agent_advisor_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_agent_advisor/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
