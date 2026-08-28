---
name: "rar-cowork-cookbook-teams-update-retire-assets"
description: "Drafts a Teams channel post on retire assets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_retire_assets", "rar_sha256": "4085e5dd89d4440997e39aefb15e8be7d1a182060c54c2e77e52a0cbbac8d2e0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_retire_assets_agent.py` and embedded as the fenced Python below (sha256 4085e5dd89d44409…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_retire_assets_agent.py` first:

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
    "version": '2.0.1',
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
