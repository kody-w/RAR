---
name: "rar-cowork-cookbook-audit-negotiate-and-finalize-quotations"
description: "Audits negotiate and finalize quotations records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_negotiate_and_finalize_quotations", "rar_sha256": "e053e88e67016e8c17a7fc5a9de243b9e46cf82257bd80ad0412d885a33a7b7f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_negotiate_and_finalize_quotations_agent.py` and embedded as the fenced Python below (sha256 e053e88e67016e8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_negotiate_and_finalize_quotations_agent.py` first:

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
    "version": '2.0.0',
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
