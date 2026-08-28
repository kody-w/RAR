---
name: "rar-cat-agent-skills-enterprise-agent-design-authority"
description: "An enterprise design review framework that helps architects build secure, scalable, governable, and production-ready Microsoft Copilot Studio agents."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/enterprise_agent_design_authority", "rar_sha256": "1b8d67a3b9d2dab18a77b43f93af6285ad595ac5b44c49ff0568605b8a596f6f", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Faride Ilanda", "tags": ["assessment", "review", "architecture", "enterprise", "design_review", "copilot_studio"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/enterprise_agent_design_authority`. The original RAPP
agent is preserved byte-for-byte in `enterprise_agent_design_authority_agent.py` and in the RCI capsule.

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
