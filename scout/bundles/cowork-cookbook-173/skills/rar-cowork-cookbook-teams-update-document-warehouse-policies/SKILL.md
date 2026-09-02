---
name: "rar-cowork-cookbook-teams-update-document-warehouse-policies"
description: "Drafts a Teams channel post on document warehouse policies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_document_warehouse_policies", "rar_sha256": "0a3afefe6ed23305d6e25cb7258f409bd6224fc8a41d0e62d611f928fce4001a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_document_warehouse_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-document-warehouse-policies:50b622df69d27bbf20c4eac2e8f42ee04a8c4ecfe7f35d41cb0f5377244869a5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_document_warehouse_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_document_warehouse_policies_agent.py` is
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

Document warehouse policies Teams Channel Update — Drafts a Teams channel post on document warehouse policies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-document-warehouse-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_document_warehouse_policies_agent.py` and embedded as the fenced Python below (sha256 0a3afefe6ed23305…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_document_warehouse_policies_agent.py` first:

```bash
python3 teams_update_document_warehouse_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_document_warehouse_policies_agent.py   # or on stdin
python3 teams_update_document_warehouse_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Document warehouse policies Teams Channel Update — Drafts a Teams channel post on document warehouse policies status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-document-warehouse-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_document_warehouse_policies',
    "version": '2.0.0',
    "display_name": 'Document warehouse policies Teams Channel Update',
    "description": 'Drafts a Teams channel post on document warehouse policies status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-document-warehouse-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-document-warehouse-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1df7d79fc9e42459',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/document-warehouse-policies'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-document-warehouse-policies', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDocumentWarehousePolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDocumentWarehousePolicies'
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
    print(TeamsUpdateDocumentWarehousePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
