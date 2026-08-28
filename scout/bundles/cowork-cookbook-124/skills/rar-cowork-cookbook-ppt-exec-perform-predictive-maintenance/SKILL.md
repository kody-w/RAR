---
name: "rar-cowork-cookbook-ppt-exec-perform-predictive-maintenance"
description: "Generates an executive-ready PowerPoint deck on perform predictive maintenance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_predictive_maintenance", "rar_sha256": "061393638c89955745293efc7c443c76aeccb856677260e0763680dfd10b5c02", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_perform_predictive_maintenance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_perform_predictive_maintenance_agent.py` and in the RCI capsule.

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

Perform predictive maintenance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on perform predictive maintenance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-predictive-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_perform_predictive_maintenance_agent.py` and embedded as the fenced Python below (sha256 061393638c899557…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_perform_predictive_maintenance_agent.py` first:

```bash
python3 ppt_exec_perform_predictive_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_perform_predictive_maintenance_agent.py   # or on stdin
python3 ppt_exec_perform_predictive_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform predictive maintenance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on perform predictive maintenance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-predictive-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_perform_predictive_maintenance',
    "version": '2.0.1',
    "display_name": 'Perform predictive maintenance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on perform predictive maintenance status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-perform-predictive-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-perform-predictive-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d80853b2aab4422',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-predictive-maintenance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-perform-predictive-maintenance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecPerformPredictiveMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPerformPredictiveMaintenance'
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
    print(PptExecPerformPredictiveMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
