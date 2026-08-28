---
name: "rar-cowork-cookbook-teams-update-return-goods-to-suppliers"
description: "Drafts a Teams channel post on return goods to suppliers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_return_goods_to_suppliers", "rar_sha256": "24bcc3413ba12d659214c300dc4974ed4f757717c4a9af8b71115a8beb1d885f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_return_goods_to_suppliers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_return_goods_to_suppliers_agent.py` and in the RCI capsule.

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

Return goods to suppliers Teams Channel Update — Drafts a Teams channel post on return goods to suppliers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-return-goods-to-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_return_goods_to_suppliers_agent.py` and embedded as the fenced Python below (sha256 24bcc3413ba12d65…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_return_goods_to_suppliers_agent.py` first:

```bash
python3 teams_update_return_goods_to_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_return_goods_to_suppliers_agent.py   # or on stdin
python3 teams_update_return_goods_to_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to suppliers Teams Channel Update — Drafts a Teams channel post on return goods to suppliers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-return-goods-to-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_return_goods_to_suppliers',
    "version": '2.0.0',
    "display_name": 'Return goods to suppliers Teams Channel Update',
    "description": 'Drafts a Teams channel post on return goods to suppliers status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-return-goods-to-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-return-goods-to-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8fc853d383a5bbf1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/return-goods-to-suppliers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-return-goods-to-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateReturnGoodsToSuppliers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReturnGoodsToSuppliers'
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
    print(TeamsUpdateReturnGoodsToSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
