---
name: "rar-cowork-cookbook-teams-update-retire-assets"
description: "Drafts a Teams channel post on retire assets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_retire_assets", "rar_sha256": "5f911535d746619df1972be8e7b6c5af971b100cdb25db31b0c942df5e3699cc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_retire_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-retire-assets:63ad1dc25199e747ac0fa999149c2f388d8a0032d28b0c77fbbed8d1baeec03b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_retire_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_retire_assets_agent.py` is
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

Retire assets Teams Channel Update — Drafts a Teams channel post on retire assets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-retire-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_retire_assets_agent.py` and embedded as the fenced Python below (sha256 5f911535d746619d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_retire_assets_agent.py` first:

```bash
python3 teams_update_retire_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_retire_assets_agent.py   # or on stdin
python3 teams_update_retire_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire assets Teams Channel Update — Drafts a Teams channel post on retire assets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-retire-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_retire_assets',
    "version": '2.0.0',
    "display_name": 'Retire assets Teams Channel Update',
    "description": 'Drafts a Teams channel post on retire assets status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-retire-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-retire-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cab11ee1910eb056',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/retire-assets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-retire-assets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateRetireAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRetireAssets'
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
    print(TeamsUpdateRetireAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
