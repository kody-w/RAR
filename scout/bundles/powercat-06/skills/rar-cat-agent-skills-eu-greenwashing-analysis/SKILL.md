---
name: "rar-cat-agent-skills-eu-greenwashing-analysis"
description: "Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/eu_greenwashing_analysis", "rar_sha256": "60f5b0746b2395fef7e8225ba803aeb9de1264b58c9797df97fb0a80123d7a5e", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "eu_greenwashing_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/eu-greenwashing-analysis:b387017d7f3cb988dd0c9c5b3423468464f415bc68e9ad9a2a6327595fa62a2f", "kind": "skill"}, "version": "2.0.0", "author": "Remi Dyon", "tags": ["compliance", "sustainability", "greenwashing", "eu_regulation", "marketing_review", "esg"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/eu_greenwashing_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `eu_greenwashing_analysis_agent.py` is
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

EU Greenwashing Analysis — Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#eu-greenwashing-analysis
  Upstream author: Remi Dyon
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `eu_greenwashing_analysis_agent.py` and embedded as the fenced Python below (sha256 60f5b0746b2395fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `eu_greenwashing_analysis_agent.py` first:

```bash
python3 eu_greenwashing_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 eu_greenwashing_analysis_agent.py   # or on stdin
python3 eu_greenwashing_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
EU Greenwashing Analysis — Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#eu-greenwashing-analysis
  Upstream author: Remi Dyon
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/eu_greenwashing_analysis',
    "version": '2.0.0',
    "display_name": 'EU Greenwashing Analysis',
    "description": 'Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections.',
    "author": 'Remi Dyon',
    "tags": ['compliance', 'sustainability', 'greenwashing', 'eu_regulation', 'marketing_review', 'esg'],
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
        "upstream_slug": 'eu-greenwashing-analysis',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#eu-greenwashing-analysis',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd9597c05205098f3',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork', 'Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 1.0, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:compliance', 'word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class EuGreenwashingAnalysis(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'EuGreenwashingAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(EuGreenwashingAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
