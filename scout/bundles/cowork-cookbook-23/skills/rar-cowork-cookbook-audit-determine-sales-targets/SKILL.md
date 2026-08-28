---
name: "rar-cowork-cookbook-audit-determine-sales-targets"
description: "Audits determine sales targets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_determine_sales_targets", "rar_sha256": "17f88e729adb092ce193a45729f6f7d141570370b2b79c05efccb7be3a23c7d9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_determine_sales_targets`. The original RAPP
agent is preserved byte-for-byte in `audit_determine_sales_targets_agent.py` and in the RCI capsule.

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

Determine sales targets Completeness Audit — Audits determine sales targets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-determine-sales-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_determine_sales_targets_agent.py` and embedded as the fenced Python below (sha256 17f88e729adb092c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_determine_sales_targets_agent.py` first:

```bash
python3 audit_determine_sales_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_determine_sales_targets_agent.py   # or on stdin
python3 audit_determine_sales_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine sales targets Completeness Audit — Audits determine sales targets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-determine-sales-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_determine_sales_targets',
    "version": '2.0.0',
    "display_name": 'Determine sales targets Completeness Audit',
    "description": 'Audits determine sales targets records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-determine-sales-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-determine-sales-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4437a045ed395fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/determine-sales-targets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/audit-determine-sales-targets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDetermineSalesTargets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDetermineSalesTargets'
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
    print(AuditDetermineSalesTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
