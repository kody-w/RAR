---
name: "rar-cowork-cookbook-teams-update-manage-sales-channels"
description: "Drafts a Teams channel post on manage sales channels status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_sales_channels", "rar_sha256": "8548356aff7f5275bb4c5d7ec66d5423de9b5091f6bd5fd467882907a87bddb2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_manage_sales_channels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-manage-sales-channels:19111a31b45c5b2eb59b3f8f4c6c76d33bf7ce49195d82ce9785501731757ef5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_manage_sales_channels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_manage_sales_channels_agent.py` is
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

Manage sales channels Teams Channel Update — Drafts a Teams channel post on manage sales channels status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-sales-channels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_sales_channels_agent.py` and embedded as the fenced Python below (sha256 8548356aff7f5275…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_sales_channels_agent.py` first:

```bash
python3 teams_update_manage_sales_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_sales_channels_agent.py   # or on stdin
python3 teams_update_manage_sales_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales channels Teams Channel Update — Drafts a Teams channel post on manage sales channels status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-sales-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_sales_channels',
    "version": '2.0.0',
    "display_name": 'Manage sales channels Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage sales channels status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-manage-sales-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-sales-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '768a0a8cd939b056',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/manage-sales-channels'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-manage-sales-channels', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateManageSalesChannels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageSalesChannels'
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
    print(TeamsUpdateManageSalesChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
