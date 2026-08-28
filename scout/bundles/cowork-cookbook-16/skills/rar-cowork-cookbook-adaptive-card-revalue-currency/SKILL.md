---
name: "rar-cowork-cookbook-adaptive-card-revalue-currency"
description: "Produces a reusable Adaptive Card JSON snapshot of revalue currency status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_revalue_currency", "rar_sha256": "3232861e273fab5f290e377562f3a2e61479ae196e22a9ba72f361e2ff367369", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_revalue_currency`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_revalue_currency_agent.py` and in the RCI capsule.

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
