---
name: "rar-cat-agent-skills-vendor-contract-risk-review"
description: "First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vendor_contract_risk_review", "rar_sha256": "5da2d82c01864eb2ad6792ec0fe9535f2dffe88c3229432f661aef0e99efad33", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["contracts", "legal", "procurement", "risk", "vendor_management", "review"]}
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
