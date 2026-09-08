---
name: "rar-cat-agent-skills-global-greenwashing-claim-auditor"
description: "Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/global_greenwashing_claim_auditor", "rar_sha256": "37db76bce7c6b135cba2ed0f19ec2c7c15eae8f60f3cb4868d2325f5cff883e5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Chris Garty", "tags": ["greenwashing", "environmental_claims", "sustainability", "compliance", "canada", "european_union", "united_kingdom", "documents"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/global_greenwashing_claim_auditor`. The original RAPP
agent is preserved byte-for-byte in `global_greenwashing_claim_auditor_agent.py` and in the RCI capsule.

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

Global Greenwashing Claim Auditor — Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#global-greenwashing-claim-auditor
  Upstream author: Chris Garty
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `global_greenwashing_claim_auditor_agent.py` and embedded as the fenced Python below (sha256 37db76bce7c6b135…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `global_greenwashing_claim_auditor_agent.py` first:

```bash
python3 global_greenwashing_claim_auditor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 global_greenwashing_claim_auditor_agent.py   # or on stdin
python3 global_greenwashing_claim_auditor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Global Greenwashing Claim Auditor — Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#global-greenwashing-claim-auditor
  Upstream author: Chris Garty
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/global_greenwashing_claim_auditor',
    "version": '3.0.2',
    "display_name": 'Global Greenwashing Claim Auditor',
    "description": 'Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings.',
    "author": 'Chris Garty',
    "tags": ['greenwashing', 'environmental_claims', 'sustainability', 'compliance', 'canada', 'european_union', 'united_kingdom', 'documents'],
    "category": 'productivity',
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
        "upstream_slug": 'global-greenwashing-claim-auditor',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#global-greenwashing-claim-auditor',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4eb5e370798c4538',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.6, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:compliance', 'word:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class GlobalGreenwashingClaimAuditor(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GlobalGreenwashingClaimAuditor'
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
    print(GlobalGreenwashingClaimAuditor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
