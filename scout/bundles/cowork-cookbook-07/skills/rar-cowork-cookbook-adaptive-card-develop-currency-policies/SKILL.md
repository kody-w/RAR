---
name: "rar-cowork-cookbook-adaptive-card-develop-currency-policies"
description: "Produces a reusable Adaptive Card JSON snapshot of develop currency policies status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_currency_policies", "rar_sha256": "cc6e5863a0f3dc30efd16d22284725224d619ee07ef3419aac73f7f74f172a97", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_currency_policies`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_currency_policies_agent.py` and in the RCI capsule.

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

Develop currency policies Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop currency policies status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-currency-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_currency_policies_agent.py` and embedded as the fenced Python below (sha256 cc6e5863a0f3dc30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_currency_policies_agent.py` first:

```bash
python3 adaptive_card_develop_currency_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_currency_policies_agent.py   # or on stdin
python3 adaptive_card_develop_currency_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop currency policies Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop currency policies status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-currency-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_currency_policies',
    "version": '2.0.1',
    "display_name": 'Develop currency policies Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop currency policies status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-develop-currency-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-currency-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e024caadcec1ebd3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-currency-policies'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-develop-currency-policies', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDevelopCurrencyPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopCurrencyPolicies'
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
    print(AdaptiveCardDevelopCurrencyPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
