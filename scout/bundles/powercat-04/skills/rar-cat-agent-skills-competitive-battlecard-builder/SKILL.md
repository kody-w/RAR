---
name: "rar-cat-agent-skills-competitive-battlecard-builder"
description: "Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/competitive_battlecard_builder", "rar_sha256": "c2ecfa863e2631bbee32804ad0b3e1d10b4af20af55d7938b5d97c88c56e92f8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Michael Heath", "tags": ["sales_enablement", "productivity", "comparison"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `competitive_battlecard_builder_agent.py` and embedded as the fenced Python below (sha256 c2ecfa863e2631bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `competitive_battlecard_builder_agent.py` first:

```bash
python3 competitive_battlecard_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 competitive_battlecard_builder_agent.py   # or on stdin
python3 competitive_battlecard_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
