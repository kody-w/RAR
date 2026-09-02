---
name: "rar-cowork-cookbook-bulk-update-recognize-revenue"
description: "Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_recognize_revenue", "rar_sha256": "3ab183e591defcb3345ecb611f98a3f46c3ad7950c106fc6610397109eaff98d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_recognize_revenue_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-recognize-revenue:f63dc3cb7931d585d17039cc9adcf65483cb117ad7dc89c3c7a4e4fc3b8cf1be", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_recognize_revenue`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_recognize_revenue_agent.py` is
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

Recognize revenue Bulk Field Update — Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-recognize-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_recognize_revenue_agent.py` and embedded as the fenced Python below (sha256 3ab183e591defcb3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_recognize_revenue_agent.py` first:

```bash
python3 bulk_update_recognize_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_recognize_revenue_agent.py   # or on stdin
python3 bulk_update_recognize_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize revenue Bulk Field Update — Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-recognize-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_recognize_revenue',
    "version": '2.0.0',
    "display_name": 'Recognize revenue Bulk Field Update',
    "description": 'Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-recognize-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-recognize-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a05d801d8a420018',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/recognize-revenue'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-recognize-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRecognizeRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRecognizeRevenue'
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
    print(BulkUpdateRecognizeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
