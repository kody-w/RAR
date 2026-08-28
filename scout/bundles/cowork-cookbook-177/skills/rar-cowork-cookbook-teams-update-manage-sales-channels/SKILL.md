---
name: "rar-cowork-cookbook-teams-update-manage-sales-channels"
description: "Drafts a Teams channel post on manage sales channels status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_sales_channels", "rar_sha256": "8548356aff7f5275bb4c5d7ec66d5423de9b5091f6bd5fd467882907a87bddb2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_sales_channels`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_sales_channels_agent.py` and in the RCI capsule.

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
