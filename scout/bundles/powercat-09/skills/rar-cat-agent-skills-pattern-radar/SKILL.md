---
name: "rar-cat-agent-skills-pattern-radar"
description: "Scans your recent Microsoft 365 signals to surface recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) or multi-step tasks you keep doing by hand (automation candidates)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar", "rar_sha256": "90a634b339d0eba2c582866b47bb51b2256d8ec11182e3503bebd5486dbe1d1b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["productivity", "automation", "content", "email", "teams", "insights"]}
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
