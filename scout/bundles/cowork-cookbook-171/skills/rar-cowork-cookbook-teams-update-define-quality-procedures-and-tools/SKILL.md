---
name: "rar-cowork-cookbook-teams-update-define-quality-procedures-and-tools"
description: "Drafts a Teams channel post on define quality procedures and tools status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_quality_procedures_and_tools", "rar_sha256": "3ba2874418577c848a0a31d7ec69848a66eceb7d497dda346308cf951052a0fa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_quality_procedures_and_tools`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_quality_procedures_and_tools_agent.py` and in the RCI capsule.

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
