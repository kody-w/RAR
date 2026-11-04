---
name: "rar-cat-agent-skills-persona-reaction-panel"
description: "Pre-test an internal launch, comms, or enablement artefact against your own role-based personas before it ships \u2014 surfaces blackspots, domain gaps, credible-detractor risks, and concrete edits. Bring your own personas file."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/persona_reaction_panel", "rar_sha256": "df0ee4b0cb412b509cf0dd8f9eb98c6373665213472e3b933a078379eab7b0f7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Olivia Zhang", "tags": ["communications", "change_management", "launch_readiness", "personas", "qa"]}
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
