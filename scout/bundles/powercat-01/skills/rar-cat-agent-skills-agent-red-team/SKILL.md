---
name: "rar-cat-agent-skills-agent-red-team"
description: "Adversarial assurance review for agents you own: prompt injection, oversharing, leakage and tool misuse, mapped to fixes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/agent_red_team", "rar_sha256": "bd33be4ed1eedbdc195de49a108e26511b59e4ef9ee32e8839cd476334c39dac", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Marco Zama", "tags": ["copilot_studio", "security", "prompt_injection", "governance", "responsible_ai", "testing", "risk", "assessment"]}
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
