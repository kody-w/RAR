---
name: "rar-cowork-cookbook-adaptive-card-revalue-currency"
description: "Produces a reusable Adaptive Card JSON snapshot of revalue currency status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_revalue_currency", "rar_sha256": "0c61af0a33cd7195f657be023eb19cfaddc6a096a763fc9d9cde316e9aca7457", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_revalue_currency_agent.py` and embedded as the fenced Python below (sha256 0c61af0a33cd7195…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_revalue_currency_agent.py` first:

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
    "version": '2.0.1',
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
