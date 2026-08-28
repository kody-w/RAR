---
name: "rar-cowork-cookbook-audit-handle-background-job-errors-and-exceptions"
description: "Audits handle background job errors and exceptions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_handle_background_job_errors_and_exceptions", "rar_sha256": "fad47661b487978a231c7ef9baddd321a0007bc8be3fc4932a551c30cc3c3df7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_handle_background_job_errors_and_exceptions_agent.py` and embedded as the fenced Python below (sha256 fad47661b487978a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_handle_background_job_errors_and_exceptions_agent.py` first:

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
    "version": '2.0.0',
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
