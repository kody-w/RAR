---
name: "rar-cowork-cookbook-teams-update-transfer-workers"
description: "Drafts a Teams channel post on transfer workers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_transfer_workers", "rar_sha256": "ff7e6a7cb207efa85c508d10f27372307ea4c5e9c8b3091af84929a30ca67961", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_transfer_workers_agent.py` and embedded as the fenced Python below (sha256 ff7e6a7cb207efa8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_transfer_workers_agent.py` first:

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
    "version": '2.0.0',
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
