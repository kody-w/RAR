---
name: "rar-cowork-cookbook-audit-update-worker-information"
description: "Audits update worker information records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_update_worker_information", "rar_sha256": "7dfad51f276bf55349079c395dc2e50fd5975ce99127af0bb98bb3774351650f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_update_worker_information`. The original RAPP
agent is preserved byte-for-byte in `audit_update_worker_information_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_update_worker_information_agent.py` and embedded as the fenced Python below (sha256 7dfad51f276bf553…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_update_worker_information_agent.py` first:

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
    "version": '2.0.1',
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
