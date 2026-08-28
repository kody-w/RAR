---
name: "rar-cowork-cookbook-audit-develop-loyalty-programs"
description: "Audits develop loyalty programs records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_loyalty_programs", "rar_sha256": "ee0591a3b080ea51744e7eaa27e2f99404ee87ebea596ac69e050148c3b41f3d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 ee0591a3b080ea51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_loyalty_programs_agent.py` first:

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
    "version": '2.0.0',
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
