---
name: "rar-cowork-cookbook-audit-terminate-workers"
description: "Audits terminate workers records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_terminate_workers", "rar_sha256": "23f1b74c3b0cbed3c87406698b340d3bfca9d9da2186bff148da94e7359051cb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_terminate_workers_agent.py` and embedded as the fenced Python below (sha256 23f1b74c3b0cbed3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_terminate_workers_agent.py` first:

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
    "version": '2.0.1',
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
