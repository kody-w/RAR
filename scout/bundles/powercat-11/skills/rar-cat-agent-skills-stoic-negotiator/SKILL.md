---
name: "rar-cat-agent-skills-stoic-negotiator"
description: "A principled negotiation intelligence skill that combines Stoic decision disciplines with evidence-backed research to help individuals, executives, and analyst agents prepare, analyze, and execute high-quality negotiations. Supports interactive scoping workflows, Deep Research sourcing (citations and source URLs), and audit-ready outputs."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/stoic_negotiator", "rar_sha256": "8575b10ac9af4f658319a16d30a5f1171a7497cf0325d9f7363f461b52657e69", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "stoic_negotiator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/stoic-negotiator:5c423fc560b40ada4d6da6a579a03e49d99fa765baa7b6dbc81d24729ba655fa", "kind": "skill"}, "version": "2.0.0", "author": "Faride Ilanda", "tags": ["negotiation", "decision_making", "offers", "salary", "sales", "commerce", "batna", "zopa"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/stoic_negotiator`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `stoic_negotiator_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
