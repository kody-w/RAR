---
name: "rar-cat-agent-skills-pattern-radar-automation"
description: "Twice a week, scans your recent Microsoft 365 signals and posts a Teams summary of recurring patterns worth productizing \u2014 things you keep explaining (blog candidates) and multi-step tasks you keep doing by hand (automation candidates). Read-only and privacy-aware."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pattern_radar_automation", "rar_sha256": "319cb185009cc709612e02345f0c748a7e79856f0213477ae666fd0287f20ad2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Srinivas Varukala", "tags": ["automation", "productivity", "teams", "email", "content", "insights"]}
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
