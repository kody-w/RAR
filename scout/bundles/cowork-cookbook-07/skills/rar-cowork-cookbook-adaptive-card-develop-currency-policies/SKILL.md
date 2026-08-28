---
name: "rar-cowork-cookbook-adaptive-card-develop-currency-policies"
description: "Produces a reusable Adaptive Card JSON snapshot of develop currency policies status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_currency_policies", "rar_sha256": "6f33b443888d0f2eafe0a68f2f20135b2e6057eaa0c0ac136392648a0c7e861a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_currency_policies_agent.py` and embedded as the fenced Python below (sha256 6f33b443888d0f2e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_currency_policies_agent.py` first:

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
    "version": '2.0.0',
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
