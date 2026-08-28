---
name: "rar-cowork-cookbook-demo-data-review-audit-logs"
description: "Generates and creates realistic demo records for review audit logs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_review_audit_logs", "rar_sha256": "75c0317860d53e6c7622972c42ea141f90df600f0dd1b5ad3cf1489ea4d6cedb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_review_audit_logs_agent.py` and embedded as the fenced Python below (sha256 75c0317860d53e6c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_review_audit_logs_agent.py` first:

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
    "version": '2.0.1',
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
