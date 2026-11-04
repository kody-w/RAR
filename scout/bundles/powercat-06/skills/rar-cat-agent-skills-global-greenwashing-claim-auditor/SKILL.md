---
name: "rar-cat-agent-skills-global-greenwashing-claim-auditor"
description: "Audit environmental claims in CSV, XLSX, DOCX, PPTX, conversational text, and public websites with separate ANY, CA, EU, and UK findings."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/global_greenwashing_claim_auditor", "rar_sha256": "7e0ac1c1c0852d3418f1bf9f90892ca2f4598397294b05a12aa62e7d541ed7b3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Chris Garty", "tags": ["greenwashing", "environmental_claims", "sustainability", "compliance", "canada", "european_union", "united_kingdom", "documents"]}
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
