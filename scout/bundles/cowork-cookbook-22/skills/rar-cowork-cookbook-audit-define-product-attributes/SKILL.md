---
name: "rar-cowork-cookbook-audit-define-product-attributes"
description: "Audits define product attributes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_product_attributes", "rar_sha256": "d69e6a86297e539d5d5fefc99cc4b11aba432e2c106ced12e3a23b07dd89cdfd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_product_attributes_agent.py` and embedded as the fenced Python below (sha256 d69e6a86297e539d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_product_attributes_agent.py` first:

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
    "version": '2.0.0',
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
