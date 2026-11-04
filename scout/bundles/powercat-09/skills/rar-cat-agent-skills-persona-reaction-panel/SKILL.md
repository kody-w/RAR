---
name: "rar-cat-agent-skills-persona-reaction-panel"
description: "Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships \u2014 surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/persona_reaction_panel", "rar_sha256": "df0ee4b0cb412b509cf0dd8f9eb98c6373665213472e3b933a078379eab7b0f7", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Olivia Zhang", "tags": ["communications", "change_management", "launch_readiness", "personas", "qa"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `persona_reaction_panel_agent.py` and embedded as the fenced Python below (sha256 df0ee4b0cb412b50…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `persona_reaction_panel_agent.py` first:

```bash
python3 persona_reaction_panel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 persona_reaction_panel_agent.py   # or on stdin
python3 persona_reaction_panel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/persona_reaction_panel_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/persona_reaction_panel_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/persona_reaction_panel/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
