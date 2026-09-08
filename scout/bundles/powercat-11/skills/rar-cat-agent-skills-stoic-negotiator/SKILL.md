---
name: "rar-cat-agent-skills-stoic-negotiator"
description: "A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/stoic_negotiator", "rar_sha256": "c39474c15d45f3a477eb894f916d8f5fb8374755f6327fada1a1d2243ac4dfd1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Faride Ilanda", "tags": ["negotiation", "decision_making", "offers", "salary", "sales", "commerce", "batna", "zopa"]}
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
