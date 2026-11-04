---
name: "rar-cat-agent-skills-travel-cost-estimator"
description: "Price a business trip from live fares in your corporate booking tool, benchmark the non-bookable lines against your own approved expense reports, and produce an estimate a manager can approve \u2014 with a hard guardrail that never enters the booking funnel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/travel_cost_estimator", "rar_sha256": "183b5866237d0c907e5fea7feb4e9813add71493a2cf7499a273dbcd08e9989a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Al Macey", "tags": ["travel", "expenses", "browser_automation", "playwright", "finance", "productivity"]}
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
