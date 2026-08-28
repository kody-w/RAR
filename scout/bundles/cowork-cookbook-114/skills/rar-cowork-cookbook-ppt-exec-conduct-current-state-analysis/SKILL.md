---
name: "rar-cowork-cookbook-ppt-exec-conduct-current-state-analysis"
description: "Generates an executive-ready PowerPoint deck on conduct current state analysis status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_conduct_current_state_analysis", "rar_sha256": "480034430f13cc7896ff3ce1b2cd1d47345aab7dee1b529faf8dc58a04dd4eee", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_conduct_current_state_analysis_agent.py` and embedded as the fenced Python below (sha256 480034430f13cc78…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_conduct_current_state_analysis_agent.py` first:

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
    "version": '2.0.0',
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
