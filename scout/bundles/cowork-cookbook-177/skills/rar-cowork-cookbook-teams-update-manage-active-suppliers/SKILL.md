---
name: "rar-cowork-cookbook-teams-update-manage-active-suppliers"
description: "Drafts a Teams channel post on manage active suppliers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_active_suppliers", "rar_sha256": "9b1937f5f2a16b9d263feafce2e479dabd975d414fa68d6eadef8bfe14342045", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
