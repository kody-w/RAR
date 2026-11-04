---
name: "rar-cat-agent-skills-ai-usecase-assessment"
description: "Turn any AI/agentic use case idea (chat, uploaded doc, or attached file) into an evidence-grounded, rubric-scored assessment with a customer-branded HTML report. Guides the user question-by-question through intake, categorisation, strengthening, scoring, and reporting \u2014 grounded in the Agentic Use Case Assessment Rubric v2. Runs in Microsoft Scout and Microsoft 365 Copilot Cowork."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_usecase_assessment", "rar_sha256": "a0e344bae6eb0ee5cf9cc52c14d873e9db7d95e0f3c7e3c7f68bee5739b908f8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Alicja Gilderdale", "tags": ["assessment", "ai", "agent", "use_case", "scoring", "report", "html", "intake"]}
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
