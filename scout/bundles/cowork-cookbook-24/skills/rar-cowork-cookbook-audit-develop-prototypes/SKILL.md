---
name: "rar-cowork-cookbook-audit-develop-prototypes"
description: "Audits develop prototypes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_prototypes", "rar_sha256": "5ca1770020ff237acdc1fcc1339c66c976f713571c144a4e3be263f72c449346", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_prototypes`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_prototypes_agent.py` and in the RCI capsule.

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

Develop prototypes Completeness Audit — Audits develop prototypes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-prototypes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_prototypes_agent.py` and embedded as the fenced Python below (sha256 5ca1770020ff237a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_prototypes_agent.py` first:

```bash
python3 audit_develop_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_prototypes_agent.py   # or on stdin
python3 audit_develop_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop prototypes Completeness Audit — Audits develop prototypes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_prototypes',
    "version": '2.0.1',
    "display_name": 'Develop prototypes Completeness Audit',
    "description": 'Audits develop prototypes records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-develop-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b73750aba529c39',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/develop-prototypes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-develop-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopPrototypes(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopPrototypes'
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
    print(AuditDevelopPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
