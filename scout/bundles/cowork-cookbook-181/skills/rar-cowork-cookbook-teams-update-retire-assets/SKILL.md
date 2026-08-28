---
name: "rar-cowork-cookbook-teams-update-retire-assets"
description: "Drafts a Teams channel post on retire assets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_retire_assets", "rar_sha256": "5f911535d746619df1972be8e7b6c5af971b100cdb25db31b0c942df5e3699cc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_retire_assets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_retire_assets_agent.py` and in the RCI capsule.

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
