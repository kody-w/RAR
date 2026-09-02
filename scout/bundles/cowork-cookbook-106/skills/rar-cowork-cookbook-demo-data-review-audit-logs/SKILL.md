---
name: "rar-cowork-cookbook-demo-data-review-audit-logs"
description: "Generates and creates realistic demo records for review audit logs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_review_audit_logs", "rar_sha256": "82dcc202bb7632e19189ca273e91aa14a2bb576efe793efa33c474594a85cbc7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_review_audit_logs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-review-audit-logs:028086bb4cf4699f94df38f7ff40d5d0a506f48ff620104e37b649fb23f5f0b4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_review_audit_logs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_review_audit_logs_agent.py` is
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

Review audit logs Demo Data Generator — Generates and creates realistic demo records for review audit logs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-audit-logs
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_review_audit_logs_agent.py` and embedded as the fenced Python below (sha256 82dcc202bb7632e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_review_audit_logs_agent.py` first:

```bash
python3 demo_data_review_audit_logs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_review_audit_logs_agent.py   # or on stdin
python3 demo_data_review_audit_logs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review audit logs Demo Data Generator — Generates and creates realistic demo records for review audit logs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-audit-logs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_review_audit_logs',
    "version": '2.0.0',
    "display_name": 'Review audit logs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for review audit logs in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-review-audit-logs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-review-audit-logs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d4d868ef876cf37',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/review-audit-logs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-review-audit-logs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataReviewAuditLogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReviewAuditLogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(DemoDataReviewAuditLogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
