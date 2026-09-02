---
name: "rar-cat-agent-skills-phi-deidentifier"
description: "Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/phi_deidentifier", "rar_sha256": "deacbb22ef7601fa437aa51aa7ccdd07ed16fa8c3eaa345c50ff44dc6d975d6f", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "phi_deidentifier_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/phi-deidentifier:cae905e7f09c5d7f2eacb4890d1334c69fe2424fd947b5c9bbcc5eb574c184aa", "kind": "skill"}, "version": "2.0.0", "author": "Rafael Lopez Alcaraz", "tags": ["healthcare", "hls", "phi", "privacy", "redaction", "hipaa", "compliance", "scripts"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/phi_deidentifier`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `phi_deidentifier_agent.py` is
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

PHI De-identifier — Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#phi-deidentifier
  Upstream author: Rafael Lopez Alcaraz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `phi_deidentifier_agent.py` and embedded as the fenced Python below (sha256 deacbb22ef7601fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `phi_deidentifier_agent.py` first:

```bash
python3 phi_deidentifier_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 phi_deidentifier_agent.py   # or on stdin
python3 phi_deidentifier_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
PHI De-identifier — Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#phi-deidentifier
  Upstream author: Rafael Lopez Alcaraz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/phi_deidentifier',
    "version": '2.0.0',
    "display_name": 'PHI De-identifier',
    "description": 'Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed.',
    "author": 'Rafael Lopez Alcaraz',
    "tags": ['healthcare', 'hls', 'phi', 'privacy', 'redaction', 'hipaa', 'compliance', 'scripts'],
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
        "upstream_slug": 'phi-deidentifier',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#phi-deidentifier',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4c6bd1961fad5f45',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:compliance', 'word:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PhiDeidentifier(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PhiDeidentifier'
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
    print(PhiDeidentifier().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
