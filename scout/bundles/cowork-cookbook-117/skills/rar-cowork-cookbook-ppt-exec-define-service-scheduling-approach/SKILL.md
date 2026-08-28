---
name: "rar-cowork-cookbook-ppt-exec-define-service-scheduling-approach"
description: "Generates an executive-ready PowerPoint deck on define service scheduling approach status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_service_scheduling_approach", "rar_sha256": "ed1bb67f659b88cf1efb2d59d2cf4872277094d8444cef7037bd0905bcb347a6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_service_scheduling_approach_agent.py` and embedded as the fenced Python below (sha256 ed1bb67f659b88cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_service_scheduling_approach_agent.py` first:

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
    "version": '2.0.0',
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
