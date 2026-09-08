---
name: "rar-cat-agent-skills-pattern-radar"
description: "Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar", "rar_sha256": "9930229a7779137b593687d7660122e4af578d169583fbe1c7cd891c624ac443", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["productivity", "automation", "content", "email", "teams", "insights"]}
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
