---
name: "rar-cat-agent-skills-copilot-studio-agent-test"
description: "Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report \u2014 no browser automation."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_agent_test", "rar_sha256": "1075b0924639851f5066ff8f70c560ddf98829c6bbff4bf5fbfbc8bdb0cffd91", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Matteo Pagani", "tags": ["copilot_studio", "testing", "evaluation", "quality", "agents", "power_platform"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_studio_agent_test`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_agent_test_agent.py` and in the RCI capsule.

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

Copilot Studio Agent Test — Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report — no browser automation.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-agent-test
  Upstream author: Matteo Pagani
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_agent_test_agent.py` and embedded as the fenced Python below (sha256 1075b0924639851f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_agent_test_agent.py` first:

```bash
python3 copilot_studio_agent_test_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_agent_test_agent.py   # or on stdin
python3 copilot_studio_agent_test_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/copilot_studio_agent_test_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_studio_agent_test_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_studio_agent_test/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Copilot Studio Agent Test — Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report — no browser automation.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-agent-test
  Upstream author: Matteo Pagani
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_agent_test',
    "version": '3.0.2',
    "display_name": 'Copilot Studio Agent Test',
    "description": 'Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report — no browser automation.',
    "author": 'Matteo Pagani',
    "tags": ['copilot_studio', 'testing', 'evaluation', 'quality', 'agents', 'power_platform'],
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
        "upstream_slug": 'copilot-studio-agent-test',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-agent-test',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ac86f61bb9663d51',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:quality', 'tag:testing', 'word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class CopilotStudioAgentTest(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioAgentTest'
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
    print(CopilotStudioAgentTest().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
