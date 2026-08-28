---
name: "rar-cowork-cookbook-teams-update-lease-assets"
description: "Drafts a Teams channel post on lease assets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_lease_assets", "rar_sha256": "c5df35e78af8945656e258238eb49f7724ddbd022ce03e7ee80cfb2f96bb746c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_lease_assets_agent.py` and embedded as the fenced Python below (sha256 c5df35e78af89456…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_lease_assets_agent.py` first:

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
    "version": '2.0.0',
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
