---
name: "rar-cat-agent-skills-ai-usecase-assessment"
description: "Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting \u2014 grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_usecase_assessment", "rar_sha256": "4211e33a8a354bc5487314ad0398877fad82a50b75c97f855d3d613c61aa9a53", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Alicja Gilderdale", "tags": ["assessment", "ai", "agent", "use_case", "scoring", "report", "html", "intake"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/ai_usecase_assessment`. The original RAPP
agent is preserved byte-for-byte in `ai_usecase_assessment_agent.py` and in the RCI capsule.

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

AI Use Case Assessment — Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting — grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-usecase-assessment
  Upstream author: Alicja Gilderdale
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_usecase_assessment_agent.py` and embedded as the fenced Python below (sha256 4211e33a8a354bc5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_usecase_assessment_agent.py` first:

```bash
python3 ai_usecase_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_usecase_assessment_agent.py   # or on stdin
python3 ai_usecase_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AI Use Case Assessment — Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting — grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-usecase-assessment
  Upstream author: Alicja Gilderdale
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/ai_usecase_assessment',
    "version": '3.0.2',
    "display_name": 'AI Use Case Assessment',
    "description": 'Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting — grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork.',
    "author": 'Alicja Gilderdale',
    "tags": ['assessment', 'ai', 'agent', 'use_case', 'scoring', 'report', 'html', 'intake'],
    "category": 'analysis',
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
        "upstream_slug": 'ai-usecase-assessment',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#ai-usecase-assessment',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '8d143663df287664',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout', 'Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.4, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AiUsecaseAssessment(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AiUsecaseAssessment'
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
    print(AiUsecaseAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
