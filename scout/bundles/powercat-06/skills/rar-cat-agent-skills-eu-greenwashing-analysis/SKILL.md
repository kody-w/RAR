---
name: "rar-cat-agent-skills-eu-greenwashing-analysis"
description: "Detect greenwashing in product descriptions, marketing copy, and catalog entries against EU Directive 2024/825 and the Green Claims Directive. Returns a structured per-claim findings report with risk levels, regulation references, and recommended corrections."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/eu_greenwashing_analysis", "rar_sha256": "60f5b0746b2395fef7e8225ba803aeb9de1264b58c9797df97fb0a80123d7a5e", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Remi Dyon", "tags": ["compliance", "sustainability", "greenwashing", "eu_regulation", "marketing_review", "esg"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/eu_greenwashing_analysis`. The original RAPP
agent is preserved byte-for-byte in `eu_greenwashing_analysis_agent.py` and in the RCI capsule.

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
