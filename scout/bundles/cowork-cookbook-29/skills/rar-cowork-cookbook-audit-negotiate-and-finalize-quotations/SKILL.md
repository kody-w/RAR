---
name: "rar-cowork-cookbook-audit-negotiate-and-finalize-quotations"
description: "Audits negotiate and finalize quotations records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_negotiate_and_finalize_quotations", "rar_sha256": "3fc7089959a5e52652c64e841df15ba6bf4127a51a8375181d7148957d15a4b0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_negotiate_and_finalize_quotations`. The original RAPP
agent is preserved byte-for-byte in `audit_negotiate_and_finalize_quotations_agent.py` and in the RCI capsule.

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

Negotiate and finalize quotations Completeness Audit — Audits negotiate and finalize quotations records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-negotiate-and-finalize-quotations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_negotiate_and_finalize_quotations_agent.py` and embedded as the fenced Python below (sha256 3fc7089959a5e526…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_negotiate_and_finalize_quotations_agent.py` first:

```bash
python3 audit_negotiate_and_finalize_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_negotiate_and_finalize_quotations_agent.py   # or on stdin
python3 audit_negotiate_and_finalize_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Negotiate and finalize quotations Completeness Audit — Audits negotiate and finalize quotations records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-negotiate-and-finalize-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_negotiate_and_finalize_quotations',
    "version": '2.0.1',
    "display_name": 'Negotiate and finalize quotations Completeness Audit',
    "description": 'Audits negotiate and finalize quotations records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-negotiate-and-finalize-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-negotiate-and-finalize-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '98a0da8dd8ea1a49',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/negotiate-and-finalize-quotations'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-negotiate-and-finalize-quotations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditNegotiateAndFinalizeQuotations(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditNegotiateAndFinalizeQuotations'
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
    print(AuditNegotiateAndFinalizeQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
