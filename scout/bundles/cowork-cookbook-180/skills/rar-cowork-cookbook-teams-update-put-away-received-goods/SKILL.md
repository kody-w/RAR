---
name: "rar-cowork-cookbook-teams-update-put-away-received-goods"
description: "Drafts a Teams channel post on put away received goods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_put_away_received_goods", "rar_sha256": "fb16396c23dd43ceba72d5fb64d876b26b55e324f5e2fb0aeaccd5e4c4cd6bd4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_put_away_received_goods_agent.py` and embedded as the fenced Python below (sha256 fb16396c23dd43ce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_put_away_received_goods_agent.py` first:

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
    "version": '2.0.1',
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
