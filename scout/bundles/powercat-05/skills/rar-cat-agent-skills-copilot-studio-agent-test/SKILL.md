---
name: "rar-cat-agent-skills-copilot-studio-agent-test"
description: "Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report \u2014 no browser automation."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_agent_test", "rar_sha256": "1075b0924639851f5066ff8f70c560ddf98829c6bbff4bf5fbfbc8bdb0cffd91", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Matteo Pagani", "tags": ["copilot_studio", "testing", "evaluation", "quality", "agents", "power_platform"]}
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
