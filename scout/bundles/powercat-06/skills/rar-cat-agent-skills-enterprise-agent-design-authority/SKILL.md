---
name: "rar-cat-agent-skills-enterprise-agent-design-authority"
description: "An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/enterprise_agent_design_authority", "rar_sha256": "1b8d67a3b9d2dab18a77b43f93af6285ad595ac5b44c49ff0568605b8a596f6f", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "enterprise_agent_design_authority_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/enterprise-agent-design-authority:281c99f71b215bbc5a28c85ca6f4c5eed5d1489b2d875f76473fe200b9a3319d", "kind": "skill"}, "version": "2.0.0", "author": "Faride Ilanda", "tags": ["assessment", "review", "architecture", "enterprise", "design_review", "copilot_studio"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/enterprise_agent_design_authority`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `enterprise_agent_design_authority_agent.py` is
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

Enterprise Agent Design Authority (EADA) — An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#enterprise-agent-design-authority
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `enterprise_agent_design_authority_agent.py` and embedded as the fenced Python below (sha256 1b8d67a3b9d2dab1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `enterprise_agent_design_authority_agent.py` first:

```bash
python3 enterprise_agent_design_authority_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 enterprise_agent_design_authority_agent.py   # or on stdin
python3 enterprise_agent_design_authority_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enterprise Agent Design Authority (EADA) — An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#enterprise-agent-design-authority
  Upstream author: Faride Ilanda
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/enterprise_agent_design_authority',
    "version": '2.0.0',
    "display_name": 'Enterprise Agent Design Authority (EADA)',
    "description": 'An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents.',
    "author": 'Faride Ilanda',
    "tags": ['assessment', 'review', 'architecture', 'enterprise', 'design_review', 'copilot_studio'],
    "category": 'analysis',
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
        "upstream_slug": 'enterprise-agent-design-authority',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#enterprise-agent-design-authority',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b69cc3ecf5e4507e',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.375, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:review', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class EnterpriseAgentDesignAuthority(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'EnterpriseAgentDesignAuthority'
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
    print(EnterpriseAgentDesignAuthority().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
