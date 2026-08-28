---
name: "rar-cowork-cookbook-lead-qualification-consistency-check"
description: "Checks whether leads are being qualified and disqualified consistently, and surfaces disqualifications with missing or vague reasons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/lead_qualification_consistency_check", "rar_sha256": "55e84afa7b1ea56b2b27eab723f388fb6ae26a48595ab757f25c3a324c3afb76", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/lead_qualification_consistency_check`. The original RAPP
agent is preserved byte-for-byte in `lead_qualification_consistency_check_agent.py` and in the RCI capsule.

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

Lead Qualification Consistency Check — Checks whether leads are being qualified and disqualified consistently, and surfaces disqualifications with missing or vague reasons.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/lead-qualification-consistency-check
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lead_qualification_consistency_check_agent.py` and embedded as the fenced Python below (sha256 55e84afa7b1ea56b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lead_qualification_consistency_check_agent.py` first:

```bash
python3 lead_qualification_consistency_check_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 lead_qualification_consistency_check_agent.py   # or on stdin
python3 lead_qualification_consistency_check_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lead Qualification Consistency Check — Checks whether leads are being qualified and disqualified consistently, and surfaces disqualifications with missing or vague reasons.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/lead-qualification-consistency-check
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/lead_qualification_consistency_check',
    "version": '2.0.0',
    "display_name": 'Lead Qualification Consistency Check',
    "description": 'Checks whether leads are being qualified and disqualified consistently, and surfaces disqualifications with missing or vague reasons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'lead-qualification-consistency-check',
        "upstream_url": 'https://coworkcookbook.com/recipes/lead-qualification-consistency-check',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e18c74d7ad5bc1c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/qualify-and-disqualify-leads'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/lead-qualification-consistency-check', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:check'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class LeadQualificationConsistencyCheck(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LeadQualificationConsistencyCheck'
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(LeadQualificationConsistencyCheck().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
