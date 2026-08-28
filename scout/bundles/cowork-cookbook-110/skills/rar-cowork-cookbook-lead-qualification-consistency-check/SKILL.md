---
name: "rar-cowork-cookbook-lead-qualification-consistency-check"
description: "Checks whether leads are being qualified and disqualified consistently, and surfaces disqualifications with missing or vague reasons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/lead_qualification_consistency_check", "rar_sha256": "f21fdee6fc456905f690645b4d45eabfb188dfd0fb027a17421c0d30e4c75240", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `lead_qualification_consistency_check_agent.py` and embedded as the fenced Python below (sha256 f21fdee6fc456905…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `lead_qualification_consistency_check_agent.py` first:

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
    "version": '2.0.1',
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
