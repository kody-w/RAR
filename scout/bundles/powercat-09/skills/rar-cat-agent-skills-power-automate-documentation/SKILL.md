---
name: "rar-cat-agent-skills-power-automate-documentation"
description: "Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_documentation", "rar_sha256": "3344a86f74a0583dbd4ef3455746795bec78b962fa22169be50ad5f5e6094454", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["power_automate", "documentation", "audit", "governance"]}
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
