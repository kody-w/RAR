---
name: "rar-cowork-cookbook-ppt-exec-perform-predictive-maintenance"
description: "Generates an executive-ready PowerPoint deck on perform predictive maintenance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_predictive_maintenance", "rar_sha256": "e3e2836eb8baf979103ae6a85ec9e877968bf2eea94f54a4853ca4805b4fc776", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_perform_predictive_maintenance_agent.py` and embedded as the fenced Python below (sha256 e3e2836eb8baf979…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_perform_predictive_maintenance_agent.py` first:

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
    "version": '2.0.0',
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
