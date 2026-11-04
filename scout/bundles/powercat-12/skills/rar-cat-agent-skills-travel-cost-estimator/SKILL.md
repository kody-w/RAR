---
name: "rar-cat-agent-skills-travel-cost-estimator"
description: "Price a business trip from live fares in your corporate booking tool, benchmark the non-bookable lines against your own approved expense reports, and produce an estimate a manager can approve \u2014 with a hard guardrail that never enters the booking funnel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/travel_cost_estimator", "rar_sha256": "183b5866237d0c907e5fea7feb4e9813add71493a2cf7499a273dbcd08e9989a", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Al Macey", "tags": ["travel", "expenses", "browser_automation", "playwright", "finance", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `travel_cost_estimator_agent.py` and embedded as the fenced Python below (sha256 183b5866237d0c90…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `travel_cost_estimator_agent.py` first:

```bash
python3 travel_cost_estimator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 travel_cost_estimator_agent.py   # or on stdin
python3 travel_cost_estimator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/travel_cost_estimator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/travel_cost_estimator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/travel_cost_estimator/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
