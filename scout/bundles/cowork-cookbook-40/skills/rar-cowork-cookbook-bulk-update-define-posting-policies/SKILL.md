---
name: "rar-cowork-cookbook-bulk-update-define-posting-policies"
description: "Applies a bulk field update across define posting policies records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_posting_policies", "rar_sha256": "a05dbb29058efb5c331ff8f60a13171924b15a69867b5e2129cf36cab6b071fc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_posting_policies`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_posting_policies_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_posting_policies_agent.py` and embedded as the fenced Python below (sha256 a05dbb29058efb5c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_posting_policies_agent.py` first:

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
    "version": '2.0.1',
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
