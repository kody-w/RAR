---
name: "rar-cat-agent-skills-persona-reaction-panel"
description: "Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships \u2014 surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/persona_reaction_panel", "rar_sha256": "adb83b8e6e07fe792cd7d5f581885ca1a6ada5be3413e82fe4a4620520596f53", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Olivia Zhang", "tags": ["communications", "change_management", "launch_readiness", "personas", "qa"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/persona_reaction_panel`. The original RAPP
agent is preserved byte-for-byte in `persona_reaction_panel_agent.py` and in the RCI capsule.

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

Persona Reaction Panel — Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships — surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#persona-reaction-panel
  Upstream author: Olivia Zhang
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `persona_reaction_panel_agent.py` and embedded as the fenced Python below (sha256 adb83b8e6e07fe79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `persona_reaction_panel_agent.py` first:

```bash
python3 persona_reaction_panel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 persona_reaction_panel_agent.py   # or on stdin
python3 persona_reaction_panel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Persona Reaction Panel — Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships — surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#persona-reaction-panel
  Upstream author: Olivia Zhang
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/persona_reaction_panel',
    "version": '3.0.2',
    "display_name": 'Persona Reaction Panel',
    "description": 'Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships — surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file.',
    "author": 'Olivia Zhang',
    "tags": ['communications', 'change_management', 'launch_readiness', 'personas', 'qa'],
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
        "upstream_slug": 'persona-reaction-panel',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#persona-reaction-panel',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd947b7c2da61f3de',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 1.0, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PersonaReactionPanel(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PersonaReactionPanel'
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
    print(PersonaReactionPanel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
