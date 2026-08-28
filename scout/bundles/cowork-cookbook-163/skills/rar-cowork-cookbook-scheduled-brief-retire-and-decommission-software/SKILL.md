---
name: "rar-cowork-cookbook-scheduled-brief-retire-and-decommission-software"
description: "Schedulable morning-brief email summarizing retire and decommission software for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_retire_and_decommission_software", "rar_sha256": "44f78c3f2a10c1116d5754331d197d70ffc5db603485731362651af8b158060e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_retire_and_decommission_software`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_retire_and_decommission_software_agent.py` and in the RCI capsule.

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

Retire and decommission software Scheduled Email Brief — Schedulable morning-brief email summarizing retire and decommission software for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-and-decommission-software
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_retire_and_decommission_software_agent.py` and embedded as the fenced Python below (sha256 44f78c3f2a10c111…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_retire_and_decommission_software_agent.py` first:

```bash
python3 scheduled_brief_retire_and_decommission_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_retire_and_decommission_software_agent.py   # or on stdin
python3 scheduled_brief_retire_and_decommission_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire and decommission software Scheduled Email Brief — Schedulable morning-brief email summarizing retire and decommission software for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-retire-and-decommission-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_retire_and_decommission_software',
    "version": '2.0.1',
    "display_name": 'Retire and decommission software Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing retire and decommission software for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-retire-and-decommission-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-retire-and-decommission-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e2057509cc0e181',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/retire-and-decommission-software'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-retire-and-decommission-software', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefRetireAndDecommissionSoftware(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRetireAndDecommissionSoftware'
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
    print(ScheduledBriefRetireAndDecommissionSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
