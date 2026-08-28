---
name: "rar-cowork-cookbook-audit-terminate-workers"
description: "Audits terminate workers records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_terminate_workers", "rar_sha256": "55fd1247d1d5ad73f763119aa7b2beff7296e992c84e5b9eed84c0883a71840e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_terminate_workers`. The original RAPP
agent is preserved byte-for-byte in `audit_terminate_workers_agent.py` and in the RCI capsule.

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
