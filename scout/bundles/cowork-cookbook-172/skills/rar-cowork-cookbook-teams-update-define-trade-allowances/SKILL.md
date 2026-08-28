---
name: "rar-cowork-cookbook-teams-update-define-trade-allowances"
description: "Drafts a Teams channel post on define trade allowances status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_trade_allowances", "rar_sha256": "a0e11e927c6f28a8fbac316aa53cbcfaeb85f5d3ed8675b9604814132f055466", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 a0e11e927c6f28a8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_trade_allowances_agent.py` first:

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
    "version": '2.0.0',
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
