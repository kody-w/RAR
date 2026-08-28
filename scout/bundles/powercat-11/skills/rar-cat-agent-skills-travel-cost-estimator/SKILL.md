---
name: "rar-cat-agent-skills-travel-cost-estimator"
description: "Price a business trip from live fares in your corporate booking tool, benchmark the non-bookable lines against your own approved expense reports, and produce an estimate a manager can approve \u2014 with a hard guardrail that never enters the booking funnel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/travel_cost_estimator", "rar_sha256": "90fc9c773d6b9ea7d45ec20a0c13dde3ab6a6ad370d0c0915fd99ecbac14a9b9", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "2.0.0", "author": "Al Macey", "tags": ["travel", "expenses", "browser_automation", "playwright", "finance", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/travel_cost_estimator`. The original RAPP
agent is preserved byte-for-byte in `travel_cost_estimator_agent.py` and in the RCI capsule.

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
