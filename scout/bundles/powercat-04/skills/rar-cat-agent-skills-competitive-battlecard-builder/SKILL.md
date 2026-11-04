---
name: "rar-cat-agent-skills-competitive-battlecard-builder"
description: "Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/competitive_battlecard_builder", "rar_sha256": "89f511488361213aaf07ded3e0492e5111c9ad61267bbdcaf45e2363e34deff7", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Michael Heath", "tags": ["sales_enablement", "productivity", "comparison"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/competitive_battlecard_builder`. The original RAPP
agent is preserved byte-for-byte in `competitive_battlecard_builder_agent.py` and in the RCI capsule.

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

Competitive Battlecard Builder — Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#competitive-battlecard-builder
  Upstream author: Michael Heath
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `competitive_battlecard_builder_agent.py` and embedded as the fenced Python below (sha256 89f511488361213a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `competitive_battlecard_builder_agent.py` first:

```bash
python3 competitive_battlecard_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 competitive_battlecard_builder_agent.py   # or on stdin
python3 competitive_battlecard_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/competitive_battlecard_builder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/competitive_battlecard_builder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/competitive_battlecard_builder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Competitive Battlecard Builder — Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#competitive-battlecard-builder
  Upstream author: Michael Heath
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/competitive_battlecard_builder',
    "version": '3.0.2',
    "display_name": 'Competitive Battlecard Builder',
    "description": 'Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a…',
    "author": 'Michael Heath',
    "tags": ['sales_enablement', 'productivity', 'comparison'],
    "category": 'general',
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
        "upstream_slug": 'competitive-battlecard-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#competitive-battlecard-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd2d932cf8ec2e523',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.667, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:comparison'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class CompetitiveBattlecardBuilder(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CompetitiveBattlecardBuilder'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(CompetitiveBattlecardBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
