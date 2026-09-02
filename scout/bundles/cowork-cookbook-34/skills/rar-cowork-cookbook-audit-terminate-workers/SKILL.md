---
name: "rar-cowork-cookbook-audit-terminate-workers"
description: "Audits terminate workers records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_terminate_workers", "rar_sha256": "55fd1247d1d5ad73f763119aa7b2beff7296e992c84e5b9eed84c0883a71840e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_terminate_workers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-terminate-workers:96f22fd321f6611de93903120546caebf5d6914a9048ec84549b054f11a0b7e1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_terminate_workers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_terminate_workers_agent.py` is
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

Terminate workers Completeness Audit — Audits terminate workers records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-terminate-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_terminate_workers_agent.py` and embedded as the fenced Python below (sha256 55fd1247d1d5ad73…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_terminate_workers_agent.py` first:

```bash
python3 audit_terminate_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_terminate_workers_agent.py   # or on stdin
python3 audit_terminate_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Terminate workers Completeness Audit — Audits terminate workers records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-terminate-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_terminate_workers',
    "version": '2.0.0',
    "display_name": 'Terminate workers Completeness Audit',
    "description": 'Audits terminate workers records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-terminate-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-terminate-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd71815ebff73ed24',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/terminate-workers'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-terminate-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditTerminateWorkers(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTerminateWorkers'
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
    print(AuditTerminateWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
