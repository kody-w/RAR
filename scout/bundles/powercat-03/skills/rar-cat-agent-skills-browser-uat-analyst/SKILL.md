---
name: "rar-cat-agent-skills-browser-uat-analyst"
description: "Run evidence-driven UAT on any browser-based app \u2014 Copilot Studio, Power Platform, Dataverse, Dynamics 365, admin centres, or a custom web app \u2014 with Playwright execution, a screenshot evidence ledger, and failure classification that separates product defects from tenant config."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/browser_uat_analyst", "rar_sha256": "7510a8a0f67113bdb0bafd437d5471c7c655e0420db4c4bcd2672e3678e6f387", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.0.0", "author": "Al Macey", "tags": ["testing", "uat", "playwright", "quality", "copilot_studio", "power_platform", "automation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/browser_uat_analyst`. The original RAPP
agent is preserved byte-for-byte in `browser_uat_analyst_agent.py` and in the RCI capsule.

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
