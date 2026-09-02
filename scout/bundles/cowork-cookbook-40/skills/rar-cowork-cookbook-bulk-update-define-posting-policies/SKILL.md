---
name: "rar-cowork-cookbook-bulk-update-define-posting-policies"
description: "Applies a bulk field update across define posting policies records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_posting_policies", "rar_sha256": "eb25aa1f15d6fd6e350446947d21d4a6f3b4885c375f5a54441874a823f8320d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_posting_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-posting-policies:29f6f2cdc01488ba38d44912c28b3f044a3e2313352f1ded75f2b3bc8bd2992d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_posting_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_posting_policies_agent.py` is
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

Define posting policies Bulk Field Update — Applies a bulk field update across define posting policies records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-posting-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_posting_policies_agent.py` and embedded as the fenced Python below (sha256 eb25aa1f15d6fd6e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_posting_policies_agent.py` first:

```bash
python3 bulk_update_define_posting_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_posting_policies_agent.py   # or on stdin
python3 bulk_update_define_posting_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define posting policies Bulk Field Update — Applies a bulk field update across define posting policies records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-posting-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_posting_policies',
    "version": '2.0.0',
    "display_name": 'Define posting policies Bulk Field Update',
    "description": 'Applies a bulk field update across define posting policies records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-define-posting-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-posting-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a68cbf2335ff09cc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-posting-policies'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-define-posting-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDefinePostingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefinePostingPolicies'
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
    print(BulkUpdateDefinePostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
