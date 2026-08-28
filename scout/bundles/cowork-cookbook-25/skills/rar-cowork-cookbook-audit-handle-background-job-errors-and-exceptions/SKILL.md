---
name: "rar-cowork-cookbook-audit-handle-background-job-errors-and-exceptions"
description: "Audits handle background job errors and exceptions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_handle_background_job_errors_and_exceptions", "rar_sha256": "bc605db3e8bd3d37e6e85daddda2c142558b0c009188d172d6cd7b13e4c2ae78", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_handle_background_job_errors_and_exceptions`. The original RAPP
agent is preserved byte-for-byte in `audit_handle_background_job_errors_and_exceptions_agent.py` and in the RCI capsule.

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

Handle background job errors and exceptions Completeness Audit — Audits handle background job errors and exceptions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-handle-background-job-errors-and-exceptions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_handle_background_job_errors_and_exceptions_agent.py` and embedded as the fenced Python below (sha256 bc605db3e8bd3d37…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_handle_background_job_errors_and_exceptions_agent.py` first:

```bash
python3 audit_handle_background_job_errors_and_exceptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_handle_background_job_errors_and_exceptions_agent.py   # or on stdin
python3 audit_handle_background_job_errors_and_exceptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Handle background job errors and exceptions Completeness Audit — Audits handle background job errors and exceptions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-handle-background-job-errors-and-exceptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_handle_background_job_errors_and_exceptions',
    "version": '2.0.1',
    "display_name": 'Handle background job errors and exceptions Completeness Audit',
    "description": 'Audits handle background job errors and exceptions records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-handle-background-job-errors-and-exceptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-handle-background-job-errors-and-exceptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a87b058c0d7a9355',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/handle-background-job-errors-and-exceptions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-handle-background-job-errors-and-exceptions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditHandleBackgroundJobErrorsAndExceptions(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditHandleBackgroundJobErrorsAndExceptions'
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
    print(AuditHandleBackgroundJobErrorsAndExceptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
