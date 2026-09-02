---
name: "rar-cat-agent-skills-global-greenwashing-claim-auditor"
description: "Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/global_greenwashing_claim_auditor", "rar_sha256": "3899d6d4b21a00ce391389c46b6172786c9e8e3023f60b715765165d5343d9fe", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "global_greenwashing_claim_auditor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/global-greenwashing-claim-auditor:36979b57d25aa03bb9da14981f080a9fd1f228b4917b4e7f94a302f0d3f323e1", "kind": "skill"}, "version": "2.0.0", "author": "Chris Garty", "tags": ["greenwashing", "environmental_claims", "sustainability", "compliance", "canada", "european_union", "united_kingdom", "documents"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/global_greenwashing_claim_auditor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `global_greenwashing_claim_auditor_agent.py` is
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
