---
name: "rar-cowork-cookbook-teams-update-transfer-assets"
description: "Drafts a Teams channel post on transfer assets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_transfer_assets", "rar_sha256": "ddbf82e84a7ea7bffcd5b30f62450e736eb6d776a14cf86ea7c095cd778834de", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_transfer_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-transfer-assets:f692815842b7ff9778f4063d9c51de8001c7d6ca3c2d2b7f544c563900f611e2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_transfer_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_transfer_assets_agent.py` is
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

Transfer assets Teams Channel Update — Drafts a Teams channel post on transfer assets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-transfer-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_transfer_assets_agent.py` and embedded as the fenced Python below (sha256 ddbf82e84a7ea7bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_transfer_assets_agent.py` first:

```bash
python3 teams_update_transfer_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_transfer_assets_agent.py   # or on stdin
python3 teams_update_transfer_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer assets Teams Channel Update — Drafts a Teams channel post on transfer assets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-transfer-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_transfer_assets',
    "version": '2.0.0',
    "display_name": 'Transfer assets Teams Channel Update',
    "description": 'Drafts a Teams channel post on transfer assets status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-transfer-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-transfer-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'db19b40f518bfff7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/transfer-assets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-transfer-assets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateTransferAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTransferAssets'
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
    print(TeamsUpdateTransferAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
