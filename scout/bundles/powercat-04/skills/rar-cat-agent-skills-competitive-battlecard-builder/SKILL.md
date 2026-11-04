---
name: "rar-cat-agent-skills-competitive-battlecard-builder"
description: "Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/competitive_battlecard_builder", "rar_sha256": "89f511488361213aaf07ded3e0492e5111c9ad61267bbdcaf45e2363e34deff7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Michael Heath", "tags": ["sales_enablement", "productivity", "comparison"]}
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
