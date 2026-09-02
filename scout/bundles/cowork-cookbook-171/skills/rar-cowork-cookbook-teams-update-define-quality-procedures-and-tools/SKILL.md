---
name: "rar-cowork-cookbook-teams-update-define-quality-procedures-and-tools"
description: "Drafts a Teams channel post on define quality procedures and tools status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_quality_procedures_and_tools", "rar_sha256": "3ba2874418577c848a0a31d7ec69848a66eceb7d497dda346308cf951052a0fa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_quality_procedures_and_tools_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-quality-procedures-and-tools:8b4dc6da8595f9f1f61af782945b39fefe60954a79bbf7c495bb68f8960ecd2d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_quality_procedures_and_tools`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_quality_procedures_and_tools_agent.py` is
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

Define quality procedures and tools Teams Channel Update — Drafts a Teams channel post on define quality procedures and tools status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-quality-procedures-and-tools
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_quality_procedures_and_tools_agent.py` and embedded as the fenced Python below (sha256 3ba2874418577c84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_quality_procedures_and_tools_agent.py` first:

```bash
python3 teams_update_define_quality_procedures_and_tools_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_quality_procedures_and_tools_agent.py   # or on stdin
python3 teams_update_define_quality_procedures_and_tools_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define quality procedures and tools Teams Channel Update — Drafts a Teams channel post on define quality procedures and tools status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-quality-procedures-and-tools
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_quality_procedures_and_tools',
    "version": '2.0.0',
    "display_name": 'Define quality procedures and tools Teams Channel Update',
    "description": 'Drafts a Teams channel post on define quality procedures and tools status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-quality-procedures-and-tools',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-quality-procedures-and-tools',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6278d50f59a56ba6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/define-quality-procedures-and-tools'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-define-quality-procedures-and-tools', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDefineQualityProceduresAndTools(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineQualityProceduresAndTools'
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
    print(TeamsUpdateDefineQualityProceduresAndTools().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
