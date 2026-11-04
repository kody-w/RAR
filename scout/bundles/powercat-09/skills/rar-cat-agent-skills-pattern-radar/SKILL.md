---
name: "rar-cat-agent-skills-pattern-radar"
description: "Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar", "rar_sha256": "90a634b339d0eba2c582866b47bb51b2256d8ec11182e3503bebd5486dbe1d1b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["productivity", "automation", "content", "email", "teams", "insights"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pattern_radar_agent.py` and embedded as the fenced Python below (sha256 90a634b339d0eba2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pattern_radar_agent.py` first:

```bash
python3 pattern_radar_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pattern_radar_agent.py   # or on stdin
python3 pattern_radar_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/pattern_radar_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/pattern_radar_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/pattern_radar/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
