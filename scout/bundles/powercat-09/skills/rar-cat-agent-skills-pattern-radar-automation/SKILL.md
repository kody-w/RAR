---
name: "rar-cat-agent-skills-pattern-radar-automation"
description: "Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar_automation", "rar_sha256": "ab2782b399f23ea2a6097225af0525071d5d663d639f77cd09aef47502710bad", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["automation", "productivity", "teams", "email", "content", "insights"]}
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
