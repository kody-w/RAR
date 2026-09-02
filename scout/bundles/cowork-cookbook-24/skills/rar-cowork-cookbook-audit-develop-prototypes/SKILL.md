---
name: "rar-cowork-cookbook-audit-develop-prototypes"
description: "Audits develop prototypes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_prototypes", "rar_sha256": "b99c89b3461557412123261961ed63139352d3d3260bd7e3d2ff98c08b232752", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_develop_prototypes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-develop-prototypes:dd97cca2d218bc9ea1383c792552e88cb2decffac478c1947b9a82243238a290", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_develop_prototypes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_develop_prototypes_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_prototypes_agent.py` and embedded as the fenced Python below (sha256 b99c89b346155741…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_prototypes_agent.py` first:

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
    "version": '2.0.0',
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
