---
name: "rar-cat-agent-skills-travel-cost-estimator"
description: "Price a business trip from live fares in your corporate booking tool, benchmark the non-bookable lines against your own approved expense reports, and produce an estimate a manager can approve \u2014 with a hard guardrail that never enters the booking funnel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/travel_cost_estimator", "rar_sha256": "90fc9c773d6b9ea7d45ec20a0c13dde3ab6a6ad370d0c0915fd99ecbac14a9b9", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "travel_cost_estimator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/travel-cost-estimator:853de0c3ccd717f292ec57d70545e4199f13c2b17db7a637bbdde07ceb5e2735", "kind": "skill"}, "version": "2.0.0", "author": "Al Macey", "tags": ["travel", "expenses", "browser_automation", "playwright", "finance", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/travel_cost_estimator`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `travel_cost_estimator_agent.py` is
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

Travel Cost Estimator — Price a business trip from live fares in your corporate booking tool, benchmark the non-bookable lines against your own approved expense reports, and produce an estimate a manager can approve — with a hard guardrail that never enters the booking funnel.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#travel-cost-estimator
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `travel_cost_estimator_agent.py` and embedded as the fenced Python below (sha256 90fc9c773d6b9ea7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `travel_cost_estimator_agent.py` first:

```bash
python3 travel_cost_estimator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 travel_cost_estimator_agent.py   # or on stdin
python3 travel_cost_estimator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Travel Cost Estimator — Price a business trip from live fares in your corporate booking tool, benchmark the non-bookable lines against your own approved expense reports, and produce an estimate a manager can approve — with a hard guardrail that never enters the booking funnel.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#travel-cost-estimator
  Upstream author: Al Macey
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/travel_cost_estimator',
    "version": '2.0.0',
    "display_name": 'Travel Cost Estimator',
    "description": 'Price a business trip from live fares in your corporate booking tool, benchmark the non-bookable lines against your own approved expense reports, and produce an estimate a manager can approve — with a hard guardrail that never enters the booking funnel.',
    "author": 'Al Macey',
    "tags": ['travel', 'expenses', 'browser_automation', 'playwright', 'finance', 'productivity'],
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
        "upstream_slug": 'travel-cost-estimator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#travel-cost-estimator',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'dc0f5e9e0e0f3842',
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class TravelCostEstimator(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TravelCostEstimator'
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
    print(TravelCostEstimator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
