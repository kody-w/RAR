---
name: "rar-cowork-cookbook-teams-update-transfer-assets"
description: "Drafts a Teams channel post on transfer assets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_transfer_assets", "rar_sha256": "a6c346ce90716165b77fb04379904d89b0c90f389546ee0f026d6b78db742057", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_transfer_assets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_transfer_assets_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_transfer_assets_agent.py` and embedded as the fenced Python below (sha256 a6c346ce90716165…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_transfer_assets_agent.py` first:

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
    "version": '2.0.1',
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
