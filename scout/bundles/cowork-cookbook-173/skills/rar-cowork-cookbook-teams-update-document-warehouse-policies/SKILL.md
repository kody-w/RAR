---
name: "rar-cowork-cookbook-teams-update-document-warehouse-policies"
description: "Drafts a Teams channel post on document warehouse policies status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_document_warehouse_policies", "rar_sha256": "07573bd361a319050dc7703708d7467e3c1625ee0ea59aa065ff0a37547bbdc3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_document_warehouse_policies`. The original RAPP
agent is preserved byte-for-byte in `teams_update_document_warehouse_policies_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_document_warehouse_policies_agent.py` and embedded as the fenced Python below (sha256 07573bd361a31905…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_document_warehouse_policies_agent.py` first:

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
    "version": '2.0.1',
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
