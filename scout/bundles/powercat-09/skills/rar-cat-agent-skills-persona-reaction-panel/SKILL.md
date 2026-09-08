---
name: "rar-cat-agent-skills-persona-reaction-panel"
description: "Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships \u2014 surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/persona_reaction_panel", "rar_sha256": "adb83b8e6e07fe792cd7d5f581885ca1a6ada5be3413e82fe4a4620520596f53", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Olivia Zhang", "tags": ["communications", "change_management", "launch_readiness", "personas", "qa"]}
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
