---
name: "rar-cat-agent-skills-stoic-negotiator"
description: "A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/stoic_negotiator", "rar_sha256": "c39474c15d45f3a477eb894f916d8f5fb8374755f6327fada1a1d2243ac4dfd1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["negotiation", "decision_making", "offers", "salary", "sales", "commerce", "batna", "zopa"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stoic_negotiator_agent.py` and embedded as the fenced Python below (sha256 c39474c15d45f3a4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stoic_negotiator_agent.py` first:

```bash
python3 stoic_negotiator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stoic_negotiator_agent.py   # or on stdin
python3 stoic_negotiator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
