---
name: "rar-cowork-cookbook-teams-update-define-trade-allowances"
description: "Drafts a Teams channel post on define trade allowances status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_trade_allowances", "rar_sha256": "fafd1f160758a57ecc900e0fa58c4d9f8e9c8a13813fe02b9db7fcc8ee076e65", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_trade_allowances`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_trade_allowances_agent.py` and in the RCI capsule.

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

Define trade allowances Teams Channel Update — Drafts a Teams channel post on define trade allowances status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-trade-allowances
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 fafd1f160758a57e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_trade_allowances_agent.py` first:

```bash
python3 teams_update_define_trade_allowances_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_trade_allowances_agent.py   # or on stdin
python3 teams_update_define_trade_allowances_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define trade allowances Teams Channel Update — Drafts a Teams channel post on define trade allowances status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-trade-allowances
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_trade_allowances',
    "version": '2.0.1',
    "display_name": 'Define trade allowances Teams Channel Update',
    "description": 'Drafts a Teams channel post on define trade allowances status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-trade-allowances',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-trade-allowances',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f133654af24a0a30',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-trade-allowances'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-define-trade-allowances', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDefineTradeAllowances(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineTradeAllowances'
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
    print(TeamsUpdateDefineTradeAllowances().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
