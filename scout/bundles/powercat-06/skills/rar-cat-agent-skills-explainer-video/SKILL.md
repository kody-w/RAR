---
name: "rar-cat-agent-skills-explainer-video"
description: "Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/explainer_video", "rar_sha256": "9b6c64387e7189d3525390d4505dc759e7542d6c656deae1f0c1414bdb4ba0bc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Damien Bird", "tags": ["video", "education", "training", "communication"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/explainer_video`. The original RAPP
agent is preserved byte-for-byte in `explainer_video_agent.py` and in the RCI capsule.

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

Explainer Video — Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#explainer-video
  Upstream author: Damien Bird
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `explainer_video_agent.py` and embedded as the fenced Python below (sha256 9b6c64387e7189d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `explainer_video_agent.py` first:

```bash
python3 explainer_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 explainer_video_agent.py   # or on stdin
python3 explainer_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Explainer Video — Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#explainer-video
  Upstream author: Damien Bird
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/explainer_video',
    "version": '3.0.2',
    "display_name": 'Explainer Video',
    "description": 'Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots.',
    "author": 'Damien Bird',
    "tags": ['video', 'education', 'training', 'communication'],
    "category": 'creative',
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
        "upstream_slug": 'explainer-video',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#explainer-video',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '3922dbf6d24c64ac',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:communication'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ExplainerVideo(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ExplainerVideo'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ExplainerVideo().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
