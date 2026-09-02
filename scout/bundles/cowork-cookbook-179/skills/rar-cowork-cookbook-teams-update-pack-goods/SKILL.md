---
name: "rar-cowork-cookbook-teams-update-pack-goods"
description: "Drafts a Teams channel post on pack goods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_pack_goods", "rar_sha256": "b0a6540490f16ded7d7ea1b628bbca42b6eca77ca0408489b2dfecb152452ca1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_pack_goods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-pack-goods:25a6473b417bda746a50dee22e9dc68774082595878c87ac93101f35c6b0bd79", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_pack_goods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_pack_goods_agent.py` is
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

Pack goods Teams Channel Update — Drafts a Teams channel post on pack goods status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pack-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_pack_goods_agent.py` and embedded as the fenced Python below (sha256 b0a6540490f16ded…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_pack_goods_agent.py` first:

```bash
python3 teams_update_pack_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_pack_goods_agent.py   # or on stdin
python3 teams_update_pack_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pack goods Teams Channel Update — Drafts a Teams channel post on pack goods status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-pack-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_pack_goods',
    "version": '2.0.0',
    "display_name": 'Pack goods Teams Channel Update',
    "description": 'Drafts a Teams channel post on pack goods status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-pack-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-pack-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c774ef10fe5a05d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/pack-goods'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-pack-goods', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdatePackGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePackGoods'
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
    print(TeamsUpdatePackGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
