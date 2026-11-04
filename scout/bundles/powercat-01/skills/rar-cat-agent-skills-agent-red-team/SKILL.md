---
name: "rar-cat-agent-skills-agent-red-team"
description: "Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_red_team", "rar_sha256": "5f01b98ad41cd2a57a431bb9af01f063d2fd645d67d6548a58d36a10b3686317", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Marco Zama", "tags": ["copilot_studio", "security", "prompt_injection", "governance", "responsible_ai", "testing", "risk", "assessment"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/agent_red_team`. The original RAPP
agent is preserved byte-for-byte in `agent_red_team_agent.py` and in the RCI capsule.

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

Agent Red Team — Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-red-team
  Upstream author: Marco Zama
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_red_team_agent.py` and embedded as the fenced Python below (sha256 5f01b98ad41cd2a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_red_team_agent.py` first:

```bash
python3 agent_red_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_red_team_agent.py   # or on stdin
python3 agent_red_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/agent_red_team_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/agent_red_team_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/agent_red_team/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Agent Red Team — Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#agent-red-team
  Upstream author: Marco Zama
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/agent_red_team',
    "version": '3.0.2',
    "display_name": 'Agent Red Team',
    "description": 'Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes.',
    "author": 'Marco Zama',
    "tags": ['copilot_studio', 'security', 'prompt_injection', 'governance', 'responsible_ai', 'testing', 'risk', 'assessment'],
    "category": 'analysis',
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
        "upstream_slug": 'agent-red-team',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#agent-red-team',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'a8a2bcecd245a7bb',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.818, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:governance', 'tag:risk', 'tag:security', 'tag:testing', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AgentRedTeam(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AgentRedTeam'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AgentRedTeam().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
