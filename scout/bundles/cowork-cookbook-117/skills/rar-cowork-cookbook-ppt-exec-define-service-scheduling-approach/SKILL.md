---
name: "rar-cowork-cookbook-ppt-exec-define-service-scheduling-approach"
description: "Generates an executive-ready PowerPoint deck on define service scheduling approach status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_service_scheduling_approach", "rar_sha256": "24e1d68fb20df1c8a2f16d6e0832c83dd72784284e912e047e669f901277e90f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_service_scheduling_approach`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_service_scheduling_approach_agent.py` and in the RCI capsule.

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

Define service scheduling approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define service scheduling approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-service-scheduling-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_service_scheduling_approach_agent.py` and embedded as the fenced Python below (sha256 24e1d68fb20df1c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_service_scheduling_approach_agent.py` first:

```bash
python3 ppt_exec_define_service_scheduling_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_service_scheduling_approach_agent.py   # or on stdin
python3 ppt_exec_define_service_scheduling_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service scheduling approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define service scheduling approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-service-scheduling-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_service_scheduling_approach',
    "version": '2.0.1',
    "display_name": 'Define service scheduling approach Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define service scheduling approach status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-service-scheduling-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-service-scheduling-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ec7fe53544a9a40',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-scheduling-approach'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-define-service-scheduling-approach', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDefineServiceSchedulingApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineServiceSchedulingApproach'
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
    print(PptExecDefineServiceSchedulingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
