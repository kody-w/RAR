---
name: "rar-cowork-cookbook-audit-track-project-time"
description: "Audits track project time records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_track_project_time", "rar_sha256": "0ecd4d5d23b199f770f6237f654e79fe9a920a2ccc1ad9f57a7ddbb55eb1e9f4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_track_project_time`. The original RAPP
agent is preserved byte-for-byte in `audit_track_project_time_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_track_project_time_agent.py` and embedded as the fenced Python below (sha256 0ecd4d5d23b199f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_track_project_time_agent.py` first:

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
    "version": '2.0.1',
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
