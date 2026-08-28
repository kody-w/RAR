---
name: "rar-cat-agent-skills-stoic-negotiator"
description: "A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/stoic_negotiator", "rar_sha256": "8575b10ac9af4f658319a16d30a5f1171a7497cf0325d9f7363f461b52657e69", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.0.0", "author": "Faride Ilanda", "tags": ["negotiation", "decision_making", "offers", "salary", "sales", "commerce", "batna", "zopa"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stoic_negotiator_agent.py` and embedded as the fenced Python below (sha256 8575b10ac9af4f65…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stoic_negotiator_agent.py` first:

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
    "version": '2.0.0',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
