---
name: "rar-cat-agent-skills-travel-cost-estimator"
description: "Price a business trip from live fares in your corporate booking tool, benchmark the non-bookable lines against your own approved expense reports, and produce an estimate a manager can approve \u2014 with a hard guardrail that never enters the booking funnel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/travel_cost_estimator", "rar_sha256": "9f4e84c8f1066bcc5bf9698772221e2591e0d94f8b680fc9f47dd4c8320c7da1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Al Macey", "tags": ["travel", "expenses", "browser_automation", "playwright", "finance", "productivity"]}
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
