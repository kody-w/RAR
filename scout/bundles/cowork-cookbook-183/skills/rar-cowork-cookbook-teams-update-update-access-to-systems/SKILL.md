---
name: "rar-cowork-cookbook-teams-update-update-access-to-systems"
description: "Drafts a Teams channel post on update access to systems status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_update_access_to_systems", "rar_sha256": "a98bc3852adb8e407f869b5be334969d9248e2cb6ea8d32bb296d631764d06d3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_update_access_to_systems`. The original RAPP
agent is preserved byte-for-byte in `teams_update_update_access_to_systems_agent.py` and in the RCI capsule.

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
