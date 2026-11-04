---
name: "rar-cat-agent-skills-pattern-radar-automation"
description: "Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar_automation", "rar_sha256": "319cb185009cc709612e02345f0c748a7e79856f0213477ae666fd0287f20ad2", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["automation", "productivity", "teams", "email", "content", "insights"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pattern_radar_automation_agent.py` and embedded as the fenced Python below (sha256 319cb185009cc709…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pattern_radar_automation_agent.py` first:

```bash
python3 pattern_radar_automation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pattern_radar_automation_agent.py   # or on stdin
python3 pattern_radar_automation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/pattern_radar_automation_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/pattern_radar_automation_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/pattern_radar_automation/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
