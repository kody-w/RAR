---
name: "rar-cowork-cookbook-teams-update-transfer-workers"
description: "Drafts a Teams channel post on transfer workers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_transfer_workers", "rar_sha256": "4c3a696f06d8913748becce4f495c1d502d7e9535114d3fb6d31c81e62bbcb38", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_transfer_workers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_transfer_workers_agent.py` and in the RCI capsule.

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

Transfer workers Teams Channel Update — Drafts a Teams channel post on transfer workers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-transfer-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_transfer_workers_agent.py` and embedded as the fenced Python below (sha256 4c3a696f06d89137…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_transfer_workers_agent.py` first:

```bash
python3 teams_update_transfer_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_transfer_workers_agent.py   # or on stdin
python3 teams_update_transfer_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer workers Teams Channel Update — Drafts a Teams channel post on transfer workers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-transfer-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_transfer_workers',
    "version": '2.0.1',
    "display_name": 'Transfer workers Teams Channel Update',
    "description": 'Drafts a Teams channel post on transfer workers status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-transfer-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-transfer-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8642697b330a7e78',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/transfer-workers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-transfer-workers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateTransferWorkers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTransferWorkers'
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
    print(TeamsUpdateTransferWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
