---
name: "rar-cowork-cookbook-audit-produce-assets"
description: "Audits produce assets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_produce_assets", "rar_sha256": "31d620124172ffe72e72e6193f374d1ac02b097530cc749d90cfabd065c1d6f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_produce_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-produce-assets:d458f9a2d4ec6811cac0b205a494735e9dbfc0813b4dfe53a23932f0690d6453", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_produce_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_produce_assets_agent.py` is
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

Produce assets Completeness Audit — Audits produce assets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-produce-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_produce_assets_agent.py` and embedded as the fenced Python below (sha256 31d620124172ffe7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_produce_assets_agent.py` first:

```bash
python3 audit_produce_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_produce_assets_agent.py   # or on stdin
python3 audit_produce_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Produce assets Completeness Audit — Audits produce assets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-produce-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_produce_assets',
    "version": '2.0.0',
    "display_name": 'Produce assets Completeness Audit',
    "description": 'Audits produce assets records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-produce-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-produce-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c67e75c7e751805e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/produce-assets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-produce-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditProduceAssets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProduceAssets'
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
    print(AuditProduceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
