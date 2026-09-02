---
name: "rar-cowork-cookbook-teams-update-manage-active-suppliers"
description: "Drafts a Teams channel post on manage active suppliers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_active_suppliers", "rar_sha256": "9b1937f5f2a16b9d263feafce2e479dabd975d414fa68d6eadef8bfe14342045", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_manage_active_suppliers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-manage-active-suppliers:8e674564d674883a004daee63181a70cd886f5ee4f55c013475431761a11fa6c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_manage_active_suppliers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_manage_active_suppliers_agent.py` is
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

Manage active suppliers Teams Channel Update — Drafts a Teams channel post on manage active suppliers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-active-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_active_suppliers_agent.py` and embedded as the fenced Python below (sha256 9b1937f5f2a16b9d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_active_suppliers_agent.py` first:

```bash
python3 teams_update_manage_active_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_active_suppliers_agent.py   # or on stdin
python3 teams_update_manage_active_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage active suppliers Teams Channel Update — Drafts a Teams channel post on manage active suppliers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-active-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_active_suppliers',
    "version": '2.0.0',
    "display_name": 'Manage active suppliers Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage active suppliers status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-manage-active-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-active-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d0f768df9dfc77e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-active-suppliers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-manage-active-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateManageActiveSuppliers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageActiveSuppliers'
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
    print(TeamsUpdateManageActiveSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
