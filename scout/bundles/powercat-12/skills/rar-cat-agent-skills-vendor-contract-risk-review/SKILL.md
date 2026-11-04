---
name: "rar-cat-agent-skills-vendor-contract-risk-review"
description: "First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vendor_contract_risk_review", "rar_sha256": "5da2d82c01864eb2ad6792ec0fe9535f2dffe88c3229432f661aef0e99efad33", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["contracts", "legal", "procurement", "risk", "vendor_management", "review"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/vendor_contract_risk_review`. The original RAPP
agent is preserved byte-for-byte in `vendor_contract_risk_review_agent.py` and in the RCI capsule.

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

Vendor Contract Risk Review — First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vendor-contract-risk-review
  Upstream author: Tim Karlsson
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_contract_risk_review_agent.py` and embedded as the fenced Python below (sha256 5da2d82c01864eb2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_contract_risk_review_agent.py` first:

```bash
python3 vendor_contract_risk_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_contract_risk_review_agent.py   # or on stdin
python3 vendor_contract_risk_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/vendor_contract_risk_review_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/vendor_contract_risk_review_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/vendor_contract_risk_review/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Vendor Contract Risk Review — First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vendor-contract-risk-review
  Upstream author: Tim Karlsson
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/vendor_contract_risk_review',
    "version": '3.0.2',
    "display_name": 'Vendor Contract Risk Review',
    "description": 'First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it.',
    "author": 'Tim Karlsson',
    "tags": ['contracts', 'legal', 'procurement', 'risk', 'vendor_management', 'review'],
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
        "upstream_slug": 'vendor-contract-risk-review',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#vendor-contract-risk-review',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b809a298c80e1782',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 1.0, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:review', 'tag:risk', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class VendorContractRiskReview(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorContractRiskReview'
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
    print(VendorContractRiskReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
