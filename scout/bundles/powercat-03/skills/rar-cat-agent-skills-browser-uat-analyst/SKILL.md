---
name: "rar-cat-agent-skills-browser-uat-analyst"
description: "Run evidence-driven UAT on any browser-based app \u2014 Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app \u2014 with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/browser_uat_analyst", "rar_sha256": "7510a8a0f67113bdb0bafd437d5471c7c655e0420db4c4bcd2672e3678e6f387", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "browser_uat_analyst_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/browser-uat-analyst:e3fa18a06a71b979a57242ffa7c183b94ccfc63239e32c6af8b3534f39941920", "kind": "skill"}, "version": "2.0.0", "author": "Al Macey", "tags": ["testing", "uat", "playwright", "quality", "copilot_studio", "power_platform", "automation"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/browser_uat_analyst`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `browser_uat_analyst_agent.py` is
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

Browser UAT Analyst — Run evidence-driven UAT on any browser-based app — Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app — with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#browser-uat-analyst
  Upstream author: Al Macey
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `browser_uat_analyst_agent.py` and embedded as the fenced Python below (sha256 7510a8a0f67113bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `browser_uat_analyst_agent.py` first:

```bash
python3 browser_uat_analyst_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 browser_uat_analyst_agent.py   # or on stdin
python3 browser_uat_analyst_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Browser UAT Analyst — Run evidence-driven UAT on any browser-based app — Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app — with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#browser-uat-analyst
  Upstream author: Al Macey
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/browser_uat_analyst',
    "version": '2.0.0',
    "display_name": 'Browser UAT Analyst',
    "description": 'Run evidence-driven UAT on any browser-based app — Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app — with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config.',
    "author": 'Al Macey',
    "tags": ['testing', 'uat', 'playwright', 'quality', 'copilot_studio', 'power_platform', 'automation'],
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
        "upstream_slug": 'browser-uat-analyst',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#browser-uat-analyst',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '09f0ebd3b94914ed',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.571, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:quality', 'tag:testing'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class BrowserUatAnalyst(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BrowserUatAnalyst'
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
    print(BrowserUatAnalyst().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
