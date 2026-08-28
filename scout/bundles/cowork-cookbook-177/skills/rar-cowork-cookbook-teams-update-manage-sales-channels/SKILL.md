---
name: "rar-cowork-cookbook-teams-update-manage-sales-channels"
description: "Drafts a Teams channel post on manage sales channels status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_sales_channels", "rar_sha256": "8ba11d79bef5fbd66177149d67c5a6a9510d83265a14832703cde85e878b4d0f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_sales_channels_agent.py` and embedded as the fenced Python below (sha256 8ba11d79bef5fbd6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_sales_channels_agent.py` first:

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
    "version": '2.0.1',
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
