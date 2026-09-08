---
name: "rar-cat-agent-skills-power-automate-documentation"
description: "Turns a Power Automate solution .zip into a clean markdown reference for every flow inside it: trigger, plain-English process, connection references, and a read/write/delete table for everything it touches. Maps which flows call each other and unresolved connections automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_automate_documentation", "rar_sha256": "2f6813624393f9855a67039690460b474cd338bc60bad710bc594790761b4ab0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Mathias Salomonsen", "tags": ["power_automate", "documentation", "audit", "governance"]}
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
