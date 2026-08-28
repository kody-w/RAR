---
name: "rar-cowork-cookbook-audit-define-extensions-approach"
description: "Audits define extensions approach records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_extensions_approach", "rar_sha256": "56f4e2845aedd5e9e1919e3003d934194835b06350124ec4e733674ccb2a0446", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_extensions_approach_agent.py` and embedded as the fenced Python below (sha256 56f4e2845aedd5e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_extensions_approach_agent.py` first:

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
    "version": '2.0.0',
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
