---
name: "rar-cowork-cookbook-teams-update-collaborate-on-service-work"
description: "Drafts a Teams channel post on collaborate on service work status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_collaborate_on_service_work", "rar_sha256": "cca9db411eadb5deb4f97ac018433f4b1731647ca6ec182c5ace8c3d462e109d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_collaborate_on_service_work_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-collaborate-on-service-work:8b79de711c50f2bf9ed704726c4af88097bda3f2dd5fea1e0d5da0fe5685b9a1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_collaborate_on_service_work`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_collaborate_on_service_work_agent.py` is
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

Collaborate on service work Teams Channel Update — Drafts a Teams channel post on collaborate on service work status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-collaborate-on-service-work
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_collaborate_on_service_work_agent.py` and embedded as the fenced Python below (sha256 cca9db411eadb5de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_collaborate_on_service_work_agent.py` first:

```bash
python3 teams_update_collaborate_on_service_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_collaborate_on_service_work_agent.py   # or on stdin
python3 teams_update_collaborate_on_service_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collaborate on service work Teams Channel Update — Drafts a Teams channel post on collaborate on service work status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-collaborate-on-service-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_collaborate_on_service_work',
    "version": '2.0.0',
    "display_name": 'Collaborate on service work Teams Channel Update',
    "description": 'Drafts a Teams channel post on collaborate on service work status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-collaborate-on-service-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-collaborate-on-service-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '66657f82775bf626',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collaborate-on-service-work'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-collaborate-on-service-work', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateCollaborateOnServiceWork(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCollaborateOnServiceWork'
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
    print(TeamsUpdateCollaborateOnServiceWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
