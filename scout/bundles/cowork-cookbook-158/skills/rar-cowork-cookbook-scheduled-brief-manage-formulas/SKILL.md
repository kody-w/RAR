---
name: "rar-cowork-cookbook-scheduled-brief-manage-formulas"
description: "Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_formulas", "rar_sha256": "d3fd0240ac47c540ed2236161b30ffd9afcd0c2c1206aec780acf838f9929b17", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_formulas`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_formulas_agent.py` and in the RCI capsule.

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

Manage formulas Scheduled Email Brief — Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_formulas_agent.py` and embedded as the fenced Python below (sha256 d3fd0240ac47c540…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_formulas_agent.py` first:

```bash
python3 scheduled_brief_manage_formulas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_formulas_agent.py   # or on stdin
python3 scheduled_brief_manage_formulas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage formulas Scheduled Email Brief — Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_formulas',
    "version": '2.0.0',
    "display_name": 'Manage formulas Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage formulas for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-formulas',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-formulas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e393035e21427f17',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-formulas'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-manage-formulas', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefManageFormulas(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageFormulas'
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
    print(ScheduledBriefManageFormulas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
