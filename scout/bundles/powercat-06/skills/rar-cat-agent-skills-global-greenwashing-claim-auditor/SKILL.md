---
name: "rar-cat-agent-skills-global-greenwashing-claim-auditor"
description: "Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/global_greenwashing_claim_auditor", "rar_sha256": "3899d6d4b21a00ce391389c46b6172786c9e8e3023f60b715765165d5343d9fe", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Chris Garty", "tags": ["greenwashing", "environmental_claims", "sustainability", "compliance", "canada", "european_union", "united_kingdom", "documents"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/global_greenwashing_claim_auditor`. The original RAPP
agent is preserved byte-for-byte in `global_greenwashing_claim_auditor_agent.py` and in the RCI capsule.

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

Global Greenwashing Claim Auditor — Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#global-greenwashing-claim-auditor
  Upstream author: Chris Garty
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `global_greenwashing_claim_auditor_agent.py` and embedded as the fenced Python below (sha256 3899d6d4b21a00ce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `global_greenwashing_claim_auditor_agent.py` first:

```bash
python3 global_greenwashing_claim_auditor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 global_greenwashing_claim_auditor_agent.py   # or on stdin
python3 global_greenwashing_claim_auditor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Global Greenwashing Claim Auditor — Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#global-greenwashing-claim-auditor
  Upstream author: Chris Garty
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/global_greenwashing_claim_auditor',
    "version": '2.0.0',
    "display_name": 'Global Greenwashing Claim Auditor',
    "description": 'Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings.',
    "author": 'Chris Garty',
    "tags": ['greenwashing', 'environmental_claims', 'sustainability', 'compliance', 'canada', 'european_union', 'united_kingdom', 'documents'],
    "category": 'productivity',
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
        "upstream_slug": 'global-greenwashing-claim-auditor',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#global-greenwashing-claim-auditor',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4eb5e370798c4538',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.6, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:compliance', 'word:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class GlobalGreenwashingClaimAuditor(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GlobalGreenwashingClaimAuditor'
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
    print(GlobalGreenwashingClaimAuditor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
