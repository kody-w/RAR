---
name: "rar-cowork-cookbook-ppt-exec-set-operational-targets"
description: "Generates an executive-ready PowerPoint deck on set operational targets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_set_operational_targets", "rar_sha256": "5296e40a299ae901ca7f46368cace5a181121ae994f68ae1fd5d1fbdb4023628", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_set_operational_targets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-set-operational-targets:2e5ae58d85a8087d2105d88ed18d359fd53cd17418310aeca2fc29a8e4a47b56", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_set_operational_targets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_set_operational_targets_agent.py` is
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
