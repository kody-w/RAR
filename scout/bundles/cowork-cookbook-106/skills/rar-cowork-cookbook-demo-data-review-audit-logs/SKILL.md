---
name: "rar-cowork-cookbook-demo-data-review-audit-logs"
description: "Generates and creates realistic demo records for review audit logs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_review_audit_logs", "rar_sha256": "82dcc202bb7632e19189ca273e91aa14a2bb576efe793efa33c474594a85cbc7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_review_audit_logs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_review_audit_logs_agent.py` and in the RCI capsule.

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
