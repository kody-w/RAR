---
name: "rar-cowork-cookbook-adaptive-card-revalue-currency"
description: "Produces a reusable Adaptive Card JSON snapshot of revalue currency status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_revalue_currency", "rar_sha256": "3232861e273fab5f290e377562f3a2e61479ae196e22a9ba72f361e2ff367369", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_revalue_currency_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-revalue-currency:5879e593e5216be25b5cd7a08268865a71def2d168659ed21f94262a7cf5fec3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_revalue_currency`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_revalue_currency_agent.py` is
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

Revalue currency Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of revalue currency status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-currency
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_revalue_currency_agent.py` and embedded as the fenced Python below (sha256 3232861e273fab5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_revalue_currency_agent.py` first:

```bash
python3 adaptive_card_revalue_currency_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_revalue_currency_agent.py   # or on stdin
python3 adaptive_card_revalue_currency_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue currency Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of revalue currency status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-revalue-currency
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_revalue_currency',
    "version": '2.0.0',
    "display_name": 'Revalue currency Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of revalue currency status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-revalue-currency',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-revalue-currency',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5e17f0ba08f5d0b2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/revalue-currency'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-revalue-currency', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardRevalueCurrency(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRevalueCurrency'
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
    print(AdaptiveCardRevalueCurrency().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
