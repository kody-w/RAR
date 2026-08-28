---
name: "rar-cowork-cookbook-ppt-exec-set-operational-targets"
description: "Generates an executive-ready PowerPoint deck on set operational targets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_set_operational_targets", "rar_sha256": "63ee2df73e92d8b4c0df22e75efaf0dd494bb540d4d2fe85a606a11ab922804a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_set_operational_targets_agent.py` and embedded as the fenced Python below (sha256 63ee2df73e92d8b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_set_operational_targets_agent.py` first:

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
    "version": '2.0.1',
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
