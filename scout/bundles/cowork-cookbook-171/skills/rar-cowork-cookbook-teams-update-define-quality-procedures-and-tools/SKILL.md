---
name: "rar-cowork-cookbook-teams-update-define-quality-procedures-and-tools"
description: "Drafts a Teams channel post on define quality procedures and tools status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_quality_procedures_and_tools", "rar_sha256": "46f821574dedc6eb2fe92d4ca18a9e10db88c412099e3a51353a1f1dff20cdaa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_quality_procedures_and_tools_agent.py` and embedded as the fenced Python below (sha256 46f821574dedc6eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_quality_procedures_and_tools_agent.py` first:

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
    "version": '2.0.1',
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
