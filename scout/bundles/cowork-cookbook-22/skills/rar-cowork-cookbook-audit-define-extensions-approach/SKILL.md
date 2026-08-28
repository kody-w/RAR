---
name: "rar-cowork-cookbook-audit-define-extensions-approach"
description: "Audits define extensions approach records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_extensions_approach", "rar_sha256": "8b57a479ff1832d2bd31aa40b5aed85cac5c2e977fd1840eb69085991792ba89", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_extensions_approach`. The original RAPP
agent is preserved byte-for-byte in `audit_define_extensions_approach_agent.py` and in the RCI capsule.

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

Define extensions approach Completeness Audit — Audits define extensions approach records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-extensions-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_extensions_approach_agent.py` and embedded as the fenced Python below (sha256 8b57a479ff1832d2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_extensions_approach_agent.py` first:

```bash
python3 audit_define_extensions_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_extensions_approach_agent.py   # or on stdin
python3 audit_define_extensions_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define extensions approach Completeness Audit — Audits define extensions approach records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-extensions-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_extensions_approach',
    "version": '2.0.1',
    "display_name": 'Define extensions approach Completeness Audit',
    "description": 'Audits define extensions approach records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-define-extensions-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-extensions-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4321c07165aa90c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-extensions-approach'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-define-extensions-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditDefineExtensionsApproach(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineExtensionsApproach'
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
    print(AuditDefineExtensionsApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
