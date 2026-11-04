---
name: "rar-cat-agent-skills-ai-usecase-assessment"
description: "Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting \u2014 grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_usecase_assessment", "rar_sha256": "a0e344bae6eb0ee5cf9cc52c14d873e9db7d95e0f3c7e3c7f68bee5739b908f8", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Alicja Gilderdale", "tags": ["assessment", "ai", "agent", "use_case", "scoring", "report", "html", "intake"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_usecase_assessment_agent.py` and embedded as the fenced Python below (sha256 a0e344bae6eb0ee5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_usecase_assessment_agent.py` first:

```bash
python3 ai_usecase_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_usecase_assessment_agent.py   # or on stdin
python3 ai_usecase_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/ai_usecase_assessment_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/ai_usecase_assessment_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/ai_usecase_assessment/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
