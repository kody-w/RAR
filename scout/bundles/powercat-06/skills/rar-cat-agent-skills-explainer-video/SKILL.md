---
name: "rar-cat-agent-skills-explainer-video"
description: "Create narrated, captioned 1080p explainer videos with researched scripts, generated b-roll, and supplied screenshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/explainer_video", "rar_sha256": "9686a832209ed4f3e113bf25dc1f2bbd172540b760616a84fc96b45fc3d87f52", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Damien Bird", "tags": ["video", "education", "training", "communication"]}
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
