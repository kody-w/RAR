---
name: "rar-cowork-cookbook-audit-track-project-time"
description: "Audits track project time records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_track_project_time", "rar_sha256": "0092c0e80e3a93a591435cb13836924a89220eeeb9c54773ac3c1c590bd94a93", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_track_project_time_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-track-project-time:42a8d970f677909ec965f03211966fd15fc3c25774b5cdae879cdf9a9de1abbf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_track_project_time`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_track_project_time_agent.py` is
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

Track project time Completeness Audit — Audits track project time records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-track-project-time
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_track_project_time_agent.py` and embedded as the fenced Python below (sha256 0092c0e80e3a93a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_track_project_time_agent.py` first:

```bash
python3 audit_track_project_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_track_project_time_agent.py   # or on stdin
python3 audit_track_project_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project time Completeness Audit — Audits track project time records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-track-project-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_track_project_time',
    "version": '2.0.0',
    "display_name": 'Track project time Completeness Audit',
    "description": 'Audits track project time records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-track-project-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-track-project-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9d5647f2d833ebdd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-time'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-track-project-time', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditTrackProjectTime(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTrackProjectTime'
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
    print(AuditTrackProjectTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
