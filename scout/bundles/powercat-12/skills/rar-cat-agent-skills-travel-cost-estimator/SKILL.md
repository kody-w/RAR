---
name: "rar-cat-agent-skills-travel-cost-estimator"
description: "Price a business trip from live fares in your corporate booking tool, benchmark the non-bookable lines against your own approved expense reports, and produce an estimate a manager can approve \u2014 with a hard guardrail that never enters the booking funnel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/travel_cost_estimator", "rar_sha256": "9f4e84c8f1066bcc5bf9698772221e2591e0d94f8b680fc9f47dd4c8320c7da1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Al Macey", "tags": ["travel", "expenses", "browser_automation", "playwright", "finance", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `travel_cost_estimator_agent.py` and embedded as the fenced Python below (sha256 9f4e84c8f1066bcc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `travel_cost_estimator_agent.py` first:

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
    "version": '3.0.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
