---
name: "rar-cowork-cookbook-adaptive-card-define-warehouse-management-kpis"
description: "Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_warehouse_management_kpis", "rar_sha256": "fc3c4822b021a590d9e07ec27f6c19465c8a47bce7b50cc2959c94252363ac37", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_warehouse_management_kpis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-warehouse-management-kpis:6017e9713f84acf671feace4221282f5146e8994c46516d7c2b1d5c7e85591e2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_warehouse_management_kpis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_warehouse_management_kpis_agent.py` is
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

Define warehouse management KPIs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_warehouse_management_kpis_agent.py` and embedded as the fenced Python below (sha256 fc3c4822b021a590…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_warehouse_management_kpis_agent.py` first:

```bash
python3 adaptive_card_define_warehouse_management_kpis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_warehouse_management_kpis_agent.py   # or on stdin
python3 adaptive_card_define_warehouse_management_kpis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse management KPIs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_warehouse_management_kpis',
    "version": '2.0.0',
    "display_name": 'Define warehouse management KPIs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-warehouse-management-kpis',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd8d95805d858ecd7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/define-warehouse-management-kpis'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-define-warehouse-management-kpis', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDefineWarehouseManagementKpis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineWarehouseManagementKpis'
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
    print(AdaptiveCardDefineWarehouseManagementKpis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
