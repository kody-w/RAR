---
name: "rar-cat-agent-skills-explainer-video"
description: "Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/explainer_video", "rar_sha256": "9686a832209ed4f3e113bf25dc1f2bbd172540b760616a84fc96b45fc3d87f52", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Damien Bird", "tags": ["video", "education", "training", "communication"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `explainer_video_agent.py` and embedded as the fenced Python below (sha256 9686a832209ed4f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `explainer_video_agent.py` first:

```bash
python3 explainer_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 explainer_video_agent.py   # or on stdin
python3 explainer_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/explainer_video_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/explainer_video_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/explainer_video/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
