---
name: "rar-cat-agent-skills-global-greenwashing-claim-auditor"
description: "Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/global_greenwashing_claim_auditor", "rar_sha256": "37db76bce7c6b135cba2ed0f19ec2c7c15eae8f60f3cb4868d2325f5cff883e5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Chris Garty", "tags": ["greenwashing", "environmental_claims", "sustainability", "compliance", "canada", "european_union", "united_kingdom", "documents"]}
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
