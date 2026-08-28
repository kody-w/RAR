---
name: "rar-cowork-cookbook-ppt-exec-set-operational-targets"
description: "Generates an executive-ready PowerPoint deck on set operational targets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_set_operational_targets", "rar_sha256": "5296e40a299ae901ca7f46368cace5a181121ae994f68ae1fd5d1fbdb4023628", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_set_operational_targets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_set_operational_targets_agent.py` and in the RCI capsule.

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

Set operational targets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on set operational targets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-set-operational-targets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_set_operational_targets_agent.py` and embedded as the fenced Python below (sha256 5296e40a299ae901…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_set_operational_targets_agent.py` first:

```bash
python3 ppt_exec_set_operational_targets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_set_operational_targets_agent.py   # or on stdin
python3 ppt_exec_set_operational_targets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set operational targets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on set operational targets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-set-operational-targets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_set_operational_targets',
    "version": '2.0.0',
    "display_name": 'Set operational targets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on set operational targets status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-set-operational-targets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-set-operational-targets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d590998172a589b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/set-operational-targets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-set-operational-targets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecSetOperationalTargets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecSetOperationalTargets'
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
    print(PptExecSetOperationalTargets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
