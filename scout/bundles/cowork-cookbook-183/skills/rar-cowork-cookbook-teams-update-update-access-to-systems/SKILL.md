---
name: "rar-cowork-cookbook-teams-update-update-access-to-systems"
description: "Drafts a Teams channel post on update access to systems status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_update_access_to_systems", "rar_sha256": "a98bc3852adb8e407f869b5be334969d9248e2cb6ea8d32bb296d631764d06d3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_update_access_to_systems_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-update-access-to-systems:2fc7de06bcb6b3e181e0e12c1b87766799e0b91ddf79cd30c72cc47f88ed2b3c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_update_access_to_systems`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_update_access_to_systems_agent.py` is
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

Update access to systems Teams Channel Update — Drafts a Teams channel post on update access to systems status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-access-to-systems
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_update_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 a98bc3852adb8e40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_update_access_to_systems_agent.py` first:

```bash
python3 teams_update_update_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_update_access_to_systems_agent.py   # or on stdin
python3 teams_update_update_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update access to systems Teams Channel Update — Drafts a Teams channel post on update access to systems status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-update-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_update_access_to_systems',
    "version": '2.0.0',
    "display_name": 'Update access to systems Teams Channel Update',
    "description": 'Drafts a Teams channel post on update access to systems status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-update-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-update-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f50f30462424a91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/update-access-to-systems'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-update-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateUpdateAccessToSystems(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateUpdateAccessToSystems'
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
    print(TeamsUpdateUpdateAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
