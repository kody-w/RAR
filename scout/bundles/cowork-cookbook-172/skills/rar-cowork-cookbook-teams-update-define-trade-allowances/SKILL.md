---
name: "rar-cowork-cookbook-teams-update-define-trade-allowances"
description: "Drafts a Teams channel post on define trade allowances status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_trade_allowances", "rar_sha256": "a0e11e927c6f28a8fbac316aa53cbcfaeb85f5d3ed8675b9604814132f055466", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_trade_allowances_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-trade-allowances:5e5cf59480d85deee3fbe2cc556cebb72cee6190bbf514083d6fa15fca9e0485", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_trade_allowances`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_trade_allowances_agent.py` is
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
