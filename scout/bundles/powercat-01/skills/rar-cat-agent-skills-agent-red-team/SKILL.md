---
name: "rar-cat-agent-skills-agent-red-team"
description: "Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_red_team", "rar_sha256": "5f01b98ad41cd2a57a431bb9af01f063d2fd645d67d6548a58d36a10b3686317", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Marco Zama", "tags": ["copilot_studio", "security", "prompt_injection", "governance", "responsible_ai", "testing", "risk", "assessment"]}
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
