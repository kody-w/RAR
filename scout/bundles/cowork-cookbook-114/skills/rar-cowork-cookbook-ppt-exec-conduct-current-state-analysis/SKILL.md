---
name: "rar-cowork-cookbook-ppt-exec-conduct-current-state-analysis"
description: "Generates an executive-ready PowerPoint deck on conduct current state analysis status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_conduct_current_state_analysis", "rar_sha256": "d18f39611fee35cf09e2d157c2e6d4225f67010b365f027d914412e632a9f668", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_conduct_current_state_analysis`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_conduct_current_state_analysis_agent.py` and in the RCI capsule.

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

Conduct current state analysis Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on conduct current state analysis status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-current-state-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_conduct_current_state_analysis_agent.py` and embedded as the fenced Python below (sha256 d18f39611fee35cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_conduct_current_state_analysis_agent.py` first:

```bash
python3 ppt_exec_conduct_current_state_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_conduct_current_state_analysis_agent.py   # or on stdin
python3 ppt_exec_conduct_current_state_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct current state analysis Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on conduct current state analysis status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-conduct-current-state-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_conduct_current_state_analysis',
    "version": '2.0.1',
    "display_name": 'Conduct current state analysis Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on conduct current state analysis status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-conduct-current-state-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-conduct-current-state-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b7459c06cf57262',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/conduct-current-state-analysis'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-conduct-current-state-analysis', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecConductCurrentStateAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecConductCurrentStateAnalysis'
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
    print(PptExecConductCurrentStateAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
