---
name: "rar-cat-agent-skills-stoic-negotiator"
description: "A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/stoic_negotiator", "rar_sha256": "c74fb9856ed7018e68218cddcd1930ac99ccd995855c5106c6feb4cab241d398", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["negotiation", "decision_making", "offers", "salary", "sales", "commerce", "batna", "zopa"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/stoic_negotiator`. The original RAPP
agent is preserved byte-for-byte in `stoic_negotiator_agent.py` and in the RCI capsule.

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

Stoic Negotiator — A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#stoic-negotiator
  Upstream author: Faride Ilanda
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stoic_negotiator_agent.py` and embedded as the fenced Python below (sha256 c74fb9856ed7018e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stoic_negotiator_agent.py` first:

```bash
python3 stoic_negotiator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stoic_negotiator_agent.py   # or on stdin
python3 stoic_negotiator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/stoic_negotiator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/stoic_negotiator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/stoic_negotiator/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Stoic Negotiator — A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#stoic-negotiator
  Upstream author: Faride Ilanda
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/stoic_negotiator',
    "version": '3.0.2',
    "display_name": 'Stoic Negotiator',
    "description": 'A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs.',
    "author": 'Faride Ilanda',
    "tags": ['negotiation', 'decision_making', 'offers', 'salary', 'sales', 'commerce', 'batna', 'zopa'],
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
        "upstream_slug": 'stoic-negotiator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#stoic-negotiator',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'c1a8d265f7e75943',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.8, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:decision_making', 'word:analyze', 'word:research'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class StoicNegotiator(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StoicNegotiator'
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
    print(StoicNegotiator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
