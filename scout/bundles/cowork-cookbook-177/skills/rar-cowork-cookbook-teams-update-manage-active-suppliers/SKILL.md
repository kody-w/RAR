---
name: "rar-cowork-cookbook-teams-update-manage-active-suppliers"
description: "Drafts a Teams channel post on manage active suppliers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_active_suppliers", "rar_sha256": "9b3f1dca8d345d03f4e12e4bc3a342410b506127994be3ad5c26800830e9ecd2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_active_suppliers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_active_suppliers_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_active_suppliers_agent.py` and embedded as the fenced Python below (sha256 9b3f1dca8d345d03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_active_suppliers_agent.py` first:

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
    "version": '2.0.1',
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
