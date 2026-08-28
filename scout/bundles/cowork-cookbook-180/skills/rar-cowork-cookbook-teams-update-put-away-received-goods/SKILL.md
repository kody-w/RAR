---
name: "rar-cowork-cookbook-teams-update-put-away-received-goods"
description: "Drafts a Teams channel post on put away received goods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_put_away_received_goods", "rar_sha256": "d17deb55c876439c6c8512468239c7319dc9d202f714462755155b6f42fcf95e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_put_away_received_goods`. The original RAPP
agent is preserved byte-for-byte in `teams_update_put_away_received_goods_agent.py` and in the RCI capsule.

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
