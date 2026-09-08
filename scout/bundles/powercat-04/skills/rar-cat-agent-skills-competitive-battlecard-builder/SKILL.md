---
name: "rar-cat-agent-skills-competitive-battlecard-builder"
description: "Build an interactive comparison app, either a sales battlecard advocating for your product against named competitors, or a neutral, unbiased comparison across two or more peer items with no side taken. Filterable by item and category, with live search, a compact scorecard, and copy-to-clipboard talking points. Every claim is tagged verified or unverified so nothing invented ends up in front of a\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/competitive_battlecard_builder", "rar_sha256": "c2ecfa863e2631bbee32804ad0b3e1d10b4af20af55d7938b5d97c88c56e92f8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Michael Heath", "tags": ["sales_enablement", "productivity", "comparison"]}
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
