---
name: "rar-cat-agent-skills-explainer-video"
description: "Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/explainer_video", "rar_sha256": "9b6c64387e7189d3525390d4505dc759e7542d6c656deae1f0c1414bdb4ba0bc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Damien Bird", "tags": ["video", "education", "training", "communication"]}
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
