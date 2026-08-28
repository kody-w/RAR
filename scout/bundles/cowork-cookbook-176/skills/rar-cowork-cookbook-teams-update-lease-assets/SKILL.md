---
name: "rar-cowork-cookbook-teams-update-lease-assets"
description: "Drafts a Teams channel post on lease assets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_lease_assets", "rar_sha256": "0c18f2cc744b370e15ff9717a3e14439a244e391aafd416788423ea8305fd03e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_lease_assets`. The original RAPP
agent is preserved byte-for-byte in `teams_update_lease_assets_agent.py` and in the RCI capsule.

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

Lease assets Teams Channel Update — Drafts a Teams channel post on lease assets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-lease-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_lease_assets_agent.py` and embedded as the fenced Python below (sha256 0c18f2cc744b370e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_lease_assets_agent.py` first:

```bash
python3 teams_update_lease_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_lease_assets_agent.py   # or on stdin
python3 teams_update_lease_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lease assets Teams Channel Update — Drafts a Teams channel post on lease assets status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-lease-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_lease_assets',
    "version": '2.0.1',
    "display_name": 'Lease assets Teams Channel Update',
    "description": 'Drafts a Teams channel post on lease assets status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-lease-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-lease-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7e0d32f930181e00',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/lease-assets'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-lease-assets', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateLeaseAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateLeaseAssets'
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
    print(TeamsUpdateLeaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
