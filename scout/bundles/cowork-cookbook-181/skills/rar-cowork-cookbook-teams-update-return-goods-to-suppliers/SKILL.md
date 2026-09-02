---
name: "rar-cowork-cookbook-teams-update-return-goods-to-suppliers"
description: "Drafts a Teams channel post on return goods to suppliers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_return_goods_to_suppliers", "rar_sha256": "24bcc3413ba12d659214c300dc4974ed4f757717c4a9af8b71115a8beb1d885f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_return_goods_to_suppliers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-return-goods-to-suppliers:8e5798d29cb302f44a6bb089a157e5c2ba3415101ffd9eb445a6ca8c5a30c3d7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_return_goods_to_suppliers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_return_goods_to_suppliers_agent.py` is
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
