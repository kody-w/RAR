---
name: "rar-cat-agent-skills-global-greenwashing-claim-auditor"
description: "Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/global_greenwashing_claim_auditor", "rar_sha256": "7e0ac1c1c0852d3418f1bf9f90892ca2f4598397294b05a12aa62e7d541ed7b3", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Chris Garty", "tags": ["greenwashing", "environmental_claims", "sustainability", "compliance", "canada", "european_union", "united_kingdom", "documents"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `global_greenwashing_claim_auditor_agent.py` and embedded as the fenced Python below (sha256 7e0ac1c1c0852d34…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `global_greenwashing_claim_auditor_agent.py` first:

```bash
python3 global_greenwashing_claim_auditor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 global_greenwashing_claim_auditor_agent.py   # or on stdin
python3 global_greenwashing_claim_auditor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/global_greenwashing_claim_auditor_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/global_greenwashing_claim_auditor_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/global_greenwashing_claim_auditor/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
