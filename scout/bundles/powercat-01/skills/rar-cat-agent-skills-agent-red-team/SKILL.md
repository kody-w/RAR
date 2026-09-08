---
name: "rar-cat-agent-skills-agent-red-team"
description: "Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_red_team", "rar_sha256": "bd33be4ed1eedbdc195de49a108e26511b59e4ef9ee32e8839cd476334c39dac", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Marco Zama", "tags": ["copilot_studio", "security", "prompt_injection", "governance", "responsible_ai", "testing", "risk", "assessment"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_red_team_agent.py` and embedded as the fenced Python below (sha256 bd33be4ed1eedbdc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_red_team_agent.py` first:

```bash
python3 agent_red_team_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_red_team_agent.py   # or on stdin
python3 agent_red_team_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
