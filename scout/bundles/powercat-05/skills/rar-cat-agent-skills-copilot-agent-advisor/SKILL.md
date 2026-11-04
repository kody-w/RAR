---
name: "rar-cat-agent-skills-copilot-agent-advisor"
description: "Tells you which Microsoft 365 / Copilot Studio agent option fits your scenario \u2014 use M365 Copilot as-is, build a standard (declarative) agent, or build a custom (custom engine) agent \u2014 and which Copilot Studio harness (GitHub Copilot, standard, or Copilot chat) to build on."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agent_advisor", "rar_sha256": "cf82b12d57ab776f1e9e989e305df5f5cb1acbf749e45dc601841f6e62d83b2d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sandra Boucenna", "tags": ["copilot_studio", "agents", "decision_support", "architecture", "advisor"]}
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
