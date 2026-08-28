---
name: "rar-cowork-cookbook-audit-update-worker-information"
description: "Audits update worker information records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_update_worker_information", "rar_sha256": "84551f1866630092496b3ab51c6872316ddc2561553eb2eb7e0a2c46c6edc1d7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
