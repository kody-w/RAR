---
name: "rar-cat-agent-skills-power-automate-documentation"
description: "Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_documentation", "rar_sha256": "3344a86f74a0583dbd4ef3455746795bec78b962fa22169be50ad5f5e6094454", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["power_automate", "documentation", "audit", "governance"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/power_automate_documentation`. The original RAPP
agent is preserved byte-for-byte in `power_automate_documentation_agent.py` and in the RCI capsule.

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

Power Automate Documentation — Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-automate-documentation
  Upstream author: Mathias Salomonsen
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_automate_documentation_agent.py` and embedded as the fenced Python below (sha256 3344a86f74a0583d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_automate_documentation_agent.py` first:

```bash
python3 power_automate_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 power_automate_documentation_agent.py   # or on stdin
python3 power_automate_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/power_automate_documentation_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/power_automate_documentation_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/power_automate_documentation/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Power Automate Documentation — Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-automate-documentation
  Upstream author: Mathias Salomonsen
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/power_automate_documentation',
    "version": '3.0.2',
    "display_name": 'Power Automate Documentation',
    "description": 'Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically.',
    "author": 'Mathias Salomonsen',
    "tags": ['power_automate', 'documentation', 'audit', 'governance'],
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
        "upstream_slug": 'power-automate-documentation',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#power-automate-documentation',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4c5eb6e7dd7c2d70',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'tag:governance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PowerAutomateDocumentation(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PowerAutomateDocumentation'
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
    print(PowerAutomateDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
