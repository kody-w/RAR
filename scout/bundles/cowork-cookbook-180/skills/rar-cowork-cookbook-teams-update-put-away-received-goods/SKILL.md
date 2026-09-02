---
name: "rar-cowork-cookbook-teams-update-put-away-received-goods"
description: "Drafts a Teams channel post on put away received goods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_put_away_received_goods", "rar_sha256": "d17deb55c876439c6c8512468239c7319dc9d202f714462755155b6f42fcf95e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_put_away_received_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-put-away-received-goods:1ebfa60f9b7f1424f94b75361e85a8fe7384d5b2894b4dc5e3c0ac20399ee017", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_put_away_received_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_put_away_received_goods_agent.py` is
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

Put away received goods Teams Channel Update — Drafts a Teams channel post on put away received goods status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-put-away-received-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_put_away_received_goods_agent.py` and embedded as the fenced Python below (sha256 d17deb55c876439c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_put_away_received_goods_agent.py` first:

```bash
python3 teams_update_put_away_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_put_away_received_goods_agent.py   # or on stdin
python3 teams_update_put_away_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Put away received goods Teams Channel Update — Drafts a Teams channel post on put away received goods status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-put-away-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_put_away_received_goods',
    "version": '2.0.0',
    "display_name": 'Put away received goods Teams Channel Update',
    "description": 'Drafts a Teams channel post on put away received goods status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-put-away-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-put-away-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '70a3f728f871a210',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/put-away-received-goods'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-put-away-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdatePutAwayReceivedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePutAwayReceivedGoods'
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
    print(TeamsUpdatePutAwayReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
