---
name: "rar-cowork-cookbook-teams-update-develop-service-catalogs"
description: "Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_service_catalogs", "rar_sha256": "4cca61b74b8e150822448d800b42fba02b40748304ad63a0bdbfa3bb72ac4a0e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_develop_service_catalogs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-develop-service-catalogs:4e7c8c66e4855cb0107cd3230194701cd7a8bf756fb0cf77496e87b24e9cf005", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_develop_service_catalogs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_develop_service_catalogs_agent.py` is
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

Develop service catalogs Teams Channel Update — Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_service_catalogs_agent.py` and embedded as the fenced Python below (sha256 4cca61b74b8e1508…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_service_catalogs_agent.py` first:

```bash
python3 teams_update_develop_service_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_service_catalogs_agent.py   # or on stdin
python3 teams_update_develop_service_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service catalogs Teams Channel Update — Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_service_catalogs',
    "version": '2.0.0',
    "display_name": 'Develop service catalogs Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop service catalogs status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-service-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-service-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '868d68191755aec1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-catalogs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-develop-service-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDevelopServiceCatalogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopServiceCatalogs'
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
    print(TeamsUpdateDevelopServiceCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
