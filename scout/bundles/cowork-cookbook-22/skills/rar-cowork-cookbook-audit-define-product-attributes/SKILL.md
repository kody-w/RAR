---
name: "rar-cowork-cookbook-audit-define-product-attributes"
description: "Audits define product attributes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_product_attributes", "rar_sha256": "476b971f12fd904a3b7220125569128a79b2604b01e8ca82a42dbae20d50c2a0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_product_attributes`. The original RAPP
agent is preserved byte-for-byte in `audit_define_product_attributes_agent.py` and in the RCI capsule.

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

Define product attributes Completeness Audit — Audits define product attributes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-product-attributes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_product_attributes_agent.py` and embedded as the fenced Python below (sha256 476b971f12fd904a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_product_attributes_agent.py` first:

```bash
python3 audit_define_product_attributes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_product_attributes_agent.py   # or on stdin
python3 audit_define_product_attributes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product attributes Completeness Audit — Audits define product attributes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-product-attributes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_product_attributes',
    "version": '2.0.1',
    "display_name": 'Define product attributes Completeness Audit',
    "description": 'Audits define product attributes records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-product-attributes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-product-attributes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b8856383ba1faef2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-attributes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-define-product-attributes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDefineProductAttributes(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineProductAttributes'
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
    print(AuditDefineProductAttributes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
