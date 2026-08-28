---
name: "rar-cowork-cookbook-bulk-update-define-banking-policies"
description: "Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_banking_policies", "rar_sha256": "f97bd4e13bf95ca1e4e567a815d33d585de97e35897afa25127c71b991303d38", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_banking_policies`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_banking_policies_agent.py` and in the RCI capsule.

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

Define banking policies Bulk Field Update — Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-banking-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_banking_policies_agent.py` and embedded as the fenced Python below (sha256 f97bd4e13bf95ca1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_banking_policies_agent.py` first:

```bash
python3 bulk_update_define_banking_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_banking_policies_agent.py   # or on stdin
python3 bulk_update_define_banking_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define banking policies Bulk Field Update — Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-banking-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_banking_policies',
    "version": '2.0.0',
    "display_name": 'Define banking policies Bulk Field Update',
    "description": 'Applies a bulk field update across define banking policies records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-banking-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-banking-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6848bd3db14b5448',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-banking-policies'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-define-banking-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineBankingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineBankingPolicies'
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
    print(BulkUpdateDefineBankingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
