---
name: "rar-cowork-cookbook-audit-develop-loyalty-programs"
description: "Audits develop loyalty programs records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_loyalty_programs", "rar_sha256": "a07416bd75be2043c8ce1204f268c46024f47153b96ef8b48a6b71cb99db48c3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_loyalty_programs`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_loyalty_programs_agent.py` and in the RCI capsule.

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

Develop loyalty programs Completeness Audit — Audits develop loyalty programs records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-loyalty-programs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 a07416bd75be2043…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_loyalty_programs_agent.py` first:

```bash
python3 audit_develop_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_loyalty_programs_agent.py   # or on stdin
python3 audit_develop_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop loyalty programs Completeness Audit — Audits develop loyalty programs records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_loyalty_programs',
    "version": '2.0.1',
    "display_name": 'Develop loyalty programs Completeness Audit',
    "description": 'Audits develop loyalty programs records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e5bdf08f586dda6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-loyalty-programs'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-develop-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDevelopLoyaltyPrograms(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopLoyaltyPrograms'
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
    print(AuditDevelopLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
