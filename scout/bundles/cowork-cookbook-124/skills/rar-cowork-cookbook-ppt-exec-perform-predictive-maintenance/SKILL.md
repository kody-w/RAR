---
name: "rar-cowork-cookbook-ppt-exec-perform-predictive-maintenance"
description: "Generates an executive-ready PowerPoint deck on perform predictive maintenance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_predictive_maintenance", "rar_sha256": "e3e2836eb8baf979103ae6a85ec9e877968bf2eea94f54a4853ca4805b4fc776", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_perform_predictive_maintenance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-perform-predictive-maintenance:922bfbdd859a52edba58a0392a6b01fea3d34e6b01d3f48e235a18a10211d4c5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_perform_predictive_maintenance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_perform_predictive_maintenance_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
