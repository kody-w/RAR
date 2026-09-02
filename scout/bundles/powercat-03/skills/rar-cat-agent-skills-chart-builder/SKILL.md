---
name: "rar-cat-agent-skills-chart-builder"
description: "Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/chart_builder", "rar_sha256": "f8c8b03dc4628aed2f0ddb36fee0bade66fb9ee1ceff7e2d407c92a7ff4dedf0", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "chart_builder_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/chart-builder:8ac4e40970de2216662b82c9982f27e8c92fcf2b82d9208bf5d4f66a7a5a6b02", "kind": "skill"}, "version": "2.0.1", "author": "Adi Leibowitz", "tags": ["data", "charts", "matplotlib", "scripts"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/chart_builder`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `chart_builder_agent.py` is
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

Chart Builder — Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#chart-builder
  Upstream author: Adi Leibowitz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `chart_builder_agent.py` and embedded as the fenced Python below (sha256 f8c8b03dc4628aed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `chart_builder_agent.py` first:

```bash
python3 chart_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 chart_builder_agent.py   # or on stdin
python3 chart_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Chart Builder — Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#chart-builder
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/chart_builder',
    "version": '2.0.1',
    "display_name": 'Chart Builder',
    "description": 'Generate clean, consistently-styled matplotlib charts (bar, line, scatter, histogram, pie) from a DataFrame or CSV with one call.',
    "author": 'Adi Leibowitz',
    "tags": ['data', 'charts', 'matplotlib', 'scripts'],
    "category": 'devtools',
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
        "upstream_slug": 'chart-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#chart-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'f32fa164a482da33',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.4, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:data'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ChartBuilder(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ChartBuilder'
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
    print(ChartBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
