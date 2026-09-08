---
name: "rar-cat-agent-skills-ai-usecase-assessment"
description: "Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting \u2014 grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_usecase_assessment", "rar_sha256": "4211e33a8a354bc5487314ad0398877fad82a50b75c97f855d3d613c61aa9a53", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Alicja Gilderdale", "tags": ["assessment", "ai", "agent", "use_case", "scoring", "report", "html", "intake"]}
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
