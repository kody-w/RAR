---
name: "rar-cowork-cookbook-bulk-update-collect-interest"
description: "Applies a bulk field update across collect interest records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_collect_interest", "rar_sha256": "26cbba41597e4e1a906e61408bf3164d8edc6c38dc59ead91723103a5c58ae91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_collect_interest_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-collect-interest:7ddb3148a4b4fa3a7964b2fd52a991fe9e10a6ec8a377bed199f2572d3014dcd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_collect_interest`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_collect_interest_agent.py` is
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

Collect interest Bulk Field Update — Applies a bulk field update across collect interest records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-collect-interest
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_collect_interest_agent.py` and embedded as the fenced Python below (sha256 26cbba41597e4e1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_collect_interest_agent.py` first:

```bash
python3 bulk_update_collect_interest_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_collect_interest_agent.py   # or on stdin
python3 bulk_update_collect_interest_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect interest Bulk Field Update — Applies a bulk field update across collect interest records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-collect-interest
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_collect_interest',
    "version": '2.0.0',
    "display_name": 'Collect interest Bulk Field Update',
    "description": 'Applies a bulk field update across collect interest records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-collect-interest',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-collect-interest',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f440add5373570fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/collect-interest'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-collect-interest', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateCollectInterest(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCollectInterest'
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
    print(BulkUpdateCollectInterest().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
