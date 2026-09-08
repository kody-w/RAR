---
name: "rar-cat-agent-skills-pattern-radar-automation"
description: "Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar_automation", "rar_sha256": "ab2782b399f23ea2a6097225af0525071d5d663d639f77cd09aef47502710bad", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["automation", "productivity", "teams", "email", "content", "insights"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/pattern_radar_automation`. The original RAPP
agent is preserved byte-for-byte in `pattern_radar_automation_agent.py` and in the RCI capsule.

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

Pattern Radar (Scheduled) — Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing — things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pattern-radar-automation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pattern_radar_automation_agent.py` and embedded as the fenced Python below (sha256 ab2782b399f23ea2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pattern_radar_automation_agent.py` first:

```bash
python3 pattern_radar_automation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pattern_radar_automation_agent.py   # or on stdin
python3 pattern_radar_automation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pattern Radar (Scheduled) — Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing — things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pattern-radar-automation
  Upstream author: Srinivas Varukala
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/pattern_radar_automation',
    "version": '3.0.2',
    "display_name": 'Pattern Radar (Scheduled)',
    "description": 'Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing — things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware.',
    "author": 'Srinivas Varukala',
    "tags": ['automation', 'productivity', 'teams', 'email', 'content', 'insights'],
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
        "upstream_slug": 'pattern-radar-automation',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#pattern-radar-automation',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '137112290f4a7fbf',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.421, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:email'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PatternRadarAutomation(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PatternRadarAutomation'
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
    print(PatternRadarAutomation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
