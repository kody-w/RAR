---
name: "rar-cowork-cookbook-teams-update-pack-goods"
description: "Drafts a Teams channel post on pack goods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_pack_goods", "rar_sha256": "b0a6540490f16ded7d7ea1b628bbca42b6eca77ca0408489b2dfecb152452ca1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_pack_goods`. The original RAPP
agent is preserved byte-for-byte in `teams_update_pack_goods_agent.py` and in the RCI capsule.

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
