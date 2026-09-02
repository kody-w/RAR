---
name: "rar-cowork-cookbook-teams-update-transfer-workers"
description: "Drafts a Teams channel post on transfer workers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_transfer_workers", "rar_sha256": "ff7e6a7cb207efa85c508d10f27372307ea4c5e9c8b3091af84929a30ca67961", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_transfer_workers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-transfer-workers:faf783f460fedb61d65b0ecfad1b1ca4c2883b3d28d3be2d575c8d6438b8235d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_transfer_workers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_transfer_workers_agent.py` is
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
