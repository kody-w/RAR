---
name: "rar-cowork-cookbook-audit-update-worker-information"
description: "Audits update worker information records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_update_worker_information", "rar_sha256": "84551f1866630092496b3ab51c6872316ddc2561553eb2eb7e0a2c46c6edc1d7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_update_worker_information_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-update-worker-information:cdb99b2216dd60285f7bd2a9bb3e0f085cdb806a9ff8213dfb8faeb3d65235f2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_update_worker_information`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_update_worker_information_agent.py` is
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

Update worker information Completeness Audit — Audits update worker information records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-update-worker-information
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_update_worker_information_agent.py` and embedded as the fenced Python below (sha256 84551f1866630092…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_update_worker_information_agent.py` first:

```bash
python3 audit_update_worker_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_update_worker_information_agent.py   # or on stdin
python3 audit_update_worker_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update worker information Completeness Audit — Audits update worker information records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-update-worker-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_update_worker_information',
    "version": '2.0.0',
    "display_name": 'Update worker information Completeness Audit',
    "description": 'Audits update worker information records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-update-worker-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-update-worker-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '060b4c4f158da6dc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/update-worker-information'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-update-worker-information', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditUpdateWorkerInformation(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditUpdateWorkerInformation'
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
    print(AuditUpdateWorkerInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
