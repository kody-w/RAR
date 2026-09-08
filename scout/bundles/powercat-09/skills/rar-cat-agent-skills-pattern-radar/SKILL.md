---
name: "rar-cat-agent-skills-pattern-radar"
description: "Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar", "rar_sha256": "9930229a7779137b593687d7660122e4af578d169583fbe1c7cd891c624ac443", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["productivity", "automation", "content", "email", "teams", "insights"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/pattern_radar`. The original RAPP
agent is preserved byte-for-byte in `pattern_radar_agent.py` and in the RCI capsule.

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

Pattern Radar — Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing — things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pattern-radar
  Upstream author: Srinivas Varukala
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pattern_radar_agent.py` and embedded as the fenced Python below (sha256 9930229a7779137b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pattern_radar_agent.py` first:

```bash
python3 pattern_radar_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pattern_radar_agent.py   # or on stdin
python3 pattern_radar_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pattern Radar — Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing — things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pattern-radar
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/pattern_radar',
    "version": '3.0.2',
    "display_name": 'Pattern Radar',
    "description": 'Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing — things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates).',
    "author": 'Srinivas Varukala',
    "tags": ['productivity', 'automation', 'content', 'email', 'teams', 'insights'],
    "category": 'productivity',
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
        "upstream_slug": 'pattern-radar',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#pattern-radar',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'cde1b5f304153695',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:email'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PatternRadar(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PatternRadar'
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
    print(PatternRadar().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
