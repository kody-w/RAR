---
name: "rar-cowork-cookbook-teams-update-transfer-assets"
description: "Drafts a Teams channel post on transfer assets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_transfer_assets", "rar_sha256": "ddbf82e84a7ea7bffcd5b30f62450e736eb6d776a14cf86ea7c095cd778834de", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
