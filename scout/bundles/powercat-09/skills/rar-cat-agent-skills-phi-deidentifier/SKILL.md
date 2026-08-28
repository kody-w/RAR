---
name: "rar-cat-agent-skills-phi-deidentifier"
description: "Redact the 18 HIPAA Safe Harbor identifiers from clinical text (or produce a Limited Data Set) with consistent pseudonym tokens and an audit manifest of what was removed."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/phi_deidentifier", "rar_sha256": "deacbb22ef7601fa437aa51aa7ccdd07ed16fa8c3eaa345c50ff44dc6d975d6f", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Rafael Lopez Alcaraz", "tags": ["healthcare", "hls", "phi", "privacy", "redaction", "hipaa", "compliance", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/phi_deidentifier`. The original RAPP
agent is preserved byte-for-byte in `phi_deidentifier_agent.py` and in the RCI capsule.

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
