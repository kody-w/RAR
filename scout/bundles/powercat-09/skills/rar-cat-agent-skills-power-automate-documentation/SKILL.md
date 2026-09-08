---
name: "rar-cat-agent-skills-power-automate-documentation"
description: "Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_documentation", "rar_sha256": "2f6813624393f9855a67039690460b474cd338bc60bad710bc594790761b4ab0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["power_automate", "documentation", "audit", "governance"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_automate_documentation_agent.py` and embedded as the fenced Python below (sha256 2f6813624393f985…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_automate_documentation_agent.py` first:

```bash
python3 power_automate_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 power_automate_documentation_agent.py   # or on stdin
python3 power_automate_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
