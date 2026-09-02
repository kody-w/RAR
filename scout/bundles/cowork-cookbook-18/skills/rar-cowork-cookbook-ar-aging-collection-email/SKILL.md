---
name: "rar-cowork-cookbook-ar-aging-collection-email"
description: "Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ar_aging_collection_email", "rar_sha256": "506d2305f1393dfdd66d0e2f018115060c46d3b932e57fea0c362c3c3c38486f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ar_aging_collection_email_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ar-aging-collection-email:f7e228132244b57946d518317199d2ae860baf1bdbe040ae6afa94bfa78875a2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ar_aging_collection_email`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ar_aging_collection_email_agent.py` is
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

AR Aging Collection Email Draft — Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ar-aging-collection-email
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ar_aging_collection_email_agent.py` and embedded as the fenced Python below (sha256 506d2305f1393dfd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ar_aging_collection_email_agent.py` first:

```bash
python3 ar_aging_collection_email_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ar_aging_collection_email_agent.py   # or on stdin
python3 ar_aging_collection_email_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AR Aging Collection Email Draft — Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ar-aging-collection-email
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ar_aging_collection_email',
    "version": '2.0.0',
    "display_name": 'AR Aging Collection Email Draft',
    "description": 'Drafts polite-but-firm collection emails to customers with overdue invoices, grouped by severity bucket.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ar-aging-collection-email',
        "upstream_url": 'https://coworkcookbook.com/recipes/ar-aging-collection-email',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee17c25e99830559',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ar-aging-collection-email', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ArAgingCollectionEmail(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ArAgingCollectionEmail'
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
    print(ArAgingCollectionEmail().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
