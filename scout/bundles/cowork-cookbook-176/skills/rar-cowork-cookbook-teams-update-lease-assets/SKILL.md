---
name: "rar-cowork-cookbook-teams-update-lease-assets"
description: "Drafts a Teams channel post on lease assets status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_lease_assets", "rar_sha256": "c5df35e78af8945656e258238eb49f7724ddbd022ce03e7ee80cfb2f96bb746c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_lease_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-lease-assets:92aca64fbc8e4060aa3b021b34b7e124b20c8c3d3975e14d8ea34f824d98bb8a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_lease_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_lease_assets_agent.py` is
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
